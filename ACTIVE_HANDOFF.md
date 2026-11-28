# ANRE Trainer | ACTIVE_HANDOFF

**CKPT-433 | Full-bank candidate HTML ready | 2026-11-28**

Current authority: [Mission Control](docs/MISSION_CONTROL.md). [CKPT-433 report](docs/CONSULTFORM/CKPT_433_FULL_BANK_REPORT.md), [grade crosswalk](docs/CONSULTFORM/CKPT_433_GRADE_MATCH_305.json), [Electro/PDF metadata](docs/CONSULTFORM/CKPT_433_ELECTRO_PDF_IMPORT_METADATA.json).

582 unique CONSULTFORM questions: 580 Excel + V3 Q8/Q25 material variants only, no separate PDF tests. G1 431, G2 581, 430 common. 291/305 LEG/NOR exact cached ANRE source matches; 14 unmatched -> both; all 275 Electro common. Direct live XLSX retrieval blocked. 275/275 Electro keys match yellow highlights; no technical answer revalidation. Original source markers retained for history. 18 media elements across 12 questions, including 11 OOXML diagrams converted to SVG (full visual fidelity pending). 305 prior cards preserved, 11 Electro original observations, 264 Electro + 2 PDF answer-only cards. Do not redo grade mapping or import. Remaining card work: reuse compatible historical Electro explanations where possible, explicitly mark gaps. No forced approval.

Local HTML candidate `ANRE_CKPT433_Candidate_582.html` SHA256 b6ead39829afecb91f3a577462f59054f9fd52c3a135dd6805ea7d80cba751ef; local JSON bank `ANRE_CKPT433_bank_582.json` SHA256 8b48cc5038a01f23b98995ee04f3f122cb47882df534c61bbb7b81b9a87736ed; local Android build kit `ANRE_CKPT433_HTML_Android_Build_Kit.zip` SHA256 d22869712874d446d10435b5913dc50c6dc563dd9706322aa4812c9489ac5423. Chromium offline 3492/3492 option permutations PASS, 18/18 media loaded, filters and wrong/remember/repeat PASS, no JS errors or external network. Actual APK not built, Android SDK/Gradle unavailable. Physical device/persistence/diagram visual acceptance pending. Public repo metadata only; generated full bank remains local. No paid Actions, no merge/release.

NEXT: MC-003 finish compatible historical Electro cards without reopening keys, MC-004 actual APK compilation, MC-005 physical/functional QA and acceptance. Preserve previous versions and all audit evidence. No separate V1–V5 test feature.

## Historical CKPT-427 (superseded operational plan, preserved for provenance)

# ANRE Trainer | ACTIVE_HANDOFF

**CKPT-427: 400/822 G1/G2 grade routes VALIDATED FOR EDUCATIONAL CONTENT; 236/568 distinct QABC groups.** 2026-11-25 | [PR #7](https://github.com/AcoBenny/ANRE_Trainer/pull/7) Draft, unmerged | `audit/anre-v8-priority-17-20261109`.

## Resume here; avoid loop/repeated validation
1. `docs/QUESTION_AUDIT/CKPT_427_GFR_400_OF_822_EDUCATIONAL_VALIDATIONS_2026_11_25.md`: CKPT-427 report, exact technical countermodels, exclusions, limitations and link to independent evidence.
2. `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_427_19_ORIGINAL_QABC_36_GRADE_ROUTES_EVIDENCE_2026_11_25.json`: **19 newly validated ORIGINAL QABC, 36 grade routes** (17 common G1/G2 + 2 G1-only). Exact original ABC/keys, source workbook/row, old SHA, technical URLs and independent AI reviewer IDs.
3. `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_427_14_DIDACTIC_QABC_14_ROUTES_EVIDENCE_2026_11_25.json`: **14 newly validated G2 DIDACTIC QABC, 14 grade routes**; distinctly trainer-authored supplemental/not ANRE originals.
4. `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_427_568_QABC_MASTER_2026_11_25.json`: 568 group ledger: **236 validated, 136 historical hold, 196 pending**.
5. `docs/QUESTION_AUDIT/CLOSURE_PILOT/CKPT_427_822_GRADES_MASTER_2026_11_25.json`: 822 grade ledger: **400 validated, 200 historical hold, 222 pending**.
6. `docs/QUESTION_AUDIT/CLOSURE_PILOT/LEARNING_CONTENT_ACCEPTANCE_POLICY_V2_2026_11_23.json`: content-specific validation rule (not an official scored-key or product release gate).

## Fixed restrictions
- Re-review approved 236 QABC ONLY if genuinely new source contradiction, edition change, material alternative or original checksum divergence. Do not count previously validated routes twice. 200 historical-held grade routes and 136 QABC held groups must remain in separate queue. Pending cases cannot be promoted based on absent flags or mere URL.
- Original question/ABC/barem never edited. Reviewer source/ABC and original import key align with every promoted grade ID. All technical arguments and limitations are evidence-linked; case QABC-0197 balance assumption, QABC-0106 linked flux, QABC-0001 stiff source, QABC-0054 not exclusive to magnetization, QABC-0241 common polarity.
- Deliberately not promoted: QABC-0165, 0064, 0028, 0206, 0093, 0510, 0537, until exact source/wording resolved. Don't resume these blindly.
- Distinct external AI reviewer runs were real; **NO certified human ANRE signoff**. Verbatim source preceding and following original paragraphs and offline legal use rights/anchors **NOT** fully verified or integrated: editorial teaching context paraphrases are explicitly labelled, never fabricated source quotations. No actual HTML/APK QA in these batches.
- PR #7 remains Draft, no merge/main/release. No original XLSX/HTML/APK change, no unauthorized paid tool, no recurring background worker. GFR + ARA means smallest useful authorized resource set, not indiscriminate plugins.
- Maintain cumulative evidence and versioned checkpoints; no regression/false progress; verify all source/ABC key mappings before write then read GitHub files and compare branch diff after commit.

## Next GFR + ARA
CKPT-428 target **450/822**, 50 additional newly eligible grade routes out of **222 pending**. Keep 200 historical holds separate. Once full source/ABC bank adjudication closes, authenticate original source before-highlight-after text/offline links and rights, integrate app, test real HTML/APK (grading, shuffling, repeat mistakes, navigation), request release approval only after independent QA.
