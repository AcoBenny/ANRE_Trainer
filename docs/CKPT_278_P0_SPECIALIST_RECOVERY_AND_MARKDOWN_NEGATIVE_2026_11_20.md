# CKPT-278 | Academy P0 targeted agent-training and source QA snapshot | 2026-11-20

## Measured work
- P0 original exact-copy queue: 12 distinct QABC / 24 grade placements, immutable, derived from V149; original keys and HTML/APK untouched.
- Initial priority cohort 0013/0019/0024/0025: [run 44757996875](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44757996875) yielded 6 model-role outputs for three text questions; QABC-0024 figure blocked before calls. Do not count source diagram absence as workbook absence: original 22 OOXML drawing shapes recovered in prior CKPT-255 but not yet validated into a model image input.
- Next 8 QABC [44761592780](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44761592780): 37 real API attempts, 16 nonempty role outputs, 3 units with all roles present structurally; remaining five had provider or format failures.
- One-role QABC-0065 linguistic retest [44763821572](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44763821572): 1 Groq GPT-OSS-20B call, complete role format, requires reconciliation.
- Six missing-role batch [44764156731](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44764156731): 7 provider attempts, 5 complete model-role responses (0025 linguistic, 0050 skeptic, 0080 skeptic, 0091 linguistic, 0096 linguistic), QABC-0050 linguistic still failed due empty Groq output/Requesty timeout. The job was correctly marked failed and saved all partial traces.
- One final targeted QABC-0050 linguistic retry [44764679837](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44764679837): 1 real Groq GPT-OSS-20B response, but it used **Markdown bold headings** `**A:**`, `**B:**`, `**C:**` followed by mostly verbatim choices, **not** distinct per-option analysis. The run failed structurally and does not certify a question. It also speculated a one-directional harmonic-period ratio without fixed numerator convention; no official 2026 scoring or source certification.

## Actual QA training changes
- Distinct Groq GPT-OSS-20B linguistic model to escape exhausted OpenRouter/Requesty routes, without using paid OpenAI API; same actual model IDs across gateways still fail the independence test.
- Strict maximum two free provider candidates per P0 role and per-unit/role retry support, so missing roles are retried without repeating successful model traces.
- Explicit `reasoning_effort=low` for Groq 20B to avoid empty visible responses where possible; does not guarantee technical truth.
- Output parser now recognizes Markdown-bold field labels for accurate *diagnostics*, but detects copy-only A/B/C and refuses to mark them as substantive reviews. Regression introduced from the actual QABC-0050 negative trace and earlier QABC-0080 similar error. It does not silently accept formatted text as correct reasoning.
- Source/edition gate, ABC/PAIR constraint checks, model independence, no fabricated acronym/counterexample and semantic-warning fail-closed controls remain.
- Latest offline regression CI [44765039962](https://github.com/AcoBenny/ANRE_Trainer/actions/runs/44765039962) **PASS**, including Markdown false-positive test. No new real provider calls on this CI run.

## What is truly incomplete
- QABC-0050 linguistic **substantive** analysis is still not complete despite model response; do not retry another cascade now. Other recovered role outputs are NOT reconciled with earlier independent model outputs or authenticated source passages.
- Full 2026 source applicability, original graded ANRE keys, qualified independent professional QA, and review of the remaining V149 questions are unfinished. No question gets automatic `approved_for_learning`.
- QABC-0024's validated source diagram must be carried to image-bearing prompt (no hallucinated topology). The 6 V144 original-vs-canonical blockers remain separately gated.
- Agent 'training' here means prompt instruction updates and tested QA checks; **no LLM weights trained** and no Academy stable skill promoted.

## Safety and next action
- No more full-batch repeats; next action must be source-grounded independent adjudication of high-risk QABC (harmonic periods, E/D electric flux, GIS, generator assumptions), with original source paragraph and grade/edition gates. Preserve model disagreements as evidence and get user interpretation only where critical exact-source ambiguity remains.
- PR #13 Draft, PR #7 Draft, no merge/release and no modification to canonical QABC, keys, HTML or APK.
