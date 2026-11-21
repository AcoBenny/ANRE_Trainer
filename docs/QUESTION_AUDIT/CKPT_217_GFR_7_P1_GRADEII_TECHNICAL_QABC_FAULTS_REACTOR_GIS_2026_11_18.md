# CKPT-217 | GFR 7 Grade II P1 technical cases: feeder reactors, fault sequences, GIS, single phasing | 2026-11-18

## Source-control and QA gates
- 7 distinct existing P1 grade II QABC, no duplicate of CKPT-216 direct cases, input V73 Git blob c027d417a8e4e605c830b2016fb55b099b8d130b. Previous candidate or 2026 exam official key NOT independently approved. Sources from manufacturer, CIGRE, open academic textbooks, IEC abstract; explicitly index-only IEEE 666 item, never pretend PDF visually validated.
- Preserve old answer key and A/B/C, separate physical model and negative distractor tests. HV switchgear context is explanatory, **not** field switching instructions. Single assistant, not truly independent agents. No canonical, app, APK, HTML or release changes.

### G2-ELEC-162 | SOURCE_COMPATIBLE_INDUCTION_AUXILIARIES
- Original question: Cele mai des utilizate pentru serviciile interne ale centralelor electrice sunt:
- A: motoarele de curent continuu
- B: motoarele sincrone
- C: motoarele asincrone
- Imported key **C**, preserved. Source workbook: ELECTROTEHNICA-09.2024-2.xlsx, row 17.
- A/B/C exact-object analysis: A DC motors occur in special emergency/DC-battery duties; B synchronous motors used for selected high power or specialized processes; C squirrel-cage induction/asynchronous motors dominate auxiliary pumps, fans and drives at conventional generating stations. The question lacks plant era/technology, so prevalence supported generically, not a universal 2026 plant count.
- Source: IEEE 666-1991 power station auxiliary motor guidance (search-indexed, PDF not visually opened): https://www.mdpi.com/1996-1073/17/5/1066
- Gate: SOURCE_COMPATIBLE_INDUCTION_AUXILIARIES, `independent_QA=NOT_RUN`, `approved_for_learning=NO`, `2026_exam_key=NOT_VERIFIED`.

### G2-ELEC-167 | DIRECT_DOWNSTREAM_REACTOR
- Original question: Bobinele montate pe plecari radiale limiteaza curentii de scurtcircuit
- A: atat inainte, cat si dupa punctele lor de racordare la barele statiei;
- B: inainte de punctele lor de racordare la barele statiei;
- C: dupa punctele lor de racordare la barele statiei.
- Imported key **C**, preserved. Source workbook: ELECTROTEHNICA-09.2024-2.xlsx, row 22.
- A/B/C exact-object analysis: An in-series reactor added at a radial outgoing feeder increases feeder fault impedance only for fault paths downstream of that reactor; C after bus connection is intended. A both upstream and downstream would imply reactor common to all fault paths, false; B upstream before it not limited by feeder reactor. Exact words 'dupa punctele lor de racordare' describe feeder downstream.
- Source: Networks for Electricity Distribution, current limiting reactor location: https://www.phasetophase.nl/book/book_1_4.html
- Gate: DIRECT_DOWNSTREAM_REACTOR, `independent_QA=NOT_RUN`, `approved_for_learning=NO`, `2026_exam_key=NOT_VERIFIED`.

### G2-ELEC-179 | CONDITIONAL_ALL_DISTRIBUTION_LEVELS
- Original question: Scheme cu un sistem de bare colectoare şi un întreruptor pe circuit sunt folosite
- A: numai pentru staţii de conexiuni de 6 kV
- B: pentru toate treptele de tensiune din reţelele de distribuţie
- C: numai pentru staţii de conexiuni de medie tensiune până la 6o kV
- Imported key **B**, preserved. Source workbook: ELECTROTEHNICA-09.2024-2.xlsx, row 37.
- A/B/C exact-object analysis: A 6 kV-only over-narrow; B single-busbar/single-breaker arrangement used across various distribution voltage levels and sometimes subtransmission where low-cost and less redundancy acceptable; C 'numai medie tensiune pana la 60 kV' is also over-narrow. But 'toate treptele de tensiune' is an absolute about applicability, not proof it is universally optimal or physically used at every voltage. C has typo '6o kV'.
- Source: Substation busbar configuration guide by EE Power: https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/
- Gate: CONDITIONAL_ALL_DISTRIBUTION_LEVELS, `independent_QA=NOT_RUN`, `approved_for_learning=NO`, `2026_exam_key=NOT_VERIFIED`.

### G2-ELEC-199 | CONDITIONAL_SINGLE_PHASING_TRANSFORMER
- Original question: Funcţionarea în doua faze a unui transformator trifazat are ca efect:
- A: supraîncălzirea acestuia
- B: suprasarcina
- C: reducerea puterii tranzitate
- Imported key **A**, preserved. Source workbook: ELECTROTEHNICA-09.2024-2.xlsx, row 60.
- A/B/C exact-object analysis: A overheating may result from phase loss/unbalanced excitation and currents, as Schneider warns; B loading constraints can yield thermal overload; C transmitted power/secondary quality can be reduced depending loading and construction. Without load, remaining phases, core and connection, more than one outcome is plausible, so intended A is not a uniquely demonstrated universal effect.
- Source: Schneider single-phasing three phase transformer technical FAQ: https://www.se.com/nz/en/faqs/FA107378/
- Gate: CONDITIONAL_SINGLE_PHASING_TRANSFORMER, `independent_QA=NOT_RUN`, `approved_for_learning=NO`, `2026_exam_key=NOT_VERIFIED`.

### G2-ELEC-334 | CONDITIONAL_POLLUTION_COATING_VS_DISTANCE
- Original question: Printre măsurile de reducere a distanţelor de izolare pot fi:
- A: folosirea dispozitivelor de limitare a curenţilor de scurtcircuit;
- B: aplicarea unui strat protector pe izolatoare pentru micşorarea efectelor poluării din marile oraşe sau de pe unele platforme industriale;
- C: micşorarea densităţii dielectricilor gazoşi.
- Imported key **B**, preserved. Source workbook: ELECTROTEHNICA-09.2024-2.xlsx, row 205.
- A/B/C exact-object analysis: A short-circuit limiting reactors act on current, not dielectric withstand or creepage distance. B hydrophobic coatings improve pollution resistance and can enable shorter insulator length / in appropriate engineering context creepage; C lower gas density normally worsens dielectric strength rather than enabling reduced clearance. But B does not universally justify arbitrary reducing of all isolation distances: type, pollution severity and standards govern.
- Source: CIGRE Electra 317 technical brochure on silicone coatings pollution: https://electra.cigre.org/317-august-2021/technical-brochures/coatings-for-improvement-of-electrical-performance-of-outdoor-insulators-under-pollution-conditions.html
- Gate: CONDITIONAL_POLLUTION_COATING_VS_DISTANCE, `independent_QA=NOT_RUN`, `approved_for_learning=NO`, `2026_exam_key=NOT_VERIFIED`.

### G2-ELEC-346 | DIRECT_GIS_ENCLOSURE_TYPE_PRINCIPLE
- Original question: Spaţiul ocupat de o instalaţie capsulată depinde în principal de:
- A: curentul nominal al legăturilor electrice;
- B: mediul de stingere a arcului electric;
- C: realizarea capsulării: capsulare tripolară sau monopolară.
- Imported key **C**, preserved. Source workbook: ELECTROTEHNICA-09.2024-2.xlsx, row 217.
- A/B/C exact-object analysis: A conductor rated current changes cross-sectional areas but not the main reason for the space saving of GIS; B interruption medium matters for breaker design, but C single/three phase enclosure architecture has a principal impact on GIS envelope/compactness. Exact 'principal' is context-dependent, so intended C supported conceptually, not a quantitative proof.
- Source: IEC 62271-203 2022 phase enclosure definitions and gas insulated switchgear concept: https://standards.iteh.ai/catalog/standards/clc/69ec8103-3522-4394-9ad8-6ddf96b05d9d/en-iec-62271-203-2022
- Gate: DIRECT_GIS_ENCLOSURE_TYPE_PRINCIPLE, `independent_QA=NOT_RUN`, `approved_for_learning=NO`, `2026_exam_key=NOT_VERIFIED`.

### G2-ELEC-353 | DIRECT_SEQUENCE_NETWORK_EXACT_FAULT
- Original question: Schema echivalentă de calcul în cazul producerii unui scurtcircuit între două faze ale unei reţele izolat de pământ şi fără arc electric se compune din:
- A: schema de secvenţă directă (pozitivă) înseriată cu triplul impedanţei arcului
- B: schemele de secvenţă directă (pozitivă) şi inversă (negativă) conectate în paralel
- C: schemele de secvenţă directă (pozitivă), inversă (negativă) şi homopolară (zero) conectate în paralel
- Imported key **B**, preserved. Source workbook: ELECTROTEHNICA-09.2024-2.xlsx, row 224.
- A/B/C exact-object analysis: For a line-line fault without earth, zero sequence current I0=0; the positive and negative sequence networks connect in parallel at fault terminals in the standard fault network diagram, so B. A injects triple arc impedance (but prompt says no arc) and omits negative sequence; C incorrectly includes zero-sequence ground network for non-grounded line-line fault. Distinguish source Thevenin series impedance sum Z1+Z2 in current formula from parallel terminal connection on network diagram.
- Source: Engineering LibreTexts Kirtley Unbalanced Faults §4.6 Figure 13: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Introduction_to_Electric_Power_Systems_%28Kirtley%29/04%3A_Introduction_to_symmetrical_components/4.06%3A_Unbalanced_Faults
- Gate: DIRECT_SEQUENCE_NETWORK_EXACT_FAULT, `independent_QA=NOT_RUN`, `approved_for_learning=NO`, `2026_exam_key=NOT_VERIFIED`.

## Totals and next action
- 7 existing grade IDs and source-focused cases, no new unique bank questions, 0 changed keys, 0 learner approvals. High-confidence textbook intended candidates B for G2-ELEC-353 positive/negative sequence, C for G2-ELEC-167 feeder reactor, C for G2-ELEC-162 general plant auxiliary. Do not certify unconditional results at 179/199/334 from topic proximity; exact scope still important.
- Next prioritize I7/normative grade I and II using exact section and neighboring exceptions; maintain PR7 Draft. No app tasks until bank validated.
