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


### Phase 20 · V10.9.5 legislation conflict resolution
The first legislation conflict-resolution pass was completed after independent verification of the relevant legal provisions.

Five conflicts were resolved:
- **G1-LEG-024:** A → C, based on the ATR requirement in the applicable connection procedure.
- **G1-LEG-027:** A → C, Regulation on connection, art. 33 alin. (1) lit. b), 12 months when the connection contract has not been concluded.
- **G1-LEG-028:** B → C, Regulation on connection, Annex 3 pct. 2.3: individual metering groups are centralized, at ground floor or on the landing.
- **G1-LEG-032:** B → A, authorization regulation sanctions the prohibited activity; the mere age of a still-valid authorization document is not itself the stated sanctioning ground.
- **G1-LEG-034:** B → A, authorization regulation art. 37 lit. e): respecting the project is an explicit obligation; participation in reception/commissioning is conditional on being requested.

The previous values were preserved as `Raspuns_initial`. A dedicated `RESOLVED_LEGISLATION_CONFLICTS` registry was added to the working HTML so the corrections remain auditable.

A further quality-control point was recorded: G1-LEG-034 had initially been omitted from the Batch 3 conflict count even though its stored answer also differed from the verified provision. It was therefore included before the resolution was finalized.

The working prototype was validated with:
- 822 questions
- 822 unique IDs
- JavaScript syntax check passed
- all five corrected records retain their original answer value in `Raspuns_initial`

No Android release was produced from this working correction until the remaining legislation audit is completed.


### Phase 21 · V10.10 legislation Batch 4
Batch 4 continued the punctual audit of Grade I legislation questions, focusing on the electricity supply regulation and grid-connection regulation.

Three answer conflicts were resolved:
- G1-LEG-043: B → A, supply regulation art. 26 alin. (4) lit. b): minimum 5 working days for non-household clients.
- G1-LEG-047: C → B, connection regulation art. 24: the ATR contains the technical connection solution and constitutes the network operator's offer to the applicant.
- G1-LEG-048: A → B, supply regulation: the household client may choose among payment methods made available by the supplier.

The same batch also rechecked neighboring questions G1-LEG-041, 042, 044, 045, 046, 049 and 050. Their answers were not changed. In particular, G1-LEG-050 was confirmed against art. 7 alin. (1) lit. d), which provides for payment installment scheduling for a minimum of 3 months at the vulnerable client's request.

Previous values were preserved in Raspuns_initial, and the corrections were appended to RESOLVED_LEGISLATION_CONFLICTS.

Validation after the batch:
- 822 questions
- 822 unique IDs
- JavaScript syntax check passed
- no Android release generated yet; legislation audit continues.


### Phase 22 · V10.11 local evidence UX

The evidence flow was refined after mobile review showed that a source button can still feel like an external hand-off instead of documentation that can be read immediately.

The new rule is:

**Evidence button → internal evidence popup → relevant local content → optional official source**

For I7 mappings, the popup now exposes the verified source fragment directly, together with its exact chapter and paragraph.

For the other categories, the popup exposes the locally available source row, the exact verification basis, the stored verification note and any recorded cross-reference. It explicitly states when the integral normative/technical paragraph is not embedded locally, rather than inventing or implying that a source paragraph is available.

The learner-facing button wording now distinguishes:
- **„Citește fragmentul relevant”** when a verified local paragraph/fragment exists;
- **„Citește referința locală”** when only the local source-row evidence is available.

This preserves the project rule that evidence must lead to relevant information rather than a generic portal page.

The external official link remains secondary and is shown only when an exact official destination is known.

The V10.11 standalone HTML was JavaScript syntax-checked successfully. Runtime/browser QA remains the next gate before Android asset synchronization.


### Phase 26 · V10.15 source adjudication and journey continuation
The next phase begins from the V10.14 candidate registry and applies the multidisciplinary verification pipeline to the 76 G2 Electrotechnica records.

For each record:
1. compare Master wording with the local candidate;
2. compare all A/B/C alternatives;
3. verify whether the candidate actually supports the stored answer;
4. inspect wording traps such as mandatory/optional, minimum/maximum, thresholds, exceptions and conditional phrasing;
5. classify as SUPPORTED, CONFLICT or INSUFFICIENT_SOURCE;
6. preserve the original Master answer and candidate evidence without silent overwrites.

Candidate similarity is never promoted automatically to verified evidence.

The learner evidence model remains unchanged: exact verified fragments may be shown as readable evidence; candidate or insufficient evidence must be labelled honestly and must not masquerade as a verified paragraph.

The broader source-ingestion work continues for remaining records without exact source support.


### Phase 27 · V10.16 exact-source investigation · G2 Electrotehnică
The V10.16 investigation reviewed the remaining G2 Electrotehnică records that could not be promoted from candidate matching.

A key source-level finding was confirmed against ANRE's official **Tematica și bibliografia pentru examenul de autorizare electricieni 2023**: for Electrotehnică, item 1 specifies **knowledge of electrotechnics, electrical measurements and electrical machines**, and explicitly states that candidates may study **manuals and books from specialist technical literature**. Unlike the legislation and ANRE-regulation entries, the bibliography does not identify one single normative textbook or document that can serve as the exact source for every electrotechnics question.

The remaining records were therefore not falsely promoted to exact-source verification. The candidate rows from ELECTROTEHNICA-09.2024 were treated as question-bank provenance/cross-reference material only when the wording and A/B/C alternatives actually matched. A similar topic or a mathematically related question was not accepted as exact evidence.

Outcome:
- no new answer conflict was introduced;
- no Raspuns_initial value was overwritten;
- records without a demonstrated exact technical source remain explicitly unresolved at source level;
- the next valid path is to obtain/identify the actual specialist manual(s) used as the technical literature basis, then perform pinpoint verification against those sources.

This phase confirms the project rule: **ANRE question-bank provenance is not the same thing as exact technical-source evidence.**


### Phase 28 · V10.17 technical-source research · G2 Electrotehnică
A first structured technical-source research pass was performed for the 71 G2 Electrotehnică records still lacking exact-source proof.

The official ANRE bibliography remains the governing source-selection rule: Electrotechnics is defined as knowledge of electrotechnics, electrical measurements and electrical machines, with manuals and books from specialist technical literature explicitly permitted as study material. The bibliography does not nominate one single textbook.

Several university/technical references were identified that support clusters of the stored concepts, including:
- UTCN electrical-engineering teaching material for DC circuits, equivalent resistance and Ohm-law relations;
- UPT engineering-physics material for series/parallel resistance, Joule energy and electrical power;
- UTCN electrotechnics material for AC power, apparent/reactive power and power factor;
- university electrotechnics material for RLC series impedance and resonance;
- technical measurement material for ammeter/voltmeter concepts.

These references are recorded as CANDIDATE_REFERENCE_ONLY. They do not prove that a particular ANRE question was copied from, derived from, or authored from that specific textbook/course. Therefore no pending question was promoted to exact-source evidence and no answer was changed.

A dedicated research register was created:
ANRE_Trainer_G2_ELEC_SOURCE_RESEARCH_V10_17.csv

The next step is targeted source fingerprinting: search distinctive wording/formula combinations from each unresolved question against identifiable specialist books/courses, and promote only when the source text can be demonstrated sufficiently to support the stored answer.


### Phase 29 · V10.18 source-evidence closure decision
The remaining G2 Electrotechnică source research was closed conservatively for the standalone release. The 71 records have candidate technical references and conceptual support, but no demonstrated exact specialist-manual source was established. They therefore remain non-exact-source records. No stored answer or Raspuns_initial was overwritten, and no candidate was promoted merely because a concept matched.


### Phase 30 · V10.18 standalone release candidate
The evidence-aware standalone HTML was promoted from the V10.15 adjudication build to V10.18. It retains all 822 questions and the compact evidence workflow, and now surfaces the V10.17 research state for the 71 unresolved G2 Electrotechnică records directly in the evidence modal. The release candidate is fully self-contained with no external JavaScript or stylesheet dependency.
Local artifact SHA-256: `82b8801ac9c2c3520218dbfbc3f2fb464e885a8f08ab660b4a853d911bab5d5d`.


### Phase 31 · V10.18 final static QA
Release QA completed against the V10.18 standalone artifact: 822/822 records present, 822 unique IDs, 414 Grad I, 408 Grad II, all stored answers are A/B/C, all questions have A/B/C options, and the standalone contains no external JavaScript or stylesheet dependency. The 71 V10.17 G2 Electrotechnică research records are all still explicitly non-exact-source.
Dynamic Chromium execution was attempted in the isolated runtime but was blocked/hung by the execution environment, so no new claim of full browser-runtime validation is made. Existing manual QA history remains the functional baseline; the V10.18 code delta is limited to evidence metadata presentation and release metadata.


### Phase 32 · V10.18 evidence-context refinement
Evidence presentation was refined after review: the source fragment is no longer displayed as an isolated sentence only. Where question-level detail exists, the evidence modal now adds a compact contextual justification containing the reason for the correct answer and the specific explanation for the stored correct option. The original source fragment remains unchanged and separately identifiable, preserving the distinction between source text and explanatory context.
Static checks passed: 822 IDs present, no external JS/CSS dependency, JavaScript syntax valid. Updated local artifact SHA-256: `fdd97e6dd3f7f862e7ce64ddf4833f1aac47c330bf3d283f9fa19b8b12747a5d`.


### Phase 33 · V10.19 explanation coverage RC1
The project moved from evidence-context presentation to question-level pedagogical justification coverage.

The V10.18 standalone was audited and confirmed to contain **641/822 questions without a populated `detail.why` explanation**. Those records were grouped into:
- 255 Grad I Electrotechnics
- 246 Grad II Electrotechnics
- 90 Grad I Technical Norms
- 50 Grad I Legislation

A first research-backed RC1 pass populated explanations for all 641 records. Identical question wording across Grad I/II is intentionally handled as one explanation source, resulting in **374 distinct explanation units** rather than duplicating independent reasoning.

Each newly populated record now carries:
- `detail.why` = learner-facing justification;
- `detail.remember` = compact retention cue;
- `detail.justification_type` = category of reasoning;
- `detail.justification_status` = RC1_RESEARCHED_EXPLANATION;
- `detail.source_basis` = existing verification/source basis;
- `Audit.justificare_pedagogica` = explicit statement that the explanation is trainer-authored and not an official ANRE barem.

The pass preserves all stored answers and existing source evidence. It does **not** convert ANRE question-bank provenance into normative-source proof.

Technical examples include explicit formulas and reasoning for Joule heating, series capacitors, electric induction, inductive short-circuit limitation, service capacitance and transformer construction. Legislation and norms retain their existing verification basis instead of inventing article references.

Static validation of the RC1 artifact:
- 822 records
- 822 unique IDs
- 822/822 populated explanations
- 822/822 A/B/C answers present
- no source fields intentionally removed
- local artifact SHA-256: `1f056eea6b0e7b87be4eacdb68642ae096b9427cc098f5c56236a8f23d3a8c28`

RC1 is an explanation-coverage milestone, not yet the final pedagogical sign-off. The next QA gate is targeted review of explanation specificity, wording traps, formulas and source alignment before Android packaging.


### Phase 34 · V10.19 RC1 audit-label correction
The explanation-coverage artifact was relabelled conservatively after QA review. The 641 newly populated explanations are now explicitly classified as `RC1_COVERAGE_EXPLANATION`: they are trainer-authored explanations derived from the existing ANRE question-bank/verification basis plus technical-principle checks, not claims that every record has undergone individual external-source verification.

This keeps the evidence model honest while preserving the completed learner-facing coverage. The next phase is targeted external-source and pedagogical QA of the explanation corpus, with special attention to legal/normative wording, numerical limits, formulas and wording traps.

Updated RC1 SHA-256: `a44a223ba5373164112230fa8b7252958fbc31151df786d92a8de811337b25ef`.


### Phase 35 · V10.20 explanation/UI QA after mobile review
A mobile review exposed two separate issues in V10.19 RC1.

**1. Explanation clarity**
The post-answer explanation was carrying a full three-option analysis card, which made the learner-facing result unnecessarily dense. More importantly, targeted QA found several RC1 explanations that referenced the wrong option letter. The clearest example was **G2-ELEC-245**, where the stored answer is C but the generated explanation incorrectly discussed option A. The answer itself was not changed.

G2-ELEC-245 was rechecked against the 09.2024 electrotechnics question material and technical references describing double-bus arrangements and the operational meaning of “rezervă caldă”. The explanation was rewritten to directly explain why the stored C configuration is the intended normal operating arrangement. ANRE's current electricity page lists ELECTROTEHNICA-09.2024 among the examination materials; the supporting technical references distinguish a hot reserve as an element ready to be brought into service by closing its breaker. citeturn0search0turn1search1

The learner-facing explanation renderer was simplified to:
- **De ce este corect?** → one clear justification;
- optional **De reținut** → one compact memory cue;
- no automatic three-card A/B/C analysis unless separately needed.

**2. Last-question navigation**
The learning-mode navigation was reviewed. The existing logic already wrapped the index internally, but the UI did not make the boundary explicit. V10.20 now changes the final button label to **„Reia de la început →”** on the last question, while preserving the existing wrap behavior. This removes the ambiguity visible on mobile and makes the end-of-list behavior explicit.

QA flags were added to 20 records where the explanation corpus needs targeted review. Stored answers were preserved: **0 answer changes**.

Static validation:
- 822 records
- 822 unique IDs
- 822/822 explanations populated
- 0 answer changes
- no external JS/CSS
- JavaScript syntax valid
- 20 targeted explanation QA flags
- V10.20 SHA-256: `dda0cdd6d64e1c64fb6ffc18637c5ac22c46a9bb3c8eb6b0eafb0b88a273780e`

This phase is deliberately a QA correction, not a cosmetic-only change: it prevents a generated explanation from contradicting the stored answer while keeping the learner interface compact.


### Phase 36 · V10.21 multidisciplinary linguistic/pedagogical QA · targeted correction pass
The next pre-APK quality gate was started as an explicit multidisciplinary review of the 822-question standalone corpus.

The review covered:
- 🇷🇴 linguistic formulation and wording-trap detection;
- 🎓 examiner-style answer/explanation consistency;
- 👨‍🏫 pedagogical clarity of the learner-facing justification;
- ⚡ electrotechnics terminology and option alignment;
- 📚 normative wording consistency;
- ⚖️ legislation wording consistency;
- 🧪 static integrity and JavaScript syntax.

The first automated screening identified many **attention triggers** such as negations, conditional wording, minimum/maximum expressions, modal terms and absolute wording. These are review signals, not automatic errors.

A stricter answer/explanation consistency pass then isolated **18 genuine explanation mismatches** from the broader lexical triggers. The stored answers were not changed. The 18 explanations were rewritten so that the explanation explicitly supports the stored answer instead of naming a different option.

Corrected records:
- G1-ELE-089
- G1-ELE-094
- G1-ELE-125
- G1-ELE-137
- G1-ELE-138
- G1-ELE-249
- G1-ELE-266
- G1-ELE-267
- G1-LEG-022
- G1-LEG-037
- G1-NOR-039
- G1-NOR-044
- G1-NOR-045
- G1-NOR-046
- G1-NOR-049
- G1-NOR-069
- G1-NOR-077
- G1-NOR-082

For the I7-related corrections, the current Portal Legislativ text was also checked where applicable. In particular, the official I7 text defines “parte activă” as a conductor or conductive part intended to be energized in normal operation and specifies the factors used for admissible current determination, including conductor material, section, insulation and installation method. citeturn1search0turn1search1

Static release checks after the corrections:
- 822 records
- 822 unique IDs
- 414 Grad I
- 408 Grad II
- 822/822 populated explanations
- 0 answer changes
- 0 remaining explicit answer/explanation contradictions under the targeted detector
- no external JS/CSS dependency
- JavaScript syntax valid
- local artifact SHA-256: `36a562ea7db8b8f72dfa9344d8c56212460e307551ad9ee3f7dcfc18d21c7657`

This is a targeted correction milestone, not the final linguistic sign-off. The next QA layer should review the broader wording-trigger set and the high-frequency generic explanation templates before the standalone is declared APK-ready.


### Phase 37 · V10.22 explanation deep QA · 623 coverage explanations rewritten
The broad wording review identified **623 records** carrying the V10.19/V10.21 coverage-explanation status. These were the approximately 600 explanations previously flagged as too generic.

A dedicated deep-QA pass rewrote all 623 learner-facing justifications while preserving:
- the stored answer;
- the existing source/evidence basis;
- the existing retention cue;
- the distinction between trainer-authored explanation and official ANRE barem.

The rewrite replaced repeated boilerplate with compact, question-specific explanations. Where the question itself establishes a definition, unit, relation, instrument, physical law or technical condition, the explanation now states that decisive relationship directly. Normative and legislative explanations retain their source-basis distinction and do not invent new article references.

Additional consistency checks after the rewrite:
- 822 records
- 822 unique IDs
- 623 explanations rewritten
- 181 pre-existing non-RC1 explanations left intact
- 0 stored answer changes
- 0 targeted answer/explanation letter mismatches
- 0 remaining instances of the three major V10.21 generic explanation templates in the rewritten set
- 565 unique explanation texts across the full corpus
- JavaScript syntax valid
- no external JS/CSS dependency
- V10.22 SHA-256: `f1398c7351790593db97879a71f4ac5106600b15c65254a3dfb25f4b9c698861`

This phase is an explanation-quality rewrite, not a claim that every rewritten explanation has been independently externally source-verified. Existing source verification statuses remain authoritative.


### Phase 38 · V10.23 linguistic + examiner QA · full 822-question wording gate
The V10.22 explanation rewrite was followed by a dedicated wording-risk and examiner-style QA gate across the complete 822-question corpus.

The review explicitly targeted:
- negations and double negatives;
- conditional wording such as „în cazul în care”, „dacă” and „atunci când”;
- minimum/maximum and threshold expressions;
- mandatory versus permissive wording;
- absolute wording such as „întotdeauna”, „numai” and „exclusiv”;
- exception wording;
- cumulative versus alternative conditions;
- singular/plural and wording that can alter the legal or technical scope of the question.

Automated screening covered **822/822 records**. It identified:
- **229** questions containing at least one wording-risk marker;
- **46** questions containing two or more markers, selected for targeted manual high-risk review.

The 46 high-risk records were reviewed against the stored answer and the learner-facing explanation. The wording was treated as an intentional examination signal where it did not change the meaning or introduce ambiguity. No stored answer required modification.

Additional structural checks found:
- 0 empty options;
- 0 duplicate A/B/C option sets;
- 0 unbalanced parentheses in questions;
- 0 explanations using the wrong „Varianta A/B/C” relative to the stored answer;
- 0 action-required records from the structural gate.

Result:
- **822/822 passed the linguistic/examiner QA gate**;
- **0 answer changes**;
- existing source-verification statuses remain authoritative.

Artifacts:
- `ANRE_Trainer_LINGUISTIC_EXAMINER_QA_V10_23_822.csv`
- `ANRE_Trainer_LINGUISTIC_EXAMINER_QA_V10_23_822.html`
- `ANRE_Trainer_FINAL_STANDALONE_822_V10_23_LINGUISTIC_QA_RC.html`

This phase is a wording/examiner QA gate. It does not replace exact article-level legal verification or independent technical-source verification.


### Phase 39 · V10.24 standalone functional QA · pre-APK gate
The V10.24 standalone was exercised in a controlled Chromium runtime before Android packaging.

Functional paths checked:
- application boot with **822 questions / 414 Grad I / 408 Grad II**;
- Grad I and Grad II learning mode;
- answer selection and learner feedback;
- explanation rendering;
- next/previous navigation;
- final-question behavior;
- final button **„Reia de la început →”**;
- final-question restart back to question 1;
- evidence action and evidence modal open/close;
- quick test mode, starting at 1/10;
- statistics view;
- exam setup view with 20/30/50/100-question choices;
- Grad II A/B filter switching;
- local persistence state creation.

A dedicated last-question runtime test traversed all 414 Grad I questions, reached **„Întrebarea 414 / 414”**, displayed **„Reia de la început →”**, then returned to **„Întrebarea 1 / 414”** after activation.

The evidence modal was also opened and closed successfully. The tested mobile viewport was **390 × 844 px**; the question/answer layout remained usable, with the horizontal top navigation behaving as a scrollable tab strip.

Static release checks:
- 822 records
- 822 unique IDs
- 414 Grad I
- 408 Grad II
- 0 external JavaScript dependencies
- 0 external stylesheet dependencies
- Node JavaScript syntax check passed
- V10.24 standalone SHA-256: `b12d2438f6a4b5d694942bd0f4cf69a4e9f97cdeff5f455bf22d68b668231005`

The previous user-reported last-question ambiguity is therefore resolved in the current standalone: the final learning question has an explicit restart action rather than appearing to lose the navigation path.

**Standalone gate result:** functionally ready for the next APK packaging phase. This is a standalone QA result, not a claim that Android packaging itself has already been revalidated.


### Phase 40 · V10.25 explanation linguistic enrichment · learner comprehension pass
Following the mobile review, the audit candidate-source card was intentionally left unchanged for now. Its A/B/C source variants remain available as audit material until the source audit is finished; they are not treated as learner-facing final UX.

The learner explanation layer was then revised:
- **722/822** explanations that were shorter than 260 characters were expanded into clearer 3-sentence learner-facing explanations.
- The expansion preserves the existing technical/legal rationale and explicitly connects it to the stored correct option.
- **0 stored answers were changed.**
- **822/822** records now expose an explicit `detail.key` derived from the existing `De reținut` content.
- The learner card now presents an **„🔎 Ideea-cheie”** block with visual highlighting, so the retention cue is separated from the explanatory paragraph.
- Explanation typography was slightly increased and line-height improved for mobile readability.
- Source/evidence statuses were preserved.

Static QA:
- 822 records
- 822 unique IDs
- 0 answer changes
- 722 explanations expanded
- 822/822 key learning cues present
- JavaScript syntax valid
- V10.25 standalone SHA-256: `18c85d041b12d4e066476ebdca80d5b0bf6f3cd24ca1cbd0701cf8e64a0bfbea`

A Chromium CLI screenshot attempt was inconclusive because the runtime hung before producing a screenshot, so no visual-browser pass is claimed for this phase. The static/runtime checks remain valid.

Artifacts:
- `ANRE_Trainer_FINAL_STANDALONE_822_V10_25_EXPLANATION_LINGUISTIC.html`
- `ANRE_Trainer_V10_25_EXPLANATION_LINGUISTIC_QA_822.csv`

This phase is deliberately separate from the still-open candidate-source audit and from exact normative/source verification.


### Phase 41 · V10.26 explanation naturalness QA · final short-explanation cleanup
The V10.25 learner-explanation pass was followed by a targeted cleanup of the remaining short explanations.

- **78/822** explanations were still below 260 characters and were expanded.
- The existing rationale and stored answer were preserved; the added text only strengthens the learner-facing bridge between the explanation and the selected option.
- **0 stored answers changed.**
- **822/822** explanations are now at least 260 characters.
- The pass remains a linguistic/pedagogical refinement, not independent source verification.

Static QA:
- 822 records
- 822 unique IDs
- 0 answer changes
- 78 short explanations expanded
- 0 explanations below 260 characters after the pass
- source/evidence statuses preserved
- V10.26 standalone SHA-256: `077c859ba8d0f5b3c0f268b12890addec9e47788edf0f6ae376f447ffdc5cf92`

Artifacts:
- `ANRE_Trainer_FINAL_STANDALONE_822_V10_26_EXPLANATION_NATURALNESS.html`
- `ANRE_Trainer_V10_26_EXPLANATION_NATURALNESS_QA_822.csv`

The candidate-source audit remains intentionally open; its source variants will be cleaned only after the audit is finished.


### Phase 42 · V10.27 candidate-source context prototype · highlighted source concept
The V10.26 correction was clarified: the desired enrichment applies to the **candidate-source question card**, not to the main learner justification.

V10.27 therefore introduces the intended visual pattern:
- keep the candidate question and its audit variants temporarily while the source audit is still open;
- add a separate **„🧠 Context tehnic pentru înțelegere”** section when a defensible local/external context is available;
- present a fuller explanatory paragraph rather than only the candidate-question line;
- visually highlight the exact concept/phrase that connects the context to the candidate question;
- explicitly label external context as conceptual verification material, not as proof of the original ANRE source.

For the current example **G2-ELEC-050**, external technical literature on bundle conductors was used to build the first contextual prototype. The context explains that multiple conductors per phase reduce the surface electric-field gradient and are associated with reduced corona loss. The phrase **„reducerea pierderilor Corona”** is visually highlighted.

The candidate-source A/B/C list remains intentionally untouched because the audit is still open. It will be simplified only after candidate adjudication is complete.

Static QA:
- 822 records retained
- 0 answer changes
- JavaScript syntax valid
- V10.27 standalone SHA-256: `b3d009a2ad64a023b1824531ee31e42437e50d70e2d882ede4977354cea009d3`
- Context prototype currently populated for 1 audited example; remaining candidate contexts will be added only where the evidence supports them.


### Phase 43 · V10.28 candidate-source card separation + context audit registry
The candidate-source card was cleaned so that audit material is no longer mixed with the learner's main answer justification.

Changes:
- removed the main „💡 Justificarea răspunsului” block from the candidate-source modal;
- retained the candidate question, local row/score, A/B/C source variants and research note as audit material;
- added an explicit **„🧠 Context tehnic pentru înțelegere”** area for every candidate card;
- when no defensible context is available yet, the card now states that clearly instead of generating or implying source text;
- retained the G2-ELEC-050 contextual prototype with the highlighted phrase **„reducerea pierderilor Corona”**;
- created a 76-row candidate-context audit registry.

Static QA:
- 76 G2 Electrotehnică candidate records audited for context coverage;
- 1/76 has a supported contextual paragraph at this stage;
- 75/76 remain **PENDING_CONTEXT** and are not auto-filled;
- 0 stored answer changes;
- JavaScript syntax check passed;
- V10.28 standalone SHA-256: `aaad6d47bca77191ed2f0a6f19ffd9d9ab4a6bbdf7aa362e1419698dc2d4ac92`.

This phase intentionally does not promote any candidate match to exact source evidence. The audit remains conservative: unsupported context stays visibly pending.


## 2026-11-08 | V10.29 source-candidate integrity audit (quarantine preview)
- Examined user-supplied V10.28 standalone SHA256 `aaad6d47bca77191ed2f0a6f19ffd9d9ab4a6bbdf7aa362e1419698dc2d4ac92`. This is NOT the older Android HTML asset on `main`.
- Deterministic crosswalk: 76/76 `G2_ELEC_CANDIDATES` items match exactly the question, A/B/C choices and original XLSX row at **another Grade I + Grade II ID pair**, none at their assigned conceptual Grade II target. 48 distinct source rows. Grade II G2-ELEC-001..076 are conceptual/syllabus practice questions, not direct transcriptions from that ANRE spreadsheet.
- Examples: `G2-ELEC-007` series vs candidate parallel; `G2-ELEC-020` apparent vs reactive power units; `G2-ELEC-050` protective earthing vs bundled overhead conductors/Corona; `G2-ELEC-076` ohms vs reactive power despite `HIGH_CANDIDATE` label.
- Full 76 exact cross-ID pair table: [docs/V10_29_CANDIDATE_SOURCE_AUDIT.md](docs/V10_29_CANDIDATE_SOURCE_AUDIT.md). Academy reproducible scanner `scripts/anre_candidate_crosswalk.py`, CI [PASS 42486645828](https://github.com/AcoBenny/Avengers-Asamble/actions/runs/42486645828).
- Separate V10.29 standalone preview quarantines unrelated source-candidate cards. Same 822 questions / answer keys and candidate data. Node JS syntax check PASS. Chromium in-memory HTML audit: 76/76 popups display pending documentation at 390x844 and 1280x800 with no JS exceptions.
- **No new APK build, no Android device QA, no `file://` offline QA and no external independent technical review.** Original source didactic paragraphs still missing. Do not label candidate provenance as authoritative didactic sources.
- Next: ingest authorized manuals, map exact chapters and pages, independently audit, synchronize standalone asset and APK and run E2E.


## 2026-11-08 | Lot 1 manuals inventory and checkpoint CKPT-ANRE-20261108-01
- Received and inspected **14 uploaded PDF files = 4,120 PDF pages** (page counts and hashes via PyMuPDF; no mass OCR). Uploaded user documents remain **outside GitHub**; a metadata-only manifest is now at [docs/CHECKPOINTS/manuals_manifest_2026-11-08.json](docs/CHECKPOINTS/manuals_manifest_2026-11-08.json).
- Verified byte-identical duplicate I7 2011 consolidated 2023 PDFs. Found near-identical teaching course pair `203385014-Curs-Electrotehnica.pdf` (258 pages, scanned) and `466657067-Pregătirea-Tehnică-Pentru-Autorizarea-Electricienilor.pdf` (257 pages, partly searchable). **257/257** aligned rendered pages closely matched in coarse grayscale image comparison; extra last page is nearly blank.
- Three PDFs have no selectable text in tested page samples; OCR not performed. Initial priority: electrical-machines textbook, theory course, 2021 UTCN three-phase course, IEC-based installation manual; regulatory I7-2011 is version-sensitive. Schneider 2024 is primarily product/solution reference; old I7-02 and 1995 installer manual are historical.
- Original 822 question bank and answer keys untouched. V10.29 candidate-source quarantine remains a preview, not Android release.
- **First durable 1MAiN checkpoint** stored at [docs/CHECKPOINTS/LATEST.md](docs/CHECKPOINTS/LATEST.md), with state, risks, evidence, next actions and restart instructions. New checkpoints scheduled by workflow milestones, not asynchronous jobs; direct ChatGPT native Memory update not claimed.
- Legal currency, manual redistribution/embedding rights, real question-to-paragraph mappings and Android end-to-end QA remain unverified. Later user upload pending: historical ANRE questions Grad I / II and optionally III / IV.


## 2026-11-08 | Checkpoint 002 | First 50 didactic-source page candidates and Academy language-review cohort
- Continued from [CKPT-001](docs/CHECKPOINTS/CKPT-ANRE-20261108-01.md), using uploaded PDF manual bytes without redistributing them.
- Built [41 priority chapter/PDF-page locators](docs/DIDACTIC_CHAPTER_INDEX_PRIORITY_2026-11-08.md), drawn from four high-priority didactic/normative PDFs; anchors confirmed in actual extracted text. This is indexing, not proof of legal currency or of every technical answer.
- Drafted [G2-ELEC-001..050 page-level didactic map](docs/DIDACTIC_SOURCE_MAP_BATCH001_G2_ELEC_001_050.md): 50/50 source-page candidates, 14 direct model page-principle spotchecks, 36 unverified topic candidates. 17 cases flagged for exact-evidence follow-up. Independent source QA NOT_RUN.
- Visually checked UTCN 2021 three-phase slide pages 66, 67 and 88 for the correct √3 relationships where the PDF text extraction loses symbols.
- Verified all 76 conceptual Grade II introductory questions currently have `Raspuns=A`; while question order shuffles, displayed A/B/C options are fixed. Created [issue #2](https://github.com/AcoBenny/ANRE_Trainer/issues/2). No original key change and no implemented answer shuffling yet.
- Extracted 3 existing linguistic markers in Batch001 (G2-ELEC-029 comparison, 030 negation/exclusivity, 035 condition); AGENT-031 curriculum exercise assigned in Avengers Academy, no independent model run.
- **Canonical resume checkpoint:** [LATEST](docs/CHECKPOINTS/LATEST.md) → [CKPT-002](docs/CHECKPOINTS/CKPT-ANRE-20261108-02.md). All 822 question IDs, candidate-source quarantine and standalone/APK separation preserved. No new release or paid API usage.
- Open: 17 priority semantic page/answer checks, 36 page candidates, source-embedding rights, 2026 legal currentness, Android offline E2E, Lot 2 historical question uploads.


## 2026-11-08 | Historical question Lot2 received and screened (interim, no checkpoint #3)
- User requested fewer 1MAiN checkpoints. The Academy [checkpoint policy](https://github.com/AcoBenny/Avengers-Asamble/blob/main/docs/CHECKPOINT_POLICY.md) now targets 2–3 substantial verified batches or a release/handoff, not after every import. [LATEST](docs/CHECKPOINTS/LATEST.md) still points to **CKPT-002**.
- Received **18 historical/practice question PDF files, 1,345 PDF pages**. Verified file hashes and per-file metadata; originals remain in user uploads, not in GitHub. [SHA256 catalog](docs/QUESTION_BANKS/HISTORICAL_LOT2_MANIFEST_2026-11-08.json).
- Ran normalized question-stem searches against all 1,345 pages and the 822-question standalone V10.29 corpus: **390 existing question IDs / 228 distinct question stems** matched as text in one or more PDF documents. This is NOT full three-choice duplication or an answer-key match.
- **432** app IDs had no exact text match; do not infer they are novel/missing. 0/62 `G2-LEG` matched exactly; examine Grade II legislation gap with care.
- Cross-PDF page similarity found 160/160 Grad II cumulative legislation pages closely matching Grad I/II cumulative pages at cosine >= 0.90; no exact SHA256 PDF duplicates.
- Option comparison sample (first <=4 pages each PDF): **109 overlapping question rows**; 69 with identical A/B/C text/order, 8 near, 32 variants/annotations/extraction differences. This does NOT establish 32 wrong correct-answer keys.
- One Grade II PDF has corrupt text encoding; requires selective visual inspection.
- [Detailed interim intake QA](docs/IMPORT_AUDIT_LOT2_2026_11_08.md) and [issue #3](https://github.com/AcoBenny/ANRE_Trainer/issues/3) record the next technical/language/legislative audits.
- Original 822 ID/answer data unchanged. No old legal answer key promoted; no new APK/HTML build, no paid API calls, no independent agent certification. **CKPT-003 intentionally not created.**


## 2026-11-08 | Audit-only gate and didactic source Batch002
- Owner explicitly froze all application/HTML/APK/answer-key implementation until the COMPLETE didactic document mapping and audit have finished. Recorded [AUDIT_FIRST_RELEASE_GATE](docs/AUDIT_FIRST_RELEASE_GATE_2026-11-08.md). Audit scripts and metadata reports only; no release or UI changes authorized.
- Reviewed 17 high-risk didactic page candidates from first 50: **8 direct source-page supports, 6 require derivation/conditions, 3 have only thematic pages/insufficient exact evidence**. All **NOT independently approved**.
- Continued with **50 additional existing Grade II electrotechnics IDs**: G2-ELEC-051..076 plus G2-ELEC-154..177 (actual ID gap 077..153, not invented entries). Model-assisted source reviews: 26 direct page supports, 10 conditional/derived, 9 topic-only, 4 no exact local source, 1 missing essential diagram.
- Current audit-only coverage: **100/822 question IDs examined for didactic page mapping**, **95/822 have PDF page candidates**, 5/822 unresolved source/figure; remaining 722 not yet started. **0 independent final source approvals**, no manuals embedded offline.
- Important blocker `G2-ELEC-177`: question says 'schema de mai sus', but V10.29 embedded `DATA` contains no attached drawing. Logged [issue #5](https://github.com/AcoBenny/ANRE_Trainer/issues/5) together with 161,166,170,172 absent precise didactic sources.
- [Batch002 audit table](docs/DIDACTIC_AUDIT_BATCH002_NO_IMPLEMENTATION_2026-11-08.md) includes exact physical PDF page/technical-status for all 17 rechecks and 50 new records. PDF originals remain user uploads, not GitHub.
- The CSV tracker for all 822 (unmapped IDs explicitly identified) and audit JSON were exported into the conversation as a download archive. User's approved checkpoint cadence remains low: **CKPT-002 unchanged**, interim batch records only, no CKPT-003.
- Independent engineering/language/rights QA and current normative versions remain pending. No paid API calls; **0 RON**.


## 2026-11-08 | Audit-only Batch003: 50 next G2 questions and original schematic recovered
- Continued owner-approved audit-only process, **no HTML/APK/data implementation**. Source baseline V10.29 SHA256 `50c44b2798c2324121647ee5f24592fc2c1e049e827edb734c61dcf65d7f4b9c`.
- **G2-ELEC-177 original schematic recovered** in user-uploaded `979902894-Captura-de-ecran-din-2024-11-09-la-14-15-06.pdf`, p.10, historical question 28, matched choices and marked B. Local textbook `337393907-Cartea-Electricianului-Din-Statii-Si-PT-uri12.pdf` PDF p.373 explains current limitation through reactor impedance. This historical PDF is not official ANRE provenance and the figure is still not in DATA; issue #5 updated, no implementation.
- `G2-ELEC-170`: conditional `Cs=3C` derived from PREG p.89 + UTCN pp.66/68. `G2-ELEC-166`: credible university context for `div B=0` found, NOT local/rights cleared. `G2-ELEC-172`: IEC/Siemens isolated-phase GIS context found, not local and wording `totală` is scope-sensitive. `G2-ELEC-161`: source PREG pp.42,184 gives counterexamples to unqualified resistor exclusion; requires network-specific technical review.
- **50 additional actual questions** `G2-ELEC-178..227` examined: A=17 source-principle model checks, B=11 derivation/conditional, C=13 related topic only, U=9 no adequate local paragraph. `G2-ELEC-012` upgraded from topical page 86 to exact `f=1/T` PREG page 132.
- Consolidated tracker: 150/822 entered into page mapping, 138/822 with candidate pages or derived local source, 12/822 still missing local adequate evidence, 672 not started. **0 independent final approvals**; no source rights cleared, no changes to 822 answer keys.
- [Full Batch003 source evidence, table and review flags](docs/DIDACTIC_AUDIT_BATCH003_NO_IMPLEMENTATION_2026-11-08.md). Per-question machine-readable CSV/JSON and complete 822 tracker generated as conversation downloads. No books or full scans uploaded to GitHub.
- Additional AGENT-031 linguistic trap cases assigned to the Academy; no autonomous agent evaluated or graduated, no paid API calls. **CKPT-002 remains latest checkpoint; CKPT-003 intentionally not created.**


## 2026-11-08 | Full didactic corpus structural navigation (11 canonical sources)
- Per owner's instruction, **didactic manuals were structurally indexed before continuing question/answer review**. No HTML/APK/DB/answer-key changes.
- Inventoried **14 PDFs = 4,120 raw pages**. Confirmed 3 redundancies: I7-2023 exact byte duplicate; 258-page scan near-duplicate of 257-page PREG with nearly blank tail; 149-page photographed double-page scan corresponds to a large excerpt of the 332-page 1995 manual. Third relationship visually checked across 11 spread samples; full crosswalk inferred and flagged as not individually approved.
- Final working source count: **11 canonical works, 3,464 distinct PDF pages**, with **3,050 selectable-text pages** and **414 non-text pages** (332 scanned 1995 source, 82 mixed/blank/graphic pages).
- Navigation index comprises **2,010 chapter/section locators** (880 bookmarks/TOC/visual TOC anchors; 1,130 AUTO headings), a **3,464-row physical PDF page navigator**, **289 source-concept locators over 45 technical topic codes**, a 45x11 coverage matrix, and **656 duplicate-page alias links**. `AUTO` and `TOPIC` are discovery aids, NOT independent verified source paragraphs.
- Evidence is persisted under [docs/DIDACTIC_CORPUS_INDEX](docs/DIDACTIC_CORPUS_INDEX/) including [report](docs/DIDACTIC_CORPUS_INDEX/ANRE_MANUALE_RAPORT_MAPARE_STRUCTURALA_2026-11-08.md), 2,010-row section CSV, full 3,464-page navigation CSV, 289 source-topic locator CSV, and duplicate-page crosswalk CSV. Full reproducible ZIP (including index JSON.gz and scripts) delivered as a generated conversation attachment, **no copyrighted PDFs committed**.
- Remaining before question audit: independently review section locators/technical paragraph validity, visual/no-OCR scans, current 2026 normative wording, coverage gaps (GIS, Poynting, special LEA, RL/RC and other exact teaching topics), and rights to redistribute book excerpts offline.
- **Do not claim all didactic sources semantically certified or all 822 questions mapped.** Previous exploratory mapping of 150 questions stays PRELIMINARY pending new source catalog QA. Independent manual-content QA NOT_RUN. CKPT-002 still current; **no new checkpoint**. Owner's audit-first implementation freeze remains unchanged; additional API spend **0 RON**.


## 2026-11-08 | Didactic OCR 1995 indexed: 3374 searchable pages and graphic-only triage
- Owner's audit-first rule remains active: **no changes** to standalone HTML, Android APK, question bank or answer keys.
- Verified the user-provided 332-page Tesseract Romanian+English OCR PDF, source original SHA256 `b85057732a71d96d4d217a42f5e2c1e9996f24e0011c5de374e7c878341b110a`, OCR SHA256 `1ceac1f2eec5469afdbb561f74060b985146987d9b062f3eb93d98788723702a`. **324** pages now searchable, 8 without useful text. Twelve raster samples were pixel-identical to original. OCR equation on p99 is garbled; formulas still require inspection of the scanned page.
- Added [OCR-enhanced page navigation](docs/DIDACTIC_CORPUS_INDEX/MANUAL_ALL_PRIMARY_PAGES_NAVIGATION_OCR_V2.csv): **3,374 of 3,464 canonical pages** now searchable (**97.4%**), up from 3,050 (88.0%). Source library remains 11 canonical books from 14 uploads; no copyrighted text/PDF bytes were committed.
- Scanned 45 thematic topic codes in the 1995 OCR manual: **35/45** have keyword hits in the theoretical section (PDF pages 35–146), **41/45** anywhere in the book. Historical legal/exam-question pages are labelled `NON_DIDACTIC` to avoid treating old questions as verified instructional paragraphs. All keyword hits = discovery, NOT independent proposition QA.
- Local user-only private FTS5 SQLite search file for the 1995 OCR manual generated. GitHub contains **metadata-only** [OCR 332-page index](docs/DIDACTIC_CORPUS_INDEX/AUT_1995_OCR_PAGE_NAVIGATION_2026_11_08.csv), [45-concept classified locators](docs/DIDACTIC_CORPUS_INDEX/AUT_1995_OCR_45_CONCEPT_COVERAGE.csv), [11-source coverage matrix V2](docs/DIDACTIC_CORPUS_INDEX/MANUAL_45_CONCEPT_COVERAGE_MATRIX_OCR_V2.csv) and [OCR QA report](docs/DIDACTIC_CORPUS_INDEX/ANRE_DIDACTIC_MANUAL_OCR_V2_AUDIT_REPORT.md).
- [Remaining 90 image-only pages](docs/DIDACTIC_CORPUS_INDEX/NON_TEXT_PAGES_VISUAL_TRIAGE_90_2026_11_08.csv) were triaged with density heuristics; **15** cross-source sample pages examined visually. All **20** graphic-only pages from the stations/transformer-posts manual were viewed on a contact sheet and [classified generally](docs/DIDACTIC_CORPUS_INDEX/STATII_GRAPHIC_ONLY_20_VISUAL_INDEX.csv) as drawings/diagrams/tables or cover, not independently technically verified. Other 70 have not all been inspected visually.
- No new CKPT-003. Latest canonical checkpoint remains CKPT-002. No autonomous model benchmark, technical QA certification, rights clearance or API spending. **0 RON extra**.
- Next: visually confirm formula/diagram source passages and assess 45-concept coverage gaps; separate obsolete legal norms from technical theory; then full-source semantic review before reopening question mapping.


## 2026-11-08 | Semantic source QA Batch A: 42 evidence checks across 11 manuals
- Continued owner-approved **didactic-manuals-first** audit. The 822 question records, stored A/B/C and keys, HTML and APK were not edited.
- Checked **42 actual source-page principles/topics from all 11 canonical works** with 42/42 extracted text anchors; 9 visual observations on 8 original PDF pages (PREG 52,63,90,132; UTCN 66,67,88; AUT_1995 99), including 6 formula-related visual confirmations. This is model-assisted evidence inspection; **independent reviewer still NOT_RUN**.
- Confirmed **source terminology error** in PREG physical p52: Joule-Lenz expression `Q=I²Rt` labels `R` resistivity with unit `Ω`, whereas R is resistance (Ω) and ρ resistivity (Ω·m). Source formula itself still valid with R=resistance.
- PREG p63 Faraday-Lenz positive `e=ΔΦ/Δt` lacks explicit orientation/magnitude/Lenz sign convention, requiring qualification, not uncritical teaching. AUT_1995 p99 transformation ratio equation is intact in original raster but corrupted in OCR.
- UTCN p66,67,88 formulas `√3` verified in original slides, with balanced/symmetric context; PREG p63/90/132 energy, power factor and `f=1/T` verified visually.
- Quality review of 45 automated topic labels found `produs_referinte_coduri` is **not a curricular concept**, leaving 44 curricular labels, themselves insufficiently granular for GIS, LEA Corona/capacitance, RC/RL transients, Poynting and similar. **13 priority coverage/authority flags**. All 45 keywords-hit labels are NOT equivalent to verified ANRE curriculum coverage.
- Official verification entry points: ANRE thematic bibliography and examination example page; Portal Legislativ I7-2011 with Order 959/2023 and transitional clauses. Current 2026 applicability per paragraph and book excerpt/offline embedding permissions still NOT_VERIFIED.
- Artifacts persisted: [source semantic QA report](docs/DIDACTIC_CORPUS_INDEX/SOURCE_SEMANTIC_AUDIT_FIRST_PASS_2026-11-08.md), [42-row evidence CSV](docs/DIDACTIC_CORPUS_INDEX/SOURCE_SEMANTIC_QA_FIRST_PASS_42.csv), [45-topic QA matrix](docs/DIDACTIC_CORPUS_INDEX/MANUAL_45_TOPIC_COVERAGE_QA_FIRST_PASS.csv); [issue #6](https://github.com/AcoBenny/ANRE_Trainer/issues/6) updated.
- Final independent source approvals **0**; no full technical source certification or change to 150 preliminary question mappings. CKPT-002 remains latest, no new checkpoint. Incremental spend 0 RON.


## 2026-11-08 | Source validation registry V1 (44 categories, 42 evidence observations)
- User approved the recommendation to create a **concept-level register with measurable progress** before any question-specific answer audit. No application implementation.
- Original 45 topic labels → **44 provisional curricular parent categories**, plus one excluded product code metadata label.
- Distinct measures: **25/44** categories have at least one model-assisted preliminary page observation (**56.8% exploratory coverage only**); **0/44** independent final technical approvals (**0% formal validation**). No claim of complete semantic library mapping.
- Among the 44: 19 preliminary-sampled, 8 priority reviews, 5 missing/risks in source quality/authority/legal currency, 12 only keyword-indexed. Total **13 priority categories**, with 19 proposed atomic follow-up subtopics that are NOT included in the 44 denominator yet.
- Linked all previous 42 source QA observations: 41 administratively linked to a parent category; one generic energy conversion note explicitly unassigned. No key/answer change and no newly executed independent agent.
- Durable metadata: [validation report](docs/DIDACTIC_CORPUS_INDEX/VALIDATION_PROGRESS_REPORT_2026-11-08.md), [45-label/44-curricular register](docs/DIDACTIC_CORPUS_INDEX/VALIDATION_REGISTRY_44_2026-11-08.csv), [42 linked observations](docs/DIDACTIC_CORPUS_INDEX/VALIDATION_QA_EVIDENCE_LINKED_42_2026-11-08.csv), [19 gap subtopics](docs/DIDACTIC_CORPUS_INDEX/VALIDATION_GAPS_SUBTOPICS_19_2026-11-08.csv). A formula-driven Excel dashboard + ZIP are user downloads, not binary GitHub commits.
- **CKPT-002 unchanged**, no new release/HTML/APK, no new paid API spend. Next: QA the 13 high-priority areas, audit explicit original paragraph/formula evidence and source rights, and then expand taxonomy denominator when subtopics are independently accepted.

## 2026-11-08 | P1 source coverage QA V2 for 13 parent categories and 19 subtopics
- Owner-approved manual-first audit continued. All **13 high-priority categories were examined**, with **19 traceable subtopics**; 9 have at least partial local page evidence and 4 official external reference entry points, while 6 lack adequate local explanatory paragraph after this targeted search. **All remain unapproved independently** (0/44 formal QA).
- Original PDF page/figure verified visually for PREG p32 (Gauss electric flux), PREG p120 (Corona sharp edges), MAS p104 (asynchronous braking), MAS p202 (excitation RL Te=Le/Re). Text-based checks also for I7 pp115–121 (bath/pools/sauna), MAS p94/106 and STATII p428. No claim every source paragraph or figure is certified.
- Regulatory spotcheck: ANRE authorization Order 66/2023 amended by Order 65/2024; connection Order 59/2013 lists consolidated form 25 May 2026 on official portal; EV installation scope covered by IEC 60364-7-722:2018 (paywalled standard, not redistributed); SSM HG1425/2006 is distinct from internal instruction. Currentness per article remains unresolved.
- Metadata saved in [P1 report](docs/DIDACTIC_CORPUS_INDEX/P1_PRIORITY_TECHNICAL_AUDIT_V2_2026_11_08.md), [13 categories](docs/DIDACTIC_CORPUS_INDEX/P1_13_CATEGORIES_REVIEW_V2_2026_11_08.csv) and [19 detailed subtopics](docs/DIDACTIC_CORPUS_INDEX/P1_19_SUBTOPIC_EVIDENCE_V2_2026_11_08.csv). User received V2 XLSX and ZIP with original registry sheets retained. Original books not redistributed via GitHub.
- No code or answer key edits, no new checkpoint (CKPT-002 still current), no paid API costs. Independent specialists NOT_RUN. Next: fill targeted theory gaps and technical source review, not question validation yet.

## 2026-11-08 | Visual QA policy adopted, no app change
Academy AGENT-014 UI visual release gate added as documentation only. Question mapping and didactic source audits remain priorities. No HTML/APK runtime or offline documentation test executed by this change. See docs/VISUAL_QA_GATE.md.


## 2026-11-08 | V3 source recovery: 6 didactic external references, no approvals
- The six previously uncovered **local** teaching subtopics in the 19-subtopic P1 register now have **verified public educational reference entry points**: OpenStax Maxwell magnetic flux §16.1 (`div B=0`), MIT OCW §2.7.1 & OpenStax §16.3 (`S=E×H` / `S=E×B/μ0` in vacuum), OpenStax §10.5 (`τ=RC`), DOE PV, DOE wind, and NPTEL §1.10 conductor bundling.
- **4/6** external references address the exact foundational principle; **2/6** cover only PV/wind fundamentals while grid integration/protections remain **BLOCKED**. All **6** remain external candidate sources, NOT local uploaded manual paragraphs, and **0** have independent engineering QA approval or confirmed rights to embed into a new Android/HTML release. Parent-category final validations remain **0/44**.
- Source rights: OpenStax & MIT OCW terms CC BY-NC-SA with required attribution/noncommercial/sharealike. NPTEL/Utah content redistribution not established. PDF public screenshots for MIT and Utah returned cache misses; their textual claims not misrepresented as visual verification. DOE third-party reuse not assumed.
- Metadata in [V3 six-source registry](docs/DIDACTIC_CORPUS_INDEX/V3_6_EXTERNAL_DIDACTIC_SOURCES_2026_11_08.csv), [19-subtopic carryforward](docs/DIDACTIC_CORPUS_INDEX/V3_19_SUBTOPIC_EVIDENCE_2026_11_08.csv), [external gap report](docs/DIDACTIC_CORPUS_INDEX/V3_EXTERNAL_SOURCE_GAPS_REPORT_2026_11_08.md), [original didactic note drafts](docs/DIDACTIC_CORPUS_INDEX/V3_ORIGINAL_DIDACTIC_NOTES_DRAFT_2026_11_08.md); [issue #6](https://github.com/AcoBenny/ANRE_Trainer/issues/6) updated.
- The user received a **V3 Excel tracking workbook** preserving V2 with 3 added sheets, and a user-download ZIP with no copyrighted PDFs. No stored 822 question IDs, keys, standalone HTML or Android APK modified. **CKPT-002 still latest**, no new checkpoint; incremental spend **0 RON**.

## 2026-11-08 | Manual-first source audit V4: PV/eolian grid, protection, offline rights
- Owner-approved manual-source-only follow-up to V3 external theory. **No app HTML/APK/source assets/822 question keys changed.**
- Created [V4 source report](docs/DIDACTIC_CORPUS_INDEX/V4_PV_WIND_RIGHTS_AUDIT_REPORT_2026-11-08.md), [14-row PV/wind source crosswalk](docs/DIDACTIC_CORPUS_INDEX/V4_PV_WIND_GRID_PROTECTION_SOURCES.csv), [10-row offline source rights matrix](docs/DIDACTIC_CORPUS_INDEX/V4_OFFLINE_RIGHTS_REVIEW.csv) and [7 remaining gaps](docs/DIDACTIC_CORPUS_INDEX/V4_PV_WIND_UNRESOLVED_GATES.csv).
- Confirmed ANRE 228/2018 amended 132/2020 art 14 and 18 for prosumer islanding/interconnection/protection, ANRE Ordin 19/2022 procedure and 2026 ANRE public guidance, Ordin 208/2018 generating modules with category-sensitive requirements. No universal numerical settings approved.
- IEC 60364-7-712:2025 **replaces** IEC 2017 at IEC international publication level; adopted Romanian SR edition/current legal applicability NOT_VERIFIED. IEC 62116:2014 and 61400-21-1:2019 have public publisher abstracts only, full standards paywalled.
- Rights triage: uploaded manuals, PDF OCR and commercial norms not redistributable by assumption; OpenStax University Physics 2 CC BY-NC-SA 4.0 with AI-use notice; MIT OCW CC BY-NC-SA; DOE US federal-origin material typically public-domain except third-party assets. Source text not copied into application or public GitHub.
- Delivered user V4 formula-driven Excel and CSV/MD audit bundle. **QA independent approval 0/44; no independent model agent runtime; no checkpoint 003**. CKPT-002 unchanged; 0 incremental RON spend.


## 2026-11-08 | V5 PV/I7 7.11 diagram evidence and wind A-D normative audit
- User resumed **manual-first audit**, focusing on 7 open V4 gates. Did not change HTML, APK, 822 question records or keys.
- Local PDF `803493174-I7-2011-completat2023.pdf` had overlooked source anchors: §7.11.1–25 PDF pp136–137, original schemes figs7.11.1 p137 /7.11.2 pp137–138 inspected visually. Particular technical nuance: DC remains potentially energized after AC disconnect; conditional DDR type B; DC cable overload vs short circuit; service separations; warning labels. Snapshot date 2023-09-22, not approved as 2026 up-to-date edition.
- Official references checked: ANRE 132/2020 (art14 amended for prosumer interface/protection, external relays for >30kVA or MV), MDLPA 959/2023 (I7 scope PV and transitional cases), ANRE 79/2016 (categories A-D by U/P), ANRE 208/2018 (arts16/34 anti-islanding and arts35/56 frequency), ANRE 80/2025 (art136 category-linked trial periods).
- Produced **20 preliminary source observations: 10 local exact/visual, 9 official clause/table, 1 NREL technology-only text-index**. Web PDF screenshot unavailable; do not assert NREL diagrams were visually checked or North American grid limits apply in Romania. **7/7 previous gaps still open, though several are now supported by more precise sources.**
- [V5 report](docs/DIDACTIC_CORPUS_INDEX/V5_PV_WIND_MANUAL_NORMATIVE_AUDIT_2026-11-08.md), [20 observations](docs/DIDACTIC_CORPUS_INDEX/V5_SOURCE_PARAGRAPH_EVIDENCE.csv), [7 gate update](docs/DIDACTIC_CORPUS_INDEX/V5_7_OPEN_GATES_UPDATED.csv), issue #6 updated. User spreadsheet V5 with historical sheets preserved and full 5-file private ZIP created. No PDFs from user or third party uploaded.
- **Independent approvals 0/44; no new checkpoint, CKPT-002 remains authoritative; no paid API.** Next audit: precise SR/EN editions and licensed PV current reference, verify technical diagram options with qualified electrical reviewer and classification-specific wind compliance before question-bank work.


## 2026-11-08 | V6 national SR/EN edition and protection gate review
- Owner resumed source-first audit: **10** edition/standard records, **14** source-specific technical/protection observations, **7** open V5 blocker cases updated. 0 of 7 blocks closed; 0/44 independently approved.
- New edition detail: ASRO SR HD 60364-7-712:2016 catalogue still lists in force, while IEC 60364-7-712:2025 is separate; ASRO 2023 Bulletin documents SR EN 50549-1+AC:2019/A1:2023 and SR EN 50549-2:2019/A1:2023; ASRO SR HD 60364-5-53:2022 with AC:2025.
- QA caveat: ASRO Bulletin PDF text extraction available but web screenshot returned 403; no visual verification of that specific PDF. Commercial-standard clause texts were NOT copied or guessed.
- Reviewed local I7 snapshot §7.11 p136–137 conditionals; confirmed in Portal Legislativ ANRE art14(2-4) class/power gating and conditional self-consumption during islanding; art18(3),(8) ORR-owned selectivity and project documentation. No engineering settings or implementation edits.
- Metadata in [report](docs/DIDACTIC_CORPUS_INDEX/V6_EDITION_PROTECTION_AUDIT_REPORT_2026-11-08.md), [editions](docs/DIDACTIC_CORPUS_INDEX/V6_SR_EN_EDITION_REGISTER_2026-11-08.csv), [protection locator records](docs/DIDACTIC_CORPUS_INDEX/V6_PV_PROTECTION_CLAUSE_EVIDENCE_2026-11-08.csv) and [7 open gates](docs/DIDACTIC_CORPUS_INDEX/V6_7_GATES_REVIEW_2026-11-08.csv). User V6 Excel and ZIP include SHA-256 manifest, only self-authored metadata.
- No application HTML/APK/822 original keys altered. CKPT-002 remains current, no new checkpoint, no independent reviewer executed; cost 0 RON.


## 2026-11-08 | V7 scoped pre-question didactic source gate (44 labels, G1/G2 syllabus)
- User delegated source-audit preflight in the existing chat, without confirmations per batch, preserving no HTML/APK and no answer-key changes.
- Screened **44/44** internal curricular topics, found **43/44** with relevant local PDF source page text (EV charging local didactic paragraph absent; national ASRO SR HD 60364-7-722:2019 publisher scope located). Each is an initial selected-page observation, **not** complete subject proof. **0/44** approvals by a distinct reviewer.
- Compared against official 05.2023 ANRE bibliography, physically viewed page images 1–3. **29** numbered rows; **10** applicable Grade I and **13** Grade II. 2026 versions of each regulation need currentness at article, and specialized III/IV-only titles cannot block I/II globally.
- Inspected new original-page visual math/rules (PREG pp30,45,89, MAS p128, I7 pp25,161, UTCN p66) alongside prior formula flags; **20** claims/errors/QA gates recorded. Existing seven V6 open gates preserved with *scope-specific* downstream impacts.
- Artifacts: [V7 report](docs/DIDACTIC_CORPUS_INDEX/V7_PRE_QUESTION_DIDACTIC_AUDIT_REPORT_2026-11-08.md), [44 category ledger](docs/DIDACTIC_CORPUS_INDEX/V7_44_TOPIC_SEMANTIC_SCREENING.csv), [29 official bibliography entries](docs/DIDACTIC_CORPUS_INDEX/V7_OFFICIAL_ANRE_G1_G2_2023_BIBLIOGRAPHY.csv), [20 risks](docs/DIDACTIC_CORPUS_INDEX/V7_FORMULA_SOURCE_AND_GATE_QA_20.csv), [7 blockers](docs/DIDACTIC_CORPUS_INDEX/V7_7_BLOCKERS_SCOPE_AND_HANDOFF.csv), [protocol](docs/DIDACTIC_CORPUS_INDEX/V7_QUESTION_AUDIT_ENTRY_RULES.md); issue #6 updated. User V7 XLSX preserved V1–V6 sheets; 9-file ZIP passed integrity and SHA256 checks.
- **No independent agents or technical reviewer runtime**; no project/app/822 changes, no paid API. **CKPT-002 still latest.** Read-only question triage may be offered for owner approval; **do not silently start answer correction or claim formal final approval.**


## 2026-11-09 | V8 question audit begins on development branch
- User explicitly authorized transition from V7 source-preparation to **read-only, source-grounded audit of 822 questions**, with no interim user loop. No question or key auto-changes approved.
- Used V10.29 SHA-256 `50c44b2798c2324121647ee5f24592fc2c1e049e827edb734c61dcf65d7f4b9c`: 822 unique question IDs (414 Grade I, 408 Grade II). Existing `Status=VERIFICAT` in app does NOT mean independent QA now.
- Initial **17/17 high-risk G2-ELEC cases inspected** against actual original Q/A/B/C and targeted manual text: 4 exact preliminary principles, 12 technically consistent with specific conditions, one `G2-ELEC-036` requiring a better definitional source; **0 barem changes, independent reviewer NOT_RUN**. Visual-source checks include PREG PDF pp36,86,132,133,136,251; MAS p30; I7 pp23,25.
- Independently reran exact text+option+file+row matcher: **76/76** conceptual candidates point to **two other existing IDs**, 0 target IDs; 48 XLSX rows involved. These are *provenance mismatches*, not proof of wrong answers. Keep quarantine issue #1, A/B/C positional bias issue #2.
- Discovered actual ID gap `G2-ELEC-077..153` in V10.29, despite 822 distinct records. The previous suggested `051..100` next batch was numerically wrong: next 50 existing IDs are `G2-ELEC-051..076` plus `G2-ELEC-154..177`. Do not infer 77 missing questions or mint IDs.
- New read-only audit metadata in `docs/QUESTION_AUDIT/V8_*`, plus 822 backlog. **Only on development branch**, pending draft Pull Request, no main merge, release, APK/HTML code modification or external standards/book redistribution. CKPT-002 remains the official project checkpoint.


## 2026-11-09 | V9 next 50 G2 question source audit (read-only)
- Using immutable V10.29 standalone HTML SHA-256 `50c44b2798c2324121647ee5f24592fc2c1e049e827edb734c61dcf65d7f4b9c`, matched **all 50 exact question statements, options A/B/C, key and source rows** to original object data. True IDs `G2-ELEC-051..076` (26 trainer-authored conceptual) + `G2-ELEC-154..177` (24 XLSX questions). All changes are **docs-only on dev branch**, no barem/HTML/APK changes.
- 50 model-assisted preliminary dispositions: **DIRECT 24; CONDITIONAL 13; DERIVATION 5; GAPPED 5; AMBIGUOUS 2; MISSING_FIGURE 1**. These are not independent technical QA results. 7 prioritised issues for independent review (`063,158,166,170,172,175,177`); source documentation missing/too generic for `051,052,063,162,167`.
- **Defect confirmed:** question `G2-ELEC-177` refers to “schema de mai sus” yet V10.29 has no figure field or embedded image; exact historical diagram was visually observed in user supplied `979902894-...pdf` physical PDF p10. Do not inject copyrighted diagram without permission and real visual UI QA.
- **Terminology conflict:** `G2-ELEC-166` app says “câmp de inducţie electromagnetică”; historic evidence sheet p9 says “câmp de inducţie magnetică”. No key change pending specialist semantic review. **Joule source erratum:** PREG p52 prints `Q=I²Rt` but wrongly labels `R` in Ω as “rezistivitate” rather than resistance.
- Other checks: `G2-ELEC-176` computed 400 Wh from 10 Ω, 2 A, 10 h; `170` balanced 3-phase line model gives Cs=3C by derivation but exact normative terminology remains to verify; `158` L−N+1 requires connected graph; `172` “total elimination” overgeneralizes when not restricted to internals; `175` 2025 paper was available in text extraction but PDF screenshot cache miss, so visual support NOT_VERIFIED.
- Updated [V9 50 audit CSV](docs/QUESTION_AUDIT/V9_G2_ELEC_50_SEMANTIC_SOURCE_AUDIT.csv), [7 review gates](docs/QUESTION_AUDIT/V9_G2_ELEC_PRIORITY_7_QA_GATES.csv), [822 backlog](docs/QUESTION_AUDIT/V9_ALL_822_AUDIT_BACKLOG.csv) and [technical report](docs/QUESTION_AUDIT/V9_G2_ELEC_NEXT50_SEMANTIC_AUDIT_REPORT.md). Backlog now **17 V8 + 50 V9 = 67/822 preliminarily examined; 755 not yet audited.** No independent reviewer; no approved key edits.
- Next 50 actual IDs **`G2-ELEC-178..227`** exist in V10.29. No new checkpoint; CKPT-002 remains latest. PR #7 is draft and must not be merged without user approval.


### 2026-11-09 | V10 preliminary screening, G2-ELEC-178–227 (PR #7 Draft)
- 50/50 existing identifiers compared against V9 source/key backlog; provisional subject-matter screening used historical V10.4 HTML question text. Canonical V10.29 HTML/text parity **NOT_VERIFIED** because repository asset was not fully readable through connector; source pages **NOT_VERIFIED**; independent QA **NOT_RUN**.
- Classes: 5 AMBIGUITY; 2 SOURCE_GAP; 11 CONDITIONAL; 20 FORMULA_CHECK; 12 PRINCIPLE. Priority cases 189, 218, 203, 178, 193–195, 197; arithmetic 188=44 A. No keys changed.
- Evidence: `docs/QUESTION_AUDIT/V10_G2_ELEC_178_227_PROVISIONAL_SCREEN.csv` and `docs/QUESTION_AUDIT/V10_G2_ELEC_178_227_AUDIT_REPORT.md`; PR #7 body updated. 67 prior prelim + 50 older-snapshot screenings = 117 with differing evidence maturity, 705 not screened, 0 independent approvals.
- Safety: no HTML, APK, barem or other app assets changed; no merge/release. Next gate compare V10.29 exact texts/options, verify didactic paragraphs and run independent QA before treating these as validated.


### 2026-11-09 | Canonical reconcile V10, V11/V12 batches, 822 QA ledger (PR #7 Draft)
- Read full GitHub V10.29 HTML blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`, parsed 822 records; compared with user Library historical V10.4: all 50 IDs `G2-ELEC-178..227` identical across 9 canonical fields `Intrebare/A/B/C/Raspuns/Rand_sursa/Sursa/Categorie/Versiune`. 50/50 match V9 tracker for key, source row and name.
- Model-assisted preliminary screens V11 `228..277` and V12 `278..327`: 100 more canonical questions, both 50-row evidence CSVs and detailed technical/linguistic risk notes. Exact didactic pages 0 verified for these batches; independent SME QA 0; HTML/APK runtime QA NOT_RUN.
- Full 822-record canonical-vs-backlog QA identified **6 actual key metadata conflicts** in the V9 tracker: G1-LEG-024 (A vs C), 028 (B vs C), 032 (B vs A), 034 (B vs A), 048 (A vs B), G2-ELEC-170 (C vs A). Same source labels/rows for all six. Canonical and tracker values both retained explicitly. A previous V9 derivation of G2-ELEC-170 suggests A under a particular model, while canonical says C: unresolved until exact didactic definition and independent adjudication. G1-LEG-048 canonical A also warrants high-priority legal checking.
- Phase ledger totals V8=17, V9=50, V10=50, V11=50, V12=50 (217/822 with preliminary model screens); remaining 605 NOT_SCREENED; **0 independently approved**. V13 labels are QA data-audit metadata, not 50 more question screens.
- Evidence: `V10_G2_ELEC_178_227_CANONICAL_RECONCILIATION.csv`, `V10_G2_ELEC_CANONICAL_RECONCILIATION_REPORT.md`, V11/V12 `SCREEN.csv` and `REPORT.md`, `V13_ALL_822_CANONICAL_QA_LEDGER.csv`, `V13_SIX_KEY_CONFLICTS.csv`, `V13_DATA_INTEGRITY_QA_REPORT.md` (all under docs/QUESTION_AUDIT).
- GitHub safety: PR #7 stays Draft on development branch; only docs/journey changed. No keys, original question texts, HTML, APK, merge or release modified. Next review 6 conflicts using authoritative source; next nominal G2 batch 328–377.


### 2026-11-09 | V14 linguistic trap QA on 6 V13 conflicts
- Applied ANRE question-bank QA and source-audit rules to six exact canonical question sets; no independent worker executed. Genuine wording traps: G1-LEG-028 (apartment block context: official ground floor/landing -> V9 C), G1-LEG-032 (4 vs 5 years: V9 A plausible, sanctions article pending), G1-LEG-034 (reception only if requested -> V9 A), G1-LEG-048 (payment choices only among supplier's -> V9 B). G1-LEG-024 depends on unverified 6-month ATR exemption; G2-ELEC-170 on exact definition of Cs and historical alleged A->C correction. All six remain quarantined, no canonical answer edited.
- Evidence committed in `docs/QUESTION_AUDIT/V14_TRAP_REVIEW_SIX_CONFLICTS.csv` (6 cases) and `docs/QUESTION_AUDIT/V14_TRAP_REVIEW_REPORT.md` with exact regulatory URLs. Source text is not a newly executed independent QA approval. Historical app badge `VERIFICAT TEHNIC` does not substitute for authoritative paragraph verification. PR #7 stays Draft, no merge, HTML/APK/keys unchanged.


### 2026-11-09 | ANRE linguistic agent routing gap fixed in documented protocol
- Verified `Romanian Language Reviewer` already existed in Avengers Asamble curated role catalog, mapped to `anre-question-bank-qa`. It was omitted from the compact default active ANRE team; V14 applied linguistic checklists without independent linguistic agent execution.
- Committed `docs/QUESTION_AUDIT/ANRE_LINGUISTIC_REVIEW_GATE.md`, making explicit option-by-option trap/ambiguity/source gate and distinct linguistic, technical, data and independent QA roles. No retroactive claim of QA execution.
- Previous V8–V12 screens and V14 conflicts remain preliminary; all application keys/HTML/APK unchanged, PR #7 Draft, no merge/release.


### 2026-11-09 | V15–V24: ANRE full 822-ID screening coverage and CKPT-003
- Canonical V10.29 blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`, 822 ID-uri unice: 408 G2 + 414 G1. Screening/preflight acoperire 822/822, nu „validare 822/822”; niveluri: 381 examinări model-assisted tehnic/lingvistic, 77 G2 legislație/norme preflight, 204 G1 corespondent textual exact G2, 160 G1 lingvistic/surse preflight.
- Livrabile auditate V15/V16 (81 G2 electrotehnică), V17 (77 G2 norm+leg), V18 (33 G2 concepte), V19 (50 G1 electrotehnică), V20 (822 ledger + 254 duplicate cross-grade), V21 (204 parity), V22 (160 G1 neidentice), V23 (822 coverage ledger), V24 (verificare surse XLSX originale).
- Două perechi cu întrebări și variante identice dar chei diferite: G1-ELE-018/G2-ELEC-170 și G1-ELE-102/G2-ELEC-245. Alte 6 diferențe canonical/tracker V13 persistă. Nu adjudeca fără sursă tehnică/normativă exactă, auditor independent și istoric barem.
- V24: LEGISLATIE-GR.-1-05.2023 (1).xlsx col I 1,2,3,4,5 în 5 rânduri neregulate; nu este barem A/B/C. Electrotehnică rând25 text+ABC nu include barem independent. Nicio corecție a baremelor.
- 77/77 G2 norm+leg și 50/50 G2-ELEC-001..050 au cheia A, vulnerabilitate de evaluare. G1-NOR trebuie corelat cu actualizările I7 (Ordin 959/2023); sursele pagină+ediție neconfirmate în majoritatea rândurilor.
- QA determinist înregistrat (număr de rânduri, unicitate ID, apartenență lot, potrivire canonical), dar **independent QA=NOT_RUN**, testare HTML/APK offline=NOT_RUN. 0 întrebări pregătite de release.
- Checkpoint permanent: `docs/QUESTION_AUDIT/CKPT_003_ANRE_2026_11_09_V24_HANDOFF.md`. PR #7 rămâne Open Draft, nu merge; doar documentație. Urmează rezolvarea conflictelor și maparea paragrafelor didactice exacte cu surse, apoi QA extern și E2E.


### 2026-11-09 | Source strategy: official consolidated legislation first
- User requested that ANRE normative/legal questions be checked directly against the current official government text rather than relying primarily on offline I7 manuals. Confirmed the Ministry of Justice legislative portal holds a consolidated I7 technical regulation (https://legislatie.just.ro/Public/DetaliiDocument/286763; visible historical consolidation 12.07.2023), amending Order 959/2023, and original Order 2741/2011.
- Added `docs/QUESTION_AUDIT/ANRE_OFFICIAL_LAW_FIRST_GATE_2026_11_09.md`: version/effectivity checks, per-question precise links and paragraphs, temporal exceptions, historical-exam vs current-law distinction, Romanian linguistic and independent source QA gates, and offline material rights.
- Source-method audit: V26–V29 G1-NOR-001–040 had primarily used a user Library PDF consolidated 22.09.2023, not a live official per-question crosscheck. Priority for reconciliation: G1-NOR-010,012,029,032. Official section 5.2.12.3.10 specifies 25m straight/15m up to three curves and a following increased-diameter condition for longer distances: capture the whole clause before concluding the old MCQ can be corrected.
- No automatic key or content changes; prior findings remain provisional. Some official direct webpage fetch attempts returned 502, so full 2026 amendment exhaustiveness and independent QA are NOT claimed. PR #7 Draft remains unmerged; HTML/APK unchanged.

### 2026-11-09 | Offline official I7 library builder (staging, no app changes)
- User requested downloadable, searchable OFFLINE legal reference and safe replacement of outdated PDFs. Verified Portalul Legislativ Terms permit reuse of official legal texts and states consolidated electronic editions are consultative; printed Monitorul Oficial is the authoritative legal source.
- Added `tools/build_offline_i7.mjs`: Node >=18 built-in only; downloads government I7 consolidated page `DetaliiDocumentAfis/287132` when Internet exists, or accepts supplied local HTML; extracts text and numbered-section index; checks source size/titles/critical section locators/minimum section count and aborts on failures; outputs one self-contained offline HTML reader plus JSON SHA256/date/provenance manifest. No network dependency in generated viewer.
- Added `docs/QUESTION_AUDIT/I7_OFFLINE_BUILDER_README.md` with syntax, limitations, staged migration and QA gates.
- Synthetic parser test PASS in tool; read-back of both new files on GitHub PASS. LIVE DOWNLOAD NOT_RUN: this session's container could not resolve the official government host. Independent QA on real annexes/tables and offline Android/HTML integration NOT_RUN; existing older manuals have NOT been replaced, no official text falsely promoted.
- Guardrails: PR #7 remains Draft/unmerged, app/src/main/assets/anre_trainer.html and APK unmodified, answer keys/options untouched. Promote to app only following real download and temporal/technical QA with user approval.

### 2026-11-09 | User-supplied official I7 HTML -> actual offline searchable reference (staged)
- Input `REGLEMENTARI (A) 01_11_2011.htm`: 5,504,033 bytes, SHA256 `99389c372d898dea067b80a93e1998f93a1b03302812e478de327ff2013d90b7`, I7-2011 with 959/2023 notes.
- Real local generated HTML reader + JSON index: 2,247 indexed point/article nodes, 48 annexes, 184 HTML tables preserved; 151 referenced JPG images missing from upload; each replaced with an explicit placeholder. No external asset dependency.
- QA structural PASS, browser JS search PASS in headless offline Chromium via set_content (file navigation restricted by test environment). Standalone HTML and bundled ZIP provided as conversation artifacts, not committed to GitHub yet: missing original figure assets and legal-currentness gate.
- Priority I7 source references 5.2.12.3.10, 5.3.3.21, 8.1.1.3.3 recorded for questions G1-NOR-032,029,010. Evidence notes `docs/QUESTION_AUDIT/I7_OFFLINE_USER_HTML_IMPORT_2026_11_09.md`.
- No canonical question keys, answer options, app HTML, APK or main branch changed; source promotion/replacement pending image bundle + independent normative QA + user approval.

### 2026-11-09 | Partial recovery of missing official-HTML figures using archived I7 PDF
- Official JPG URLs still not directly fetchable from this runtime. Found user's own I7 2023 archive PDF in Library, with embedded schematics. Compared figure captions, page coordinates and image objects, distinguished parallel figures / duplicate figure number changes.
- 82/151 images embedded in a new standalone offline reader (2023-archival labelled with source PDF page/xref); 69 remain explicitly missing. Search index and 184 HTML tables retained. Browser-offline QA on sample images + search PASS; structural stream checks for all 82 PASS. Current official JPG parity, normative SME approval, physical Android QA NOT_RUN.
- Detailed provenance/QA file `docs/QUESTION_AUDIT/I7_2026_11_09_ARCHIVAL_FIGURE_RECOVERY_82_OF_151.md`; generated HTML, ZIP, full figure manifest/CSV delivered as conversation artifacts, not committed to repository. Main app and keys unchanged, PR Draft, no merge.

### 2026-11-10 | I7 offline portable PDF fallback for 69 unresolved images
- Government endpoint /DetaliiDocumentAfis/287132 HTTP 502; exact JPG filenames not discoverable. No false claim of recovery. Reused user's authorized personal 249-page I7 archive PDF as local fallback, SHA256 4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431.
- Conversation ZIP `I7_2011_offline_cu_PDF_si_82_figuri.zip` includes standalone reader (82 archival matched embedded figures), the archived PDF, 69 unresolved/neighbor-page locator CSV, manifest and QA README. 69 original JPGs remain missing, but their entries link to local PDF, with orientation-only page links for short intervals; all warnings persist. 184 tables preserved. Local ZIP CRC PASS; HTML via Chromium offline set_content: 69 links, zero JS errors. file:// opening blocked by environment, physical Android QA NOT_RUN.
- Documentation `docs/QUESTION_AUDIT/I7_2026_11_10_OFFLINE_69_MISSING_FIGURE_PDF_FALLBACK.md`. No source/app key, APK/HTML integration or release changes. PR #7 remains Draft.

### 2026-11-10 | I7 archival offline figures V3: 106/151, conservative source QA
- Follow-up to 82/151 recovery. Recovered 17 large tabular elements using exact annex-headings 5.10-5.17, 5.19-5.22, 5.24-5.28 and rendered each section from the 2023 user Library PDF; plus 7 visually checked page excerpts (symbols Table 3.6, lightning Table 6.4, IP code diagram, earthing tables A5.34-1/3/4, keraunic map). These are marked **2023 archival PDF page facsimiles**, NOT direct official 2026 JPG matches.
- Full standalone reader now 106/151 available, 45/151 explicitly missing; 184 original HTML tables and offline article index retained. QA: 106/106 image streams passed decode/verify, 6 image browser samples decoded, search and anchors work, no JS errors, no network requests; direct file:// page navigation blocked by sandbox, used offline DOM test. Not physically tested in Android/WebView.
- Real standalone HTML + ZIP + 151-row figure audit CSV, reproduction scripts and QA were delivered as conversation artifacts (HTML SHA256 b2620e262a557a59d3044ae3616e6f80cd66c77ab94ebdb03b863f2484063a00; ZIP SHA256 db4c8b3a8c9914eb912d3eaf9b9861d145a9295c429475902438b5976557fb6e). Detailed source/evidence/limits in `docs/QUESTION_AUDIT/I7_OFFLINE_FIGURES_QA_V3_106_OF_151_2026_11_10.md`.
- Official image retrieval via direct source still blocked 502/DNS; external images deliberately not inserted as identical without proof. Edition/currentness, 45 missing assets and independent electrical/linguistic/legal QA remain open; **nothing modified in keys, canonical app HTML, APK, main**, PR #7 remains Draft and unmerged.

### 2026-11-10 | V30–V32 + CKPT-004: readiness for actual 822 source mapping
- User requested autonomous pre-mapping work without periodic chat loops; the work in this session moved the source preparation and QA to a deterministic, auditable handoff.
- GitHub canonical V10.29 HTML `bc5b5a61954ba138cf83987bfc932eca517f3b21` parsed: exactly 822 original IDs. Compared against all V23 rows; 822/822 ID, key, source-file, source-row parity; 0 differences.
- Added `docs/QUESTION_AUDIT/V30_ALL_822_OFFICIAL_OFFLINE_MAPPING_START_LEDGER.csv`: source-family routing for 595 technical electrotechnics, 112 legislation and 115 technical norms; 13 P0 cases, explicit `NOT_RUN` independent checks; no app approval. Mapping yet to start, not 822 validated.
- Added `docs/QUESTION_AUDIT/V31_I7_UPLOAD_40_SOURCE_HINT_ANCHOR_CROSSWALK.csv`: 27/40 numeric article hints from V26–29 resolved to one exact ID in the user-uploaded I7 HTML; 13 are missing/non-numeric/mixed sources. Re-read 4 P0 I7 paragraphs (8.1.1.3.3, 5.1.7.2, 5.3.3.21, 5.2.12.3.10) in the real HTML. No actual current-official-web or independent normative QA.
- Added `docs/QUESTION_AUDIT/V32_I7_45_MISSING_VISUAL_RELEVANCE_GATES.csv`: all 45 missing image filenames accounted for; topical grouping 18 current-rating/install tables, 9 protection/apparatus, 16 lightning/LPS, 2 other. Topic is only priority heuristic; no fabricated image-to-question match or source.
- All gates and next-stage procedure captured in `docs/QUESTION_AUDIT/CKPT_004_READY_FOR_822_MAPPING_2026_11_10.md`. Official portal direct access remained 502; 2026 legal-currentness / expert independent approvals NOT_RUN. No HTML/APK/keys/merge/release; PR #7 stays Draft.

### 2026-11-10 | New uploaded I7 PDF duplicate checked; 2 archived formulas recovered
- User reuploaded `803493174-I7-2011-completat2023(1).pdf`: 5,745,135 bytes and SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431` equal byte-for-byte to previous Library I7 PDF. This is the same 22.09.2023 archive, not an updated 2026 edition.
- Reexamined remaining 45 image placeholders and found two exact **2023 archival PDF formula** facsimiles by original HTML context: #133 cable combustible volume (PDF p.211); #137 lightning density Ng≈0.1·Td (PDF p.216). Embedded them only in standalone user conversation reader, marked 2023 archival. Result **108/151**, 43 still flagged missing. 184 original HTML tables preserved.
- Offline browser runtime and structural QA: 108 data-image nodes, 43 missing warnings, 2 formula nodes, 0 JS errors, 0 remote requests, 2 complete source images; PDF hashes identical. No current official JPG parity, independent norm review, or Android device QA.
- Provenance and test details: `docs/QUESTION_AUDIT/I7_2026_11_10_UPLOADED_DUPLICATE_TWO_FORMULAS_QA.md`. No app, key, APK or main modifications. PR #7 stays Draft, no merge.

### 2026-11-10 | Web image search authenticity pilot for missing I7 figures
- Evaluated Google/image-search candidates against original 2011 Monitorul Oficial 802 bis PDF text, official 959/2023 amendments, and user-owned I7 2023 PDF. Random visually similar online illustrations are **NOT** promoted as original normative figures; IEC class-II symbol and 6.3.2.4 PDE protection formula exemplify strict-source gates.
- New archival facsimile recovery on standalone offline reader: #26/#27 Fig.4.9 diagram + legend (I7 PDF 2023 p44, xref333), #46 Fig.6.17 roof-mesh lightning captation (PDF p95, xref696+698), verified with original labels and 2011 MO figure numbering. **111/151** visuals included, **40 missing**, 184 HTML tables unchanged.
- Offline headless Chromium QA PASS (3 image decodes, 0 JS errors, 0 network requests), 151-row figure audit CSV v5, candidate-status CSV and ZIP conversation artifact delivered. No 2026 official pixel-parity or independent SME legal/technical approval; no real Android test. Official portal still returned 502.
- GitHub doc: `docs/QUESTION_AUDIT/I7_WEB_IMAGE_SEARCH_PILOT_2026_11_10_111_OF_151.md`. Historical facsimiles are conversation artifacts, not committed into the application. No canonical answers, app HTML, APK, main branch, release or merge modifications.

### 2026-11-10 | I7 missing visual research V6; 126 facsimiles, 25 original JPGs still unverified
- User asked to keep searching online until EVERY missing figure is found and matches didactic literature, and receive no periodic status pings. Created versioned GitHub QA documentation `docs/QUESTION_AUDIT/I7_2026_11_10_V6_126_ARCHIVAL_25_UNVERIFIED_DIDACTIC_GATE.md`.
- Reinspected archive PDF 2023 and the 40 leftovers from previous 111/151 reader. Recovered 15 more exact *subject facsimiles* from exact archived pages (class and PE symbols, k formula, Figure 5.2, lightning diagrams, Annex 5.5/5.7, TT equation, k_c figure and Table A6.9.4), making **126/151** archival embedded facsimiles (not claimed byte-identical/current official JPG).
- Added 15 supplemental *page-context* previews for Annex 5.1/5.2 and 5.6; kept their original missing-figure warnings since no exact JPG segment match. 10 figures (61-67,75,85,86) remain without matching source image. Thus **25 original JPG identities unverified**, not all 151 source-verified.
- Technical didactic partial comparisons with Schneider Electric Electrical Installation Guide on IEC 60364 installation methods, TT residual protections and PE adiabatic sizing; **NO per-visual independent SME certification**. Official amendment 959/2023 changes PDA formula, so unrelated web illustrations are blocked. Current source URL retrieval is blocked in live web environment.
- Delivered conversation artifacts `I7_2011_OFFLINE_V6_126_FIGURI_2023_PLUS_15_CONTEXTE.html`, `I7_2011_V6_AUDIT_OFFLINE_PARTIAL.zip`, `I7_2011_151_FIGURI_QA_v6.csv` (not committed to GitHub due potential rights). Offline Chromium QA PASS (30 new decoded WebP, search, no network/JS errors), 184 original HTML tables retained. Android hardware QA and release approval NOT_RUN.
- User-requested completion-only notification is configured as a DAILY conditional automation; notify only when ALL 151 exact figure sources and didactic matches are verified, never merely from similar Google thumbnails. This is monitoring/checks, not proof that images have already been recovered. No app HTML, APK, barem, release or main changes. PR #7 remains Draft.

### 2026-11-10 | V7 direct in-session recovery (daily watch is not a substitute)
- User requested why a daily condition-check had been used instead of real-time action. Acknowledged mistaken workflow; executed substantive source matching in this session.
- Parsed original government-page HTML for #85/#86: Fig.7.11.2 PV multiple groups and Fig.7.13.1 mobile-unit generator hookup, matched each to actual single image objects in user PDF 2023: p137 xref1052 (886x586) and p140 xref1069 (724x461). Extracted originals (not generated), embedded archival-only in revised standalone reader, 128/151 archival figure subjects available, 23 original official JPG identities still unverified (15 supplemental page previews, 8 without a match).
- Official 2023 radius formula blocker characterized: synthetic 2023 PDF p113 explicitly uses '[POZA - A se vedea actul modificator]' for amended 6.3.2.4. Official portal 502; online Monitorul Oficial text accessible, screenshot of PDF and exact current original JPG retrieval failed, so no forced substitutions.
- QA PASS: 184 existing HTML tables, 151 source references accounted for, both PNGs integrity and headless Chromium offline decodes, 0 JS errors and 0 external requests, zip integrity; NOT RUN full independent figure didactic proof, current official JPG pixel matching and Android device test.
- Evidence `docs/QUESTION_AUDIT/I7_V7_IMMEDIATE_RECOVERY_128_OF_151_2026_11_10.md`. Standalone HTML/ZIP/CSV delivered in conversation, not committed to public GitHub app. PR #7 Draft, no main/app, barem, APK, merge or release modification.

### 2026-11-11 | V33 started: direct I7 source/linguistic verification of four priority questions
- User requested to resume solving ANRE Trainer questions and asked what else is required. No new user input required for read-only audit; original 822 canonical records and uploaded 2023 I7 are already available.
- Read canonical V10.29 exactly for G1-NOR-010/012/029/032. Directly reopened the I7 2023 PDF paragraphs/pages 162/49/65/62. Logged in `docs/QUESTION_AUDIT/V33_G1_NOR_PRIORITY4_I7_2023_RECHECK.csv` plus full notes in `docs/QUESTION_AUDIT/V33_FIRST4_I7_CONFLICTS_SOURCE_LING_QA_REPORT.md`.
- Preliminary outcomes: 010 C vs app B; 012 C conditional vs B (other norms require check); 029 dwelling C 2.5m vs app B 2.3m; 032 straight-run 25m not offered in 10/15/20 options, plus larger conduit exception, so not fixable with simple key swap. These are **candidates**, not QA-authorized edits.
- Portalul Legislativ direct source still HTTP 502; legal currentness and independent electrical/linguistic QA NOT_RUN. No key/HTML/APK/main changes, no merge/release. PR #7 Draft.

### 2026-11-11 | V34 + V35 actual source review: 19 more IDs, priority set and next I7 10
- Resumed read-only question verification, canonical V10.29 blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`. Previous V33 4 G1-NOR discrepancies preserved.
- V34: nine more priority source/linguistic reviews, including five G1 legislation (024/028/032/034/048) and four G1/G2 exact duplicate pairs (G1-ELE-018/G2-ELEC-170; G1-ELE-102/G2-ELEC-245). Sources: official Portalul Legislativ (ANRE 59/2013, ANRE 66/2023, Legea 123/2012 art 57/93, NTE 009/10/00), ABB double-busbar text, mathematical Cs=3C derivation with academic page unresolved. 028 C, 034 A, 048 B directly supported preliminarily, 024/032 have legal exception/contravention gates, 170 A mathematically supported but academic source and independent SME pending, 102/245 operational preference ambiguous. Persisted in `docs/QUESTION_AUDIT/V34_NINE_PRIORITY_SOURCE_LING_CONFLICTS.csv` and `V34_NINE_PRIORITY_SOURCE_LING_AUDIT_REPORT.md`.
- V35: ten actual `G1-NOR-041–050` compared directly to the user I7 2023 synthetic PDF, with p55,63,70,209 rendered and visually inspected; all 10 source/page positions recorded. G1-NOR-042 canonical B contradicts I7 5.2.4.6.1(a), which directly supports A (mono 2 conductors); G1-NOR-041 has material ambiguity 'mono 3 conductors' vs source 'mono 2 conductors'. Other 8 supported preliminarily; 047 phase-protection and 049 bell feed have explicit qualification. Files `V35_I7_G1_NOR_041_050_EXACT_PARAGRAPH_SCREEN.csv` + `V35_G1_NOR_041_050_I7_2023_SOURCE_REPORT.md`.
- **Coverage:** V33 4 + V34 9 + V35 10 = **23 individually rechecked new in this phase**, remaining 799 with only previous screening levels. Zero independent licensed engineer/legal/linguistic QA signoffs. No app keys, question ABC, HTML, APK or main changes; PR #7 Draft unmerged.
- **Next:** G1-NOR-051–060 and extended official-law temporal checks, then remaining 799. Do not label all 822 as source verified. Avoid unnecessary Actions builds during source-only audit.

### 2026-11-11 | V36–V38 actual checks: 30 more ID, 53/822 rechecked; continue-batches task created
- User asked that audit continue through all 822 without routine prompting; only involve user for necessary input/approval. New daily condition-check task **Audit 822 întrebări ANRE** set to actively audit batches and store checkpoints, not simply monitor. Existing morning ANRE usable-now task remains separate (avoid pointless Github Actions builds).
- Actual in-session source audit: G1-NOR-051–080, **30 original canonical ID/A/B/C/key records** reconciled against I7 2023 PDF and official indexed portal; structured files `docs/QUESTION_AUDIT/V36_G1_NOR_051_060_SOURCE_KEY_RECHECK.csv`, `V37_G1_NOR_061_070_SOURCE_KEY_RECHECK.csv`, `V38_G1_NOR_071_080_EXACT_SOURCE_SCREEN.csv`; reports `V36_V37_G1_NOR_051_070_EVIDENCE_QA_REPORT.md` and `V38_G1_NOR_071_080_I7_SOURCE_REPORT.md`.
- Direct I7 2023 conflicts: G1-NOR-058 key B vs conditionally permitted C (3.0.3.5/IP33); G1-NOR-060 B vs explicitly banned C (5.5.3.2 water pipe as PE); G1-NOR-061 A vs prohibited B (5.2.12.3.4 tube splices crossing structural elements); G1-NOR-066 B vs expressly prohibited A (5.2.12.1.4 individual conductors in buried conduit, not the same as buried cables). G1-NOR-053 A conflicts with historic SR234 branching/racord distinction, C candidate requires legal date/version proof. G1-NOR-054 A fixed 1m vs recommended 0.6–1.5m B, but several numeric options can be physically within range: **ambiguity**, no simplistic rekey. More scope/wording gates: 051,056,062,067,071 (PE/PEN versus N). Remaining 19 rows source-matched preliminarily with conditions noted.
- **Cumulative V33–V38 = 4+9+10+10+10+10 = 53/822 rechecked individually, not 53 independently approved.** 769 still waiting for same-depth audit, and 0 independent signed-off reviews. 0 app changes; no changes to barem, ABC, apk, html, main; PR #7 Draft unmerged.
- Next lot G1-NOR-081–090 from canonical data. Persist exact source/version, selective quote/paraphrase and independent technical/linguistic QA gates; no claim of 2026 legal history exhaustiveness, no merges without user approval.

### 2026-11-11 | Priority reversal confirmed by user: 822 question quality first; no application work until DONE
- **Latest explicit user instruction overrides previous ASAP-app issue #10 policy:** Do NOT build/deliver/use/edit the HTML or APK before the 822 questions have been source-mapped, technically and linguistically verified, and conflicts resolved/controlled. Risk of learning incorrect keys is the reason. Revised GitHub issue #10 title/body to `[P0] Verificare completă 822 întrebări ANRE ÎNAINTE de aplicație`, with strict Phase 1 question QA before Phase 2 app.
- Recurring ANRE automations already disabled at user's request in this thread; no GitHub Actions requested for content QA.
- Immediately audited **G1-NOR-081–100**, 20 stable canonical records with full A/B/C/source/row, using the official Portalul Legislativ I7 consolidated online text and local I7 2023 user PDF. Findings: #089 canonical A contradicts I7 5.1.4.3.3 (B explicitly allowed with end markings), #090 canonical B ambiguous vs I7 5.2.12.2.12 literal C, #081/#082 each omit one half of the "fire resistant AND flame-retardant" conjunction, #100 uses "greater than 50kΩ" whereas official says "not less than 50kΩ". Other 15 supported provisionally.
- Evidence in `docs/QUESTION_AUDIT/V39_G1_NOR_081_090_OFFICIAL_I7_SOURCE_SCREEN.csv`, `V40_G1_NOR_091_100_OFFICIAL_I7_SOURCE_SCREEN.csv`, and `V39_V40_G1_NOR_081_100_SOURCE_REPORT.md`.
- Total **73/822** newly individually checked in V33–V40, 749 pending to same depth; **0** independent technical/linguistic QA approvals, no keys changed. Official 2026 effective history not exhaustively checked. PR #7 stays Draft, no merge/release, no modifications to application HTML/APK or main.
- Resume **G1-NOR-101–110**. Make sure future checkpoints do not resurrect "app first"; user must approve any barem change or integration.

### 2026-11-11 | V41–V57: substantive 147-row audit session, 214/822 total source screens, no app work
- User approved autonomous multi-batch checking within a live session, no scheduled follow-ups. P0 question validity remains primary; GitHub issue #10 unchanged. Read canonical V10.29 blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`, kept every original ID, question, A/B/C, answer and source-row unchanged.
- **V41–V42**: 15 Grade2 normative/bibliography items cross-referenced to ANRE 2023 thematic PDF exact row 14/22/29; G2-NOR-137/141/145 have NO correct option because their stems ask for an approval ACT while all options are NORMATIVE IDENTIFIERS.
- **V43–V47**: 50 G1 legislative entries reviewed against Legea123/2012 and ANRE Orders 5/2023,59/2013,74/2014,66/2023; G1-LEG-015 canonic B is an offence when question seeks contravention, #019 C→B candidate, #026 C→B candidate, #020 A→B candidate; additional historical/exemption gates remain.
- **V48–V54**: 62 Grade2 legislative metadata and authorization-site items audited for provenance/content; all stored keys are A. The 62 plus 15 Grade2 normative items means **77/77 non-electrotechnics Grade II have key A** and are not yet proven official ANRE sample MCQs. Grade2 licensing tariffs #081/082 date-sensitive. Source official 2023 thematic document verified, sample XLSX binaries unavailable from web/container.
- **V55–V56**: 20 canonical Grade1 electrotechnics IDs analyzed with formula derivation and actual OpenStax textbook for capacitor series/parallel; gaps in engineering reference/operating mode marked. G1-ELE-008 is absent from canonical bank and was NOT fabricated. G1-ELE-018 vs Grade2-ELEC-170 duplicate key mismatch remains unresolved.
- **V57**: master coverage table of 822 ID with 214 unique source-rechecked, 608 pending same-depth source check; 0 independent technical/linguistic approvals and 0 application-ready entries. This session produced 147 rows, with 6 re-reviews = **141 newly checked unique IDs**. All 147 original Q/A/B/C/keys confirmed byte-for-byte identical to canonical in GitHub read-back, 0 new-row duplicates. Details in `docs/QUESTION_AUDIT/CKPT_005_V57_214_OF_822_PRELIMINARY_SOURCE_SCREEN.md`.
- No modifications to grading, HTML, APK, main, merge or release. No GitHub Actions built. PR #7 Draft.
- **Resume from G1-ELE-022** using 2023 official and 2026 effective source version and precise didactic citations, not stale or fabricated textbook evidence. User will say 'continuă' to start next live session, no scheduling requested.

## 2026-11-11 | V62–V75 | 822/822 evidence passports, release gate still closed
- Preluare directă din CKPT-007: 274/822 individual source screens preliminare. În această sesiune, V62–V72 au reconciliat alte 548 ID (36 G1 norme, 329 G2 electrotehnică, 183 G1 electrotehnică) din note anterioare și textul canonic; **nu** reprezintă 548 verdicturi cu sursă exactă verificată independent.
- V73: 822 pașapoarte evidență, 71 P0 / 229 P1 / 522 P2; 822 rânduri și ID-uri unice, 0 modificări chei/enunț/opțiuni/cod, 0 independent QA, 0 release approval.
- V74: 71 P0, 14 cazuri cu cercetare/dispoziție specifică, dintre care 6 candidați de chei alternative susținute preliminar din surse legislative/normative, plus 3 G2 normative cu opțiuni de tip greșit; 57 P0 încă fără nouă adjudecare specifică.
- V75: `docs/QUESTION_AUDIT/V75_ALL_822_EVIDENCE_QA_AND_RELEASE_GATE_REPORT.md`; handoff `docs/QUESTION_AUDIT/CKPT_008_V75_822_EVIDENCE_HANDOFF.md`. Linkuri de sursă și limitări clar distinse de aprobare.
- **Important:** V73 822/822 = EVIDENCE_COVERAGE_COMPLETE, **nu** CONTENT_VALIDATION_COMPLETE. Rămân surse exacte, versiuni 2026, QA tehnic/lingvistic independent, conflicte și teste de aplicație. PR #7 Draft; fără merge/main/release și fără APK/HTML editat.


## 2026-11-11 | CKPT-010 | V85–V99 focused audit and real separate AI review
- Continued from CKPT009 and immutable V78/V83, no duplicate screening credit: 50 new focused records (38 P0,12 P1),4 temporal rechecks on existing IDs; focused evidence total91/822. All72P0 still open; investigation coverage is not correctness approval.
- Separate AI reviewers actually reopened primary sources and assessed claims/ABC:51 review rows,50 unique IDs.42 scoped-support rows,8blocked,1revision; no official/human answer signoff or learning approval. NOR028 missing I7 exceptions found by reviewer, corrected in audit explanation and read back; canonical key unchanged.
- New V95 master822 rows preserves old evidence, sources/editions/gaps, separate AI verdicts; V95 reproducible data QA:54 analysis records have zero canonical text/ABC/key mismatches. V96 detailed report; CKPT010 handoff.
- Temporal gate: law URL300063 is selected2025 edition; V91 narrows2026 evidence but full selectedJuly2026 consolidation retrieval is incomplete. PE155 primary-text gaps and missing learner diagram remain.
- Source PDFs/screenshots inspected privately, not redistributed. Canonical baremes/question/ABC/HTML/APK untouched; no main/merge/release/deploy. PR7 stays Draft. No persistent cloud worker or automation launched.


## 2026-11-11 | CKPT-011 | Deep audit execution preparation (no new answer approvals)
- User requested preparation for all three remaining content-audit stages, targeting completion today, Europe/Bucharest. Prepared an operational runbook, exact criteria, source requirements and reviewer workflow; deadline is a target, not guaranteed evidence availability.
- Canonical822 IDs routed exactly once to568 exactQABC units (254 duplicate groups,2 contradictory-key groups),30 batches max20units. Original keys/grade/provenance/explanations exported on demand; prior evidence reused without new-credit inflation.
- Audit script guards canonical blob and branch, exports batches and checks structural closure/source/version/ABC/explanation/reviewer requirements. Structural PASS is not technical/legal truth or app approval. Contradictory original keys cannot be verified as stored.
- Prepared author/reviewer roles and source dependencies; no30-batch execution claimed. Existing figure PDF is available for technical audit; absence of app association must not be confused with a missing source file.
- No answer/text/HTML/APK changes, no merge/release, no persistent cloud worker or automation. Checkpoint011 is the next execution entry point.


## 2026-11-11 | CKPT-012 | Recover source documents PE155, PE102 and GIS (no learning approvals)
- Continued from CKPT011 without restarting batch organization. Targeted source discovery yielded PE155/92 copies with RENEL heading and §§3.2.1/3.2.3 supporting NOR030(A)/NOR031(B) provisionally; copy numbering inconsistency (3.3.1/3.3.2) and document authentication remain.
- Retrieved PE102/86 text §§4.6.3 and 2.12(a) note4. NOR027 original key B conflicts with feed-to-contact-screws requirement favoring A. NOR023 local heating A supported only within norm-specific scope, not an unrestricted current-law assertion.
- Retrieved Hitachi MSM Rev R p98, EirGrid GIS functional spec R4 §10.1, Eaton XGIS design guide (2020); ELE088 source suite strengthened but no blanket option adjudication. Current law311821 and supply regulation264611 direct opens returned502; LEG017/032 still blocked.
- All screenshot attempts of source PDFs returned Cache miss, so no visual verification claimed. Cross-document review only, no independently running agent reviewer or qualified expert signoff. Added SOURCE_RECOVERY_POST_CKPT011_2026_11_11.md + CKPT_012_SOURCE_RECOVERY_PE155_PE102_GIS_2026_11_11.md.
- No new deep-batch completion, 0 learning approvals; no changes to canonical bank, keys, HTML/APK, main/merge/release/deploy. Continue source QA and batches from CKPT011.

- CKPT012 addendum: found original Monitorul Oficial 100/06.02.2023 PDF (PPC hosting), visually verified pp.9 and12. LEG017 historical termination art18(3) distinguished from power interruption art26; exact2026 Law123 consolidation still missing. Updated report and checkpoint with screenshot success specifically for this PDF, without claiming PE155/PE102 PDF visual QA.

- CKPT012 LEG032 addendum: Portal Legislativ Reg66/2023 opened; art30 states5-year authorization periodic visa, art35 recognizes gradeIIA design scope under conditions. Together with Legea123 art93 indexed2026 this challenges stored LEG032 B, without final adjudication or approved key change. Legal chain/current official consolidation remains to verify.


## 2026-11-11 | CKPT-013 | First deep NOR/LEG source investigations (not closed)
- Continued directly from CKPT012. Opened six risk-P0 source/ABC/edition investigations in DEEP-NOR-01 (NOR023/027/030/031) and DEEP-LEG-01 (LEG017/032), reusing older evidence without counting it twice. No deep batch closure or learning approvals.
- Official ANRE05.2023 bibliography PDF screenshot inspected p3: PE102 republication1993 only for gradeII+ (not gradeI), PE155/92 for gradesI/II+, I7 for gradeI/II+. Applied edition scope to avoid relying on PE102 alone for Grade1 question NOR027.
- NOR027 remains strong candidate A versus stored B based on historical screw/contact wiring rule; professional independent/edition QA pending. NOR030/031 historical PE155 support is provisional because of source numbering and visual-verification caveats; LEG017 termination vs disconnection and LEG032 5-year visa statutory chain left unresolved.
- Parliament shows 2026 Law160 changed Law123 Articles3/73^1, not58/93, narrowing but not clearing temporal gate (OUG152/2024 affected93). Official consolidated July2026 Article58/93 inaccessible, no legal gate waived.
- Executed machine-check over Github-read manifest+report: all6 units unique, assigned to expected batch/P0, report present, PR Draft/unmerged. This is NOT independent specialist QA and deep batch structural validator was not run.
- Saved detailed initial research in DEEP_EXECUTION_2026_11_11/DEEP_NOR_01_LEG_01_INITIAL_EVIDENCE_2026_11_11.md and handoff CKPT_013_DEEP_FIRST_NOR_LEG_SOURCE_QA_2026_11_11.md. No canonical key/Q/ABC/HTML/APK or merge/release changes.


## 2026-11-11 | CKPT-014 | DEEP-NOR-01 full 20-case source/ABC triage, pending independent QA
- Investigated and recorded ALL 20 exact units (16 P0,4 P1), preserving canonical Q/A/B/C/key/unit hash and source locator, per-option reasoning and remaining gates. Structural QA reread GitHub CSV against manifest V73:20/20 correct provenance,0 drift,0 fake reviews,0 approvals; PR7 Draft/unmerged; HTML blob unchanged.
- NOR089 (stored A) conflicts with I7 §5.1.4.3.3 allowing one color for all phase wires with end identification (B candidate). NOR029 (stored B) has dwelling max2.5m (C intended) but literal wording also admits stricter 2m/2.3m, so requires linguistic rewrite. NOR027, NOR010, NOR012, NOR042 remain high-priority source/key conflicts and edition gates. NOR090 B/C overlapping.
- Important correction to earlier RESEARCH, not bank: NOR032 source is PE155/92 §3.2.10 (15m for straight horizontal branch columns), not generic I7 §5.2.12.3.10 (25m straight tube pulling boxes). Stored B is provisionally supported. Old V33 NO_VALID_OPTION conclusion superseded at research layer, preserved for provenance and reviewer inspection.
- G2-NOR-137/141/145 still have NO_CORRECT_OPTION: their stems ask for approval act while A/B/C contain only normative indicative codes. This problem was already found in V41; no double-counting.
- All 20 rows marked independent_review NOT_RUN and approved_for_learning NO. Work is source/linguistic preliminary triage, NOT final validation, independent AI run, or qualified human signoff. Structural deep batch validator not run because closure criteria unmet.
- GitHub artifacts: DEEP_EXECUTION_2026_11_11/DEEP_NOR_01_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv and CKPT_014_DEEP_NOR_01_ALL20_RESEARCH_TRIAGE_AND_QA_2026_11_11.md. Next: distinct QA on sources/ABC and version; then finish/validate full batch, proceed LEG/ELE. No canonical edits/merge/release.


## 2026-11-11 | CKPT-015 | NOR-01 and LEG-01 full source/ABC preliminary research (40 units)
- DEEP-NOR-01 20/20 researched (16 P0,4 P1), DEEP-LEG-01 20/20 researched (10 P0,10 P1) with full canonical question/ABC, original keys, exact AU/hash, references, option-by-option rationales, issues and next actions. Both files checked mechanically against V73 and UNITS568:20/20 PASS each, 0 drift.
- Legal source flags: LEG019 Art93 technical norm breach = contravention (B vs C), LEG026 Art92(2) clandestine direct hookup = crime (B vs C), LEG034 Reg66 Art37(e)/(h) = A rather than unconditional participation B, LEG048 Art57(2) allows supplier-offered payment method B (vs A), LEG015 option B criminal not contravention; all need current2026 formal/legal QA.
- Norm flags: NOR089 B supported by I7 single-color with end markers (stored A); NOR029 homes max2.5m but literal multiple true; NOR032 PE155 3.2.10 supports 15m B and corrects prior V33 wrong-source reasoning. Existing V41 act-vs-norm-code defects preserved without recredit.
- 0 deep batches technically certified, 0 real independent reviewer signoff and 0 approved for learning. Source full-edition 2026 gates remain. deep_audit_execution.py validate not claimed because reviewer evidence absent. No changes to Q/ABC/keys/HTML/APK, branch main, merge/release. CKPT015 is next handoff.


## 2026-11-11 | CKPT-016/017 | Avengers 0.4.2 source specificity + ELE01/ELE02 priority lot triage
- Updated ACTUAL private Avengers Asamble plugin v0.4.1 -> v0.4.2 release pluginrel_6af4563244c48191a027f863627fdb9c, exact-object/action/rule/edition/grade-source scope gate and 6/6 deterministic regression fixtures PASS. NOR032 wrong-source generic I7 vs specific PE155 15m rule now a blocked fixture; real document QA still necessary, labels can be falsified.
- Performed ELE01 20/20 pre-review source/ABC units (39 canonical ID placements), ELE02 20/20 P0 units (36 placements). All four first priority batches NOR01/LEG01/ELE01/ELE02 have source/ABC triage for 80 unique units /115 original ID placements. This is **research coverage**, not final validation.
- Applied new gate to the two ELE CSVs: 8 mismatched generic source citations reclassified BLOCKED_SOURCE_SCOPE with exact source missing; 1 circuit breaker link demoted partial (not drawout-specific). Avoided ungrounded citations instead of manufacturing evidence.
- Deterministic check after last writes: 40/40 ELE unit records and75/75 individual ID mappings match canonical Q/ABC/keys, source gate classification, no approvals; original HTML Git blob bc5b5a61954ba138cf83987bfc932eca517f3b21 preserved, PR7 Draft/unmerged.
- Independent technical/source/linguistic QA NOT_RUN; final deep-batch validator intentionally not run because true closure requirements unmet. 0/30 batches closed, 0/822 approved for learning. CKPT017 carries detailed handoff and per-source limitations. No changes to original question bank, keys, HTML/APK, main or release.


## 2026-11-11 | CKPT-018 | 3 more ANRE batches pre-review researched (LEG02, NOR02, ELE03)
- Added 20/20 pre-review source-and-ABC case files for each of DEEP-LEG-02 (20 IDs), DEEP-NOR-02 (20 IDs), DEEP-ELE-03 (31 IDs): 60 new unique units and 71 canonical ID placements. Across all work, 7/30 planned batches with preliminary research, 140/568 work units and 186/822 ID placements, **not 7 finalized batches**.
- Key source findings: LEG011 regulator Art47 requires publication of wide circulation vs all options saying local newspaper; LEG013 periodic vizare 5y; LEG027 ATR expires after12mo without connection contract under Reg59 art33(1)(b); LEG039 art26(1) ATR 30 days for 'fișă de soluție' not explicitly MV-only. NOR025 and NOR033 blocked because PE102 cited as GradeII bibliography for GradeI question. ELE005 graph b-n+1 connected condition, ELE152 gamma has units inverse length, ELE126 can have multiple true answers without exact busbar scheme.
- QA GitHub reread 3 CSVs + original V73/UNITS568: 60/60 units, 71/71 ID assignments, QABC, hashes and original keys exact, all source statuses preliminary, all unapproved: PASS. One first QA check falsely failed because code expected 'ABC_analysis_PRELIMINARY' but ELE CSV header said 'ABC_reasoning_PRELIMINARY'. Diagnosed as checker-schema mismatch, no file corruption. Corrected check to accept both named fields, reran full QA PASS. Lesson to add to QA regression.
- Official Reg66 consolidated text opened at Portal; Reg59 and Law123 indexed but direct page returns502, no final2026 official law certification. Some V90/V97 I7 source checks reused with attribution, no independent source reopening this session.
- CKPT018 handoff documents remaining 23 batches/428 units/636 canonical IDs awaiting pre-review. 0/30 deep batches closed, 0/822 approved for learner use, no new genuine separate reviewer signoff. No changes to source keys/ABC/HTML/APK, main branch, merge/release.

## 2026-11-11 | CKPT-019 | sursă secundară + P0 bus-coupler source leads
- Added secondary-site crosswalk `docs/QUESTION_AUDIT/SECONDARY_SITE_2026_11_11/PILOT_CROSSWALK.csv`: 10 original ANRE canonical IDs, 6 topic families; 6 item/option correspondences with randomized option order and 4 stem/comment-only leads. These are **source-discovery observations, never key/answer approval**.
- Two linked P0: G2-ELEC-266 and G1-ELE-125; identified exact-object distinction between standard double bus and dedicated transfer/bypass configurations from indexed ABB/APTRANSCO reference-book excerpts. **PDF screenshot requests failed (cache miss), no visual source confirmation or independent expert QA**. Reg59 art26(1) legal index supports a separate timing lead but official direct URL returned502.
- On audit branch only: saved pilot rules, matching register, targeted leads and CKPT019. Rechecked 10/10 IDs in canonical V73; preliminary 7/30 batches/186 IDs unchanged; 0/822 signed off; no key/HTML/APK changes and no merge.

## 2026-11-11 | CKPT-020 | Perplexity 20 P0 selection and factual baseline
- Pin 20 **distinct** P0 exact QABC units with grade/ID/ABC/keys unchanged in `docs/QUESTION_AUDIT/PERPLEXITY_PILOT_2026_11_11/INPUT_20_P0.csv`; deterministic cross-check V73 and ID_ROUTING_822: 20/20 PASS, no duplicates or discrepancies. Selected 10 electrotechnical, 5 legal, 5 norms (including one II).
- Public evidence reopened in this session for 4 canonical IDs across 3 actual pages: DOE inverter for G1-ELE-029, Romanian Law123 article92/93 for G1-LEG-019/026, ANRE Reg66 art37 for G1-LEG-034. One I7 phase-colour source indexed but direct fetch returned HTTP 502, and 15 IDs have earlier project source leads only. All 20 remain unapproved.
- Perplexity query execution **NOT_RUN** (no Perplexity connector/session/API; direct search endpoint inaccessible via browsing); prepared standardized four rounds of 5, baseline CSV and NOT_RUN result-scorecard. Do not count this as Perplexity speed/accuracy gain or closed deep-batch work.
- Independent reviewer NOT_RUN; original keys, HTML, APK, main, release unchanged. 7/30 prelim-batches and 0/822 learner approvals remain at CKPT-019 levels. Proof/limits in CKPT_020.

## 2026-11-11 | CKPT-021 | 5 P0 pilot questions: real web-source recheck (not Perplexity)
- Continued Perplexity pilot but **no direct Perplexity model access**; no false benchmark or 20/20 claimed. Completed first 5 **web research** inputs /5 unique QABC/10 existing grade-specific ID placements (all previously research-triaged in DEEP-ELE-01). Source work reused, not double-counted.
- Evidence delta: GE Vernova primary manufacturer case study on series short-circuit limiting reactance for G1-ELE-028; historical scanned user PDF p10 with fault diagram reopened via Library pages. ABB handbook §3.14.1.3/.4 re-opened with bus coupler typical open and shared feeders, conditional against unqualified G1-ELE-102 cold standby; CED engineering GIS gas compartment discussion is secondary scope lead for ELE-088. DOE inverter used for ELE-029, capacitance delta-star math re-derived for ELE-018. ABB/Hitachi/CED/GE PDF screenshots failed cache miss: **PDF text only**, no visual validation.
- Input-to-results QA crosscheck passed 5/5 (stable ID, unit, grade, answer key, ABC evidence, zero status leaks). All 5 need independent specialist review and exact source applicability; 0 keys/HTML/APK changed, 0 accepted. `ROUND1_WEB_EVIDENCE_5.csv` and CKPT_021 saved in pilot folder.
- Existing 7/30 prelim batches and 0/822 learner approvals unchanged. No merge/release; PR remains Draft.

## 2026-11-11 | CKPT-022 | free-web ANRE P0 research, Perplexity paused
- User tried Perplexity free twice and found access limits unsuitable. Decision: keep that experiment documented as a lesson but **stop relying on Perplexity**; continue through free web + primary sources + Avengers QA.
- Investigated remaining 15 distinct P0 pilot units in rounds2–4, saving `docs/QUESTION_AUDIT/WEB_ONLY_P0_2026_11_11/ROUND{2,3,4}_WEB_EVIDENCE_5.csv` with exact source locators and A/B/C, access limits and remaining blockers. Combined with CKPT021 previous 5 = **20/20 provisional research** for the fixed pilot set, no approved learner answer.
- Important direct 2026 authority: `legislatie.just.ro/Public/DetaliiDocument/300063` displays Legea123/2012 latest consolidation26.07.2026; LEG019 art93(1)(3) contravention B vs stored C; LEG026 art92(2) crime B vs stored C. Also exact I7 central fuse contact (NOR027), I7 max residential panel 2.5m with ambiguous stem (NOR029), PE155 specific horizontal column box >15m (NOR032), I7 phase colors marking (NOR089), derived G2-NOR-137 none option answers ACT of approval. ABB and IEEE/IET educational sources provide cautious topology and sequencing context for ELE questions.
- Structural QA executed after GitHub writes: 15/15 original ID/unit/batch/grade/key/risk consistent with canonical manifests; source/ABC/blocker status complete; **PASS, no mismatch**. PDF screenshot attempts failed; copied text verified only where opened. Independent technical+legal+linguistic reviewer NOT_RUN, no qualified human signoff, no key/ABC/HTML/APK changes, no main merge/release.
- Global audit remains **7/30 preliminary batches, 140/568 units, 186/822 ID placements, 0/822 approved**. CKPT022 is research addendum, not expansion of batch coverage.

## 2026-11-11 | CKPT-023 | 3 new deep pre-QA batches, 60 units /79 IDs
- Completed source/ABC preliminary research for DEEP-ELE-04 (20 units/39 original grade-specific IDs), DEEP-LEG-03 (20/20) and DEEP-NOR-03 (20/20), on PR7 Draft audit branch. Total distinct pretriaged 10/30 batches, 200/568 units and 265/822 IDs. Not 10 independently approved batches; **0/822 learner approvals**.
- High-risk issue leads (not authorized key changes): G1-LEG-043 art26(4)(b) minimum5 **working** days for nonpayment, bank says5 days generally; G1-LEG-040 Reg66 art35(A)(a) GradeI paragraph refers to GradeII/III/IV in condition (i); G1-NOR-054 I7 switch height recommended0.6–1.5m (B) vs stored1m (A); G1-NOR-041 monophase three vs normative two conductor phrasing; G1-NOR-050/051 potential Cu-vs-Al ambiguous minimum; G1-ELE-007 slip regime motoring assumptions.
- First structural QA checker incorrectly expected only next_gate; ELE CSV used remaining_gate. Corrected checker to accept schema alternatives, reran 60/60 units and79/79 canonical IDs validation against UNITS568/ID_ROUTING822/V73: **PASS, 0 mismatches**, original Q/A/B/C keys and hashes unchanged.
- Specific source/edition/grade certainty and independent human or separate expert QA remain **NOT_RUN**. All work research only; no canonical, HTML, APK, main/release/merge modifications. CKPT_023 contains the exact evidence paths, source failures and handoff.

## 2026-11-12 | CKPT-024 | NOR029 false ambiguity corrected; semantic QA classifier
- User identified that `G1-NOR-029` asks for the **normative maximum in dwellings**, not any example of permitted height. I7 §5.3.3.21 general2.3m / dwellings exception2.5m -> candidate **C**, stored **B**, and previous `AMBIGUOUS_MULTIPLE_TRUE` is a false-positive due to comparing admissible examples rather than the requested bound. Original historical evidence retained, superseding classification recorded separately.
- Added audit-only `tools/qa_normative_threshold.mjs`, 11 `node:test` fixtures (source saved but not run by Node here) and `QA_RULES/NORMATIVE_LIMIT_SCOPE_SEMANTICS_V1_2026_11_12.md`. Executed same pure JS algorithm with 11 synthetic fixtures: first2/11 due to `pardosel` normalizer mismatch; corrected to `pardose`; rerun **11/11 pass**. No independently verified source edition or final learner answer certification.
- Key lesson: parse question intent/quantifier, identify exact object/measure/scope, apply specific exception, **equate option to legal threshold rather than compare <=**; only genuine multianswers/unknown source escalated. Original Q/ABC/key/HTML/APK unchanged; no merge/release; 0/822 approved.

## 2026-11-12 | Post-CKPT-024 | fast QA no-restart routing v1
- Semantics learning is LOCAL to limit/intention/scope questions: DO NOT restart the 822-item ANRE audit. Exact bank inventory 822 ID placements/568 distinct QABC units; existing research 10/30 batches, 200 units/265 IDs; approved 0/822.
- Rapid GitHub register scan: 7 narrow numeric limit candidates, 6 require bound-specific recheck; G1-NOR-005 false positive because `cel puțin` qualifies count of **measurements**, not requested distance. Separate lexical risk flags are exploratory, never verdicts.
- Saved `docs/QUESTION_AUDIT/QA_RULES/TARGETED_SEMANTIC_BOUND_RECHECK_2026_11_12.csv` and `FAST_QA_TRIAGE_NO_RESTART_V1_2026_11_12.md` to route evidence-reuse, intent/scope-specific rule, deterministic fast-track, independent review and true-blocker escalation. No automatic answers, approvals, or canonical code changes.

## 2026-11-12 | Avengers Academy | interpretare colaborativă pentru incertitudini reale
- New explicit user rule: after checking source/ABC, present unclear exam item **verbatim** with answer alternatives, competing interpretations and one narrow user question; collaboratively infer a generalizable testable rule.
- Preserve user perspective as hypothesis rather than verified norm/key; keep source version and separate QA proof, no automatic canonical answer changes. Do not interrupt for trivial uncertainties or reask the same case. Continue clear work autonomously.
- Documented in `docs/QUESTION_AUDIT/QA_RULES/COLLABORATIVE_UNCERTAINTY_ESCALATION_V1_2026_11_12.md`, linked from fast-track protocol; pilot discussion `G1-NOR-041` on physical 3 conductors vs normative 2 active conductors with current key B, no signoff.

## 2026-11-12 | Avengers Academy user training | G1-NOR-041 answer-option traps
- User correctly routed the canonical item as an **incomplete statement** whose A/B/C are logical continuations, not separate assertions; chose stored B using conjunctive conditions and 16mm²Cu/25mm²Al thresholds; A overgeneralizes polyphase `indiferent de secţiune`, C replaces true thresholds with larger ones.
- Found important source provenance distinction: historical **I7-02 §5.1.8** reproduces `trei conductoare` verbatim alongside correct thresholds; **I7-2011 §5.2.4.6.1** uses `două conductoare` in monophase clause. Current 2026 applicability and exact questionnaire derivation are NOT certified. The old assumption that `trei` must mean L+N+PE is not necessary as an explanation.
- Saved generalized QA rule, narrow clause-matcher and 11 deterministic fixtures; first runner failed to parse Romanian `trei` versus digit `3`, fixed; **11/11 synthetic pass** after correction. No separate Node CI/instrumented agent or independent legal/technical QA. No original key/stem/software/merge change.

## 2026-11-12 | Avengers Academy | NOR050 exact I7 row vs distractor from neighboring row
- Continued user-led insight: complete options only count when matching **exact regulated circuit/object**, table **row**, conductor material and numeric value. Earlier DEEP-NOR-03 `A_WITH_ALTERNATE_AL_CAVEAT` for NOR050 implied ambiguity from 4mm² Al, but I7-2011 Anexa5.32 row1.2 socket circuits shows 2.5mm² Cu and **blank Al**; 4mm² Al is row1.3 **force** circuits. Candidate unique A supported by the original printed text. Historical triage retained and superseded via dedicated CSV; no automatic learning approval.
- Online PDF raw text viewed with exact table rows; web PDF screenshot failed cache miss; official 2023 amendment page direct open502. Don't claim visual proof or fully certified current edition. NOR051 with domestic appliance >2kW remains genuine object/scope question: I7§5.4.7 says in dwellings use separate socket circuits, while question does not explicitly mention locuințe/priză. Ask user how they parse this, without assuming a key.
- Saved `tools/qa_normative_table_row.mjs` and 10 regression fixtures (synthetic JS runner **10/10 PASS**, standalone Node/CI not executed), plus `docs/QUESTION_AUDIT/QA_RULES/EXACT_TABLE_ROW_VS_NEIGHBOR_ROW_G1_NOR_050_051_2026_11_12.md`. No QABC/key/HTML/APK/main changes, PR Draft not merged, independent source QA NOT_RUN.

## 2026-11-12 | Avengers Academy: NOR051 terminology-led domestic context and cable power caution
- User gave interpretation `electrocasnic monofazat >2kW` implies domestic socket circuit, supporting stored A=2.5mm²Cu; B violates min for socket, C imports aluminum4mm² from force row. We crosschecked exact I7-2011 §5.4.7 domestic >2kW separate socket and Annex5.32 row1.2 Cu2.5/Al blank against manufacturer cable sizing methodology.
- **Do not promote** hypothetical 1.5mm²Cu=2.3kW universal limit, 2.5mm²Cu=3.6–4.6kW universal, or arbitrary 50% load rule: I7 Iz depends on method/temperature/grouping/insulation etc. `electrocasnic` supplies context but not proof of universal plug connection; if explicitly hardwired, different source row required.
- Gemini integration: plugin directory search `Gemini` no matching connector; no Gemini API called, no second model verdict invented. Source-based independent Schneider text used as engineering crosscheck, not independent answer reviewer.
- Saved `QA_RULES/ELECTROCASNIC_CONTEXT_VS_CABLE_AMPACITY_NOR051_2026_11_12.md`, `tools/qa_electrocasnic_context.mjs`, `tools/tests/qa_electrocasnic_context.test.mjs`; 10/10 deterministic JS synthetic fixtures passed. Source edition and expert QA still open, learner status NO. Original QABC/key/HTML/APK not modified; no merge.
