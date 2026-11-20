#!/usr/bin/env python3
"""One-shot, safe Requesty free-model connectivity probe (no ANRE user content)."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import sys

try:
    from .academy_free_router import (MODELS, REQUESTY_FREE_MODEL_IDS,
                                      ProviderError, call_provider)
except ImportError:
    from academy_free_router import (MODELS, REQUESTY_FREE_MODEL_IDS,
                                     ProviderError, call_provider)

PROBE_ORDER = ("requesty_nano", "requesty_gemma")
QUESTION = "Reply with only the number that equals 2 + 2."


def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--confirm", default="")
    parser.add_argument("--out", type=pathlib.Path, default=pathlib.Path("_requesty_probe"))
    args = parser.parse_args(argv)

    # Explicit opt-in; never test without the saved key.
    if args.confirm != "FREE_ONLY":
        parser.error("Use --confirm FREE_ONLY for one brief free-model probe")
    if not os.environ.get("REQUESTY_API_KEY"):
        print("REQUESTY_API_KEY is missing from GitHub Actions secrets", file=sys.stderr)
        return 2
    report = {
        "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "purpose": "Requesty free-model connectivity only, no ANRE questions",
        "requesty_key_present": True,
        "requests_attempted": 0,
        "providers": [],
        "paid_openai_calls": 0,
        "canonical_modified": False,
        "learner_approved": False,
    }
    output = args.out
    output.mkdir(parents=True, exist_ok=True)
    worked = False
    for provider in PROBE_ORDER:
        model = MODELS[provider]
        if model not in REQUESTY_FREE_MODEL_IDS:
            raise ValueError("Refusing non-allowlisted Requesty model before any API request")
        report["requests_attempted"] += 1
        record = {"provider": provider, "requested_model": model}
        try:
            result = call_provider(provider, "Give a short factual arithmetic answer.", QUESTION)
            record["actual_model"] = result["model"]
            record["finish_reason"] = result["finish_reason"]
            record["usage"] = result["usage"]
            cost = result["usage"].get("cost") if isinstance(result["usage"], dict) else None
            if cost is None:
                record["reported_cost_usd"] = "UNKNOWN_NOT_ATTESTED"
            else:
                try:
                    record["reported_cost_usd"] = float(cost)
                except (ValueError, TypeError):
                    record["reported_cost_usd"] = "UNKNOWN_UNREADABLE"
            record["status"] = "NONEMPTY_MODEL_RESPONSE"
            if isinstance(record["reported_cost_usd"], float) and record["reported_cost_usd"] > 0:
                record["status"] = "NONZERO_REPORTED_COST_STOP"
                report["providers"].append(record)
                break
            worked = True
            report["providers"].append(record)
            break
        except ProviderError as exc:
            record["status"] = exc.code
            report["providers"].append(record)
            if not exc.fallback_ok:
                break
    (output / "summary.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Requesty free probe:", "SUCCESS" if worked else "FAIL",
          "attempts:", report["requests_attempted"])
    for record in report["providers"]:
        print("Provider:", record["provider"], "status:", record["status"],
              "model:", record.get("actual_model", "none"),
              "reported cost USD:", record.get("reported_cost_usd", "not returned"))
    print("No ANRE content sent; no source or exam answer approved.")
    return 0 if worked else 1


if __name__ == "__main__":
    sys.exit(run())
