"""Offline regression tests only; never access provider APIs."""
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch
from academy_freellmapi_pilot import EXPECTED, load_cases, make_prompt, parse_url, request_one, main


def sample():
    return {
        "original_questions_and_keys_immutable": True,
        "require_real_traces_for_pass": True,
        "cases": [
            {
                "id": i, "given": "Stem differs", "reference": "I7 source pointer",
                "category": "negative", "anre_ids": ["G1"],
                "required_behavior": ["secret rubrics withheld"],
                "unsafe_behavior": ["unsafe rubrics withheld"],
                "state": "REGISTERED_NOT_BENCHMARKED"
            } for i in sorted(EXPECTED)
        ],
    }


class Test(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = pathlib.Path(self.temp.name) / "cases.json"
        self.path.write_text(json.dumps(sample()), encoding="utf8")

    def test_fixture_validation(self):
        self.assertEqual(len(load_cases(self.path)), 6)

    def test_reject_modified_state(self):
        d = sample()
        d["cases"][0]["state"] = "APPROVED"
        self.path.write_text(json.dumps(d), encoding="utf8")
        with self.assertRaises(ValueError):
            load_cases(self.path)

    def test_reject_missing_or_duplicate(self):
        d = sample()
        d["cases"][0]["id"] = d["cases"][1]["id"]
        self.path.write_text(json.dumps(d), encoding="utf8")
        with self.assertRaises(ValueError):
            load_cases(self.path)

    def test_rubrics_not_in_prompt(self):
        prompt = make_prompt(sample()["cases"][0])
        self.assertNotIn("secret rubrics", prompt)
        self.assertNotIn("unsafe rubrics", prompt)

    def test_remote_requires_https(self):
        for url in ("http://example.com", "http://10.0.0.4:3001", "https://foo.com/v1?key=a"):
            with self.assertRaises(ValueError):
                parse_url(url)
        self.assertEqual(parse_url("http://localhost:3001"), "http://localhost:3001/v1")
        self.assertEqual(parse_url("https://safe.example/v1"), "https://safe.example/v1")

    def test_preflight_makes_no_calls(self):
        outfile = pathlib.Path(self.temp.name) / "report.json"
        with patch("sys.argv", ["pilot", "--fixtures", str(self.path), "--output", str(outfile)]), patch("urllib.request.urlopen") as request:
            self.assertEqual(main(), 0)
            request.assert_not_called()
        report = json.loads(outfile.read_text())
        self.assertEqual(report["qa_approved"], 0)
        self.assertEqual(report["ai_calls_attempted"], 0)

    def test_live_requires_explicit_consent(self):
        with patch("sys.argv", ["pilot", "--fixtures", str(self.path), "--mode", "live"]), patch.dict("os.environ", {}, clear=True), patch("urllib.request.urlopen") as request:
            self.assertEqual(main(), 2)
            request.assert_not_called()

    def test_model_routing_metadata_required(self):
        class Response:
            headers = {"X-Routed-Via": "groq/model-x", "X-Fallback-Attempts": "2"}
            def __enter__(self): return self
            def __exit__(self, *_): return None
            def read(self):
                return b'{"choices":[{"message":{"content":"uncertain"}}],"usage":{"total_tokens":12}}'
        with patch("urllib.request.urlopen", return_value=Response()):
            out = request_one("http://localhost:3001/v1", "fake", "auto", sample()["cases"][0])
        self.assertEqual(out["provider_model"], "groq/model-x")
        self.assertEqual(out["fallback_attempts"], "2")


if __name__ == "__main__":
    unittest.main()
