# CKPT-432 | MC-004 partial integration: CONSULTFORM candidate
2026-11-27 | Draft PR #7 | No merge/release.

## Delivered and tested
- Local standalone HTML candidate ANRE_CKPT432_Candidate_305.html, SHA-256 597fdbbced57a587b8a03868e977d4499b77d90c2e857dedf7f271e059d646fe. Exactly 305 active CONSULTFORM questions, G1 151/G2 154, LEG 104/NOR 201; zero original stem/ABC/key/reference/grade discrepancies. No legacy questions active.
- 167 I7 original context records, 81 precise highlighted answer spans, 144 historical selected-answer explanations (overlap), 67 reference-only/missing. Original paragraph neighbors missing where unavailable; no invented source text. Historical explanations distinguish original choice letters from shuffled display letters, can be English.
- Reused the existing offline WebView wrapper, original design language, state/filter/navigation concepts; adapted runtime for CONSULTFORM-only data, stable per-session shuffled choices, preserved original keys, Reținut, Greșelile mele, quick/exam, and isolated storage. Grad II A and B share G2 pool because workbook provides no subgrade marker.
- Chromium offline set_content 390x844: 1830/1830 rendered correct-answer permutation tests PASS; filters, card rendering, wrong answer/repeat, remember, mock-storage reopen, quick duplicate prevention, exam PASS; 0 JS errors and 0 external network requests. Direct file:// and URL navigation blocked by environment; actual localStorage persistence and physical Android test NOT_RUN.
- Android build kit ANRE_CKPT432_HTML_Android_Build_Kit.zip SHA-256 14555b31c80092174f74f3eb27f971c0d03b525fa3bf6f9a345840c502991f3b contains pre-staged project, exact candidate HTML asset, personal data and builder, BUILD_APK.bat/ps1, reports. Debug candidate applicationId ro.anre.trainer.consultform prevents overwriting prior installation. SDK35, Gradle 8.9/AGP 8.7.3, JDK17 prerequisites. APK BINARY NOT BUILT: Android SDK and Gradle absent in current environment; repo has no wrapper and no authorized private-data CI route. ZIP is source/build kit, not installable APK.
- Public repo code only: tools/consultform/consultform_shell.html, consultform_runtime.js, build_consultform.py, stage_android.py. Local generator with exact repository index provides full provenance paths; delivered kit uses abbreviated source labels and record IDs (all 144 explanation texts and record IDs compared against index, zero mismatch). Repository generator/stager are not executed in this environment; local equivalent generator and staged source kit executed for HTML and packaged successfully. No raw question bank, source workbooks, or full source excerpts published. Historical app asset unchanged in repository to preserve old version and avoid publishing study data.
- Cost: zero additional paid CI calls.

## Rebuild (local checkout)
`python tools/consultform/build_consultform.py --payload PATH_TO_ANRE_CKPT431_study_cards_305.json --out PATH_OUTSIDE_REPO/anre_trainer.html`
`python tools/consultform/stage_android.py --repo . --html PATH_OUTSIDE_REPO/anre_trainer.html --out NEW_FOLDER_OUTSIDE_REPO`
From staged project: `gradle :app:assembleDebug`. Or use delivered build kit / Android Studio. Do not commit staged assets to public repo.

## Status and next
MC-004 IN_PROGRESS / HTML done, APK compilation blocked locally. MC-003 blocked until Electrotechnics workbook arrives; MC-005 device QA and owner acceptance pending. Do not redo MC-001/002 or reopen technical key validation. Full bank integration after MC-003. No merge or release.
