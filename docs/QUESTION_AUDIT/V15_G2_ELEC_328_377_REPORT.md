# V15 | G2-ELEC-328–377 electrotechnical + Romanian linguistic screening

Date: 2026-11-09. Source: V10.29 canonical GitHub asset blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`; exact question/options/key/source row included in CSV. **50/50** real IDs, no fabricated IDs. QA model assisted: manual per-question electrical reasoning + deterministic marker detector for negation, exclusivity, conditions and comparisons. **No independent AI subagent or human SME launched**. All original keys untouched.

Class counts (review category, **not** signed-off correctness): PRINCIPLE 14, AMBIGUITY 7, CONDITIONAL 15, FORMULA_CHECK 7, SOURCE_GAP 5, KEY_CONFLICT_POSSIBLE 1, EXTERNAL_DIRECT 1. 33 items with at least one lexical marker (regex captures words in options too, so flags are screening only). `INDEPENDENT_QA=NOT_RUN` for every row.

## Priority technical / linguistic review

**G2-ELEC-358**: `B=-X/(R²+X²)` for `Z=R+jX`; canonical answer C is NOT general for mixed impedance, official-question phrasing omits pure-reactance assumption. Supporting university textbook https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electricity_and_Magnetism_%28Tatum%29/13%3A_Alternating_Current/13.06%3A_Admittance

**G2-ELEC-359**: CT secondary must not be open while primary current flows; direct vendor evidence https://www.se.com/us/en/faqs/FA125574/ .

Other flagged: 329 (only enclosure protects personnel), 335 (only rotor effect), 353 and 355 (symmetrical component fault models without exact diagram), 357 (air spacing personnel vs dielectric service reliability), 365 (fuse interrupts but does not prevent rise), 367 (only real physical quantities), 350 (conservator role). Math checks: 337=6 Ω, 347=1 Ω, 344=sqrt(3) Iphase.

## Source assurance

- Only explicitly linked pages have external text checks. `EXTERNAL_TEXT_CHECKED` does NOT establish ANRE official paragraph mapping or a certified technical answer. Canonical `Sursa` refers to historical question XLSX, not didactic instruction.
- Source URLs are not incorporated as offline copies; licensing and correspondence of exact claim to each source still gate app integration. ANRE lists source example sets on https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ but an example question set is not in itself explanatory training material.
- No actual offline HTML/APK runs and no independent QA. The `VERIFICAT TEHNIC` label from historical HTML is not fresh proof.
- Stage result = preliminary expert-role screening only, not approved answer keys. Traps requiring editorial review remain open.

## QA reproduction

Reparse HTML `const DATA=[...]`, filter ordered existing ID range, assert unique IDs and identical ABC, keys and source rows to canonical, run 4 lexical patterns against `Intrebare+A+B+C`, export versioned CSV; verify CSV row count and no code/application changes. Repeat manual checks only when paragraph/paging evidence available.
