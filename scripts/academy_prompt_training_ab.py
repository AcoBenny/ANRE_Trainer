#!/usr/bin/env python3
"""Real prompt-training A/B experiment; not model weight training or exam approval."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import sys

try:
    from .academy_full_qabc_review import build_case, load_ledger, TECHNICAL, SKEPTIC
    from .academy_source_excerpt_i7_pilot import load_context
    from .academy_p0_priority_training import TRAINING_RECIPE, TRAINING_RULES
    from .academy_free_router import route_agent
except ImportError:
    from academy_full_qabc_review import build_case, load_ledger, TECHNICAL, SKEPTIC
    from academy_source_excerpt_i7_pilot import load_context
    from academy_p0_priority_training import TRAINING_RECIPE, TRAINING_RULES
    from academy_free_router import route_agent

SELECTED_IDS = ("QABC-0362", "QABC-0386")
ROLES = (
    ("technical", ("groq",), TECHNICAL, "Technical electrical source object and options"),
    ("skeptic", ("gemini",), SKEPTIC, "Independent source-scope skeptic"),
)
POLICIES = ("baseline", "trained")
MAX_ATTEMPTS = 8


def build_blind_case(row: dict, clause: dict) -> str:
    original, _ = build_case(row)
    return json.dumps({
        "original_workbook": original["original_workbook_QABC"],
        "trainer_current": original["trainer_current_QABC"],
        "unit_id": row["unit_id"],
        "grade_ids": row["grade_ids"].split("|"),
        "source_excerpt_user_supplied_2023": {
            "section": clause["section"], "text": clause["text"],
            "pdf_page": clause["pdf_page"],
        },
        "source_currentness_2026": "NOT_VERIFIED",
        "official_exam_scoring_key": "NOT_VERIFIED",
    }, ensure_ascii=False, sort_keys=True)


def trained_instruction(role: str, description: str) -> str:
    return (
        TRAINING_RULES + " Independent role: " + role + ". " + description +
        " Inspect SOURCE ORIGINAL and TRAINER CURRENT separately; do not transfer "
        "a corrected trainer choice to the original workbook question. "
        "In each of A:, B:, C: name both original and trainer option by meaning. "
        "Mention exact paragraph wording and its limits, never quote unseen norms. "
        "Source evidence from user's 2023 PDF does not prove 2026 law applicability "
        "or ANRE scored key. No answer may be marked learner-approved."
    )


def write_result(path: pathlib.Path, report: dict):
    path.mkdir(parents=True, exist_ok=True)
    (path / "results.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (path / "SUMMARY.md").write_text(
        "# Academy prompt A/B real-provider training pilot\n\n"
        "Existing prompts versus source-scope trained prompts for the same two I7 cases.\n"
        f"Calls: {report['attempts']} / {MAX_ATTEMPTS}\n"
        f"Completed outputs: {report['returned']}\n"
        "All grades and text unchanged. No 2026 edition, scored key, independent expert, "
        "learner approval or model-weight fine-tuning proven.\n"
        "This is a pilot with one run per condition, not a statistically reliable benchmark.\n",
        encoding="utf-8")


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", type=pathlib.Path, required=True)
    p.add_argument("--context", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path, default=pathlib.Path("_academy_training_ab"))
    p.add_argument("--mode", choices=("dry-run", "live-free"), default="dry-run")
    p.add_argument("--confirm", default="")
    args = p.parse_args(argv)
    if args.mode == "live-free" and args.confirm != "FREE_ONLY":
        p.error("Live A/B experiment requires FREE_ONLY")
    ledger = {row["unit_id"]: row for row in load_ledger(args.ledger)}
    context = load_context(args.context)
    if set(context) != set(SELECTED_IDS) or any(uid not in ledger for uid in SELECTED_IDS):
        raise ValueError("Unverified source case ID found")
    report = {
        "run_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "training_recipe": TRAINING_RECIPE,
        "ledger_sha256": hashlib.sha256(args.ledger.read_bytes()).hexdigest(),
        "source_context_sha256": hashlib.sha256(args.context.read_bytes()).hexdigest(),
        "mode": args.mode, "attempts": 0, "returned": 0, "results": [],
        "learner_approved": False, "model_weights_changed": False,
        "independent_professional_qa": False, "official_2026_source_validated": False,
        "paid_openai_calls": 0,
    }
    state = {"attempts": 0, "returned": 0}
    for unit_id in SELECTED_IDS:
        row = ledger[unit_id]
        message = build_blind_case(row, context[unit_id])
        for role, candidates, existing_instruction, role_description in ROLES:
            for policy in POLICIES:
                rec = {
                    "unit_id": unit_id, "role": role, "policy": policy,
                    "input_sha256": hashlib.sha256(message.encode()).hexdigest(),
                    "same_primary_provider": candidates[0],
                }
                if args.mode == "live-free":
                    if state["attempts"] >= MAX_ATTEMPTS:
                        rec["ok"] = False
                        rec["failure"] = "HARD_8_CALL_LIMIT"
                    else:
                        instruction = (existing_instruction if policy == "baseline"
                                       else trained_instruction(role, role_description))
                        reply = route_agent(instruction, message, candidates, state)
                        rec["result"] = reply
                        rec["ok"] = reply.get("ok", False)
                        rec["semantic_qa"] = "NOT_RUN_REQUIRES_SOURCE_BASED_INDEPENDENT_REVIEW"
                report["results"].append(rec)
                report["attempts"], report["returned"] = state["attempts"], state["returned"]
                write_result(args.out, report)
    print("Training A/B cases: 2; real API attempts:", state["attempts"],
          "nonempty model outputs:", state["returned"], "paid OpenAI: 0")
    if args.mode == "live-free" and (state["attempts"] != 8 or state["returned"] != 8):
        print("Incomplete baseline/trained comparison, do not certify", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
