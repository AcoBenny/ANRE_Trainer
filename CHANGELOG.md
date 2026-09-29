# Changelog

## [Unreleased]

### V10.11 · Local evidence UX
- Changed evidence actions so the learner opens an internal evidence popup rather than being sent directly to a generic source page.
- I7 mappings expose the verified paragraph/fragment directly in the popup, with exact location.
- Other categories expose the locally available source row, verification basis and audit note, while explicitly stating when the full technical/normative paragraph is not embedded locally.
- Distinguished `Citește fragmentul relevant` from `Citește referința locală` so the UI does not overstate the evidence available.
- Kept exact official Portal links as a secondary verification action where a precise destination is known.
- Standalone HTML JavaScript syntax validation passed; runtime QA and Android synchronization remain pending.

The project is currently consolidating the final evidence-backed documentation system for all 822 questions.

### V9.1 · Evidence UX cleanup
- Separated internal audit metadata from the learner-facing question screen.
- Removed cross-reference/formulation audit text from the main question and exam views.
- Kept verification status, source and reference information in a compact evidence card.
- Added full-width clickable source actions for technical-reference cards.
- Preserved direct Portal Legislativ text-fragment links for verified I7 mappings.
- Validated the updated standalone HTML JavaScript with Node syntax checking.

### V9.2 · Evidence flow completion
- Removed the evidence card from the initial question and exam renders.
- Kept documentation/source evidence in the post-answer flow.
- Changed the post-answer renderer from the I7-only source function to the generic evidence-card renderer.
- I7 questions keep their verified direct paragraph card; other norms, legislation and electrotechnics questions now receive their appropriate source card.
- Confirmed 822 unique questions and syntax-checked the standalone HTML JavaScript with Node.


### V9.3 · Pinpoint source mapping
- Added a verified I7-2011 mapping for G1-NOR-088.
- Source location: **pct. 4.1.5.3.8**.
- Replaced the generic ANRE landing-page destination for this question with a direct official I7 paragraph link.
- Kept generic ANRE links only where no exact demonstrated provision is available.
- Preserved 822 unique questions and passed JavaScript syntax validation.


### V10.7 · Grade I norm conflict resolution
- Resolved G1-NOR-061 using I7-2011 pct. 5.2.12.3.4: A → B.
- Resolved G1-NOR-089 using I7-2011 pct. 5.1.4.3.3: A → B.
- Resolved G1-NOR-094 using I7-2011 pct. 5.5.7.11: A → C.
- Preserved prior answers as `Raspuns_initial` and retained a resolution audit trail.

### V10.8 · Grade II norms
- Completed G2-NOR + G2-NORM: 15/15 questions received explicit bibliographic/source treatment.
- I7-2011 uses local document access plus official Portal Legislativ verification.
- PE 102/1986 and PE 155/1992 remain external because a complete official text suitable for offline bundling was not demonstrated.

### V10.9 · Legislation verification
- Began source verification for all 112 legislation questions.
- Established the official-source registry around Legea 123/2012, the ANRE electrician authorization regulation, the electricity supply regulation and the grid-connection regulation.
- The phase distinguishes historical exam-source wording from the current consolidated legal text.
- Exact article/paragraph mapping is added only when demonstrated by the official source.

### In progress
- Final question-level evidence mapping
- Mobile UX validation
- Final Android packaging

## Historical milestones

### V9 · Evidence system
- Expanded the documentation-card concept from a small I7 prototype toward all 822 questions.
- Added question-level evidence/status tracking.
- Kept official references separate from technical cross-reference evidence.

### V8.x · I7 documentation prototype
- Introduced compact I7 documentation cards.
- Added direct Portal Legislativ text-fragment links where applicable.
- Corrected G1-NOR-025 from 20 mm to 15 mm after exact source verification.
- Corrected additional I7 mappings and source fragments.

### Earlier versions
- Consolidated Grad I and Grad II into a unified trainer.
- Added filtering, learning mode, mistakes, quick tests, simulations, statistics and local persistence.
- Added Android WebView packaging and GitHub Actions builds.


### V10.9.3 · Legislation pinpoint mapping · Batch 2
- Closed 11 additional Grade I legislation questions at official article/alineat level.
- Added punctual mappings for Legea 123/2012 arts. 3, 58, 67 and 93.
- Added punctual mappings for the electrician authorization regulation, including arts. 22, 29, 30 and 47.
- Kept historical wording such as "adeverință/legitimație" distinct from current consolidated terminology.
- No application answer was changed during this batch.


### V10.9.5 · Legislation conflict resolution
- Resolved G1-LEG-024: A → C after verification of the ATR requirement.
- Resolved G1-LEG-027: A → C using the current connection regulation, art. 33 alin. (1) lit. b).
- Resolved G1-LEG-028: B → C using Annex 3 pct. 2.3 of the connection regulation.
- Resolved G1-LEG-032: B → A using the authorization-regulation sanctioning framework.
- Resolved G1-LEG-034: B → A using authorization regulation art. 37 lit. e).
- Preserved every previous value as `Raspuns_initial`.
- Added a dedicated `RESOLVED_LEGISLATION_CONFLICTS` audit registry.
- Validated the 822-question dataset and JavaScript syntax after the corrections.
- Kept the correction in the working evidence prototype; final Android packaging remains pending completion of the legislation audit.


### V10.10 · Legislation Batch 4
- Resolved G1-LEG-043: B → A, supply regulation art. 26 alin. (4) lit. b), minimum 5 working days for non-household clients.
- Resolved G1-LEG-047: C → B, connection regulation art. 24, ATR as the network operator's offer.
- Resolved G1-LEG-048: A → B, household client's payment-method choice.
- Rechecked neighboring G1-LEG-041, 042, 044, 045, 046, 049 and 050 without changing their answers.
- Confirmed G1-LEG-050 against supply regulation art. 7 alin. (1) lit. d), minimum 3-month payment installment scheduling for vulnerable clients.
- Preserved previous answers and extended RESOLVED_LEGISLATION_CONFLICTS.
- JavaScript syntax validation passed; Android packaging remains pending.

### V10.16 · G2 Electrotehnică exact-source investigation
- Investigated the remaining G2 Electrotehnică records that were not supported by exact candidate fragments.
- Confirmed from the official ANRE 2023 bibliography that Electrotehnică is sourced to specialist manuals/books rather than one named normative textbook.
- Kept candidate rows from ELECTROTEHNICA-09.2024 separate from underlying technical-source evidence.
- Did not promote topic similarity or partial wording matches to exact-source verification.
- No answer conflict was introduced and no stored answer was silently overwritten.
- Remaining unresolved records now have a clear next step: identify the actual specialist manual/source used for the technical literature basis and perform pinpoint verification.

### V10.17 · G2 Electrotechnică technical-source research
- Started structured source research for the 71 unresolved G2 Electrotechnică records.
- Identified university/technical references supporting clusters of concepts: DC circuits, resistance, Ohm law, AC power, RLC resonance and electrical measurements.
- Created ANRE_Trainer_G2_ELEC_SOURCE_RESEARCH_V10_17.csv with candidate references and explicit non-promotion status.
- No answer was changed and no candidate reference was presented as an exact ANRE source.
- Next step: source fingerprinting using distinctive wording/formula combinations.

### V10.18 · Source-evidence closure
- Closed the current exact-source research gate for the remaining 71 G2 Electrotechnică records.
- Kept all 71 as non-exact-source evidence.
- No answer changes and no Raspuns_initial overwrite.

### V10.18 · Standalone release candidate
- Integrated V10.17 source-research state into the evidence UI.
- Preserved all 822 questions and existing evidence safeguards.
- Produced a self-contained release candidate with no external JS/CSS dependency.
- Local artifact SHA-256: `82b8801ac9c2c3520218dbfbc3f2fb464e885a8f08ab660b4a853d911bab5d5d`.

### V10.18 · Final static QA
- 822/822 questions present and unique.
- 414 Grad I + 408 Grad II.
- All answers A/B/C and all option fields populated.
- No external JS/CSS dependency.
- 71 unresolved G2 Electrotechnică source records remain explicitly non-exact.
- Chromium runtime validation could not complete in the isolated environment; no false claim of dynamic QA was made.
