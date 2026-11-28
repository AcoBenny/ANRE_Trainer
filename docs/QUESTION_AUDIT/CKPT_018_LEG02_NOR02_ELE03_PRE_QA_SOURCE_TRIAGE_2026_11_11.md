# CKPT-018 | ANRE Trainer | LEG-02 / NOR-02 / ELE-03 source+ABC triage | 2026-11-11

**Repository:** `AcoBenny/ANRE_Trainer`; PR **#7 DRAFT**; branch `audit/anre-v8-priority-17-20261109`. Continues CKPT-017, V8–V99 and all original manifests. **Research stage only, no batch technically closed.**

## Verified artifacts created on the audit branch
- `DEEP_EXECUTION_2026_11_11/DEEP_LEG_02_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv`: **20/20 units, 20 canonical IDs**, exact original question/A/B/C/key, per-choice analysis, source locator/access condition and next gate.
- `DEEP_EXECUTION_2026_11_11/DEEP_NOR_02_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv`: **20/20 units, 20 canonical IDs**. Uses prior V90/V97 I7 evidence without double-counting source reopen. Exact I7 primary PDF NOT freshly opened this session (Portal HTTP 502).
- `DEEP_EXECUTION_2026_11_11/DEEP_ELE_03_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv`: **20/20 units, 31 canonical IDs**, technical+source+ABC research; specialized sources (DPsim circuit topology, Steer line propagation) distinguished from missing equipment-specific manufacturer documents.
- Total **3 new batches' 60 units /71 ID placements** at source-triage stage. Added to four earlier batches: **7/30 batches have pre-review files, 140/568 distinct units, 186/822 canonical ID placements.** THESE ARE NOT VALIDATED ANSWERS and they do not overwrite source master V95.

## Most important new source and linguistic checks
| ID | Stored key | Source-level observation | Remaining gate |
| --- | --- | --- | --- |
| G1-LEG-011 | C | Reg66/2023 **Art47** officially opened: duplicate authorization requires nullity declaration in `publicație de largă circulație`, while **all choices say `ziar local`**. C matches separate duplicate fee, but publication qualifier not proven | 2026 edition/precise rewrite and reviewer |
| G1-LEG-012 | C | Reg66/2023 Art30/44 establishes periodic visa **fee**, but whether it is numerically *different* from grant tariff depends on annual tariff order | Retrieve 2026 ANRE fee order before claiming C |
| G1-LEG-013 | C | Reg66/2023 Art30 says five years from issuance/last visa, supported by officially opened regulation with 2024 consolidation | Temporal refresh + reviewer |
| G1-LEG-027 | C | Reg59/2013 **Art33(1)(b) 12 months** from ATR issue if no connection agreement (indexed current consolidation); other expiry reasons exist | Complete 2026 edition/exceptions and reviewer |
| G1-LEG-039 | B | Reg59/2013 **Art26(1) max30 calendar days** from complete application for connection offer by `fișă de soluție`. Text does not restrict this to middle voltage; B names medium voltage | Source context/edition and linguistic check |
| G1-NOR-025/033 | B/A | Prior historic **PE102** source is GradeII+, but questions belong to **GradeI**, and I7/product standards differ | **BLOCKED_SOURCE_GRADE** pending exact GradeI 2026 basis |
| G1-NOR-028 | C | V97 previously recognized immediately following I7 §5.2.6.6 **exceptions to traction-force prohibition**; maintain conditional gate | Full clause/exception and independent reviewer |
| G1-ELE-005/G2-ELEC-158 | B/B | Kirchhoff KVL independent loop equations = L-N+1 **for a connected network** (DPsim teaching source) | Independent review + connectivity semantics |
| G1-ELE-152 | A | Propagation constant gamma=alpha+j beta, m^-1, unlike earlier G2-ELEC-290 which misleadingly calls it dimensionless | Review academic definition and version |
| G1-ELE-089 | B | Hitachi product information confirms gas-leak/arc **localization by compartment monitoring**, but does not by itself prove physical compartment division advantages | Source physical scope and independent QA |
| G1-ELE-126 | A | Another same-stem multi-choice issue: option B may ALSO hold in plain double-bus topology without bypass | Exact one-line and independent technical reviewer |

## Source authenticity and dates
- Reg66/2023 consolidated 13.09.2024 official Portal text **opened**, including Arts30,37,41,47: https://legislatie.just.ro/Public/DetaliiDocumentAfis/288046 . Exhaustive absence of later amendments by 11 Nov2026 is **NOT CERTIFIED**.
- Reg59/2013 current-indexed consolidated post-2025/2026 official Portal: https://legislatie.just.ro/Public/DetaliiDocumentAfis/297330 ; accessible to **web indexed search**, but direct URL open returned HTTP 502. Art26(1), Art33(1)(b) were identified via index search, not direct open.
- Legea123/2012 official text indexed: https://legislatie.just.ro/Public/DetaliiDocument/262079 ; direct open returned502. No complete official form as of26.07.2026 reopened. Prior content reused with temporal caveat.
- I7 GradeI historical PDF evidence reused from V33/V90/V97. I7 official print URL `https://legislatie.just.ro/Public/FormaPrintabila/00000G01BLZ812IXGEN16BYPVD5MO6U4` returned502 this session. Claims supported only by previous review or legacy locator clearly flagged as such.
- Technical/educational sources actually retrieved via search include DPsim https://dpsim.fein-aachen.org/docs/concepts/nodal-analysis/ ; LibreTexts Steer transmission line theory https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Fundamentals_of_Microwave_and_RF_Design_%28Steer%29/03%3A_Transmission_Lines/3.02%3A_Transmission_Line_Theory ; Hitachi Energy https://www.hitachienergy.com/in/en/products-and-solutions/high-voltage-switchgear-and-breakers/monitoring-and-controlled-switching/modular-switchgear-monitoring-msm . Source access methods indicated per row. No unsupported claim of full PDF screenshot/independent QA.

## Deterministic QA actually executed on GitHub
- After commits, reopened all 3 CSVs, canonical V73 and `UNITS_568.csv`; **60/60 unique work units, 71/71 canonical ID assignments**, exact Q/A/B/C/order, key and SHA/risk/batch all matched; complete prelim reasoning/source/gate and unapproved flags. **PASS, zero mismatch**.
- The first combined QA execution yielded a **false structural failure** because the checker expected the column `ABC_analysis_PRELIMINARY` while the earlier ELE format used `ABC_reasoning_PRELIMINARY`. Verified actual ELE03 CSV header and rows, corrected checker to accept either legal field without editing data, reran complete QA **PASS**. Logged as regression lesson: QA MUST validate schema variants explicitly before declaring a file corrupt, and retest corrected checker. No false test success was claimed.
- GitHub PR7 remains Draft, unmerged, branch correct; canonical HTML blob `bc5b5a61954ba138cf83987bfc932eca517f3b21` **unchanged**.
- **0/30 deep batches accepted, 0/822 individual IDs approved for learning, no new distinct independent AI reviewer or qualified engineer signoff in this session.** `deep_audit_execution.py validate` purposely **NOT RUN**, because its true independent review and edition gates are not met.

## Handoff / priority
1. Start with **real distinct source/technical/linguistic reviewer** of pre-triaged batches, verify every ABC and exact 2026 edition; maintain all blocked as blocked, not completed.
2. Continue remaining **23 untriaged batches (428 units /636 canonical ID placements)** in routing order, most relevant sources before low-risk duplicate handling. Exact denominator: 568-140=428; 822-186=636.
3. Resolve high-risk old P0 conflicts NOR027, NOR089, LEG019/026, ELE018/102 etc, plus new source-scope blockers. No automatic key modifications, text changes, HTML/APK, main merge or release without user's approval.
4. The Avengers plugin v0.4.2 already includes source-object exact matching; new regression case: **multiple valid preliminary CSV field names must not trigger a false invalid-data report**. Preserve failures and evidence under cumulative-evolution principle.
