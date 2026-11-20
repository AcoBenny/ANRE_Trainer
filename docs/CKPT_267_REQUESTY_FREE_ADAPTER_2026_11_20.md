# CKPT-267 | Requesty free-only API adapter pilot | 2026-11-20

## Goal / bounded execution contract
User confirmed `REQUESTY_API_KEY` was added to GitHub Actions repository secrets (the secret cannot be read back over the GitHub connector). This branch adds a small Requesty adapter to existing `academy_free_router.py` with **two allowlisted, provider-specific free endpoints**, but does not yet place Requesty into the Academy role fallback chains. No question text or private user data is sent to Requesty in the connectivity probe.

Official docs (consulted 2026-11-20):
- https://docs.requesty.ai/ (OpenAI-compatible base `https://router.requesty.ai/v1`, Bearer API key)
- https://www.requesty.ai/pricing (free plan claims up to 200 requests/day for free models)
- https://www.requesty.ai/models/nvidia/nemotron-3.5-lightning-30b-a3b (exact `nvidia/nemotron-3.5-lightning-30b-a3b` free NVIDIA endpoint)
- https://www.requesty.ai/models/google/gemma-4-31b-it (exact `google/gemma-4-31b-it` free Google endpoint)

## Safety architecture
- Add `requesty_nano` and `requesty_gemma` models; disallow arbitrary paid model IDs by an exact free whitelist **before any network request**.
- A single explicit trusted-branch `[requesty]` commit triggers a connectivity test: trivial arithmetic question, **max 2 model requests**, no exam data, no other API secrets, no OpenAI paid calls.
- Report only provider, served model, finish reason, token usage and the cost amount if Requesty supplies it. Never log key or model text. If provider reports nonzero cost, stop rather than retry. Missing cost is labelled `UNKNOWN_NOT_ATTESTED` and must not be reported as proof of a zero bill.
- No PR secrets used. Pull requests execute only Python regression tests. No scheduled/background runs. Provider-side quota/billing still requires account dashboard verification.
- After passing actual connectivity and cost preflight, requesty may be added as the **last** fallback for technical/skeptic/linguistic roles; never accept duplicate actual serving-model IDs as independent review. A source-verbatim/qualified QA gate remains mandatory.

## Evidence so far
- Initial isolated offline CI preflight: https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44743194611 : PASS (Requesty adapter regression tests plus existing router tests); no secret/live API call in this run.
- This checkpoint commit launches exactly one actual free-model connectivity smoke. Check its separate run and `academy-requesty-free-probe` artifact before enabling the fallback.
- PR #13 Draft. PR #7 Draft. 0 original ANRE QABC, keys, HTML, APK or stable branch changes. No approvals for learning.

## Live first-probe outcome and versioned correction
- Run [44743300916](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44743300916) confirmed `REQUESTY_API_KEY` was injected, but older `nvidia/nemotron-3-nano-30b-a3b` returned `HTTP_410`. The job failed safely, attempted 1 call, returned no text, and sent no ANRE content.
- Retired old model removed from the active Requesty exact-free allowlist. Replaced with provider-pinned free endpoint `nvidia/nemotron-3.5-lightning-30b-a3b`, listed at https://www.requesty.ai/model/nvidia/nemotron-3.5-lightning-30b-a3b; `google/gemma-4-31b-it` retained as secondary free fallback.
- 410 is now treated as model-unavailable and may fall back to **the other allowlisted free model** only. No automatic paid switching.
- Updated offline regression run [44743559792](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44743559792) passed. This checkpoint commit triggers one new live Requesty smoke test, max 2 requests.
