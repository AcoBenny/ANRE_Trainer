#!/usr/bin/env python3
"""Single Requesty-backed Academy technical reviewer smoke, synthetic input only."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys

try:
    from .academy_agent_orchestrator import PROMPT_POLICY, SPECIALISTS
    from .academy_free_router import MODELS, route_agent
except ImportError:
    from academy_agent_orchestrator import PROMPT_POLICY, SPECIALISTS
    from academy_free_router import MODELS, route_agent

SYNTHETIC_QABC = {
    "case": "SYNTHETIC-NOT-ANRE-QUESTION",
    "stem": "Two ideal capacitors of 2 microfarads and 3 microfarads are connected in parallel. What is the total capacitance?",
    "A": "1 microfarad",
    "B": "5 microfarads",
    "C": "6 microfarads",
}


def run(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--confirm", default="")
    parser.add_argument("--out", type=pathlib.Path, default=pathlib.Path("_requesty_role_probe"))
    args = parser.parse_args(argv)
    if args.confirm != "FREE_ONLY":
        parser.error("Explicit --confirm FREE_ONLY required")
    if not os.getenv("REQUESTY_API_KEY"):
        print("Missing Requesty secret; no calls made", file=sys.stderr)
        return 2
    technical = next(r for r in SPECIALISTS if r[0] == "technical_electrical")
    if technical[1][-2:] != ("requesty_lightning", "requesty_gemma"):
        raise ValueError("Requesty not routed as last fallback in Academy specialist")
    system = (PROMPT_POLICY + "\n" + technical[2] +
              "\nReply concisely, with distinct labels A:, B:, C: and state "
              "that no source or official ANRE answer has been authenticated.")
    state = {"attempts": 0, "returned": 0}
    result = route_agent(system, json.dumps(SYNTHETIC_QABC, sort_keys=True),
                         ("requesty_lightning",), state)
    qa = {
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "kind": "SYNTHETIC_ROLE_ONLY_NO_INDEPENDENT_QA",
        "actual_attempts": state["attempts"],
        "actual_responses": state["returned"],
        "status": "MODEL_FAILED",
        "learner_approved": False,
        "source_authenticated": False,
        "paid_openai_calls": 0,
    }
    if result.get("ok"):
        actual_text = result["text"]
        coverage = {k: bool(re.search(r"\b" + k + r"\s*:", actual_text))
                    for k in ("A", "B", "C")}
        qa.update({
            "model": result["model"],
            "provider": result["provider"],
            "usage": result["usage"],
            "finish_reason": result["finish_reason"],
            "abc_labels_present_only": coverage,
            "status": ("FORMAT_VALID_BUT_SOURCE_AND_INDEPENDENT_QA_BLOCKED"
                       if all(coverage.values()) else "ABC_FORMAT_INCOMPLETE"),
        })
    else:
        qa["provider_errors_status_only"] = result.get("errors", [])
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "report.json").write_text(
        json.dumps(qa, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Academy Requesty role:", qa["status"], "| attempts:", qa["actual_attempts"],
          "| paid OpenAI: 0; no ANRE text or approval")
    return 0 if qa["status"] == "FORMAT_VALID_BUT_SOURCE_AND_INDEPENDENT_QA_BLOCKED" else 1


if __name__ == "__main__":
    sys.exit(run())
