# CKPT | ANRE Academy free API router GFR | 2026-11-20

## Actual executed work (not speculation)
- Draft PR: https://github.com/AcoBenny/ANRE_Trainer/pull/13. Base main. No merge. No changes to original ANRE QABC/answer keys/HTML/APK. Audit PR #7 and Cloudflare PR #11 remain Draft.
- Synthetic offline Python regression suite: **9/9 PASS** on GitHub Actions. Tests protect no API calls during dry-run, untrusted fixture IDs, withholding reference rubric, paid OpenAI exclusion, explicit free-model fallback and a hard call cap. CI: https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44731519886
- Live one-case smoke: 2 distinct evaluator-model calls, both successful, Groq `openai/gpt-oss-120b` and Google `gemini-3.5-flash-lite`. GitHub Actions run: https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44731640801
- Live six CKPT-256 negative fixtures: **6/6 cases, 12/12 model responses, 12 API attempts**. Groq 6 replies (1,384 input; 5,100 completion; **6,484 reported total tokens**), Gemini 6 replies (976 input; 3,857 candidate; **4,833 reported total tokens**). Totals are provider-reported token fields and cannot be read as dollars. Run + expiring artifacts: https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44731805659
- Separate OpenRouter actual free-only probe: fixed `google/gemma-4-31b-it:free` initially HTTP 429; fallback `openrouter/free` returned an answer served by **`recursive/flint-v1.0:free`**, using 327 total tokens. Run: https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44732071601
- **No OpenAI paid call**; `OPENAI_API_KEY` not injected into the active workflow. Groq, Gemini and OpenRouter secrets authenticated for at least one live successful API response.

## Failure/supersession notes
- Initial Groq 403 under default Python-urllib client; descriptive User-Agent allowed later Groq responses. Never claim 403 could only indicate invalid key.
- Gemini `gemini-2.5-flash-lite` returned 404 for this newly created project; changed to currently available free-tier `gemini-3.5-flash-lite`, returned six successful answers. Google forum documents 2.5 access restrictions for newer users.
- Initial `openrouter/free` yielded an empty model response with 850 max tokens; a larger max output plus a fixed free fallback are implemented. Probe confirms it can serve a free model but quota can still be exhausted.

## Gates still pending
1. This is **prompt/evaluator execution**, not fine-tuning of model weights, human specialist review, legal/normative source authentication, or scientific proof that any ANRE answer key is correct.
2. Six negative fixtures give concise situation statements, not original full QABC or authenticated norm paragraphs. Model outputs still need independent semantic grading against the withheld reference rubrics, then source checks.
3. **0 / 822 learner-approved** remains the release gate. No automation may alter barems or app files, or merge/release.
4. No trustworthy dollar spend measurement is available from these responses; inspect Groq/Gemini/OpenRouter billing consoles. Free-tier membership and no paid billing must be checked at the provider-account level. Hard maximum is **24 provider attempts per 6-case run** and 850/1800 output-token caps per call. Branch-run live calls require explicit trusted commit marker `[smoke]`. No schedules/background loops exist.

## Next logical step
- Preserve this measured baseline, review all 12 traces using a **separate rubric-only evaluator** and independently inspect actual primary sources.
- Run identical source-authenticated QABC data with specialist-vs-baseline comparisons, blinded QA, provenance and reversible checkpoints.
- Prepare final ANRE knowledge approval only after source edition + A/B/C + second review are passed. Do not automatically edit canonical bank or trainer.
