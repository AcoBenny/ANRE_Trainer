import json
import os
import pathlib
import tempfile
import unittest
from unittest import mock

from scripts import academy_free_router as router
from scripts import academy_requesty_probe as probe


class RequestyAdapterTests(unittest.TestCase):
    def test_only_two_documented_provider_specific_free_models(self):
        self.assertEqual(router.MODELS["requesty_lightning"],
                         "nvidia/nemotron-3.5-lightning-30b-a3b")
        self.assertEqual(router.MODELS["requesty_gemma"],
                         "google/gemma-4-31b-it")
        self.assertTrue(all(router.MODELS[p] in router.REQUESTY_FREE_MODEL_IDS
                            for p in probe.PROBE_ORDER))
        self.assertNotIn("OPENAI_API_KEY", [router.KEYS[p] for p in probe.PROBE_ORDER])
        self.assertEqual(router.KEYS["requesty_lightning"], "REQUESTY_API_KEY")

    def test_adapter_uses_correct_requesty_url_auth_and_short_prompt(self):
        fake = {
            "model": "nvidia/nemotron-3.5-lightning-30b-a3b",
            "choices": [{"finish_reason": "stop",
                         "message": {"content": "4"}}],
            "usage": {"total_tokens": 31, "cost": 0},
        }
        with mock.patch.dict(os.environ, {"REQUESTY_API_KEY": "FAKE_API_KEY"},
                             clear=False):
            with mock.patch.object(router, "post_json", return_value=fake) as fn:
                result = router.call_provider(
                    "requesty_lightning", "answer simply", "2 + 2?")
        self.assertEqual(result["text"], "4")
        self.assertEqual(fn.call_count, 1)
        url, headers, payload = fn.call_args.args
        self.assertEqual(url, "https://router.requesty.ai/v1/chat/completions")
        self.assertEqual(headers["Authorization"], "Bearer FAKE_API_KEY")
        self.assertEqual(payload["model"], router.MODELS["requesty_lightning"])
        self.assertNotIn("OPENAI_API_KEY", headers)

    def test_non_allowlisted_model_stops_before_network(self):
        with mock.patch.dict(router.MODELS,
                             {"requesty_lightning": "openai/gpt-5.6-sol"}):
            with mock.patch.object(router, "post_json") as network:
                with self.assertRaises(router.ProviderError) as ctx:
                    router.call_provider("requesty_lightning", "a", "b")
                network.assert_not_called()
                self.assertEqual(ctx.exception.code,
                                 "REQUESTY_MODEL_NOT_ALLOWLISTED_AS_FREE")

    def test_requesty_cost_missing_or_nonzero_blocked_in_role_router(self):
        base = {
            "model": router.MODELS["requesty_lightning"],
            "choices": [{"message": {"content": "Reasoned answer."},
                         "finish_reason": "stop"}],
        }
        with mock.patch.dict(os.environ, {"REQUESTY_API_KEY": "fake"}):
            for usage, code in (
                ({"total_tokens": 12}, "REQUESTY_COST_NOT_ATTESTED"),
                ({"cost": 0.005, "total_tokens": 12}, "REQUESTY_NONZERO_REPORTED_COST"),
            ):
                with mock.patch.object(router, "post_json", return_value={
                    **base, "usage": usage,
                }):
                    with self.assertRaises(router.ProviderError) as ctx:
                        router.call_provider("requesty_lightning", "review", "some question")
                    self.assertEqual(ctx.exception.code, code)

    def test_gateway_served_model_must_match_pinned_free_endpoint(self):
        fake = {
            "model": "openai/paid-model",
            "choices": [{"message": {"content": "not appropriate"},
                         "finish_reason": "stop"}],
            "usage": {"cost": 0},
        }
        with mock.patch.dict(os.environ, {"REQUESTY_API_KEY": "fake"}):
            with mock.patch.object(router, "post_json", return_value=fake):
                with self.assertRaises(router.ProviderError) as ctx:
                    router.call_provider("requesty_lightning", "system", "message")
        self.assertEqual(ctx.exception.code, "REQUESTY_UNEXPECTED_SERVED_MODEL")

    def test_requesty_is_last_fallback_when_other_keys_absent(self):
        with mock.patch.dict(os.environ, {
                "GROQ_API_KEY": "", "GEMINI_API_KEY": "",
                "OPENROUTER_API_KEY": "", "REQUESTY_API_KEY": "fake"}):
            with mock.patch.object(router, "call_provider", return_value={
                "model": router.MODELS["requesty_lightning"],
                "text": "source checks need confirmation",
                "finish_reason": "stop", "usage": {"cost": 0},
            }) as fn:
                role_name, candidates, instruction = router.AGENTS[0]
                state = {"attempts": 0, "returned": 0}
                result = router.route_agent("source auditor", "test", candidates, state)
        self.assertEqual(result["provider"], "requesty_lightning")
        self.assertEqual(fn.call_count, 1)
        self.assertEqual(state["attempts"], 1)

    def test_missing_key_means_no_requests(self):
        with tempfile.TemporaryDirectory() as root:
            with mock.patch.dict(os.environ, {"REQUESTY_API_KEY": ""}):
                with mock.patch.object(probe, "call_provider") as fn:
                    status = probe.run(["--out", root, "--confirm", "FREE_ONLY"])
                fn.assert_not_called()
        self.assertEqual(status, 2)

    def test_probe_success_writes_no_answer_or_secrets(self):
        with tempfile.TemporaryDirectory() as root:
            with mock.patch.dict(os.environ, {"REQUESTY_API_KEY": "FAKE_SECRET"}):
                with mock.patch.object(probe, "call_provider", return_value={
                    "model": router.MODELS["requesty_lightning"],
                    "finish_reason": "stop",
                    "text": "4",
                    "usage": {"cost": 0.0, "total_tokens": 30},
                }) as fn:
                    result = probe.run(["--out", root, "--confirm", "FREE_ONLY"])
            self.assertEqual(result, 0)
            self.assertEqual(fn.call_count, 1)
            output = (pathlib.Path(root) / "summary.json").read_text()
            self.assertNotIn("FAKE_SECRET", output)
            self.assertNotIn('"text"', output)
            self.assertEqual(json.loads(output)["requests_attempted"], 1)
            self.assertEqual(json.loads(output)["providers"][0]["reported_cost_usd"], 0)

    def test_rate_limit_can_use_secondary_free_model_only(self):
        with tempfile.TemporaryDirectory() as root:
            def provider(name, system, message):
                if name == "requesty_lightning":
                    raise router.ProviderError("HTTP_429", True)
                return {"model": router.MODELS[name], "finish_reason": "stop",
                        "text": "4", "usage": {"cost": 0.0}}
            with mock.patch.dict(os.environ, {"REQUESTY_API_KEY": "fake"}):
                with mock.patch.object(probe, "call_provider", side_effect=provider) as fn:
                    result = probe.run(["--out", root, "--confirm", "FREE_ONLY"])
            self.assertEqual(result, 0)
            self.assertEqual(fn.call_count, 2)
            report = json.loads((pathlib.Path(root)/"summary.json").read_text())
            self.assertEqual(report["providers"][1]["provider"], "requesty_gemma")

    def test_requesty_nonzero_cost_blocks_and_does_not_retry(self):
        with tempfile.TemporaryDirectory() as root:
            with mock.patch.dict(os.environ, {"REQUESTY_API_KEY": "fake"}):
                with mock.patch.object(probe, "call_provider", return_value={
                    "model": router.MODELS["requesty_lightning"],
                    "finish_reason": "stop", "text": "4", "usage": {"cost": 0.01},
                }) as fn:
                    result = probe.run(["--out", root, "--confirm", "FREE_ONLY"])
            self.assertEqual(result, 1)
            self.assertEqual(fn.call_count, 1)
            report = json.loads((pathlib.Path(root)/"summary.json").read_text())
            self.assertEqual(report["providers"][0]["status"],
                             "NONZERO_REPORTED_COST_STOP")

    def test_invalid_secret_does_not_try_secondary_provider(self):
        with tempfile.TemporaryDirectory() as root:
            with mock.patch.dict(os.environ, {"REQUESTY_API_KEY": "fake"}):
                with mock.patch.object(probe, "call_provider",
                                       side_effect=router.ProviderError("HTTP_401", False)) as fn:
                    result = probe.run(["--out", root, "--confirm", "FREE_ONLY"])
            self.assertEqual(result, 1)
            self.assertEqual(fn.call_count, 1)

    def test_probe_requires_explicit_confirmation(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(SystemExit):
                probe.run(["--out", root])


if __name__ == "__main__":
    unittest.main()
