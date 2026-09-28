# Changelog

## [Unreleased]

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
