# V16 | G2-ELEC-378–408 electrotechnical + Romanian linguistic screening

Date: 2026-11-09. Source: V10.29 canonical GitHub asset blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`; exact question/options/key/source row included in CSV. **31/31** real IDs, no fabricated IDs. QA model assisted: manual per-question electrical reasoning + deterministic marker detector for negation, exclusivity, conditions and comparisons. **No independent AI subagent or human SME launched**. All original keys untouched.

Class counts (review category, **not** signed-off correctness): FORMULA_CHECK 3, SAFETY_SOURCE 2, EXTERNAL_DIRECT 2, AMBIGUITY 2, SOURCE_GAP 1, PRINCIPLE 10, CONDITIONAL 11. 18 items with at least one lexical marker (regex captures words in options too, so flags are screening only). `INDEPENDENT_QA=NOT_RUN` for every row.

## Priority technical / linguistic review

**G2-ELEC-380**: voltage transformer shorted secondary = heavy current/damage risk. ARTECHE *Theory and Technology of Instrument Transformers*, booklet 2 §4.10 p30, textual PDF inspected; screenshot fetch failed, mark `TEXT_ONLY` and not screenshot-verified. https://www.el-instaenergo.cz/files/download/produkty/artche-pristrojove-transformatory/artche-high-voltage-instrument-transformers/arteche-technical-article-theory-and-technology-of-instrument-transformers-en.pdf

**G2-ELEC-390**: CT open secondary unsafe; vendor direct https://www.se.com/us/en/faqs/FA125574/ .

**G2-ELEC-381**: cosφ=1 can occur with compensating L/C at resonance, so “pur rezistiv” refers to equivalent impedance not necessarily exclusively resistors. **392**: flux electric of D (C) versus E (V·m), ambiguous, high priority. **388**: maximum power transfer requires Thevenin model. **379**: HV separator maneuvers safety. **396**: engineering resistivity notation.

Check 378: 400/sqrt(3)=230.94 V; option C 230 V (rounded). 387: parallel identical sources e and r/n.

## Source assurance

- Only explicitly linked pages have external text checks. `EXTERNAL_TEXT_CHECKED` does NOT establish ANRE official paragraph mapping or a certified technical answer. Canonical `Sursa` refers to historical question XLSX, not didactic instruction.
- Source URLs are not incorporated as offline copies; licensing and correspondence of exact claim to each source still gate app integration. ANRE lists source example sets on https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ but an example question set is not in itself explanatory training material.
- No actual offline HTML/APK runs and no independent QA. The `VERIFICAT TEHNIC` label from historical HTML is not fresh proof.
- Stage result = preliminary expert-role screening only, not approved answer keys. Traps requiring editorial review remain open.

## QA reproduction

Reparse HTML `const DATA=[...]`, filter ordered existing ID range, assert unique IDs and identical ABC, keys and source rows to canonical, run 4 lexical patterns against `Intrebare+A+B+C`, export versioned CSV; verify CSV row count and no code/application changes. Repeat manual checks only when paragraph/paging evidence available.
