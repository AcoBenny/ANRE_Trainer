# CKPT-208 | Exact cross-grade duplicate keys: LEA service capacitance and double-busbar operation | 2026-11-18

## Source and exact data readback
Continuing CKPT-207 on PR #7 Draft. Retrieved `docs/QUESTION_AUDIT/V73_ALL_822_EVIDENCE_AND_RELEASE_GATES_MASTER.csv` from the audit branch. Checked **four original rows**, exact question and A/B/C equality in each pair, same source workbook `ELECTROTEHNICA-09.2024-2.xlsx` and same workbook source row within each pair; two cross-grade key contradictions verified by executable equality check, not inferred from identical topic keywords. No changes to canonical questions, keys or application.

## Pair A: `G1-ELE-018` / `G2-ELEC-170` (source workbook row 25)
**Original:** Capacitatea de serviciu Cs a unei linii electrice aeriene simetrice, având capacităţile C12=C23=C31 =C şi neglijînd influenţa pământului, este:
- A: `Cs=3 C`
- B: `Cs=C/3`
- C: `Cs=C`
- Imported Grade I key **A**; Grade II key **C**; both remain untouched.

### New exact affirmative physics/source review
Assuming the expressly stated *symmetric* three-phase ideal capacitive model without earth, interphase capacitors are equal `C12=C23=C31=C` (delta). For balanced three-phase potentials `V1+V2+V3=0`:
`q1=C(V1-V2)+C(V1-V3)=C(2V1-V2-V3)=3CV1`.
Therefore the line-to-neutral working/service capacity is `Cs=q1/V1=3C`. Option **A** is the unique match under this model. Option B mistakenly applies an inverse transformation; C confuses interphase capacitance `C_delta` with line-to-neutral/service capacitance.
- Independently fetched live instructional physics source: Physics LibreTexts, Tatum `5.7: Delta-Star Transform`, symmetric specialization yields `c1=3C`: https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electricity_and_Magnetism_(Tatum)/05%3A_Capacitors/5.07%3A__Delta-Star_Transform
- Secondary power-system-specific explanation with explicit `C_delta=C_n/3`: https://www.engineeringdevotion.com/electric-power-systems/lecture/chapter-7-capacitance-of-transmission-lines.html
- Negative gate: if the question's `Cs` were defined differently by its original textbook, the service-capacitance identity must be reopened. Neither source proves the precise ANRE imported scored key or official syllabus convention.
**Status: P0 HIGH-CONFIDENCE TECHNICAL CANDIDATE A FOR BOTH, KEY_CONFLICT_PRESERVED, NOT_APPLIED.**

## Pair B: `G1-ELE-102` / `G2-ELEC-245` (source workbook row 109)
**Original:** În cazul unei scheme cu două bare colectoare şi un întreruptor pe circuit este de preferat ca în regim normal de funcţionare:
- A: una dintre barele colectoare să fie sub tensiune, cealaltă bară fiind menţinută în rezervă rece;
- B: ambele bare colectoare să fie sub tensiune, cupla transversală fiind menţinută în funcţiune;
- C: ambele bare colectoare să fie menţinute sub tensiune, cupla transversală fiind în rezervă caldă.
- Imported Grade I key **A**; Grade II key **C**; unchanged.

### New primary normative context
Opened official Romanian NTE 009/10/00, `Regulamentul general de manevre în instalațiile electrice de medie și înaltă tensiune` (Ordin ANRE 25/2010): https://legislatie.just.ro/Public/DetaliiDocument/122751
- The norm defines `schema normală de funcționare` as a functioning scheme **approved by the responsible dispatch decision centre for a defined time**, not a universal topological answer to an underspecified preference.
- Defines `rezervă caldă` by breaker/disconnector state; it is not interchangeable with the coupler being in operation.
- Explicitly discusses cases where the bus coupler is **disconnected to keep short-circuit currents within breaking capacity** (section concerning interconnected busbar switching), disproving that coupler closed is always preferable.
- Thus **A** may be a valid operational regime, **B** may be possible subject to limiting conditions but cannot be asserted generally, and **C** is a common exam-intended availability/topology model; the code does not establish a universal preferred A/C without system, dispatch and short-circuit conditions.
- No physical switching instructions or authorization implied. No one should operate MV/HV equipment based on an MCQ.
**Status: P0 DOUBLE_KEY_CONFLICT_BLOCKED_MISSING_DESIGN_AND_EXAM_MODEL, no universal candidate key approved.**

## Gate and no-double-count record
- Checked exact 4 V73 records and original option strings across each grade pair; pair1 and pair2 both `QABC_EQUAL=true`, `SAME_WORKBOOK_ROW=true`, `IMPORTED_KEYS_DIFFER=true`. This is executed deterministic data QA and a *single assistant* physics/source interpretation, NOT separate independent QA.
- Primary exact-source retrieval complete for these two investigations, but **no official 2026 ANRE grading key**, no qualified human signoff or independently executing reviewer.
- `revisited_unique_QABC_units=2`, `grade_rows_checked=4`, `new_unique_units=0`, `key_changes=0`, `learner_approvals=0`; `independent_source_QA=NOT_RUN`, `independent_technical_QA=NOT_RUN`, `independent_linguistic_QA=NOT_RUN`.
- Next: independent content reviewer and official-key provenance before authorizing candidate key A for pair1; diagram/topology-specific literature required for pair2. Continue other disjoint blocked/legacy units, then app QA.
- No main merge, no release, no HTML/APK changes. Preserve PR #7 Draft.
