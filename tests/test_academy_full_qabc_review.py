import csv
import json
import pathlib
import tempfile
import unittest
from unittest import mock

from scripts import academy_full_qabc_review as qabc


HEADERS = [
    "unit_id", "grade_ids", "source_workbook", "source_row", "evidence_url",
    "source_stem_from_workbook", "source_A_from_workbook",
    "source_B_from_workbook", "source_C_from_workbook",
    "current_stem_UNCHANGED", "current_A_UNCHANGED",
    "current_B_UNCHANGED", "current_C_UNCHANGED",
    "learning_release_approved", "canonical_modified",
    "source_original_answer_key_proven", "canonical_keys_UNCHANGED",
    "candidate_original_NOT_OFFICIAL_KEY", "technical_evidence_or_countermodel",
]


def ledger(path):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HEADERS)
        w.writeheader()
        for index, case_id in enumerate(sorted(qabc.EXPECTED_UNITS)):
            w.writerow({
                "unit_id": case_id, "grade_ids": "G1-ELE-001",
                "source_workbook": "source.xlsx", "source_row": "20",
                "evidence_url": "https://example.com/verified-by-human-later",
                "source_stem_from_workbook": "Original question",
                "source_A_from_workbook": "Source A",
                "source_B_from_workbook": "Source B",
                "source_C_from_workbook": "Source C",
                "current_stem_UNCHANGED": "Original question",
                "current_A_UNCHANGED": "Source A" if index else "Edited A",
                "current_B_UNCHANGED": "Source B",
                "current_C_UNCHANGED": "Source C",
                "learning_release_approved": "NO", "canonical_modified": "NO",
                "source_original_answer_key_proven": "NO",
                "canonical_keys_UNCHANGED": "SECRET_GRADING_KEY",
                "candidate_original_NOT_OFFICIAL_KEY": "LEAKED_CANDIDATE",
                "technical_evidence_or_countermodel": "LEAKED_RATIONALE",
            })


class ReviewQA(unittest.TestCase):
    def test_original_and_trainer_are_distinct(self):
        with tempfile.TemporaryDirectory() as temp:
            path = pathlib.Path(temp) / "ledger.csv"
            ledger(path)
            rows = qabc.load_ledger(path)
            case, changed = qabc.build_case(rows[0])
            self.assertEqual(changed, ["A"])
            self.assertEqual(case["original_workbook_QABC"]["A"], "Source A")
            self.assertEqual(case["trainer_current_QABC"]["A"], "Edited A")

    def test_whitespace_only_does_not_count_as_meaning_change(self):
        row = {
            "source_stem_from_workbook": " Sonerie  :  . ",
            "current_stem_UNCHANGED": "Sonerie : .",
            "source_A_from_workbook": "numai din tablou",
            "current_A_UNCHANGED": "numai din tablou",
            "source_B_from_workbook": " numai din circuit",
            "current_B_UNCHANGED": "numai din circuit",
            "source_C_from_workbook": "din circuit",
            "current_C_UNCHANGED": "numai din circuit",
        }
        self.assertEqual(qabc.changed_after_whitespace_normalization(row), ["C"])

    def test_keys_and_rationale_never_sent(self):
        with tempfile.TemporaryDirectory() as temp:
            path = pathlib.Path(temp) / "ledger.csv"
            ledger(path)
            case, _ = qabc.build_case(qabc.load_ledger(path)[0])
            text = json.dumps(case)
            self.assertNotIn("SECRET_GRADING_KEY", text)
            self.assertNotIn("LEAKED_CANDIDATE", text)
            self.assertNotIn("LEAKED_RATIONALE", text)

    def test_dry_run_no_provider_calls_and_no_approval(self):
        with tempfile.TemporaryDirectory() as temp:
            path = pathlib.Path(temp) / "ledger.csv"
            ledger(path)
            out = pathlib.Path(temp) / "out"
            with mock.patch.object(qabc, "route_agent") as api:
                result = qabc.main(["--ledger", str(path), "--out", str(out)])
            self.assertEqual(result, 0)
            api.assert_not_called()
            data = json.loads((out / "results.json").read_text())
            self.assertEqual(data["cases"], 6)
            self.assertEqual(data["paid_openai_calls"], 0)
            self.assertEqual(data["verified_official_sources"], 0)
            self.assertFalse(data["learner_approved"])

    def test_reject_modified_release_gate(self):
        with tempfile.TemporaryDirectory() as temp:
            path = pathlib.Path(temp) / "ledger.csv"
            ledger(path)
            text = path.read_text()
            path.write_text(text.replace(",NO,NO,NO,", ",YES,NO,NO,", 1))
            with self.assertRaises(ValueError):
                qabc.load_ledger(path)

    def test_live_mode_explicit_confirmation(self):
        with tempfile.TemporaryDirectory() as temp:
            path = pathlib.Path(temp) / "ledger.csv"
            ledger(path)
            with self.assertRaises(SystemExit):
                qabc.main(["--ledger", str(path), "--mode", "live-free"])


if __name__ == "__main__":
    unittest.main()
