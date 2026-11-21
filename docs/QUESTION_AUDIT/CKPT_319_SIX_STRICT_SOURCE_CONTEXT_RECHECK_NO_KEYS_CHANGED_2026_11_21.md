# CKPT-319 | Six strict QABC disputes: source-context recheck, no answer-key changes | 2026-11-21

## Scope, provenance and safety
- Parent HEAD: `1124139c3e0ffa4d1163bcdb1565a615ed185c03` on `audit/anre-v8-priority-17-20261109`. PR #7 stays **Draft**; never merge here.
- Reconciled from V240 (all four ANRE-vs-Trainer material variants), V201 (two cross-grade key conflicts), V241 (568 unique QABC / 822 grade IDs), and CKPT-318 (40 layer structural audit).
- **New activity in this checkpoint:** reopened 2011 I7 source context around §§5.4.12–5.4.14 and §§5.5.2.1–5.5.3, independently inspected contemporary ANRE page listing source workbooks, checked technical references for propagation constants and electrostatic induction, and revisited NTE009 operational state context. These are same-assistant researches, NOT expert independent QA or official exam-key authentication.
- ANRE's current electrician page lists named downloads `ELECTROTEHNICA-09.2024`, `NORME TEHNICE Gr. 1-05.2023`, and `Tematica si bibliografie ... 2023`; *this fact by itself does not prove 2026 source applicability or official scored answers*. https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/
- The ANRE XLSX downloads could not be read directly by the web reader (binary XLSX content unsupported). Original question/ABC versions for this checkpoint therefore remain grounded in prior V240/V201 provenance; **not freshly reauthenticated from the downloadable workbook here**.
- Governmental Portal Legislativ direct URLs `https://legislatie.just.ro/Public/DetaliiDocument/286763`, `https://legislatie.just.ro/Public/DetaliiDocumentAfis/287132` and `https://legislatie.just.ro/Public/DetaliiDocument/271142` returned HTTP 502 this session. The 2011 original text below was crosschecked against a publicly available Monitorul Oficial 802 bis PDF from BJC and the LegisRO HTML reproduction. **The applicability of later modifications and exact 2026 edition remains unverified.**
- The agreed card format from `QA_RULES/CARD_SOURCE_CONTEXT_BEFORE_HIGHLIGHT_AFTER_APP_REQUIREMENT_2026_11_21.md` remains a future implementation requirement, NOT implemented by this checkpoint. Where available, specify neighboring section locators before/focus/after; never manufacture quoted context.

## Case-by-case technical + linguistic recheck

### QABC-0362 / G1-NOR-048 | version-mutated A and C | HIGH
- Original A: only direct from distribution board; original B: only normal lighting circuit; original C: from socket circuit. Imported Trainer key `A` is **not transferable** to those original alternatives. Trainer A enumerates three methods; Trainer C changes to only socket circuit.
- I7 2011 **§5.4.13** explicitly admits **normal lighting OR socket circuit OR directly from board**. Both original A and B fail the exclusive «numai» qualifier, while original C describes one allowed method without claiming exclusivity. Source original: **C technically supported for the 2011 text**. Trainer A technically supported for the *mutated* set.
- Context window: **before §5.4.12** (restrictions on circuits traversing certain environments), **focus §5.4.13** (three bell feeding routes), **after §5.4.14** (multiple circuits within same protective element). Near-neighbor text does NOT narrow the three routes to one.
- Text witnesses: https://new.bjc.ro/wp-content/uploads/2024/07/normativ-i7-2011-instalatii-electrice.pdf (Monitorul Oficial 802 bis/2011, §5.4.13) ; https://legis.medleg.ro/legislatie/2011-reglementari-reglementare-tehnica-3 (HTML reproduction). Gate: original 2026 exam-key authenticity + exact effective edition + independent source and linguist review **NOT DONE**. No key change.

### QABC-0386 / G1-NOR-072 | version-mutated B | HIGH
- Original B allows easy disconnection **without a tool**. Trainer's B requires individually disconnectable, secure connection, removable **only using a tool**; original C requires individual disconnection. Imported `B` corresponds to Trainer's altered text, not original B.
- I7 2011 **§5.5.2.3** requires each conductor attached to main earth bar to be individually disconnectable, and the connection to be safely disconnectable only using a tool. Original B contradicts source condition; original C is true but less complete. Trainer B is fully descriptive while Trainer C stays also literally true (subset), a **non-unique true-option trap**.
- Context window: **before §§5.5.2.1–5.5.2.2** (main bar conductors, distinction between direct and via main protection conductors), **focus §5.5.2.3**, **after §5.5.3 heading** (protection conductors). Key disambiguation: not every PE is individually routed directly to bar, but every *conductor actually attached to bar* is individually disconnectable under §5.5.2.3.
- Text witnesses: https://new.bjc.ro/wp-content/uploads/2024/07/normativ-i7-2011-instalatii-electrice.pdf (Monitorul Oficial 802 bis/2011, §5.5.2.3); https://legis.medleg.ro/legislatie/2011-reglementari-reglementare-tehnica-3 . Gate: original 2026 key proof and amendment check + independent source/linguist review **NOT DONE**. No key change.

### QABC-0143 / G1-ELE-152 | mutated question adjective | HIGH
- Source original stem uses «mărimea adimensională», Trainer changes to «mărimea caracteristică». Both retain A «constanta de propagare a liniei», B attenuation, C distortion.
- For a linear line, propagation constant `γ = α + jβ` has dimension inverse length, `m^-1`. The product `γ·l` is dimensionless, not `γ`. The original adjective makes the literal claim technically false; A captures intended concept only after rejecting the defective adjective. A in Trainer is consistent with standard theory.
- Source reopen: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Fundamentals_of_Microwave_and_RF_Design_%28Steer%29/03%3A_Transmission_Lines/3.02%3A_Transmission_Line_Theory ; source-original worksheet lineage V240.
- Before/focus/after card context cannot yet be represented as an **original ANRE normative quotation** from that third-party theory: source unit and definitions must be mapped to a real textbook section, not copied as an exam-key proof. Official key **NOT AUTHENTICATED**. No key change.

### QABC-0236 / G1-ELE-247, G2-ELEC-383 | mutated B induction type | HIGH
- Original B «prin inducție electromagnetică»; Trainer B «prin inducție electrostatică». They denote different mechanisms and may not be substituted in a verbatim original. Conductors placed in external static electric field redistribute surface charge; an isolated neutral conductor does **not** necessarily acquire a nonzero total net charge.
- Source reopen: OpenStax §5.2 (charging by induction and polarization) https://openstax.org/books/university-physics-volume-2/pages/5-2-conductors-insulators-and-charging-by-induction ; §6.4 (electrostatic equilibrium) https://openstax.org/books/university-physics-volume-2/pages/6-4-conductors-in-electrostatic-equilibrium .
- Original «se încarcă cu electricitate» adds a second ambiguity between charge separation and net charging; no original option has clear affirmative proof under the bare text. Trainer B is **supported for electrostatic polarization**, not unconditional net charging. Reopen V194 and V240; do not duplicate V194 or change keys.

### QABC-0017 / G1-ELE-018, G2-ELEC-170 | same original, conflicting imported A vs C | HIGH
- Original symmetric air line C12=C23=C31=C, no ground; A=3C, B=C/3, C=C. Grade I imported A, Grade II imported C.
- From the specified balanced three-phase delta of mutual phase-to-phase capacitors: `q_a=C(V_a-V_b)+C(V_a-V_c)`; since `V_a+V_b+V_c=0`, `q_a=3CV_a`. Therefore the star-equivalent phase capacitance is `3C` **if «capacitatea de serviciu» means that star-equivalent phase capacitance**. This direct algebra supports candidate A, not an authenticated ANRE key for the original undefined term.
- Outstanding gate: authoritative exact definition of `capacitate de serviciu Cs` for this ANRE line model, original equation, and official grade-specific scored key or formal error adjudication. Previous V201 rationale preserved; neither key changed.

### QABC-0094 / G1-ELE-102, G2-ELEC-245 | same original, conflicting imported A vs C | HIGH
- Double-busbar / single breaker per circuit. G1=A (one busbar energized, other cold standby), G2=C (both buses energized, bus coupler warm standby). «De preferat» is normative preference that must be justified by an explicitly scoped operation/design rule, not an automatically universal truth.
- Reopened reproduced NTE009/10/00 operative states: **warm reserve** of coupler has disconnectors closed and breaker open; **cold reserve** has disconnectors open. The document repeatedly refers to «schema normală de funcționare» and differences from that scheme. These definitions do NOT alone prove universally preferable A or C for all stations.
- Sources: https://legis.medleg.ro/legislatie/2010-regulament-general-manevre-2 ; https://lexapp.ro/just/122751 ; V201 existing exact original and two imported keys.
- Outstanding gate: exact dedicated design/operating preference source, official version and exam answer-key reconciliation. Do not infer preferred option merely from NTE's definitions. Neither key changed.

## Evidence limitations and handoff
- All 6 strict IDs remain inside the existing **136** semantic-hold union, not additive.
- This source-context pass **improves the pinpointed evidence and negative-case explanations** but is performed by the same assistant: **0/822 independently approved**. Structural PASS does not amount to source/answer validation.
- Independent qualified electrical and linguistic audit: **NOT_RUN**. Exact applicability of exam bibliography/edited norms to a 2026 examination: **NOT_AUTHENTICATED**. Source keys for original ANRE workbook: **NOT_AUTHENTICATED**.
- No original question, alternatives, imported key, HTML, APK, teacher card text, or manifest touched by this checkpoint. It writes only this audit document.
- Next pass: prioritize remaining 130 uniquely held QABC IDs, then review the other 432; preserve full source window before/focus/after at final display-integration time and do not treat third-party theory paraphrase as verbatim I7 evidence.
