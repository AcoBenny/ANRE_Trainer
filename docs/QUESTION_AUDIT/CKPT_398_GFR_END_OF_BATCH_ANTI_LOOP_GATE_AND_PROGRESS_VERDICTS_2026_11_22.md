# CKPT-398 | End-of-batch anti-loop gate implemented, positive and negative progress examples

Date: 2026-11-22. Continues CKPT-397. PR #7 remains Draft, branch `audit/anre-v8-priority-17-20261109`. This checkpoint changes only audit tooling/tests/docs and checkpoint index. It does NOT change questions, A/B/C, imported scoring, HTML, APK, main or release.

## The problem fixed at process level
The same eight historical P0 QABC were repeatedly researched and recorded in CKPT-371/374/396/397 with **no drop in outstanding 8 groups**. More docs/checkpoints are not a valid measure of progress. Additionally `docs/CHECKPOINTS/LATEST.md` was stale at CKPT-257, despite progress up to CKPT-397.

## Implemented
1. [`tools/qa_batch_progress.mjs`](../../tools/qa_batch_progress.mjs): generic Node.js CLI, end-of-batch before/after item ID and stage/gate comparison, evidence-only negative check, lost-item and reopened-gate regression detection, missing-evidence invalid claims, minimal ANRE reviewer/edition/official-key structural approval guard. Results: `PROGRESSED`, `NO_PROGRESS_REPEAT`, `REGRESSION`, `INVALID_PROGRESS_CLAIM`.
2. [`tools/tests/qa_batch_progress.test.mjs`](../../tools/tests/qa_batch_progress.test.mjs): 15 deterministic positive and negative tests. **Logic was exercised against 15 pre-commit cases in the tool session and local Node variant; committed GitHub test suite has not been observed running in GitHub CI.** No app runtime or technical-scoring validation was done.
3. [Mandatory workflow and saved examples](./BATCH_PROGRESS/README.md): run `node tools/qa_batch_progress.mjs batch.json verdict.json` after EVERY future research, implementation or audit batch. No GFR claim of progress without a structural `PROGRESSED` verdict and inspectable per-item evidence. Exit code 1 for no progress/regression/invalid claims, exit 2 for malformed input.
4. [Historical 8-item repeat input](./BATCH_PROGRESS/CKPT397_REPEAT_CHECK_INPUT.json) and [computed NO_PROGRESS_REPEAT verdict](./BATCH_PROGRESS/CKPT397_REPEAT_CHECK_RESULT.json): same eight, same three outstanding gate categories, **0** item transitions and **0** resolved gates. This is an aggregated reconstruction from prior CKPTs, not new human signoffs. Action: `STOP_REPEAT_AND_PIVOT_OR_ESCALATE`.
5. [This implementation's own before/after input](./BATCH_PROGRESS/CKPT398_IMPLEMENTATION_INPUT.json) and [PROGRESSED verdict](./BATCH_PROGRESS/CKPT398_IMPLEMENTATION_RESULT.json): one *tooling* work item BACKLOG -> REVIEW_READY with code/tests/docs evidence; outstanding independent code QA and CI integration remain open. **Not an ANRE question approval.**

## GFR loop prevention decision
- **Historical eight P0:** `SOURCE_RESEARCHED_PENDING_EXTERNAL_KEYS_AND_INDEPENDENT_REVIEW`. No more batch exclusively on the same eight unless a new official exam-key, an independently qualified reviewer, materially revised authentic normative edition or a specific previously missing exact evidence can move a gate. Blocked does not mean erased.
- **Next productive task:** systematic semantic/source adjudication of the **157 quarantined original G2 candidates**, prioritizing the 16 V332 similarity clusters and 12 cross-stage comparison records. Require unique source row IDs, no additions to learner bank, no automatic duplicate deletion or answer mapping.
- **Whole bank:** 568 current groups / 822 grade routes, still 0/822 independent learner approvals. **28 P0 routes across 24 groups** remain open, **157 G2 original candidates** still quarantined.
- **At end of every next batch** require before/after counters of `distinct new IDs researched`, `stage transitions`, `gates actually closed`, `known repeats`, and clear verdict. If `NO_PROGRESS_REPEAT`, switch queue or escalate. Do not create another checkpoint praising the same unchanged eight.

## Limitations
- This is a structural/process guard, not a proof that an evidence ref is genuine, an expert actually signed or a normative result is correct. Tooling alone cannot authenticate the official ANRE exam score.
- The CLI is now stored in ANRE_Trainer and generic by configuration; not deployed as an autonomous always-on mechanism inside every other repository or agent. The mandate applies when the GFR operator uses this process. GitHub CI/branch-protection enforcement is still **NOT SET UP**.
- No app, key, A/B/C, original source files, grade association, official signoffs, merge or release modified.

## Resume
1. Read this CKPT and `docs/QUESTION_AUDIT/BATCH_PROGRESS/README.md`.
2. For next G2-157 batch, capture a BEFORE snapshot with exact candidate IDs and states.
3. Produce a verifiable after-state, run the verifier, record verdict and move to next *distinct* work if no progress. Keep PR #7 Draft until explicit release approval.
