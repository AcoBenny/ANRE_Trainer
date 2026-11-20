import json
import pathlib
import tempfile
import unittest
from unittest import mock

from scripts import academy_source_excerpt_i7_pilot as pilot

CONTEXT = pathlib.Path("docs/ACADEMY_NORMATIVE_CONTEXT_I7_2023_TWO_CLAUSES.json")


class GroundedI7Tests(unittest.TestCase):
    def test_verbatim_context_is_pinned(self):
        clauses = pilot.load_context(CONTEXT)
        self.assertEqual(set(clauses), {"QABC-0362", "QABC-0386"})
        self.assertEqual(clauses["QABC-0362"]["pdf_page"], 70)
        self.assertEqual(clauses["QABC-0386"]["pdf_page"], 72)

    def test_context_false_positive_rejected(self):
        original = json.loads(CONTEXT.read_text(encoding="utf-8"))
        original["clauses"][0]["text"] = "Alimentarea numai direct din tablou."
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "tampered.json"
            path.write_text(json.dumps(original, ensure_ascii=False), encoding="utf-8")
            with self.assertRaises(ValueError):
                pilot.load_context(path)

    def test_no_scoring_key_in_source_context(self):
        value = CONTEXT.read_text(encoding="utf-8")
        self.assertNotIn("original_exam_key=A", value)
        self.assertFalse(json.loads(value)["official_exam_scoring_keys_authenticated"])
        self.assertFalse(json.loads(value)["current_2026_applicability_verified"])

    def test_model_calls_not_requested_in_default_dry_run(self):
        # Safe by design: invalid ledger never reaches providers.
        with mock.patch.object(pilot, "route_agent") as provider:
            with self.assertRaises(FileNotFoundError):
                pilot.main(["--ledger", "/nonexistent/ledger.csv", "--context", str(CONTEXT)])
        provider.assert_not_called()


if __name__ == "__main__":
    unittest.main()
