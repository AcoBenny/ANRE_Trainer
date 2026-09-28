# ANRE Trainer · Project Journey

This document records the development journey of ANRE Trainer, from the initial question database through source verification, documentation, testing and Android packaging.

The goal is to preserve not only the final result, but also the reasoning, corrections and verification steps that produced it.

## Project snapshot

- **Questions:** 822
- **Grad I:** 414
- **Grad II:** 408
- **Platform:** standalone HTML + Android WebView
- **Mode:** offline-capable
- **Repository:** AcoBenny/ANRE_Trainer

## Journey

### Phase 0 · Concept
The project started as an interactive trainer for Romanian ANRE electrician examination preparation, with emphasis on practical learning, explanations and progress tracking.

### Phase 1 · Question dataset
The application was consolidated around **822 questions**:
- 414 Grad I
- 408 Grad II

The dataset was separated into electrotechnics, norms and legislation, while stable question IDs were preserved.

### Phase 2 · ANRE source discovery
Official ANRE material was identified and incorporated into the verification workflow, including:
- legislation question sets
- technical norms question sets
- electrotechnics question set
- ANRE examination bibliography and topic documents

A key distinction was established between an **official ANRE question source** and an **official normative source** used to justify an answer.

### Phase 3 · Full dataset audit
All 822 application questions were compared against the five principal ANRE Excel question sets.

Result:
- **668/822** matched the supplied ANRE Excel material textually.
- The remaining questions were treated separately rather than silently assuming that every application question came from those files.

### Phase 4 · Documentation system
A documentation card was designed for questions with source evidence.

The approved compact structure became:
- document title
- verification status
- exact location
- relevant fragment
- source/point identification
- direct link to the relevant official legislation where possible

The design deliberately avoids duplicate explanatory sections.

### Phase 5 · I7 verification
The existing I7 mappings were audited against the text of I7-2011.

One important correction discovered during verification was:

**G1-NOR-025**
- Initial mapping: 20 mm
- Verified location: I7-2011, pct. 5.3.3.19.1
- Correct distance of insulation in air: **15 mm**

Other mapping corrections included:
- G1-NOR-024 → pct. 5.5.3.5
- G1-NOR-026 → exact source fragment required for text anchoring
- G1-NOR-038 → expanded definition fragment
- G1-NOR-100 → 50 kΩ branch for Un ≤ 500 V

This illustrates an important project rule: a source reference is not considered verified merely because the topic appears to be related. The exact provision must support the answer.

### Phase 6 · Legislation verification
Legislation questions were separated from the technical norms.

The workflow distinguishes:
1. the historical/source version used by the exam question set;
2. the official normative act supporting the answer;
3. the current consolidated form when relevant.

This prevents later amendments from being confused with the wording used by an older examination dataset.

### Phase 7 · Norms verification
Normative references were mapped to official or documented sources where possible.

Historical references such as **PE 102/1986** and **PE 155/1992** are retained as bibliographic references when a complete official online text could not be demonstrated. They are not represented as fully verified integral documents without sufficient provenance.

### Phase 8 · Electrotechnics verification
Electrotechnics is treated differently from I7 and legislation.

ANRE's bibliography points candidates to technical manuals and specialist literature rather than to one single official electrotechnics textbook. Therefore the application labels these references as technical cross-reference evidence rather than falsely presenting a textbook as an official ANRE normative source.

### Phase 9 · Evidence registry
A final evidence registry was created to track source status at question level.

The intended statuses include:
- 🟢 VERIFIED OFFICIAL / VERIFIED PUNCTUALLY
- 🔵 OFFICIAL REFERENCE
- 🟠 SECONDARY SOURCE / TECHNICAL CROSS-REFERENCE
- 🔴 UNCLEAR / UNCONFIRMED

The status communicates the strength of the evidence. It is not a score for the quality of a question or source.

### Phase 10 · HTML validation
The standalone HTML is treated as the primary functional test target before Android packaging. This allows the documentation cards, navigation, question logic and offline behavior to be checked before the same asset is placed in the Android WebView.

### Phase 11 · Android packaging
The application was packaged as an Android WebView application and built through GitHub Actions.

The build configuration uses:
- JDK 17
- Gradle 8.9
- Android Gradle Plugin 8.7.3
- compileSdk 35
- minSdk 24
- targetSdk 35

### Phase 12 · V9.1 evidence UX cleanup
A manual mobile review exposed an important distinction between **audit metadata** and **user-facing evidence**.

The first V9 evidence implementation displayed internal audit language directly above the answers, including cross-reference notes and formulation warnings. This made the question screen unnecessarily dense and pushed the actual answers down.

V9.1 changes:
- removed internal audit text from the normal question and exam screens;
- kept verification status and source information in a compact evidence card;
- made the evidence action an explicit, full-width clickable button;
- ensured non-I7 technical references also have a navigable official ANRE source link;
- kept the detailed audit registry in the project data/history rather than the main exam UX;
- validated the resulting JavaScript with Node syntax checking.

The design principle is now explicit:

**Audit metadata supports development; evidence cards support the learner.**

### Phase 13 · V9.2 evidence flow
Mobile testing then exposed two related rendering issues.

First, the evidence card was being inserted before the learner answered. That was removed so the initial screen stays focused on the question and A/B/C.

Second, the post-answer renderer was still calling only the I7-specific source function. As a result, non-I7 questions had no documentation card after answering.

V9.2 now uses the generic evidence-card renderer after every answer:
- I7-mapped questions receive the verified I7 card with the direct paragraph link;
- other technical-norm questions receive the compact technical-reference card;
- legislation questions receive the appropriate legislative/ANRE source card;
- electrotechnics questions receive the technical cross-reference card;
- no evidence card is shown before the answer.

The intended learner flow is:

**Întrebare → A/B/C → răspuns → feedback → card documentație → sursă**

The standalone HTML JavaScript was syntax-checked successfully after this change.

## Verification philosophy

The project deliberately records corrections and uncertainty.

A changed answer or mapping is not hidden. When verification disproves an earlier assumption, the correction becomes part of the project history.

This is especially important for an examination trainer where a plausible-looking reference can still be technically wrong.

## Continuing the journey

Future development should continue this document rather than replacing it.

Recommended commit style:

- `feat:` new functionality
- `verify:` source or answer verification
- `fix:` correction
- `test:` validation
- `docs:` documentation
- `build:` Android/release work
