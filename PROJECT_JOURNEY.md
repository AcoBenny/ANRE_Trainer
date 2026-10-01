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
