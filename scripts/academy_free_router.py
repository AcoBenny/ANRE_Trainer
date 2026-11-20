#!/usr/bin/env python3
"""Read-only ANRE Academy free-API router. Never modifies answer keys or training weights."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

EXPECTED = {f"ACA-ANRE-{i:03d}" for i in range(1, 7)}
AGENTS = (
    ("technical_reviewer", ("groq", "openrouter", "openrouter_fixed"),
     "You are an electrical engineering and source-scope ANRE reviewer. Identify hidden assumptions, compare original versus edited wording if actually supplied, and examine each supplied A/B/C. Do not guess an official answer key or claim direct source access. Output uncertainty and requested source evidence."),
    ("independent_skeptic", ("gemini", "openrouter", "openrouter_fixed"),
     "You are a separate adversarial reviewer. You have not seen any other review. Challenge physical models, edition applicability, ambiguous wording, different imported grades and claimed citations. Do not approve exam answers or invent exact normative quotations."),
)
MODELS = {
    "groq": "openai/gpt-oss-120b",
    "gemini": "gemini-3.5-flash-lite",
    "openrouter": "openrouter/free",
    "openrouter_fixed": "google/gemma-4-31b-it:free",
}
KEYS = {
    "groq": "GROQ_API_KEY",
    "gemini": "GEMINI_API_KEY",
    "openrouter": "OPENROUTER_API_KEY",
    "openrouter_fixed": "OPENROUTER_API_KEY",
}
ENDPOINTS = {
    "groq": "https://api.groq.com/openai/v1/chat/completions",
    "openrouter": "https://openrouter.ai/api/v1/chat/completions",
    "openrouter_fixed": "https://openrouter.ai/api/v1/chat/completions",
    "gemini": "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent",
}
MAX_TOTAL_CALLS = 24
MAX_CASES = 6

class ProviderError(Exception):
    def __init__(self, code: str, fallback_ok: bool):
        self.code, self.fallback_ok = code, fallback_ok
        super().__init__(code)


def read_cases(path: pathlib.Path):
    source = json.loads(path.read_text(encoding="utf-8"))
    cases = source.get("cases")
    if not source.get("original_questions_and_keys_immutable") or not isinstance(cases, list):
        raise ValueError("Invalid or mutable CKPT-256 fixtures")
    ids = [c.get("id") for c in cases]
    if len(ids) != 6 or set(ids) != EXPECTED or len(set(ids)) != len(ids):
        raise ValueError("Incorrect CKPT-256 fixture ID set")
    for c in cases:
        if c.get("state") != "REGISTERED_NOT_BENCHMARKED" or not all(
            c.get(k) for k in ("category", "given", "reference", "anre_ids", "required_behavior", "unsafe_behavior")
        ):
            raise ValueError("Fixture missing required fields")
    return sorted(cases, key=lambda c: c["id"])


def build_prompt(case: dict) -> str:
    # The positive/negative rubrics are intentionally withheld from model evaluation.
    return json.dumps(
        {k: case[k] for k in ("id", "anre_ids", "given", "reference")},
        ensure_ascii=False, sort_keys=True,
    )


def post_json(url: str, headers: dict, payload: dict):
    request = urllib.request.Request(
        url, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "ANRE-Academy-Source-Audit/1.0", **headers}, method="POST"
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as exc:
        # Do not print the provider response or echo headers / keys.
        raise ProviderError("HTTP_" + str(exc.code), exc.code in (403, 404, 408, 429, 500, 502, 503, 504)) from None
    except (urllib.error.URLError, TimeoutError):
        raise ProviderError("NETWORK_TIMEOUT", True) from None


def call_provider(provider: str, system: str, message: str):
    key = os.environ.get(KEYS[provider], "")
    if not key:
        raise ProviderError("SECRET_MISSING", True)
    if provider == "gemini":
        payload = {
            "systemInstruction": {"parts": [{"text": system}]},
            "contents": [{"role": "user", "parts": [{"text": message}]}],
            "generationConfig": {"maxOutputTokens": 1400, "temperature": 0},
        }
        obj = post_json(ENDPOINTS[provider], {"x-goog-api-key": key}, payload)
        text = "\n".join(p.get("text", "") for c in obj.get("candidates", [])
                         for p in c.get("content", {}).get("parts", []) if "text" in p)
        usage = obj.get("usageMetadata", {})
        finish_reason = str((obj.get("candidates") or [{}])[0].get("finishReason", "UNKNOWN"))
        model = obj.get("modelVersion", MODELS[provider])
    else:
        payload = {
            "model": MODELS[provider],
            "stream": False,
            "max_tokens": 1800 if provider.startswith("openrouter") else 1400,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": message}],
        }
        if provider == "openrouter":
            payload["reasoning"] = {"effort": "low"}
        obj = post_json(ENDPOINTS[provider], {"Authorization": "Bearer " + key}, payload)
        text = "\n".join(str(c.get("message", {}).get("content") or "") for c in obj.get("choices", []))
        usage = obj.get("usage", {})
        finish_reason = str((obj.get("choices") or [{}])[0].get("finish_reason", "unknown"))
        model = obj.get("model") or MODELS[provider]
    if not text.strip():
        raise ProviderError("EMPTY_MODEL_OUTPUT", True)
    if finish_reason.upper() in ("MAX_TOKENS", "LENGTH", "SAFETY", "RECITATION"):
        raise ProviderError("INCOMPLETE_OR_BLOCKED_" + finish_reason.upper(), False)
    return {"model": str(model), "finish_reason": finish_reason, "usage": usage, "text": text[:14000]}


def route_agent(system: str, message: str, candidates: tuple[str, ...], state: dict):
    errors = []
    for provider in candidates:
        if not os.environ.get(KEYS[provider]):
            errors.append({"provider": provider, "error": "SECRET_MISSING"})
            continue
        if state["attempts"] >= MAX_TOTAL_CALLS:
            return {"ok": False, "errors": errors + [{"error": "HARD_CALL_LIMIT"}]}
        state["attempts"] += 1
        try:
            value = call_provider(provider, system, message)
            state["returned"] += 1
            return {"ok": True, "provider": provider, **value, "prior_errors": errors}
        except ProviderError as exc:
            errors.append({"provider": provider, "error": exc.code})
            if not exc.fallback_ok:
                break
    return {"ok": False, "errors": errors}


def write_result(folder: pathlib.Path, report: dict):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = [
        "# ANRE Academy free-API router pilot",
        "",
        "Mod: " + report["mode"],
        "Scenarii: " + str(report["cases"]),
        "Apeluri API incercate: " + str(report["attempted"]),
        "Raspunsuri model: " + str(report["returned"]),
        "Evaluatori completati: " + str(report["complete_roles"]) + "/" + str(2 * report["cases"]),
        "OpenAI platit: DEZACTIVAT (zero apeluri).",
        "FARA APROBARE de bareme / intrebari / surse / invatare.",
        "Cotele gratuite depind de planurile conturilor, nu sunt garantate de script.",
        "Rezultatele brute se gasesc in results.json si necesita evaluare independenta.",
    ]
    (folder / "SUMMARY.md").write_text("\n".join(summary) + "\n", encoding="utf-8")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixtures", type=pathlib.Path, required=True)
    parser.add_argument("--out", type=pathlib.Path, default=pathlib.Path("_academy_free_results"))
    parser.add_argument("--mode", choices=("dry-run", "live-free"), default="dry-run")
    parser.add_argument("--cases", type=int, default=1)
    parser.add_argument("--confirm", default="")
    args = parser.parse_args(argv)
    if not 1 <= args.cases <= MAX_CASES:
        parser.error("Number of cases must be 1..6")
    if args.mode == "live-free" and args.confirm != "FREE_ONLY":
        parser.error("Live mode requires --confirm FREE_ONLY")
    cases = read_cases(args.fixtures)[:args.cases]
    report = {
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mode": args.mode, "cases": len(cases), "attempted": 0, "returned": 0,
        "complete_roles": 0, "original_keys_changed": False,
        "learner_approved": False, "independent_human_qa": False,
        "providers": [{"name": p, "model": MODELS[p], "secret_configured": bool(os.environ.get(KEYS[p]))}
                      for p in MODELS],
        "records": [],
    }
    state = {"attempts": 0, "returned": 0}
    for case in cases:
        item = {"case_id": case["id"], "roles": {}}
        if args.mode == "live-free":
            prompt = build_prompt(case)
            for name, candidates, system in AGENTS:
                item["roles"][name] = route_agent(system, prompt, candidates, state)
                if item["roles"][name]["ok"]:
                    report["complete_roles"] += 1
        report["records"].append(item)
        report["attempted"], report["returned"] = state["attempts"], state["returned"]
        write_result(args.out, report)
    print("Cases:", len(cases), "API attempts:", state["attempts"],
          "completed roles:", report["complete_roles"], "paid OpenAI calls: 0")
    if args.mode == "live-free" and report["complete_roles"] != 2 * len(cases):
        print("STOP: missing independent reviewer outputs; no approval", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
