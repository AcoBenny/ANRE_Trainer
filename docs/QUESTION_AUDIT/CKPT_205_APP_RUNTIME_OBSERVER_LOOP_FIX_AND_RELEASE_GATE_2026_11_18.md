# CKPT-205 | Android audit overlay self-triggering loop fixed on audit branch | 2026-11-18

## User priority
ANRE question audit and application finalization are past deadline. Stop rerunning G1-LEG-025 presentation-format research as a global blocker. Prioritize real answer-key defects, app regression and executable release gates. No claim of 822 approved or APK ready.

## Genuine application defect found
- Actual source on branch: `app/src/main/assets/audit_patch.js`, original blob `b819006ce504b4744ab316496aebdae85f73fba7`.
- Original algorithm `audit()` unconditionally removes `#audit-runtime` then inserts a new element, while `MutationObserver(...).observe(document.body,{childList:true,subtree:true})` schedules `audit()` for **those very same self-authored DOM mutations**. For IDs with typo repairs it also wrote `textContent` on every run whether changed or not. This creates a self-sustaining redraw/scheduling loop; plausible source of UI stalls (not experimentally linked to any particular user session/device).
- Direct fix **committed to audit branch only** at `447d3f47e0826c4dda9f33bd6534fb0357bccf96`. Latest script blob after readback: `9b6d23fda8823688c41d72875086913d26ee5897`.
- Fix: cache per-question/metadata `signature`; if rendered diagnostic box exists and signature unchanged, return without DOM writes; only repair typo text when original fragment actually occurs; coalesce MutationObserver notifications through one scheduled update, keeping observer support for question/metadata changes.

## Actual executable regression verification
- Used deterministic in-memory DOM/MutationObserver/setTimeout simulation **with actual original and patched JavaScript executed**; not just a text/pattern test.
- Original original script: callback queue **still not settled after 30 dispatches**, reproducing self-scheduled redraw loop.
- Patched script: callback queue **fully settled** after initial render; only one box inserted.
- Patched script: simulated transition from `G1-LEG-025` to `G1-LEG-026` triggers re-render once and callback queue again settles.
- Original apparent stem typo `se supun supun` corrected only in displayed DOM; canonical exam QABC unchanged. Tool readback confirmed signature guard, coalesced scheduling and guarded typo replacement.
- **Not performed:** browser Playwright/real Chromium; Android device; emulator; Java/Gradle APK build; functional offline navigation; accessibility regression. Do not promote simulated DOM QA to on-device certification.

## App build and canonical content facts inspected
- Android source `app/src/main/java/ro/anre/trainer/MainActivity.java` loads `file:///android_asset/anre_trainer.html` and injects `audit_patch.js` after `onPageFinished` via `evaluateJavascript`.
- HTML asset `app/src/main/assets/anre_trainer.html` blob SHA is `bc5b5a61954ba138cf83987bfc932eca517f3b21` which matches `V95_EXECUTED_DATA_QA_SUMMARY.json` `canonical_blob`; file is 1,581,242 bytes. The connected fetch_file operation returned empty content for this large file so direct HTML-body functional analysis is NOT done in this session. Do not pretend full HTML tested merely because blob SHA agrees.
- Existing GitHub Actions `.github/workflows/build-apk.yml` builds APK on pushes to `main` and on manual workflow dispatch; this **audit-branch commit did not trigger that workflow**. No APK or release produced.
- Project README/journey notes 822 grade questions, 568 unique QABC units. Baseline CKPT-180: 331 model-supported, 142 conditional, 50 blocked, 45 legacy-only; no independent validation or learner approval. V95 master contains 822 rows with 0 final approvals. These are audit states, not proof the new candidate keys are applied.

## Question audit progress
- CKPT-203: user decision for G1-LEG-025 B, exact legal scope annotation remains, do not reopen absent new facts.
- CKPT-204: next five P0 (G1-LEG-026, 028, 032, 034, 048) now have source-supported provisional candidates B, C, A conditional, A, B respectively. Especially G1-LEG-028 **Anexa 3, pct.2.3** official exact source recovered from 2013 racordare regulation. No keys modified, independent QA remains pending.
- Avoid counting the same 5 as new source coverage; label `EXISTING_PRELIMINARY_REVISITED`.

## Safe next, executable
1. Triage the 50 blocked and 45 legacy/precheck-only **unique units**, reusing CKPT-180–204 to avoid duplicate research; do not re-litigate user-decided cases without new evidence.
2. For each candidate correction, perform separate legal/technical + language/option counterexample review and edition check, then seek explicit approval before changing canonical keys. Do not imply a model-only adjudication is qualified human signoff.
3. Once questions pass, run HTML/offline/I7 anchors/random/repeat-mistakes checks, browser DOM loop regression and Android build QA on audit/development only.
4. User must approve any merge, release, or publication for exam learning. PR #7 must stay Draft until explicitly approved.

## Guardrails and integrity
- Modified application source: only `app/src/main/assets/audit_patch.js` (non-canonical UI annotation script), no HTML, no APK, no bank barems, no original QABC.
- No main merge/deployment. Last checked PR#7 is Draft, unmerged at HEAD `447d3f47e0826c4dda9f33bd6534fb0357bccf96`.
