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

### Phase 14 · V9.3 pinpoint source mapping
Mobile testing exposed that a generic ANRE landing-page link is not sufficient when the exact normative provision is known.

The tested question **G1-NOR-088** was mapped to **I7-2011, pct. 4.1.5.3.8**, which directly addresses metal enclosures of prefabricated distribution installations and their possible use as protective conductors.

V9.3:
- adds the punctual I7 mapping for G1-NOR-088;
- uses the same direct text-fragment mechanism as the other verified I7 references;
- keeps the generic ANRE page only for questions where no demonstrated pinpoint source is available;
- preserves the 822-question dataset and unique IDs;
- passes JavaScript syntax validation after the change.

The rule is now explicit:

**If an exact source provision is demonstrated, the learner gets the exact provision, not a generic portal homepage.**

### Phase 15 · V10.7 conflict resolution
The Grade I technical-norm verification reached three explicit answer conflicts where the application answer differed from the verified I7-2011 provision.

Resolved after punctual source verification:
- **G1-NOR-061:** A → B, I7-2011 pct. 5.2.12.3.4
- **G1-NOR-089:** A → B, I7-2011 pct. 5.1.4.3.3
- **G1-NOR-094:** A → C, I7-2011 pct. 5.5.7.11

The previous values were preserved as `Raspuns_initial` and the correction was recorded in a dedicated resolution registry. No conflict was silently overwritten.

### Phase 16 · V10.8 Grade II norms
The Grade II technical-norm/documentation batch was reviewed:
- **G2-NOR:** 12 questions
- **G2-NORM:** 3 questions
- **15/15** received an explicit bibliographic/source treatment.

The references were separated into three groups:
- **I7-2011:** local document access plus official Portal Legislativ verification;
- **PE 102/1986:** official ANRE bibliography reference, but no complete official text was demonstrated for safe offline bundling;
- **PE 155/1992:** official ANRE bibliography reference, but no complete official text was demonstrated for safe offline bundling.

### Phase 17 · V10.9 legislation verification
The next verification phase covers the **112 legislation questions**:
- 50 Grad I
- 62 Grad II

The legislation workflow uses the historical 05.2023 ANRE question-set context while checking the answer against the relevant official legal act and, where appropriate, its current consolidated form.

The initial official-source registry includes:
- **Legea nr. 123/2012**
- **Regulamentul pentru autorizarea electricienilor**, approved by Ordinul ANRE nr. 66/2023, with later amendments
- **Regulamentul de furnizare a energiei electrice la clienții finali**, approved by Ordinul ANRE nr. 5/2023
- **Regulamentul privind racordarea utilizatorilor la rețelele electrice de interes public**, approved by Ordinul ANRE nr. 59/2013, with subsequent amendments
- relevant ANRE thematic/bibliographic acts and tariff decisions where explicitly required.

The phase preserves the distinction between:
1. the source/version relevant to the historical exam question;
2. the exact legal provision supporting the stored answer;
3. the current consolidated form.

### Phase 18 · V10.9.2 legislation pinpoint mapping · Batch 1
The first punctual legislation batch was verified against the official Portal Legislativ.

**13 questions were closed at article/alineat/literă level without changing the application dataset yet.**

Important mapping corrections discovered in this batch:
- **G1-LEG-004** → Legea 123/2012, art. 58 alin. (5)
- **G1-LEG-005** → Legea 123/2012, art. 23 alin. (8), replacing the overly broad art. 52 reference
- **G1-LEG-015** → art. 92 alin. (1)
- **G1-LEG-016** → art. 92 alin. (1)
- **G1-LEG-021** → art. 49 alin. (1) lit. f)
- **G1-LEG-022** → art. 49 alin. (1) lit. a)
- **G1-LEG-023** → art. 2
- **G1-LEG-025** → art. 1 alin. (2) lit. b)
- **G1-LEG-026** → art. 92 alin. (2)
- **G1-LEG-038** → art. 3 alin. (1) pct. 13
- **G1-LEG-042** → art. 52 alin. (1)
- **G1-LEG-044** → art. 52 alin. (4)
- **G1-LEG-049** → art. 58 alin. (6)

No answer was silently changed. The work at this stage updates the evidence registry only. Answer changes, if ever required, will follow the same explicit conflict-resolution procedure used in V10.7.

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


### Phase 19 · V10.9.3 legislation pinpoint mapping · Batch 2
The second punctual legislation batch was verified against official Portal Legislativ sources.

**11 questions were closed at article/alineat level:**
- G1-LEG-001 → Legea 123/2012, art. 3 alin. (1) pct. 15
- G1-LEG-002 → art. 58 alin. (4)
- G1-LEG-003 → art. 58 alin. (4)
- G1-LEG-009 → art. 93 alin. (1) pct. 3
- G1-LEG-010 → Regulamentul aprobat prin Ordinul 66/2023, art. 29
- G1-LEG-011 → art. 47 alin. (1)-(2)
- G1-LEG-013 → art. 18 alin. (1) / art. 30 alin. (1)
- G1-LEG-014 → art. 22
- G1-LEG-017 → Legea 123/2012, art. 58 alin. (4)
- G1-LEG-018 → art. 67 lit. a)
- G1-LEG-019 → art. 93 alin. (1) pct. 3

The batch also exposed a useful version-control rule: current authorization regulations use the term "autorizație" while older question wording may use "adeverință/legitimație". Such terminology differences are retained in the audit rather than silently normalized.

No application answer was changed in this phase. The evidence mapping is being accumulated first; any answer correction will use an explicit conflict-resolution record.
