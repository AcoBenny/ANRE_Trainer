# CKPT-252 | GFR: zero legacy pointer gaps; 5 high-risk legal key discrepancies | 2026-11-19

## Concrete repository execution
- Retained V73 canonical exact QABC/key blob `c027d417a8e4e605c830b2016fb55b099b8d130b` and V129 evidence ledger blob `225f23204f094a25afc00575cc0ebfe378a45a62`; both fully re-fetched read-only. No canonical edits or application edits.
- Inspected **four original historical source CSVs**: `V77_18_P0_EXACT_SOURCE_AND_LANGUAGE_RECHECK.csv`, `V80_FOUR_CROSSGRADE_CONFLICT_RECHECK_DELTA_CAPACITANCE_AND_BUS_BARS.csv`, `V81_TEN_SWITCHING_SEQUENCE_AND_BUS_COUPLER_PRIMARY_SOURCE_CHECKS.csv`, `V82_NINE_ELECTRICAL_P0_SOURCE_FORMULA_CONDITION_CHECKS.csv`.
- Exactly **37/37 ID records with `V129.new_analysis_files` originally empty** have an entry in one of those 4 source artifacts: 14 V77, 4 V80, 10 V81, 9 V82.
- Programmatically compared each historical source record's **entire original question, A/B/C and original key** against immutable V73. **37/37 exact QABC/key matches, 0 mismatches**. No implication that the past technical interpretations were independently correct.
- Evidence: [V131 historical canonical pointer crosswalk](V131_37_HISTORICAL_POINTERS_EXACT_QABC_KEY_RECONCILED_2026_11_19.csv), preserved as a separate correction to V129 instead of rewriting history.
- Produced and validated [V132 full 568-unit workqueue](V132_CANONICAL_568_QABC_WORKQUEUE_HISTORY_POINTERS_RESOLVED_2026_11_19.csv), superseding V130 (which remains historical): 568 distinct unchanged QABC, 25 columns, 822 ID assignments, **37 resolved analysis pointers, 0 `HISTORICAL_BATCH_ONLY` references remaining**. Queue now **2 exact key-conflict units plus 566 source/option/edition/independent-QA units**. These are routing categories, not 566 newly unresearched questions and not 566 technically false results.

## Primary-law focused recheck: 5 exact legal questions (previously researched, not counted as new distinct coverage)
- Used official Portal Legislativ **Legea 123/2012**, `https://legislatie.just.ro/Public/DetaliiDocument/300063`, page lists its latest consolidated historical form **26.07.2026**; personally read original art. 92(1)-(2), art. 93(1) pct.3 and pct.28 and art.57(2). A versioned 2026 legal reading is more probative than old 2013 pages but still not an official ANRE examination key.
- Used official `https://legislatie.just.ro/Public/DetaliiDocumentAfis/288046`, **Ordin ANRE 66/2023 Regulation art.37 e/h**, the portal indicates consolidated change date **13.09.2024**, to test obligations versus conditional reception participation.
- Recorded complete per-case primary-source locator, original unchanged imported key, recommended technical/legal candidate and remaining gates in [V133 five legal source/key discrepancies](V133_FIVE_LEGAL_PRIMARY_SOURCE_KEY_CONFLICT_RECHECK_2026_11_19.csv).
- `G1-LEG-015`: imported **B** vs primary-law **A candidate**. Art.93(1) pt.28 expressly covers refusal of meter access as contravention; B corresponds to an act described as criminal at art.92(1). Penal basis of C needs distinct proof; do not label the full three-option adjudication complete.
- `G1-LEG-019`: imported **C** vs **B candidate**, directly supported by art.93(1) pt.3; treating named statutory contravention as generic “abatere” misclassifies it.
- `G1-LEG-026`: imported **C** vs **B candidate**, directly supported by art.92(2), expressly describing clandestine direct network connection as criminal; “contravenţie sau infracţiune, după caz” lacks the exact statutory match for the stated act.
- `G1-LEG-034`: imported **B** vs **A candidate**, art.37(e) respects project, 37(h) participates at reception **if requested**, contrary to alternative B's “chiar dacă nu i se solicită”; note that source is official 2024 consolidated form.
- `G1-LEG-048`: imported **A** vs **B candidate**, art.57(2) offers a choice **among payment methods provided** by supplier, not arbitrarily imposed methods.
- **All 5 have explicit positive legal support for their candidate**, but no independent legal reviewer, full 2026 exam key proof, current session-specific source check or learner approval. **0 canonical key modifications**.

## Academy integration and negative regression lessons
- Preserve precise difference between (a) source-text legal conclusion, (b) ANRE exam-intended answer, (c) imported canonical key and (d) approved training answer.
- Always challenge legal answer options that introduce “sau”, “chiar dacă nu”, “orice” and classification-changing words: article-specific criminal vs contraventional offense is not freely interchangeable.
- Historical evidence references must be reattached using exact full QABC and original key, not ID alone; V131's executable comparison is a useful Academy test case.
- This is **one-assistant source-guided review and deterministic programmatic QC**, not a 3-model independent trial or qualified legal human signoff. Academy validation/promotion remains NOT_RUN.

## Safety and next handoff
- `canonical_key_changes=0`; `question_ABC_changes=0`; `HTML_APK_changes=0`; `learner_approvals=0/822`; `independent_content_QA=NOT_RUN`.
- First adjudicate these 5 source-backed legal discrepancies and 2 crossgrade key contradictions without editing canonical data. Then process other high-risk source/edition linguistic conflicts. Draft PR #7 must remain open and unmerged.
- On next run use V132 + V133, not V130's now superseded historical-pointer queue. No separate parallel copy of Academy exercises.
