# CKPT-277 | Academy targeted role recovery: 5/6 successful, one final QABC-0050 retry | 2026-11-20

## Real recovered review roles
- Run [44764156731](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44764156731), saved artifact `academy-p0-six-only-role-retests`: six exact missing specialist roles attempted via **seven API requests**, **five independent nonempty model responses**. Workflow returned nonzero as designed because one role failed; all other evidence preserved.
- QABC-0025 linguistic: Groq `openai/gpt-oss-20b`, 1 attempt, A/B/C analysis format PASS.
- QABC-0050 independent skeptic: Gemini `gemini-3.5-flash-lite`, 1 attempt, format PASS.
- QABC-0080 independent skeptic: Gemini `gemini-3.5-flash-lite`, 1 attempt, format PASS. Prior copied-only answer rejected; new model trace is a retest, not automatically source-truth.
- QABC-0091 linguistic and QABC-0096 linguistic: Groq `openai/gpt-oss-20b` each, 1 attempt, format PASS.
- **Only QABC-0050 linguistic remains incomplete**: Groq 20B returned `EMPTY_MODEL_OUTPUT`, Requesty Gemma `NETWORK_TIMEOUT` (2 provider attempts). All five successful slot reports are labelled `ROLE_RETEST_PRESENT_NOT_RECONCILED`. Reconciliation with earlier independent model traces and real source evidence is still mandatory.

## Single targeted technical fix and live validation
- Groq GPT-OSS 20B supports `reasoning_effort=low` in Chat Completions, documented at https://console.groq.com/docs/reasoning . This may reduce hidden reasoning tokens consuming the completion cap without guaranteeing semantic correctness.
- Router change applies **only** to `groq_linguistic`. New regression verifies request parameter, and retains distinct-model/cost/source gates.
- Explicit `[p0-last]` commit triggers **only** QABC-0050 linguistic reviewer via Groq 20B with Requesty Gemma fallback, max 2 free API attempts, no other QABC replay. Full original stem/options preserved with source SHA.
- This review is model evidence only, **not** official ANRE scored key, source authentication, 2026 edition verification, independent professional signoff or learner approval. No bareme/HTML/APK/main merge. PR #13 and PR #7 Draft.

After this test, prioritize exact primary-source/grade-semantic review; **do not initiate repetitive retry loops** when API quotas deny further attempts.
