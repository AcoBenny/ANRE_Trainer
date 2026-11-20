#!/usr/bin/env python3
"""Read-only source-grounded I7 comparison (two cases, four free-tier evaluations)."""
import argparse
import datetime as dt
import json
import pathlib
import sys

try:
    from .academy_full_qabc_review import load_ledger, build_case
    from .academy_free_router import route_agent
except ImportError:
    from academy_full_qabc_review import load_ledger, build_case
    from academy_free_router import route_agent

EXPECTED = {"QABC-0362": "5.4.13", "QABC-0386": "5.5.2.3"}
PROMPT_TECH = (
    "You are a technical ANRE auditor. Analyze the exact original and trainer "
    "question/ABC against the provided excerpt from a user-supplied 2023 I7 PDF. "
    "The excerpt is NOT authenticated as the complete applicable 2026 normative edition. "
    "In Romanian write at most 220 words in five numbered lines: "
    "1 EXACT differences including whether only whitespace changed; "
    "2 SOURCE: quote the decisive wording from the supplied paragraph (not elsewhere); "
    "3 ORIGINAL: independently evaluate A/B/C against that paragraph, without guessing official scoring; "
    "4 TRAINER: separately evaluate A/B/C; "
    "5 GATE: say which source edition and official examination key checks remain. "
    "Do not invent STAS clauses or extrapolate from a different topic. "
    "Use prior Academy rule: where source permits X OR Y OR Z, a nonexclusive "
    "statement X can be TRUE even if it does not list Y or Z; 'ONLY X' is "
    "false if alternatives are permitted. Omission of a second necessary condition "
    "does not automatically make a first true condition false; explicit 'WITHOUT X' "
    "contradicts mandatory X. Evaluate original and trainer A/B/C separately and "
    "do not infer a unique official scoring key from partial source-truth."
)
PROMPT_SKEPTIC = (
    "You are a different skeptical auditor who has NOT seen technical reviewer outputs. "
    "Given exact original/trainer QABC and one *verified-to-user-PDF* I7 passage, "
    "challenge every claim that contradicts the supplied paragraph. "
    "In Romanian under 220 words, five numbered lines: "
    "1 FIELD DIFFERENCE, 2 I7 EVIDENCE with exact phrase, "
    "3 WRONG-OPTION COUNTEREXAMPLE, 4 SCOPE/2026 VALIDITY LIMIT, "
    "5 RELEASE GATE. Do not invent other normative documents, make up scored exam keys, "
    "or claim the 2023 user PDF alone proves 2026 applicability. "
    "Apply the Academy allowed-vs-exclusive transfer rule: 'X' as a permissible "
    "single example is not false merely because 'Y' is also allowed; 'ONLY X' "
    "is false when other options are allowed. Distinguish 'WITHOUT X' negation "
    "from omitted details which may leave an option incomplete but true. "
    "Inspect ALL source and trainer A/B/C, not just the first option."
)


def load_context(path):
    v = json.loads(path.read_text(encoding="utf-8"))
    if v.get("schema") != "academy_source_excerpt_v1" or v.get("current_2026_applicability_verified") is not False:
        raise ValueError("Missing 2026 edition disclaimer")
    if v.get("official_exam_scoring_keys_authenticated") is not False:
        raise ValueError("Exam key must remain unproven")
    clauses = v.get("clauses", [])
    if len(clauses) != 2 or {x["unit_id"]: x["section"] for x in clauses} != EXPECTED:
        raise ValueError("Exactly two known I7 clauses required")
    for x in clauses:
        if not x.get("pdf_page") or not x.get("text") or not x.get("verified_by"):
            raise ValueError("Missing verbatim context")
    exact_clauses = {
        "QABC-0362": (70, ("dintr-un circuit de iluminat normal",
                               "dintr-un circuit de prize", "direct din tabloul de distribuţie")),
        "QABC-0386": (72, ("deconectat individual",
                               "numai prin intermediul unei scule")),
    }
    for x in clauses:
        expected_page, expected_fragments = exact_clauses[x["unit_id"]]
        if x["pdf_page"] != expected_page or any(fragment not in x["text"]
                                                 for fragment in expected_fragments):
            raise ValueError("Authenticated I7 2023 source excerpt changed: STOP")
    return {x["unit_id"]: x for x in clauses}


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", type=pathlib.Path, required=True)
    p.add_argument("--context", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path, default=pathlib.Path("_academy_i7_results"))
    p.add_argument("--mode", choices=("dry-run", "live-free"), default="dry-run")
    p.add_argument("--confirm", default="")
    args = p.parse_args(argv)
    if args.mode == "live-free" and args.confirm != "FREE_ONLY":
        p.error("Free-only live mode requires --confirm FREE_ONLY")
    ledger = {r["unit_id"]: r for r in load_ledger(args.ledger)}
    context = load_context(args.context)
    state = {"attempts": 0, "returned": 0}
    result = {
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mode": args.mode, "cases": 2, "attempted": 0, "completed": 0,
        "paid_openai_calls": 0, "official_2026_sources_verified": False,
        "learners_approved": False, "keys_changed": False, "records": [],
    }
    for unit in sorted(context):
        item, changed = build_case(ledger[unit])
        # Include only source excerpt and original texts, no expected answer or prior audit candidate.
        item["source_excerpt_user_supplied_2023"] = context[unit]
        item["2026_current_edition_unverified"] = True
        record = {"unit_id": unit, "changed_raw_fields": changed, "roles": {}}
        if args.mode == "live-free":
            prompt = json.dumps(item, ensure_ascii=False)
            for name, primary, secondary, instruction in (
                ("technical", "groq", "openrouter", PROMPT_TECH),
                ("skeptic", "gemini", "openrouter", PROMPT_SKEPTIC),
            ):
                record["roles"][name] = route_agent(instruction, prompt, (primary, secondary), state)
        result["records"].append(record)
    result["attempted"], result["completed"] = state["attempts"], state["returned"]
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "results.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.out / "SUMMARY.md").write_text(
        "# 2 real source-grounded I7 cases\n"
        f"API attempts: {state['attempts']}\nResponses: {state['returned']}\n"
        "User-supplied PDF version 2023, no certified 2026 applicability.\n"
        "No scored answer or learner approval. No answer key edits.\n", encoding="utf-8")
    print("User-I7 cases:", len(result["records"]), "returned:", state["returned"],
          "paid OpenAI calls: 0")
    return 0 if args.mode == "dry-run" or state["returned"] == 4 else 1


if __name__ == "__main__":
    sys.exit(main())
