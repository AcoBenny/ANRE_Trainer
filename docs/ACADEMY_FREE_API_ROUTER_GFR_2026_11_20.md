# ANRE Academy | Free API router pilot | 2026-11-20

## Purpose
Use the existing **six CKPT-256 negative fixtures**, without changing original ANRE questions, answer letters, HTML, APK or audit PR #7. All model outputs are preliminary practice, **not** technical/normative source validation, SME signoff or released exam answers.

## Inputs and routing
GitHub repository -> Settings -> Secrets and variables -> Actions -> Repository secrets:
- `GROQ_API_KEY` technical reviewer primary; fixed model `openai/gpt-oss-120b`.
- `GEMINI_API_KEY` independent skeptic primary; fixed model `gemini-2.5-flash-lite`.
- `OPENROUTER_API_KEY` fallback for 429/5xx, fixed router `openrouter/free`, which uses a free model.
- `OPENAI_API_KEY` is intentionally NOT injected into this workflow. **Paid calls disabled**.

Never put the raw key or even a screenshot of it into source control, PRs, issues, logs or chat. Secrets cannot be read back after saving. GitHub connector cannot reveal whether they are present, so the *live smoke test* is necessary to verify they actually work.

## Behaviour and limitations
- Offline tests run on PRs without access to secrets. Real model calls only run on **pushes to the exact trusted pilot branch**, after Python QA passes, and only on **one** fixture. No PR-triggered live calls and no scheduled repeat.
- Single smoke run: **2 independent roles**, up to **4 network API attempts**, per-provider fallback only for rate limit, timeout or server error; no fallback after auth errors or other unexpected 4xx. Global cap **24** attempts for the 6-case CLI.
- On a failed provider, output the HTTP **status only**. Raw HTTP response and all tokens/keys are never logged. A return that is empty also triggers fallback.
- No evidence of direct access to the referenced normatives is implied. The fixture rubric/expected answer and unsafe answer text are withheld from model prompts. Their full original QABC is not in the fixture; **not suitable for final ANRE QA**.
- Free routes do not guarantee zero charges if provider accounts have paid billing enabled. Review provider-side tier/budget limits. `openrouter/free` chooses the actual serving free model and may change between requests. Its real `model` identifier and token usage are recorded in the artifact.
- Successful independent reviewer outputs are only *raw traces*. A separate source-grounded reviewer must grade them. A model cannot self-certify exam keys.

## How to check
1. [GitHub Actions](https://github.com/AcoBenny/ANRE_Trainer/actions): open `ANRE Academy free-API router smoke / QA`. Its first PR/branch run does 7 offline tests; on trusted branch push it also attempts **only one free-tier case**.
2. Download the `academy-free-router-smoke` artifact and inspect `SUMMARY.md` + `results.json`: records contain requested provider, actually served model, usage, and full response. No source approval recorded.
3. Before any expansion to 6 cases or all 568 distinct QABC (822 grade IDs), require zero failed role reports, review actual cost/billing panels, verify versioned sources, independently score a sample, and preserve the separate audit/learner-approval gate.

## Manual local verification (no keys necessary)
```bash
python -m unittest discover -s tests -p 'test_academy_free_router.py' -v
python scripts/academy_free_router.py --fixtures path/to/six-fixtures.json --mode dry-run --cases 6
```

GitHub live smoke is disabled on merge to main; do not merge or release without approval.

Sources: [Groq models](https://console.groq.com/docs/models), [Google Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), [OpenRouter free router](https://openrouter.ai/openrouter/free), [GitHub security](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).
