# CKPT-264 | Avengers Asamble API-role integration (ANRE) | 2026-11-20

## Contract / status
- PR #13 branch `academy/free-api-router-gfr-20261120`, Draft; PR #7 independent audit Draft. Original ANRE QABC, keys, HTML and APK remain untouched. No merge/release.
- **Source queue**: `docs/ACADEMY_NEXT_12_EXACT_SOURCE_QABC_QUEUE_2026_11_20.json`, pinned Git blob `dc66cf1aa4ff96afe11385b5c6f59c27727f16e1` (12 QABC / 24 grade IDs).
- **Specialists** are real, separate API calls only when the explicitly gated `[academy]` workflow is used. The skill named `avengers-asamble/agent-router` itself is a selector/rule book, not an external subagent runtime.
- **Prompt Architect** = a deterministic, versioned prompt compiler, **not a separate executed AI model**.
- **Adaptive Selector** = chooses two blind, independent API roles for all cases, and adds an independent linguistic/scope model for prior risk flags QABC-0001/0005/0007/0011. Risk flag rationale is withheld from model prompts.
- **Electrical Technical Specialist** => Groq GPT-OSS 120B with free OpenRouter fallback.
- **Independent Skeptic** => Gemini Flash-Lite with free OpenRouter fallback.
- **Linguistic/Scope Reviewer** => OpenRouter free; requested only on semantically flagged cases.
- **Source-version Auditor** and **QA gate** = deterministic no-source-status and post-response checks; do **not** claim to have read or authenticated normative source paragraphs. Independent qualified human/external expert QA remains NOT_RUN.

## Security and anti-false-positive controls
- Each role initially receives identical original stem and A/B/C; no stored letter, no previous agent output, no prior provisional key.
- Require nonempty output, actual model ID, response finish status from router, and A/B/C mentions; these are only **structural preflight**, not correctness checks.
- If two intended separate reviewer roles fall back to the same actual model, independence is **not proven** and the QA gate blocks it.
- Source is only a pointer to workbook provenance. Missing exact source paragraph + current edition + scope means **no answer approval**, irrespective of provider consensus.
- `OPENAI_API_KEY` is **never** passed to this workflow. Max 24 provider attempts per 4-case pilot. No scheduled job. Workflow secrets only allowed on trusted branch push with marker `[academy]`; PR jobs run zero provider calls.
- Proposed Academy lessons are a **review queue**, never automatically installed into agent skills or used as proof of fine-tuning.

## Evidence
- Offline tests and dry-run preflight: https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44736664294 (PASS).
- New script: `scripts/academy_agent_orchestrator.py`; tests: `tests/test_academy_agent_orchestrator.py`; workflow: `.github/workflows/academy-agent-orchestration.yml`.
- The first actual four-case role trial is gated by this checkpoint's `[academy]` commit. Its run and results must be reviewed before extension.

## Remaining gates
- Evaluate structured outputs *semantically* against original A/B/C and independent sources with exact physical object, conditions, grade and edition.
- Apply test/retest and negative false-positive cases, including false equivalence between model roles, no source, reasoning contradiction, outdated edition and option bias.
- Require human/expert approval before learner release. No canonical data changes under this integration.

## First live run and focused retest
- First four-case real run: https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44736791421 . Offline checks succeeded. Nine independent role attempts returned responses from Groq, Gemini and OpenRouter. QA correctly marked QABC-0004 incomplete because the skeptic named B but omitted explicit A and C. No answer approved.
- A targeted, separate only-role retry is now available. The next gated run must use `--only-unit QABC-0004 --only-role independent_skeptic`, not replay the other seven previously sufficient model role traces. Quality status is `ROLE_RETEST_PRESENT_NOT_RECONCILED`, which cannot certify independent roles by itself.
- Reconcile with the original technical trace and the actual primary source before any QA completion. Untrusted model output is not evidence of a correct key.

## Continuare GFR pe următoarele opt întrebări
- CKPT-265 documentează prima execuție și erorile semantice reale.
- În această rulare se testează loturile QABC-0005–0008 și QABC-0009–0012 separat, cu aceleași secrete free-tier și fără apeluri OpenAI plătite.
- Rapoartele sunt numai dovezi de model și QA preliminar. Nu se schimbă bareme și nu se aprobă învățarea.
