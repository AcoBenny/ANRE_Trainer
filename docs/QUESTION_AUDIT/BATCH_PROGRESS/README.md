# End-of-batch anti-loop gate | ANRE / Avengers Asamble
Effective from CKPT-398. This is a **working process rule**, not proof of independently qualified ANRE source, keys, review or app QA.

## Mandatory end-of-batch contract (every GFR batch)

1. **BEFORE work** record a stable `task_id`, immutable work-item `id`s, each `stage`, `open_gates`, and per-item `evidence_refs`. Use the latest actual batch baseline; do not reconstruct a desired target from reporting text. Use `stage_order` for a non-ANRE project.
2. **AFTER work**, record actual states of the **same IDs**, any newly researched unique IDs, and the newly inspectable evidence reference for each claimed transition or cleared gate. New checkpoints, increased verbosity, more tests of the same unchanged item, and elapsed work are **not** progress by themselves.
3. Run `node tools/qa_batch_progress.mjs input.json verdict.json`. The command returns exit code **0 only for `PROGRESSED`**, code **1** for nonprogress, regression or invalid claim, and **2** for malformed input. On a nonzero verdict do **not** claim the batch advanced or create a second nearly identical batch. Record the diagnostic instead.
4. **PROGRESSED** = new non-BACKLOG unique processed items, stage advanced, or an existing source/approval gate genuinely closed, with new item-specific evidence. **NO_PROGRESS_REPEAT** = repeated same item states or evidence-only paperwork. **REGRESSION** = previous work disappeared, a status fell, or previously closed gates reopened. **INVALID_PROGRESS_CLAIM** = missing evidence or unsafe approval claim.
5. When `NO_PROGRESS_REPEAT`: mark task `BLOCKED_EXTERNAL` or `RESEARCH_COMPLETE_PENDING_APPROVAL` in its **planning narrative**, preserve evidence, and pivot to the next distinct backlog task. Reopen only on materially new authentic sources, reviewers, grade editions or exact objection. Do not lower the tracked progress stage to "blocked".
6. Summarize every batch in **one concise line**: `batch | unique items advanced | gates closed | repeated items | verdict | next different task`. Update `docs/CHECKPOINTS/LATEST.md` on the same branch. Never imply qualified reviewer execution or release from this structural tool.

## Example: the eight repeated P0 historical cases

[CKPT397_REPEAT_CHECK_INPUT.json](./CKPT397_REPEAT_CHECK_INPUT.json) versus [CKPT397_REPEAT_CHECK_RESULT.json](./CKPT397_REPEAT_CHECK_RESULT.json): eight QABC groups already source-researched remain eight with the same outstanding three broad approval gates. CKPT-397 adds reports but no new closed gate, so the verifier **returns NO_PROGRESS_REPEAT** and requires a pivot.

This historical example is a checkpoint-derived *aggregate illustration*, not an authenticated original file's eight individual signatures. It is a negative control; do not relabel it as an executed independent reviewer result.

## Scope and gates

- The verifier checks structural and cited-state differences; reference strings are **not** independently downloaded, authenticated or judged true by the script. Qualifying changes still need exact authoritative sources and real independent reviewer work.
- An `APPROVED`/later stage requires reviewer and decision references; ANRE also requires an authenticated official exam-key reference and edition flag. This is a minimal structural guard, never an automatic certification.
- For ANRE: no scoring, HTML, APK or original A/B/C changes, no merge/release without separate authorization. The 157 staged Grade-II source candidates remain quarantined. 0/822 final learner approvals.
- This script is generic enough for Jarvis/Academy by configuring project and stages, but **is installed and tested here only in ANRE_Trainer**. Other repositories must adopt/integrate it separately; no hidden global automation is asserted.

## Smoke tests

`node --test tools/tests/qa_batch_progress.test.mjs` exercises 15 deterministic positive/negative cases, including the historical eight unchanged, real new Grade-II item, gate regression, missing evidence, duplicate IDs and fake approval. These are **programmatic state tests**, not technical answer-key QA or APK tests.

## Next distinct work item

Stop re-opening the historical eight until a relevant external source/key or independent reviewer materially changes the evidence. Focus next GFR on **new original G2 candidate review groups**, starting with existing V332's 16 clusters, while keeping 157 original candidate rows in quarantine.
