# CKPT-268 | Requesty free API integrated with Avengers Academy | 2026-11-20

## Real execution, strictly verified
- User confirmed GitHub Actions repository secret `REQUESTY_API_KEY`; API connectivity independently confirmed by GitHub Actions. **No secret value was read, copied to source, logged or shared.**
- First attempt on retired model `nvidia/nemotron-3-nano-30b-a3b`: HTTP 410; run [44743300916](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44743300916). Removed the retired model from the live free allowlist.
- Replacement `nvidia/nemotron-3.5-lightning-30b-a3b`: actual call `stop`, `usage.cost=0`, `169` tokens; [44743640687](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44743640687). This proves **one free API response**, not an unlimited free allowance.
- First real Academy synthetic Q/A/B/C role call produced **EMPTY_MODEL_OUTPUT** through Lightning; blocked safely, no content gate pass. Run [44744533441](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44744533441).
- Second targeted live Academy synthetic role run [44744868106](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44744868106): **2 free API attempts, 1 completed response**, fallback `requesty_gemma` served `google/gemma-4-31b-it`, `usage.cost=0`, 1,071 tokens, `finish_reason=stop`. A/B/C headings present. Source verification NOT performed; independent expert/model QA NOT performed; **no learner key approved**.
- The request was a **synthetic** capacitor question, not a user's original ANRE workbook question. No original question/key/HTML/APK was sent or changed by these smoke tests.

## Implemented final integration
- `scripts/academy_free_router.py`: Requesty two exact, provider-pinned free-model allowlist; `requesty_gemma` before `requesty_lightning` **after** direct Groq/Gemini and existing free OpenRouter fallbacks. Reject not-allowlisted models before network, unexpected served model, missing/nonzero reported cost, invalid key, and incomplete outputs. Free-model quota and future dollar cost still require checking in Requesty account dashboard.
- `scripts/academy_agent_orchestrator.py`: adaptive electrical specialist, blind skeptic, and optional linguistic reviewer can use Requesty as the final free fallback. Distinct gateway labels serving the same underlying base model do **not** count as independent model evaluation. No auto-learning/model fine-tuning or model answer key promotion.
- `scripts/academy_requesty_probe.py`, `scripts/academy_requesty_role_smoke.py` and 15 Requesty-specific regression tests.
- Existing gated live Academy GitHub Actions workflow steps receive `REQUESTY_API_KEY` only on trusted branch + explicit commit marker. No PR-triggered real calls; no scheduled automated work. Paid OpenAI API key never injected into these workflows.
- All current-head GitHub Actions tests **PASSED** at commit `2f2768b9000d6917fc2c9fac42392d5cda3e934b`: [Requesty 15 + router 9 tests](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44745224568), [orchestrator 16 tests](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44745224636); other source-fidelity CI also passed at same SHA.
- No large ANRE batch was run automatically using Requesty in this checkpoint. Only implementation, the isolated test and the synthetic one-role test are verified.

## Security / limits and next action
- Requesty official public pricing advertises free models and **200 free requests/day** on the free plan, but rate/cost conditions can change. See https://www.requesty.ai/pricing and https://www.requesty.ai/models/free .
- Provider `usage.cost=0` was observed for individual calls, **not proof of a future universal zero balance**. Check Requesty spend limits/console. If provider cost becomes nonzero, the adapter marks the result as rejected, but cannot undo a charge already incurred.
- The free tier may permit training/data usage depending on provider and terms. Do not send confidential data or private credentials; all tests here use synthetic content. Review https://www.requesty.ai/terms .
- Academy answers remain provisional; source-specific electrical and linguistic QA, exact edition/grade and qualified independent validation required. **0/822 student-learning approvals** remains the release gate.
- Existing PR #13 stays Draft. Audit PR #7 stays Draft. No merge/release/main/answer-key/question/HTML/APK writes. Next: continue source-backed QABC QA in small, bounded lots, with all API model outputs checked rather than automatically trusted.
