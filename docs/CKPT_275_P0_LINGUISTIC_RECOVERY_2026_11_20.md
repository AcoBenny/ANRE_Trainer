# CKPT-275 | P0 linguistic failover to distinct Groq model | 2026-11-20

## Exact reason
Prior P0 remaining-eight run [44761592780](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44761592780) produced 16 outputs across 37 provider attempts, with most missing roles at OpenRouter/Requesty 429 or timeout. Repeating all eight cases would waste calls. Detailed six-role queue: [CKPT-274](CKPT_274_P0_EIGHT_REAL_API_REPORTS_AND_6_ROLE_RETEST_QUEUE_2026_11_20.md).

## Bounded fallback improvement and live test
- Existing Groq technical reviewer runs `openai/gpt-oss-120b`. For **linguistic reviewer only**, use *different actual model* `openai/gpt-oss-20b` on the Groq API, which has an advertised free tier. See https://console.groq.com/docs/rate-limits and https://console.groq.com/docs/model/openai/gpt-oss-20b . This is **not the paid OpenAI API**. Free-tier access is account-dependent; no promise of cost or unlimited use.
- Source-preserving role selector `SPECIALISTS` now routes linguistic to `groq_linguistic` first, then bounded explicit `requesty_gemma` fallback. Both are independent actual model IDs versus Groq GPT-OSS-120B and Gemini 3.5 Flash-Lite when those are available.
- Existing Python suite verified deterministic tests, including new role-routing assertion, without network.
- **This explicitly gated [p0-single] push** runs exactly `QABC-0065` linguistic reviewer alone, with max 2 provider attempts, preserving original options, response and usage as a short-lived CI artifact. No other question/role is replayed. Successful output is `ROLE_RETEST_PRESENT_NOT_RECONCILED` and requires reconciliation with previously saved Groq/Gemini roles.
- Source and 2026 applicability unknown; no independent professional source review, official key or learner approval. No canonical QABC/key/HTML/APK/main changes or merge. PR #13 and PR #7 remain Draft.
