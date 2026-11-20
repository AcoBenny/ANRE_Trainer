# CKPT-286 | Remaining three P0 cases and research coverage of the 12 source-row cohort | 2026-11-20

## Evidence basis and precise claim
- Original user-uploaded `ELECTROTEHNICA-09.2024-2(2).xlsx` source SHA-256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`, actual `Sheet1` cells inspected with artifact_tool. Prior 12-row fingerprint ledger is CKPT-284.
- This pass adds **three source-conditioned, manually researched interpretations** for QABC-0013, QABC-0019 and QABC-0080, not independent AI or qualified expert review and **not official answer-key validation**.
- The full 12-QABC priority cohort now has **at least one research trail**, split: 3 cases in CKPT-282 original two-model/one-model reconciliation (0036/0050/0065), QABC-0024 in CKPT-284, 5 in CKPT-285 (0025/0042/0069/0091/0096) and these remaining 3 (0013/0019/0080). Unique total **3+1+5+3=12**, **not 12 newly source-certified answers**. Earlier work is reused rather than attributed to this checkpoint.

## QABC-0013 | Sheet1!A21:D21 | G1-ELE-014 / G2-ELEC-166
> Câmp fără surse este: A numai un câmp de curenţi de conducţie în regim staţionar; B câmpul electric; C câmpul de inducţie electromagnetică
- The mathematical qualifier **`fără surse`** depends on the *definition of source* (zero divergence of the relevant vector field, not the statement that a field has no physical generating mechanism).
- Maxwell's law for **magnetic induction B** is `div(B)=0` globally (no magnetic monopole sources), supporting **conditional C** only if `câmpul de inducţie electromagnetică` was meant to denote `câmpul de inducţie magnetică B`. This exact noun is not defined by the question and must not be silently rewritten.
- **A is overexclusive** because its `numai` would incorrectly rule out magnetic fields, and in charge-conserving steady conduction `div(J)=0` can itself be true. **B** electric field has nonzero divergence in regions with charge `div(E)=rho/epsilon0` (in vacuum), but can also be locally divergence-free where rho=0; thus avoid an unconditional never/always interpretation of the noun alone.
- Original context/source and independent terminology check needed. General scientific source: https://openstax.org/books/calculus-volume-3/pages/6-5-divergence-and-curl and https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Book%3A_Applications_of_Maxwells_Equations_%28Cochran_and_Heinrich%29/04%3A_The_Magnetostatic_Field_I/4.01%3A_Introduction .
- **Disposition:** `MAGNETIC_B_DIVERGENCE_FREE_RESEARCH / ORIGINAL_C_TERM_AMBIGUITY / NOT_APPROVED`. No certified letter.

## QABC-0019 | Sheet1!A27:D27 | G1-ELE-020 / G2-ELEC-172
> Capsularea monopolară conduce la : A eliminarea totală a posibilităţii apariţiei unui scurtcircuit între faze; B micşorarea riscului unor pierderi de gaz izolant; C reducerea cheltuielilor de realizare a instalaţiilor.
- Exact object: **single-phase enclosed GIS**, each phase in its own enclosure, distinct from a three-phase shared enclosure. The IEEE GIS overview explicitly distinguishes these constructions: https://technav.ieee.org/topic/gas-insulated-substations-gis/ . The metal enclosures interpose grounded barriers, supporting the **qualitative avoidance of interphase arcs inside shared gas volume**.
- **A is a conventional specific candidate** for inside the segregated apparatus, BUT `eliminarea totală` is absolute and does not prove that no interphase fault can occur anywhere in the entire connected installation (terminations, connections, enclosure transitions, multiple failure modes). This **scope restriction is mandatory**, not a license to change the original wording.
- **B** is not affirmed by segregation alone: extra gas-tight interfaces and enclosures can carry leak risks, but neither reduction nor increase is universally established without enclosure design and seals. **C** is not automatically a cheaper configuration; requires commercial/layout data, none supplied.
- **Disposition:** `PHASE_SEGREGATION_SUPPORTS_A_INTENT_WITH_ABSOLUTE_WORD_WARNING / KEY_NOT_PROVEN / NOT_APPROVED`.

## QABC-0080 | Sheet1!A95:D95 | G1-ELE-088 / G2-ELEC-233
> Împărţirea fiecărei faze a unei instalaţii capsulate într-un anumit număr de compartimente atrage după sine: A limitarea posibilităţilor de producere a unui defect în instalaţie; B mărirea riscului de producere a unor scăpări de gaz; C mărirea cantităţilor de gaz ce trebuie manipulate în cazul intervenţiei la un compartiment.
- Fundamental scope distinction: **compartmentation** can limit the **extent/consequences** of a fault or gas release and allow maintenance with unaffected bays isolated (IEEE GIS overview), but that does **NOT directly prove a reduction in the physical probability of defect INITIATION** as worded in A. Strong warning: do not substitute `fault propagation/extent` for `fault occurrence`.
- **B is an open competing hypothesis**, since dividing gas volumes may require more separate seals, interfaces and monitoring/access points, potentially affecting risk of leakage. However an accessible source proving a deterministic net increase in leak probability for *this exact physical installation* was NOT authenticated in the current research; do not claim B verified. Detailed manufacturer seal and leak-rate documentation is needed.
- **C conflicts with the usual aim of partitioning**, which confines gas handling to an isolated compartment; nevertheless actual gas volumes and maintenance procedures are not described. Do not assert every intervention uses less gas without evidence on cross-compartment transfers.
- Sources: https://technav.ieee.org/topic/gas-insulated-substations-gis/ for confinement, https://www.hitachienergy.com/me/en/products-and-solutions/high-voltage-switchgear-and-breakers/monitoring-and-controlled-switching/modular-switchgear-monitoring-msm for gas compartment identification and fault localization.
- **Disposition:** `A_FAULT_PROBABILITY_VS_CONSEQUENCE_SCOPE_MISMATCH / B_LEAKAGE_HYPOTHESIS_PENDING / C_GAS_VOLUME_UNPROVEN / SOURCE_AND_KEY_BLOCKED`. **No guessed A/B/C**.

## Research coverage and independent QA gates
| Work | Quantity | What it proves |
|---|---:|---|
| Exact initial P0 rows with all 4 workbook cells present | 12/12 | Source text/A/B/C presence only |
| Distinct QABC in at least one documented technical/scope research thread through CKPT-286 | 12/12 | Research coverage, not correctness |
| QABC-0024 vector drawing | 22 forms in relevant group | Original source figure can be inspected locally, not automatically shared to CI |
| Independent professional reviewer + official keyed 2026 exam proof | 0 | Still blocked |
| Approved student questions | 0 | App remains not ready for learner release |

**Method:** source text and option qualifier preserved; generic source not substituted for exact source scope; reviewer disagreement remains unresolved; no official key or specialized evidence invented. Old research retained in CKPT-282, 284 and 285 without repeated AI requests.

## Next shortest useful actions
1. Resolve **QABC-0080** by official course/manual explanation of *fault occurrence versus containment* and *gas-leak probability versus gas loss extent*; use independent source review before answer letter.
2. Resolve QABC-0013's original electrotechnics wording `câmp de inducţie electromagnetică` vs `inducţie magnetică B`, and QABC-0019's `eliminarea totală` apparatus scope.
3. Resume next priority units from previous consolidated 568-QABC/822-grade audit ledger, reusing existing evidence. Do not move to app until learner-gate approval.

**0 new API calls, 0 original QABC/key/HTML/APK/main changes, 0 merge/release. PR #7 and PR #13 Draft.**
