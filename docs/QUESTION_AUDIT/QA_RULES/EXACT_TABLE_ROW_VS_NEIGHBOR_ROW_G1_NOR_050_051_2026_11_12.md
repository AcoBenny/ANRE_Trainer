# Avengers Academy | G1-NOR-050/051: the exact normative TABLE ROW first | 2026-11-12

## User-derived rule applied
Continuing the preceding lesson `G1-NOR-041`: evaluate the **entire completed statement** and all conditions, not isolated true numeric phrases. Exact object and **specific normative table row** are first-class qualifiers; an answer can use a correct figure belonging to an adjacent row and still be a distractor. Preserve legitimate traps, never rewrite the original bank.

## G1-NOR-050 (Grade I, DEEP-NOR-03)
- Original: `Secţiunea minimă admisă pentru conductoare de fază din circuite pentru prize monofazate în instalaţiile electrice din interiorul clădirilor este de:`
- A `2,5 mm2 cupru`; B `1,5 mm2 cupru, 2,5 mm2 aluminiu`; C `4 mm2 aluminiu`. Stored key **A**, unchanged.
- Exact source: **I7-2011, §5.4.6 and Anexa 5.32 rows 1.2 and 1.3, Monitorul Oficial nr802bis/14.11.2011, printed page387**:
  - row1.2, **circuite pentru prize monofazate:** Cu **2,5 mm²**; aluminum table cell **EMPTY**;
  - row1.3, **circuite de putere (forță):** Cu **1,5 mm²**, Al **4 mm²** (note4).
- Primary printed-source reproduction as text: https://curentulelectric.ro/wp-content/uploads/2019/01/NORMATIV_I7_2011_actualizat.pdf , searchable lines in web PDF. Secondary *independent textual reproduction of same regulatory publication*, HTML https://www.infodosar.ro/monitorul-oficial/ministerul-dezvoltarii-regionale-si-turismului/132763-reglementari-0-2011 . This is not two different primary normative editions.
- **Evidence-access gate:** pdf text rows and printed page identified; `web.screen` page386 attempt failed cache miss, so we do **not claim visual inspection** of the PDF table. Official 2023 amending order https://legislatie.just.ro/Public/DetaliiDocument/271142 found and indexed, direct open failed502; exact current 2026 consolidated table is **NOT_CERTIFIED**. It is an important required revision gate, not permission to infer.
- Option-by-option:
  - **A supported as unique original-barem candidate** by precise row1.2.
  - **B unsupported** because it introduces values that are not row1.2 minimum for Cu, nor an aluminum entry; conjunction of invalid numeric choices cannot become valid.
  - **C unsupported for the asked row**, even though 4mm² Al **does** appear *right below* under 1.3 (force circuit). Empty row1.2 Al cell means **no minimum aluminum value is specified there**; this evidence alone does not prove a global ban of Al in every possible socket situation.
- **Prior pre-QA classification** `A_WITH_ALTERNATE_AL_CAVEAT` from `DEEP_NOR_03_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv` is **SUPERSEDED for G1-NOR-050** by `A_SUPPORTED_EXACT_ROW__C_ADJACENT_ROW_DISTRACTOR`. Retain prior triage intact.
- No edits to bank, stored key, HTML/APK; independent source/edition review NOT_RUN, approved_for_learning NO.

## G1-NOR-051: next human interpretation gate, NOT solved automatically
- Original: `Secţiunea minimă admisă a conductorului de fază pentru circuitul unui receptor electrocasnic monofazat cu putere de peste 2 kW este de:`
- A `2,5 mm2 cupru`; B `1,5 mm2 cupru, 2,5 mm2 aluminiu`; C `4 mm2 aluminiu`. Stored key **A**, unchanged.
- I7 §5.4.7 expressly says *in locuințe* receptoare >2kW require **separate socket circuits**, sized to load but no lower than Annex5.32. This supports mapping a domestic device (washing machine/AC example) to row1.2 in **locuințe**.
- But the question as stored does **not explicitly say** `locuințe` or `priză` and can in principle describe a hard-wired single-phase appliance or another building type. The potential object inference is `receptor electrocasnic >2kW => circuit separat de priză (in locuințe)`. That is a **genuine semantic/scope uncertainty**; do not transfer G1-NOR-050's result automatically.
- Proposed collaborative question: „Când vezi «circuitul unui receptor electrocasnic monofazat de peste 2 kW», înțelegi automat circuitul de priză separat din locuință, așa cum spune I7 §5.4.7, sau consideri că enunțul trebuie să menționeze explicit priză/locuință?”
- Human perspective enters `USER_HYPOTHESIS`, not source truth. Independently verify material, scope, edition and exact 2026 bibliography before signoff.

## Tested algorithm
`tools/qa_normative_table_row.mjs` + `tools/tests/qa_normative_table_row.test.mjs`:
1. Match object `circuite pentru prize monofazate` vs `circuite de putere` to exactly one I7 table row;
2. Normalize Cu/Al, 2.5 vs 2,5, mm² vs mm2, and validate the **full option**, including compound options;
3. Compare numeric value to the minimum **in that same row and material**. A missing material entry is `NOT_SPECIFIED_IN_SOURCE_ROW`, not proof of universal prohibition;
4. Missing/derived source-object matches or duplicate valid options => **blocked/escalated**, never auto-approve.

Ran **10/10 deterministic synthetic fixtures** using pure JS function equivalent in this tool session: original NOR050 A, NOR051 `SOURCE_OBJECT_MAPPING_REQUIRED`, force row with C, force copper with A, duplicate 2.5Cu, no valid choice, missing locator, incomplete ABC, wrong circuit, no-diacritics. Node test files saved in repo but **not run separately in CI/Node**. No independent expert QA.

## Follow-up
Use human interpretation + exact updated normative source to resolve NOR051. New semantics rule only applies to cases where a row-object match exists. Keep `0/822 learner approvals` until independent QA evidence; do not turn a deterministic regression into an answer signoff.
