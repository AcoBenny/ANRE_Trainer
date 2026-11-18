# CKPT-209 | ANRE app audit overlay QA and false VERIFIED badge fix | 2026-11-18

## Purpose and continuity
Resume CKPT-208 on PR #7 Draft. User requests immediate next phase focused on executable regression and final audit gates, no redundant question research. Source is `AcoBenny/ANRE_Trainer`, audit branch `audit/anre-v8-priority-17-20261109`. No main merge/release; question text, A/B/C, imported keys, canonical HTML and APK unchanged.

## Executed QA of actual script in a Node.js VM
- The exact old GitHub script `app/src/main/assets/audit_patch.js` had blob SHA **9b6d23fda8823688c41d72875086913d26ee5897**. Local reconstructed bytes verified this exact Git blob SHA **before testing**.
- Ran actual JavaScript through Node.js `vm.runInNewContext` with an explicit simulated DOM, `MutationObserver` and timeout queue. No external network, not a browser.
- Baseline **6/6 PASS**: initial box; display-only typo fix; stable observer callbacks; question navigation updates with negation/exclusivity; metadata update; identical text mutation does not redraw; second question typo fix.
- Negative control: deleting the signature early-return in a **temporary local test copy** triggered `SELF-SCHEDULING MUTATION LOOP: >60 dispatched callbacks`, as intended. Original production script was not modified by the negative fixture.

## Newly detected real risk and safe fix
- The old metadata test `/DOCUMENTAR OFICIAL ANRE|VERIFIED|VERIFICAT CU I7/i.test(x)` **matches NOT_VERIFIED, UNVERIFIED, VERIFIED_PENDING and NOT VERIFIED** (for some variations). This could falsely show `audit-official` for a non-verified item. Negative assertion against the exact old script failed reproducibly: `NOT_VERIFIED is falsely marked audit-official`.
- Applied a minimal edit **only** to `app/src/main/assets/audit_patch.js` on audit branch, requiring *exact badge text* after whitespace trimming and uppercasing: `DOCUMENTAR OFICIAL ANRE`, `VERIFIED`, or `VERIFICAT CU I7`. Conservatively avoids unintended substring certification. No data/QABC/barem edit.
- New exact script Git blob SHA: **61b56c7b61831f2e85694c1127d33dbe234f612b**, independently matching local patched source.
- Executed patched source in same Node VM: **8/8 PASS** (six baseline categories + explicit negated/pending badges stay non-official + three positive badge states still recognized). Observer settled in the simulator; 11 diagnostic insertions/10 removals across all transitions, final event queue empty, peak scheduled queue length 1.
- New negative control still fails after removing the signature guard, as expected. `node --check` passed on both local actual script and local regression harness.
- Commits: **9a2b761d23ffaf8489933fe40faae551a2a3afb8** patched script, **41604178540e097099785964d5ae0c1657b2b3b5** initial regression script, **886e09d66799f3ac26a4ded278ce86107b7d9f4a** tests for false-positive labels.
- Repeatable repository test `tools/tests/test_audit_patch_vm.cjs`; run `node tools/tests/test_audit_patch_vm.cjs`. Inject negative control with `ANRE_NEGATIVE_NO_SIGNATURE_GUARD=1 node tools/tests/test_audit_patch_vm.cjs` and **expect nonzero**. The local eight-scenario equivalent was executed; checked-in script read back from GitHub with eight checks and negation cases. Do not claim CI execution of the checked-in script.

## Data integrity recheck directly from live V73/V95 (JS CSV parser)
- V73 exact 822 data rows and 24 columns, no malformed row widths; 822 distinct grade IDs, I=414, II=408. 568 exact unique QABC tuples, 254 duplicate QABC groups, precisely **2 cross-grade key-conflict groups**:
  1. G1-ELE-018=A vs G2-ELEC-170=C (same question/A/B/C)
  2. G1-ELE-102=A vs G2-ELEC-245=C (same question/A/B/C)
- `approved_for_learning=NO` for **822/822** rows. No learner approval created.
- V73 risk: P0=71, P1=229, P2=522. V95 risk: P0=72, P1=228, P2=522. Compared all 822 IDs, keys and risk levels: **one priority-layer difference** `G1-NOR-042` is P1 in V73, P0 in V95, identical imported key B. Treat as a documented priority-layer reclassification candidate, **not source corruption or a key mismatch**; clarify intended authority of V95 in downstream reports.

## Executable and release boundaries
- Chromium was invoked against the audit fixture but it hung and timed out after 25 seconds. **A second minimal HELLO HTML page also timed out** (9 seconds), so this is an environment-level Chromium launch problem, not proof the script hangs or passes in a real browser.
- `CHROMIUM_BROWSER_QA=BLOCKED_ENVIRONMENT`; `ANDROID_WEBVIEW_QA=NOT_RUN`; `APK_BUILD=NOT_RUN`; `FULL_HTML_OFFLINE_I7_GRADE_RANDOM_MISTAKES_QA=NOT_RUN`.
- Source code checked via live GitHub connectors, but full 1.58 MB HTML was not mounted locally. No installation, real Android session or screenshot tested.
- All eight green tests are **simulated DOM/observer contract tests** using actual JS, not device certifications. No independent technical/legal reviewer or qualified human signed off any candidate answer key.

## Next smallest safe phase
1. Preserve script fix and add browser/Android app-regression execution when a browser, device or suitable CI runner is available. Keep diagnostic labels conservative.
2. Reconcile evidence quality and ANRE edition for the two cross-grade contradictory keys and remaining blocked + legacy-only QABC, reusing CKPT-180–208. Prioritize direct exam-key risk and avoid repeat format demos.
3. Obtain independent content QA and user authorization before applying answer-key changes, merging or releasing app for exam study.

**Current:** Audit PR #7 Draft; no merge/release; no approved learning bank.
