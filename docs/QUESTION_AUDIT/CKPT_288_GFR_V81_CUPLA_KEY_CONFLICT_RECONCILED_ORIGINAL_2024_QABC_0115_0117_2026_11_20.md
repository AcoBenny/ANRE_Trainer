# CKPT-288 | Bounded GFR: QABC-0115/0116/0117 cross-source adjudication and V81 deduplication | 2026-11-20

## Scope and unchanged inputs
- Reopened the **actual user-supplied unmodified Excel** `ELECTROTEHNICA-09.2024-2(2).xlsx`, SHA-256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`, `Sheet1!A131:D133`. Valid ZIP. **No separate official scored-key field** in this workbook.
- Reopened V149 568-QABC release-gate ledger, Git blob `ee2ac5536c78eb06a0461243be34c117e257188f`, selecting the exact tuple `(ELECTROTEHNICA-09.2024-2.xlsx, source_row)`. Original QABC text and A/B/C in the ledger match the uploaded workbook; preserved existing imported keys **A / B / A**, **not edited**.
- Crucial re-opened historical file: `V81_TEN_SWITCHING_SEQUENCE_AND_BUS_COUPLER_PRIMARY_SOURCE_CHECKS.csv`, blob `0e7ade26da660a968c9f880111f1ff6416c9331e`. **V81 ALREADY FLAGGED QABC-0115 (both grade placements) as `C_POSSIBLE` against imported A**, with separate technical/language QA `NOT_RUN`. It also flagged QABC-0116 `NO_UNIQUE_KEY_YET` and QABC-0117 `A_CONDITIONAL`. Therefore CKPT-287's wording `NEW_P0_IMPORTED_A_SOURCE_CONFLICT` must be **superseded**: the conflict is **RECONFIRMED / NOT NEW**. Do not double-credit as a newly discovered problem or reset the previous audit.
- Source hierarchy: original 2024 Excel (verbatim options, no key) > historical V81 import-key snapshot (preserves but does not authenticate grade) > public technical courses for interpreting intended engineering function. Source dates do not automatically establish a historical meaning change.

## Additional technical source evidence from this bounded pass
- A publicly accessible Romanian course on station connection schemes includes a dedicated paragraph **“Funcțiile cuplei transversale sunt”** followed by at least **energizing an isolated busbar to check insulation**, **parallel connection of two live busbar systems**, **feeder redistribution**, and **bypass of a circuit-breaker in an appropriate connection scheme**. Read adjoining context about the **two-busbar, one-breaker-per-circuit layout** and restrictions for simplified bypass circuits. Source: https://www.academia.edu/16422253/SCHEME_DE_CONEXIUNI_PENTRU_STATII_ELECTRICE (content around 5.3 and 5.9). This is an independent technical explanation in publicly hosted course material, **not ANRE's authenticated answer key and not qualified human signoff**.
- A separate publicly hosted university-course copy describes cross-coupler bypass using one busbar freed of other feeders and series routing, and its topology-dependent limitations: https://www.academia.edu/12426427/SCHEME_PRINCIPIALE_FOLOSITE_PENTRU (section around fig. 3.18). A different practical topology may not support bypass; the generic word `cupla transversală` alone does not prove the exact local arrangement.
- In a **2020 teaching slide copy** `https://ro.scribd.com/presentation/633373385/Prezentare-examen-si-Intrebari-electrotehnica-2020` (search-rendered text, around slide/question 116), the *comparable* A wording omits the word **`numai`** whereas the **uploaded 2024 Excel, A131** includes **`numai`**. The source must NOT be described as an authenticated ANRE revision chain; it is a **copy-to-copy textual difference**. Without `numai`, a generic A (paralleling) and C (insulation check) are BOTH possible, so a copied historical A grading position cannot be transferred to the 2024 option text without review. No proof of why/when that word changed.
- A recent independently published educational explanation at `https://scientia.ro/tehnologie/96-internet/10558-test-oficial-anre-pentru-electricieni-275-de-intrebari-electrotehnica-masini-si-retele-electrice-cu-raspunsuri-si-explicatii.html` also proposes **C** for question 124, **B conditional on bypass topology** for 125, and **A** for 126; source indexed but direct full webpage fetch failed. It is **a secondary worked-answer source, not official ANRE scored-key authentication**.
- Previously cited primary regulation `NTE 009/10/00 art.34/38`: direct `legislatie.just.ro/Public/DetaliiDocument/122751` fetch returned 502 in this pass, so original exact legal article was **NOT reopened directly this session**. Alternative indexed mirrors exist, but not a signed 2026-consolidated original text with precise article context; don't claim a direct official-law revalidation.
  
## Exact QABC and bidirectional option checks

### QABC-0115, source row 131; grade placements G1-ELE-124 / G2-ELEC-266
- **Imported existing key: A; prior V81 research C_POSSIBLE; current engineering candidate C**.
- A says the cross-coupler can be used **`numai`** for paralleling two energized bus systems. If C's documented insulation test of a previously deenergized bar is possible, this exclusive A statement is false. The technical course provides the positive C functionality, so **not just elimination**.
- B says bypass is impossible. In special schematics with bypass/appropriate switches it is possible; in ordinary topology bypass may not be available. As a universal negative, B is not proven for every two-bar station, and does not invalidate C.
- C says the cross-coupler can energize an out-of-service bus for checking its insulation. This is affirmatively supported under the appropriate interlocks, voltage and safety conditions. This is a **function description, not a procedure to perform unsupervised**.
- A vs C: **mutually exclusive** when the latter is feasible, because A says `numai`. B vs C: bypass possibility and insulation-check ability are different functions; not inherently mutually exclusive. A vs B: the false absolute on A does not prove B correct.
- **Disposition:** `IMPORTED_A_IN_TECHNICAL_CONFLICT / C_TECHNICALLY_SUPPORTED_UNDER_CONDITIONS / RECONFIRMED_FROM_V81 / OFFICIAL_KEY_NOT_AUTHENTICATED / INDEPENDENT_HUMAN_QA_MISSING / NO_RELEASE`.

### QABC-0116, source row 132; grade placement G1-ELE-125
- **Imported existing key B; already V81 flagged topology-dependent**.
- A denies that the cross-coupler can parallel live bars: contradicted by the documented standard function subject to switching/interlocking conditions.
- B permits bypass of a line breaker for revision: **possible with requisite bypass disconnectors/transfer arrangements**. Without such topology, two busbars alone do NOT guarantee this function. Affirmative conditional candidate, not universal engineering truth.
- C says the only function is insulation checking: false exclusive `numai`, since parallel coupling exists.
- Option-pair checks: B vs C conflict on exclusivity, A vs C independently contradicted by normal parallel function, and A vs B target different physical operations. **Do not infer topology solely from the imported B key**.
- **Disposition:** `IMPORTED_B_TECHNICALLY_POSSIBLE_TOPOLOGY_CONDITIONAL / CONFIRMS_V81 / NO_APPROVAL`.

### QABC-0117, source row 133; grade placement G1-ELE-126
- **Imported existing key A; V81 already A_CONDITIONAL**.
- A permits paralleling two energized busbar systems, provided protection/interlocking and electrical compatibility permit it. **Affirmative technical source support**.
- B denies bypass: can fail for a bypass-capable topology, though true in a simple topology without additional bypass components.
- C denies insulation-check possibility: contradicted by explicitly documented busbar energization function with proper controls.
- Pairs: A and B can **both** hold in a simple non-bypass topology; this is why A is the **intended best candidate** but automatic universal exclusivity cannot be asserted from the stem alone. A and C diverge under documented insulation-check arrangements. No forced unique letter via elimination.
- **Disposition:** `IMPORTED_A_TECHNICALLY_SUPPORTED_WITH_TOPOLOGY_SCOPE / CONFIRMS_V81 / NO_APPROVAL`.

## QA & no-double-counting
- Three **original row records**, four grade placements: `0115` has two placements, `0116` one, `0117` one. **0 new distinct canonical questions discovered**, **0 question keys changed**, **0 new provider AI calls**. One **source comparison / semantic clarification** added, with positive independent published sources; **no real independent human electrical signoff**.
- A 2020 third-party slide copy vs the uploaded 2024 original is **not** an ANRE-server edition byte-identity proof; no key lineage proven.
- The precise 2010 law was not re-fetched from its official host (502); exam-2026 bibliography applicability and professional reviewer still block approval.
- The 2024 original workbook has no scored-answer column, and full current 2026 ANRE grading-letter provenance remains unverified. All three remain **NOT_APPROVED_FOR_LEARNING**.
- **No HTML, APK, original QABC/key/grade mapping/main changes. No merge. PR #7 and PR #13 remain Draft.**

## Next bounded lot
1. Keep QABC-0115 flagged as **V81 known + independently source-reconfirmed**, not new; investigate authentic scored-key origin and exact exam-era course, only if source newly available.
2. Proceed through 0080/0081 grouped GIS scope and 0013 exact field terminology only when new exact-source evidence is found, otherwise leave research gates unresolved, not repeated.
3. Reuse V149 568-QABC workqueue and prioritize those with source mismatches or contradictory imported keys over routine repetition; do not restart the 822-ID audit from zero.
