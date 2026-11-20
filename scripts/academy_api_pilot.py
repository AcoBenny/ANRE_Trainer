#!/usr/bin/env python3
"""Small, manually triggered, read-only ANRE Academy multi-provider pilot."""
import argparse
import datetime as dt
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

EXPECTED_CASES = {f"ACA-ANRE-{n:03d}" for n in range(1, 7)}
OPENAI_URL = "https://api.openai.com/v1/responses"
GEMINI_ROOT = "https://generativelanguage.googleapis.com/v1beta/models/"
BASELINE = (
    "Analizeaza cazul ANRE in romana. Ofera o evaluare concisa. "
    "Nu pretinde ca ai accesat documente pe care nu le-ai primit."
)
SPECIALIST = (
    "Esti auditor tehnic ANRE pentru un benchmark, nu corector de bareme. "
    "Separi explicit textul original, formularea din aplicatie si cheia presupusa. "
    "Analizezi fiecare optiune A/B/C numai daca textul optiunilor este furnizat. "
    "Verifici obiectul fizic, conditiile, gradul si versiunea sursei. "
    "Nu deduci un barem oficial dintr-un workbook sau dintr-o explicatie. "
    "Daca nu ai acces direct la sursa, scrie NECONFIRMAT, nu inventa citate. "
    "Semnaleaza contradictii si contraexemple; nu modifica intrebarile."
)
CRITIC = (
    "Esti un al doilea evaluator ANRE, independent de primul. "
    "Nu ai acces la rezultatele primului evaluator. Cauta ipoteze ascunse, "
    "conflatii intre versiuni, erori de sursa, presupuneri despre barem si "
    "exceptii. Nu pretinde ca ai verificat direct documente sau norme. "
    "Pastreaza rezultatul provizoriu si explica ce dovezi lipsesc."
)


def post_json(url, headers, payload):
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", **headers},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=40) as res:
            return json.load(res)
    except urllib.error.HTTPError as exc:
        # Never echo a provider response, headers or a credential into CI logs.
        raise RuntimeError(f"Provider returned HTTP {exc.code}") from None
    except urllib.error.URLError:
        raise RuntimeError("Provider network error") from None


def openai_call(system, user, model):
    key = os.getenv("OPENAI_API_KEY", "")
    if not key:
        raise RuntimeError("OPENAI_API_KEY secret absent")
    payload = {
        "model": model,
        "instructions": system,
        "input": user,
        "store": False,
        "max_output_tokens": 900,
    }
    obj = post_json(OPENAI_URL, {"Authorization": "Bearer " + key}, payload)
    parts = [
        block.get("text", "")
        for item in obj.get("output", [])
        if item.get("type") == "message"
        for block in item.get("content", [])
        if block.get("type") == "output_text"
    ]
    return {"text": "\n".join(parts), "usage": obj.get("usage", {}), "response_status": obj.get("status", "unknown")}


def gemini_call(system, user, model):
    key = os.getenv("GEMINI_API_KEY", "")
    if not key:
        raise RuntimeError("GEMINI_API_KEY secret absent")
    if not model.replace("-", "").replace(".", "").isalnum():
        raise RuntimeError("Gemini model identifier invalid")
    url = GEMINI_ROOT + urllib.parse.quote(model, safe="-_.") + ":generateContent"
    payload = {
        "systemInstruction": {"parts": [{"text": system}]},
        "contents": [{"role": "user", "parts": [{"text": user}]}],
        "generationConfig": {"temperature": 0, "maxOutputTokens": 900},
    }
    obj = post_json(url, {"x-goog-api-key": key}, payload)
    parts = [
        p.get("text", "")
        for candidate in obj.get("candidates", [])
        for p in candidate.get("content", {}).get("parts", [])
        if "text" in p
    ]
    return {"text": "\n".join(parts), "usage": obj.get("usageMetadata", {}), "response_status": "returned"}


def load_cases(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    ids = [case.get("id") for case in cases]
    if len(ids) != 6 or set(ids) != EXPECTED_CASES:
        raise ValueError("Six exact CKPT-256 Academy fixture IDs are required")
    if len(ids) != len(set(ids)) or not data.get("original_questions_and_keys_immutable"):
        raise ValueError("Immutable benchmark fixture validation failed")
    for case in cases:
        if case.get("state") != "REGISTERED_NOT_BENCHMARKED":
            raise ValueError("Unexpected fixture state; stop and revalidate")
        for field in ("given", "reference", "category", "anre_ids", "required_behavior", "unsafe_behavior"):
            if not case.get(field):
                raise ValueError(f"Fixture {case['id']} missing {field}")
    return cases


def write_report(out, report):
    out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# ANRE Academy | pilot independent agent traces",
        "",
        f"Date UTC: {report['created_utc']}",
        f"Mode: {report['mode']}",
        f"Fixtures validated: {report['fixture_count']}",
        f"Calls planned: {report['calls_planned']}",
        f"Calls attempted: {report['calls_attempted']}",
        f"Provider responses returned: {report['provider_responses']}",
        f"Provider errors: {report['errors']}",
        "",
        "Not a source-authenticated legal/electrical review. No benchmark pass,",
        "training-weight change, exam key correction or learner approval is implied.",
        "Required/unsafe reference answers were withheld from all model prompts.",
        "Human/qualified review is required to score these raw traces.",
        "",
        "Results are stored in results.json. Review the full responses and token usage there.",
    ]
    (out / "SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixtures", required=True, type=pathlib.Path)
    parser.add_argument("--out", default="_academy_results", type=pathlib.Path)
    parser.add_argument("--mode", choices=("dry-run", "openai", "both"), default="dry-run")
    parser.add_argument("--openai-model", default="gpt-4.1-mini")
    parser.add_argument("--gemini-model", default="gemini-3.1-flash-lite")
    parser.add_argument("--confirm", default="")
    args = parser.parse_args()
    cases = load_cases(args.fixtures)
    per_case = 0 if args.mode == "dry-run" else (3 if args.mode == "both" else 2)
    report = {
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mode": args.mode,
        "fixture_count": len(cases),
        "calls_planned": len(cases) * per_case,
        "calls_attempted": 0,
        "provider_responses": 0,
        "errors": 0,
        "records": [],
        "learner_approval": False,
        "qualified_sme_signoff": False,
    }
    if args.mode != "dry-run" and args.confirm != "RUN":
        raise ValueError("Paid API calls require explicit --confirm RUN")
    if args.mode != "dry-run" and not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is not configured")
    if args.mode == "both" and not os.getenv("GEMINI_API_KEY"):
        raise ValueError("GEMINI_API_KEY is not configured")

    for case in cases:
        # Deliberately exclude the fixture answer/rubric so models cannot see grading hints.
        question = json.dumps(
            {k: case[k] for k in ("id", "category", "anre_ids", "given", "reference")},
            ensure_ascii=False,
        )
        trace = {"case_id": case["id"], "responses": {}}
        for agent, provider, system, model in (
            ("baseline", "openai", BASELINE, args.openai_model),
            ("academy_specialist", "openai", SPECIALIST, args.openai_model),
            ("independent_critic", "gemini", CRITIC, args.gemini_model),
        ):
            if provider == "gemini" and args.mode != "both":
                continue
            if args.mode == "dry-run":
                continue
            if report["calls_attempted"] >= 18:
                raise ValueError("Hard maximum of 18 API calls reached")
            report["calls_attempted"] += 1
            try:
                response = (
                    openai_call(system, question, model)
                    if provider == "openai"
                    else gemini_call(system, question, model)
                )
                report["provider_responses"] += 1
                trace["responses"][agent] = {"provider": provider, "model": model, **response}
            except RuntimeError as exc:
                report["errors"] += 1
                trace["responses"][agent] = {
                    "provider": provider, "model": model, "error": str(exc)
                }
                # Avoid further paid calls after provider failure until investigated.
                report["records"].append(trace)
                write_report(args.out, report)
                print(f"Stopped safely: {str(exc)}", file=sys.stderr)
                return 1
        report["records"].append(trace)
    write_report(args.out, report)
    print(
        f"Validated {len(cases)} cases; attempted {report['calls_attempted']} calls; "
        f"returned {report['provider_responses']}. No exam answers were approved."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
