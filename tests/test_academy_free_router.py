import json
import os
import pathlib
import tempfile
import unittest
from unittest import mock

from scripts import academy_free_router as router


def fixture_file(folder):
    cases = []
    for i in range(1, 7):
        cases.append({
            "id": f"ACA-ANRE-{i:03d}",
            "category": "SCOPE_CHECK",
            "given": "Verify source context and grade scope",
            "reference": "A test-only public source",
            "anre_ids": ["G1-ELE-001"],
            "required_behavior": ["Detect incorrect source"],
            "unsafe_behavior": ["Guess the answer"],
            "state": "REGISTERED_NOT_BENCHMARKED",
        })
    path = folder / "fixture.json"
    path.write_text(json.dumps({"original_questions_and_keys_immutable": True, "cases": cases}))
    return path


class RouterTests(unittest.TestCase):
    def test_six_immutable_cases_required(self):
        with tempfile.TemporaryDirectory() as temp:
            path = fixture_file(pathlib.Path(temp))
            self.assertEqual(len(router.read_cases(path)), 6)
            obj = json.loads(path.read_text())
            obj["cases"][0]["id"] = "DUPLICATE"
            path.write_text(json.dumps(obj))
            with self.assertRaises(ValueError):
                router.read_cases(path)

    def test_do_not_leak_grading_rubric_into_prompt(self):
        case = {"id": "ACA-ANRE-001", "anre_ids": ["G1-NOR-001"],
                "category": "TEST", "given": "case", "reference": "ref",
                "required_behavior": ["SECRET_ANSWER"], "unsafe_behavior": ["SECRET_DISTRACTOR"]}
        rendered = router.build_prompt(case)
        self.assertNotIn("SECRET_ANSWER", rendered)
        self.assertNotIn("SECRET_DISTRACTOR", rendered)

    def test_fallback_on_rate_limit_only_to_free_openrouter(self):
        state = {"attempts": 0, "returned": 0}
        def simulate(provider, system, prompt):
            if provider == "groq":
                raise router.ProviderError("HTTP_429", True)
            return {"model": "example-free:free", "usage": {"total_tokens": 5}, "text": "review"}
        with mock.patch.dict(os.environ, {"GROQ_API_KEY": "fake", "OPENROUTER_API_KEY": "fake"}):
            with mock.patch.object(router, "call_provider", side_effect=simulate) as fn:
                result = router.route_agent("role", "case", ("groq", "openrouter"), state)
        self.assertTrue(result["ok"])
        self.assertEqual(result["provider"], "openrouter")
        self.assertEqual(result["model"], "example-free:free")
        self.assertEqual(state["attempts"], 2)
        self.assertEqual(fn.call_count, 2)

    def test_auth_failure_never_attempts_fallback(self):
        state = {"attempts": 0, "returned": 0}
        with mock.patch.dict(os.environ, {"GROQ_API_KEY": "fake", "OPENROUTER_API_KEY": "fake"}):
            with mock.patch.object(router, "call_provider", side_effect=router.ProviderError("HTTP_401", False)) as fn:
                result = router.route_agent("role", "case", ("groq", "openrouter"), state)
        self.assertFalse(result["ok"])
        self.assertEqual(fn.call_count, 1)

    def test_hard_call_cap_prevents_network(self):
        state = {"attempts": router.MAX_TOTAL_CALLS, "returned": 0}
        with mock.patch.dict(os.environ, {"GROQ_API_KEY": "fake"}):
            with mock.patch.object(router, "call_provider") as fn:
                result = router.route_agent("role", "case", ("groq",), state)
        self.assertFalse(result["ok"])
        fn.assert_not_called()

    def test_dry_run_no_network_and_no_approval(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = pathlib.Path(temp)
            fixture = fixture_file(folder)
            with mock.patch.object(router, "post_json") as fn:
                result = router.main(["--fixtures", str(fixture), "--out", str(folder / "out"),
                                      "--mode", "dry-run", "--cases", "6"])
            self.assertEqual(result, 0)
            fn.assert_not_called()
            report = json.loads((folder / "out" / "results.json").read_text())
            self.assertEqual(report["attempted"], 0)
            self.assertFalse(report["learner_approved"])

    def test_live_requires_positive_confirmation(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = fixture_file(pathlib.Path(temp))
            with self.assertRaises(SystemExit):
                router.main(["--fixtures", str(fixture), "--mode", "live-free"])


if __name__ == "__main__":
    unittest.main()
