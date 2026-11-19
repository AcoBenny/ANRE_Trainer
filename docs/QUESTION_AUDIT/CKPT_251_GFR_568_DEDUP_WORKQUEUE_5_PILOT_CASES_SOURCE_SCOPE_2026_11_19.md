# CKPT-251 | GFR: V130 full QABC workqueue + 5 evidence-gated Academy pilot rechecks | 2026-11-19

## Baseline, actual executed operations, and result
- Based on canonical V73 blob `c027d417a8e4e605c830b2016fb55b099b8d130b` and evidence ledger V129 blob `225f23204f094a25afc00575cc0ebfe378a45a62`. Exact full files fetched from audit branch in 100-physical-line chunks and parsed with a CSV quote-aware state machine in orchestration JavaScript, not by naive newline/column splitting.
- **Observed V73:** 822 CSV data records, 24 columns and 822 unique IDs, all row lengths valid; **568 distinct normalized-by-exact-QABC (no text changes)**, 254 cross-grade twin groups, both twins sharing source workbook/source row. Grades: I=414; II=408. There are **exactly 2 conflicting imported-key QABC groups**: `G1-ELE-018(A) / G2-ELEC-170(C)` and `G1-ELE-102(A) / G2-ELEC-245(C)`. No other exact-QABC different-key conflict found in this source snapshot.
- **Observed V129:** 822 records, 17 columns, 822 unique IDs, all with a `focused_evidence_batches` entry and no human signoffs or learning approvals. 37 ID records have an *empty `new_analysis_files` cell* despite a historical evidence batch reference, representing 27 QABC units; this is a **missing explicit new-file pointer**, NOT automatically missing all historical evidence.
- Reconciled every V73 ID with V129: same grade, category, original answer key; no missing evidence-batch labels. No canonical keys, Q/A/B/C, HTML or APK changed.
- **New artifact**: [V130 canonical 568 distinct-QABC workqueue](V130_CANONICAL_568_QABC_INDEPENDENT_QA_WORKQUEUE_2026_11_19.csv) (568 records, 24 columns, full unchanged Q/A/B/C plus keys per grade and batch/analysis/source/edition pointers), successfully locally re-parsed before GitHub commit. Route counts: 2 key-conflict units, 27 units needing a more explicit historical analysis-file pointer before source/QA, 539 standard source-and-QA queue. **Those counts are mutually exclusive routing classes, not judgments of answer correctness.** No `LEARNER_APPROVED` flags.
- `V130` references and broad status flags are a workqueue, NOT a source-certified adjudication or evidence of independent specialist model executions.

## Focused 5-unit pilot source/scope rechecks (all 5 already previously studied; 0 newly distinct source-audited units credited)
Cases selected from [Academy pilot assignments](ANRE_ACADEMY_PILOT_CASES_2026_11_19.json) and existing CKPT-208/CKPT-250/CKPT-040. This revisits **5 distinct QABC units, 9 grade IDs**, does not double count the historical 568 research coverage.

### Case 1: `G1-ELE-018 / G2-ELEC-170` (A versus C)
- Original: “Capacitatea de serviciu Cs a unei linii electrice aeriene simetrice, având capacităţile C12=C23=C31 =C şi neglijînd influenţa pământului, este:” options A=`Cs=3 C`, B=`Cs=C/3`, C=`Cs=C`. Imported A/C preserved.
- Technical reverse test: with a balanced 3-phase interconductor delta capacitance and neglected earth, `q1=C(V1-V2)+C(V1-V3)=3CV1` since `V1+V2+V3=0`. Thus `Cs=3C` **under the explicit ideal model and phase-to-neutral service definition**, supporting A over C technically, not an ANRE grading key.
- Historic source: CKPT-208 educational delta-star evidence. The AFahC academic PDF at `https://www.afahc.ro/ro/facultate/cursuri/electro_b.pdf` was **not accessible in this pass (HTTP 502)**, and a LibreTexts direct link had a cache miss; no claim of a fresh exact-source reopen for that textbook. Keep `KEY_CONFLICT`, `EXACT_Cs_DEFINITION_OR_EXAM_KEY_NOT_PROVEN`, independent QA NOT_RUN.

### Case 2: `G1-ELE-102 / G2-ELEC-245` (A versus C)
- Exact original options/key are preserved in CKPT-208; same workbook row 109. NTE 009/10/00 on official Romanian legislative portal `https://legislatie.just.ro/Public/DetaliiDocument/122751` defines operational states and dispatcher-approved normal schemes. Search-indexed official text found; **direct official page reopen returned 502** in this pass. Multiple legitimate normal configurations remain, and “de preferat” lacks an optimization criterion.
- Status `P0_OPERATIONAL_PREFERENCE_AMBIGUOUS`: neither A nor C can be certified solely from a generic operating-state definition. Require exact textbook schematic/operational objective and independently read official normative text.

### Case 3: `G1-ELE-122 / G2-ELEC-264` (“doar”)
- Exact original and A/B/C are preserved in CKPT-250. Imported A/A. A says `doar selectarea sistemului de bare`, B describes isolation from energized busbar, C generic switching of normal operating current.
- Source-scope nuance **new explicit regression**: Schneider's accessible `https://www.electrical-installation.org/enwiki/Elementary_switching_devices` is about **LV IEC 60947-3**, not sufficient on its own to settle an HV multiple-busbar separator. IEC official catalog `https://webstore.iec.ch/en/publication/75708` for **IEC 62271-102:2018+AMD1:2022** explicitly announces ratings for *bus-transfer current and voltage*, so a blanket claim that no HV disconnector can ever transfer bus current is too strong. This DOES NOT prove normal load-breaking capability or make option C generally true. Exact qualifier and equipment-specific rating remain necessary.
- Status `A_VS_B_SCOPE_CONFLICT`; `B` remains a **technical candidate only**, not approved or changed. Negative training fixture: low-voltage generic isolator definition cannot certify high-voltage bus transfer/selection; do not equate transfer current with generic load breaking.

### Case 4: `G1-NOR-032` (PE155 vs I7)
- Original from CKPT-040: “Montarea dozelor de trecere este obligatorie în cazul în care lungimea coloanelor în linie dreapta, pe orizontală, depăşeşte:” A=10 m, B=15 m, C=20 m. Imported B unchanged.
- Retrieved text from PE 155/1992 PDF mirror `https://www.baluna.ro/wp-content/uploads/2018/02/pe_155_92.pdf`, **§3.2.10** (horizontal columns >15 m); immediately neighboring §3.2.9 and §3.2.11 also available as text, as well as vertical-run exception. A/B/C: B historically source-matched, A and C not the text's threshold. **PDF screenshot request cache-missed**; PDF publication and current consolidated applicability still need verification.
- **Important new official bibliography confirmation:** ANRE's own currently linked `Tematica şi bibliografie ... actualizată în 05.2023` at `https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf`, table entry 29 (PDF page 3, 0-based page 2), explicitly lists **PE 155/1992 applicable to Grades I and II**. This closes only the **published 2023 examination bibliography grade-scope question**, NOT 2026 session/update status, source-image authenticity or independent option QA. Historical generic I7 25 m is the wrong physical object. Keep learner approval NO.

### Case 5: `G1-ELE-139 / G2-ELEC-277` (transformer Y0d-5 neutral/earth)
- Original from CKPT-250: transformer group Y0d-5, balanced supply; A=line voltage B=phase voltage C=zero voltage, imported C/C preserved. C holds in the ideal balanced earth-referenced case, but vector-group notation alone does not prove an actual earth connection/bond and reference. Unless the source establishes the earthing convention, preserve `NEUTRAL_EARTHING_CONDITION_UNSPECIFIED` and independent QA NOT_RUN. No newly authenticated exact source in this pass; no false certified verdict.

## Academy outcome and training truth-in-labeling
- Read and applied installed Avengers Asamble `agent-router`, `anre-source-audit`, `anre-question-bank-qa`, `qa-evidence-gate`, `agent-benchmark` and Precision Lab `prompt-architect`/`docs-intelligence` role contracts **as guidance for one assistant**.
- 5 assigned pilot cases re-examined, original sources/statuses differentiated (official ANRE, IEC catalog, manufacturer LV guide, mirror, inaccessible academic PDF); no actual separately executed model subprocess, no baseline-vs-skill comparison, no 3x real trials, no independent reviewer. **`TRAINING_CASE_ANALYSIS_SINGLE_ASSISTANT`; `REAL_MODEL_TRIALS_NOT_RUN`; `INDEPENDENT_QA_NOT_RUN`.**
- Transferable lessons: (1) bibliographic grade applicability is distinct from source-era/current-session validity; (2) disconnector LV generic behavior cannot adjudicate HV bus transfer; (3) identical QABC across grades permits reusing *evidence*, but not silently resolving different imported keys.

## Next exact sequence
1. Reconcile 27 legacy analysis pointer units to their specific versioned source artifacts without repeating their historical technical review.
2. Adjudicate the two key-conflict QABC units with authentic edition-specific sources and distinct reviewer where available; unresolved ones remain blocked explicitly.
3. Continue risk-first source/option QA across remaining 539 units, retaining every exact original option and all exception/grade gates; Academy captures redacted negative cases only. Move to offline HTML/APK only after learning gate is objectively passed.
4. Check source publication/edition against actual autumn 2026 official session bibliographic document before attributing 2026 currency to ANRE 2023 PDF. No unsupported shortcut to `approved`.

## Safety and release gate
- `V73_QABC_OR_KEY_CHANGED=NO`, `HTML_APK_CHANGED=NO`, `LEARNER_APPROVALS=0`, `PR7_DRAFT_UNMERGED`.
- All 568 source/QABC rows are now *queued*; no claim that 568 have been independently technically certified.
