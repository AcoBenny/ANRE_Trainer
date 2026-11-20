#!/usr/bin/env python3
"""Read-only six-fixture ANRE Academy FreeLLMAPI smoke test; never approves answers."""
import argparse
import datetime as dt
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

EXPECTED = {f"ACA-ANRE-{n:03d}" for n in range(1, 7)}


def parse_url(raw: str) -> str:
    u = urllib.parse.urlsplit(raw.rstrip("/"))
    local = u.hostname in {"localhost", "127.0.0.1", "::1"}
    if not u.hostname or u.username or u.password or u.query or u.fragment:
        raise ValueError("Invalid FreeLLMAPI base URL")
    if u.scheme != "https" and not (u.scheme == "http" and local):
        raise ValueError("HTTPS required for remote FreeLLMAPI; HTTP only for localhost")
    if u.path and u.path not in ("/v1",):
        raise ValueError("Base URL must end at /v1")
    return raw.rstrip("/") + ("" if u.path == "/v1" else "/v1")


def load_cases(path: pathlib.Path):
    data = json.loads(path.read_text(encoding="utf8"))
    cases = data.get("cases", [])
    ids = [c.get("id") for c in cases]
    if (len(ids) != 6 or set(ids) != EXPECTED or
            data.get("original_questions_and_keys_immutable") is not True or
            data.get("require_real_traces_for_pass") is not True):
        raise ValueError("Only the six immutable CKPT-256 Academy fixtures are permitted")
    for c in cases:
        if c.get("state") != "REGISTERED_NOT_BENCHMARKED":
            raise ValueError("Unexpected fixture approval state")
        if not c.get("given") or not c.get("reference"):
            raise ValueError("Missing fixture case or source pointer")
    return cases


def make_prompt(case):
    # Expected and unsafe behavior deliberately withheld from the model.
    return json.dumps({
        "case_id": case["id"], "category": case.get("category"),
        "question_ids": case.get("anre_ids"),
        "incident": case["given"], "source_pointer_unverified": case["reference"],
    }, ensure_ascii=False)


def request_one(base_url, key, model, case):
    payload = {
        "model": model,
        "stream": False,
        "temperature": 0,
        "max_tokens": 700,
        "messages": [
            {"role": "system", "content": (
                "Audit ANRE provenance as a research model, not a qualified reviewer. "
                "Distinguish original versus edited text, grade, source version and hidden assumptions. "
                "Never invent quotes or official answer keys. If the exact Q/A/B/C or normative paragraph "
                "is unavailable, label it NOT VERIFIED and do not approve learning. "
                "Report counterexamples and what primary evidence is needed."
            )},
            {"role": "user", "content": make_prompt(case)},
        ],
    }
    req = urllib.request.Request(
        base_url + "/chat/completions",
        data=json.dumps(payload).encode(), method="POST",
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=75) as res:
            body = json.load(res)
            headers = res.headers
    except urllib.error.HTTPError as err:
        raise RuntimeError(f"FreeLLMAPI HTTP {err.code}") from None
    except urllib.error.URLError:
        raise RuntimeError("FreeLLMAPI network error") from None
    choices = body.get("choices", [])
    if not choices or not isinstance(choices[0].get("message", {}).get("content"), str):
        raise RuntimeError("FreeLLMAPI returned no usable message")
    route = headers.get("X-Routed-Via", "NOT_REPORTED")
    if not route or route == "NOT_REPORTED":
        raise RuntimeError("Missing X-Routed-Via: cannot attribute model")
    return {
        "provider_model": route[:200],
        "fallback_attempts": headers.get("X-Fallback-Attempts", "0")[:30],
        "fallback_trail": headers.get("X-Fallback-Trail", "")[:400],
        "usage": body.get("usage"),
        "response": choices[0]["message"]["content"][:12000],
        "evidence_status": "UNREVIEWED_AI_TRACE_NOT_ANRE_APPROVAL",
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--fixtures", type=pathlib.Path, required=True)
    p.add_argument("--output", type=pathlib.Path, default=pathlib.Path("academy_freellmapi_result.json"))
    p.add_argument("--mode", choices=["preflight", "live"], default="preflight")
    p.add_argument("--model", default="auto")
    args = p.parse_args()
    try:
        cases = load_cases(args.fixtures)
        report = {
            "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "mode": args.mode, "case_count": 6, "model_requested": args.model,
            "ai_calls_attempted": 0, "ai_calls_returned": 0, "qa_approved": 0,
            "records": [],
        }
        if args.mode == "live":
            if os.getenv("ACADEMY_CONFIRM_LIVE") != "RUN_6":
                raise ValueError("Live mode requires ACADEMY_CONFIRM_LIVE=RUN_6")
            key = os.getenv("FREELLMAPI_UNIFIED_KEY", "")
            if not key:
                raise ValueError("Missing FREELLMAPI_UNIFIED_KEY")
            url = parse_url(os.getenv("FREELLMAPI_BASE_URL", "http://localhost:3001/v1"))
            for case in cases:
                report["ai_calls_attempted"] += 1
                try:
                    result = request_one(url, key, args.model, case)
                except RuntimeError as exc:
                    report["records"].append({"id": case["id"], "error": str(exc)})
                    break  # fail closed on unknown or exhausted provider state
                report["records"].append({"id": case["id"], **result})
                report["ai_calls_returned"] += 1
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
        print(f"mode={args.mode} fixtures=6 calls={report['ai_calls_attempted']} returned={report['ai_calls_returned']}")
        return 1 if report["ai_calls_attempted"] != report["ai_calls_returned"] else 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"Preflight refused: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
