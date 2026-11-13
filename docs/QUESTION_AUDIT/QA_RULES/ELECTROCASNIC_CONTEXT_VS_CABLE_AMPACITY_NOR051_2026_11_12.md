# Avengers Academy | G1-NOR-051 | Terminology-led context vs cable power limits | 2026-11-12

## User reasoning and new QA lesson
The user argues **A = 2.5 mm² Cu** because the stem says **receptor electrocasnic monofazat de peste 2 kW**: domestic context strongly indicates a dedicated socket circuit; 1.5 mm² Cu and 4 mm² Al seem inappropriate to the expected socket installation. This is a **user perspective/hypothesis** which must be checked against the actual regulatory paragraph and separate engineering assumptions.

**Core new rule:** use *domain term + power condition + explicitly applicable norm* to recover an otherwise implied context, but **inferred context does NOT imply universal physical certainty**. A domestic appliance can sometimes be permanently connected; if stated, stop the socket inference and apply the correct separate rule.

## Canonical question
- ID `G1-NOR-051`, Grad I, `DEEP-NOR-03`; original key **A**, QABC unchanged.
- Stem: `Secţiunea minimă admisă a conductorului de fază pentru circuitul unui receptor electrocasnic monofazat cu putere de peste 2 kW este de:`
- A `2,5 mm2 cupru`; B `1,5 mm2 cupru, 2,5 mm2 aluminiu`; C `4 mm2 aluminiu`.

## Evidence (distinguish source from hypothesis)
- I7-2011 **§5.4.7** explicitly says in **locuințe** receivers **peste 2 kW**, e.g. washing machines and air conditioners, require **circuite de priză separate**, and their cross sections are sized to receiver load, *not lower* than I7 **Anexa5.32**. Source officially indexed text: https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4 ; official page direct open produced **502** in this turn. Readable reproduction: https://www.infodosar.ro/monitorul-oficial/ministerul-dezvoltarii-regionale-si-turismului/132763-reglementari-0-2011 .
- I7 Anexa5.32 row **circuite pentru prize monofazate** shows Cu **2.5mm²**, Al **not specified**. Row **circuite de putere** has Cu **1.5mm²**, Al **4mm²**. Thus C borrows Al figure from another circuit category, B is not an exact minimum for the indicated socket row. Reproduction https://www.electroschema.ro/blog/sectiuni-minime-circuite ; prior `EXACT_TABLE_ROW_VS_NEIGHBOR_ROW_G1_NOR_050_051_2026_11_12.md`.
- Source scope nuance: the stem does not explicitly state `locuință` or `priză`. Its wording closely parallels the I7 household appliance example, supporting *historical intended answer A*, but connection can sometimes be hardwired and actual minimum then depends on the exact type of circuit, building, equipment and norm. Avoid claiming that `electrocasnic => prize` with mathematical certainty. Match source object/era before promoting learning approval.
- `Ordin 959/2023` modifies I7-2011: https://legislatie.just.ro/public/DetaliiDocument/271142 . The full current consolidated 2026 chain and any amendment to the exact sections is NOT independently certified.

## Physical correction / very important QA independence
The user proposed 1.5mm² Cu has a maximum 2.3kW, and 2.5mm² Cu 3.6–4.6kW, and 50% of a presumed maximum for safety. **These are not universal cable ratings or automatic normative dimensioning rules.**
- `2.3kW /230V ≈10A` for a resistive load, but Iz for a given 1.5mm² or 2.5mm² conductor depends on **installation method, insulation, ambient temperature, grouping, active conductors, correction factors, circuit length/voltage drop, protective device and load power factor**.
- I7-2011 current-rating method §5.2.4.1 and annex5.10–5.21: https://legislatie.just.ro/Public/FormaPrintabila/00000G3GW51PBYM7GIP1NKJV30HYMZM0 (official text indexed).
- Independent engineering crosscheck from Schneider Electric guide: https://www.electrical-installation.org/enwiki/Conductor_sizing%3A_methodology_and_definition and https://www.electrical-installation.org/enwiki/Recommended_simplified_approach_for_cable_sizing . For a real design check `I_b <= I_n <= I_z` plus voltage drop and any special equipment constraints, not arbitrary 50% derating.
- **Normative floor is distinct from current-carrying capacity**. The example's A=2.5mm² Cu is the prescribed **minimum under intended socket context**, not proof it can carry any load above2kW or cannot be exceeded by a higher section.

## Cross-model verification: Gemini
- Queried available ChatGPT plugin directory by `Gemini` exactly and `Google Gemini AI`: **no Gemini chat plugin found**. The Google Drive/Calendar/marketing connectors are NOT Google Gemini chat access, so do not assert Gemini independently reviewed this question.
- An external Google Gemini review could be obtained via user's separate Gemini interface or, with explicit setup, the **Gemini Developer API**. Google docs https://ai.google.dev/gemini-api/docs/pricing and https://ai.google.dev/gemini-api/docs/rate-limits mention limited free-tier access and account/project-specific quotas. **NO API call was made; no Gemini verdict exists.**
- If an independently generated Gemini report is later supplied, compare its source/article/edition, exact material table and *answer-by-answer premises*, not model's yes/no alone.

## Tested semantic prototype
- `tools/qa_electrocasnic_context.mjs` cautiously emits `CANDIDATE_INFERRED_DOMESTIC_SOCKET_CONTEXT` with letter **A** for original, flags `INFERRED_NOT_LOGICALLY_FORCED`, `MINIMUM_NORMATIVE_NOT_CABLE_POWER_RATING`, `ACTUAL_CABLE_SIZING_REQUIRED`.
- Test file `tools/tests/qa_electrocasnic_context.test.mjs`: 10 synthetic cases, original, explicit socket, hardwired, industrial scope, low power, wrong material, missing norm, duplicate options, phase mismatch, area dimension wrong. Same JS functions executed in JS tool runner **10/10 PASS**; persisted standalone Node/CI tests **not executed independently**. No source edition certification or expert QA in this run.
- All canonical question/options/key unchanged. `INDEPENDENT_QA=NOT_RUN`, `APPROVED_FOR_LEARNING=NO` for source/answer validity. PR Draft, no merge/release.
