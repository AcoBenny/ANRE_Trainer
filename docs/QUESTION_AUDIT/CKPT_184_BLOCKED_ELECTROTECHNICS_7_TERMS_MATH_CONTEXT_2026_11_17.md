# CKPT-184 | Seven existing blocked electrotechnics cases: exact QABC, cross-grade readback, source/mathematical QA | 2026-11-17

## Continuity and QA scope
Continue after CKPT-181–183 from existing 568/568 source-scope phase. **Seven pre-existing unique units, not new question credit.** Original source: CKPT-141 and CKPT-144, with exact 822-ID canonical V73 crosscheck. Role-based analysis source/electrotechnics/linguistics done within a **single assistant**, **not genuine independent agents**. No changes to original QABC, answer keys, HTML, APK, release ledger, main. PR #7 remains Draft.

## Seven evidence cards

### G1-ELE-014 | TERM_NOT_UNIQUE
- Stable unit: `AU-2c324f18fe2143ed`; QABC sha256 `2c324f18fe2143eda69d82af02e0984302bbfe8ef1de09f7ee83eb628a91a464`; grade-ID members: G1-ELE-014, G2-ELEC-166; **original keys preserved**: G1-ELE-014=C, G2-ELEC-166=C.
- **Original question:** Câmp fără surse este
- **A:** numai un câmp de curenţi de conducţie în regim staţionar
- **B:** câmpul electric
- **C:** câmpul de inducţie electromagnetică
- **Technical and ABC/linguistic assessment:** A describes a conduction-current field, not necessarily solenoidal as named; B electric field may have electric-charge sources (Gauss-electric); C is compatible with source-free *magnetic induction field B* because div(B)=0, but wording «câmp de inducţie electromagnetică» is not technically identical to B without course definition.
- **Direct or indexed source:** OpenStax University Physics vol2 §16.1, Gauss laws E and B. https://openstax.org/books/university-physics-volume-2/pages/16-1-maxwells-equations-and-electromagnetic-waves
- **Exam intended interpretation:** C intended under B magnetic-flux interpretation. **Blocking condition:** No unique answer can be certified until original Romanian course terminology binds «câmp de inducție electromagnetică» to magnetic induction B.
- `approved_for_learning=NO`; independent source/technical/linguistic QA = NOT_RUN; official ANRE exam key, grade edition = NOT_VERIFIED.

### G1-ELE-029 | ONLY_INDUCTION_COUNTEREXAMPLE
- Stable unit: `AU-74e7f2339e0faf2e`; QABC sha256 `74e7f2339e0faf2eec3c25b87291eeefffec562a4afed2db59e12f861e6cbb44`; grade-ID members: G1-ELE-029, G2-ELEC-178; **original keys preserved**: G1-ELE-029=C, G2-ELEC-178=C.
- **Original question:** Curentul electric alternativ poate fi produs numai prin fenomene:
- **A:** termice
- **B:** chimice
- **C:** de inducţie electromagnetică
- **Technical and ABC/linguistic assessment:** A thermal effect alone does not describe a self-oscillating output; B electrochemical source is commonly DC; C electromagnetic induction generates AC in alternators, but «numai» is contradicted by power electronic DC–AC inverters.
- **Direct or indexed source:** US Department of Energy inverter page explicitly explains DC-to-AC switching: https://www.energy.gov/cmei/systems/solar-integration-inverters-and-grid-services-basics
- **Exam intended interpretation:** C intended for alternator, but statement false as universal. **Blocking condition:** Physics counterexample explicitly defeats «numai»; question cannot be learner-certified as universally correct without declared model (electromechanical generation only) or official key provenance.
- `approved_for_learning=NO`; independent source/technical/linguistic QA = NOT_RUN; official ANRE exam key, grade edition = NOT_VERIFIED.

### G1-ELE-043 | NO_DIRECT_LINEAR_PROPORTIONALITY
- Stable unit: `AU-61b27d9384e3d14f`; QABC sha256 `61b27d9384e3d14f6fe84793dd88cd8fe83a9ec1bf6deb5c784d8d1406b8cb41`; grade-ID members: G1-ELE-043, G2-ELEC-189; **original keys preserved**: G1-ELE-043=A, G2-ELEC-189=A.
- **Original question:** Curentul din circuitul statoric al unui generator crește direct proporţional:
- **A:** cu tensiunea între faze
- **B:** numai cu puterile active generate
- **C:** cu puterile reactive generate
- **Technical and ABC/linguistic assessment:** A at constant P and Q gives I inversely proportional to voltage U; B word «numai» P excludes Q and U; C reactive power Q changes current magnitude by sqrt(P²+Q²), not generally directly proportional when P≠0.
- **Direct or indexed source:** Schneider Electrical Installation Guide «Definition of reactive power», 3φ S=√3 U I, P=S cos φ, Q=S sin φ. https://www.electrical-installation.org/enwiki/Definition_of_reactive_power
- **Exam intended interpretation:** No unique linear answer under generic P,Q,U. **Blocking condition:** Derive I=√(P²+Q²)/(√3 U) for balanced sinusoidal 3-phase. Without fixed constraints and a model, none of A/B/C universally linear.
- `approved_for_learning=NO`; independent source/technical/linguistic QA = NOT_RUN; official ANRE exam key, grade edition = NOT_VERIFIED.

### G1-ELE-057 | HARMONIC_OVERLAPPING_PERIOD_RATIOS
- Stable unit: `AU-84185dba0d7b87f1`; QABC sha256 `84185dba0d7b87f1af2bd7bce9a59ccfeabe83f8f278afb8a842419a491ac1d4`; grade-ID members: G1-ELE-057, G2-ELEC-203; **original keys preserved**: G1-ELE-057=A, G2-ELEC-203=A.
- **Original question:** Două funcţii periodice sinusoidale sunt armonice între ele dacă:
- **A:** raportul perioadelor lor este un număr întreg oarecare
- **B:** au aceeaşi perioadă
- **C:** raportul perioadelor lor este egal cu 1/2
- **Technical and ABC/linguistic assessment:** A an integer ratio of periods can describe harmonically related frequencies if the numerator/order is clarified; B same period is n=1 harmonic/fundamental in many conventions; C T1/T2=1/2 means doubled frequency, the second harmonic. Hence options overlap depending definition of harmonic vs first/fundamental and ratio order.
- **Direct or indexed source:** Tektronix AC power measurements harmonics describe integer multiples; https://www.tek.com/en/documents/application-note/fundamentals-ac-power-measurements
- **Exam intended interpretation:** A traditional intended but B/C overlap. **Blocking condition:** Exact A/C/B all can reflect a harmonic family, no unique answer proven. Require exact intended theoretical definition and explicit distinction between 'first harmonic' and a 'higher harmonic'.
- `approved_for_learning=NO`; independent source/technical/linguistic QA = NOT_RUN; official ANRE exam key, grade edition = NOT_VERIFIED.

### G1-ELE-222 | SUSCEPTANCE_NOT_GENERIC_INVERSE_REACTANCE
- Stable unit: `AU-ca89b1b43e098b0f`; QABC sha256 `ca89b1b43e098b0ffaab1dc9a6b5c1c5531b718e9de96097b8dd7b5975474e4b`; grade-ID members: G1-ELE-222, G2-ELEC-358; **original keys preserved**: G1-ELE-222=C, G2-ELEC-358=C.
- **Original question:** Susceptanţa unui circuit de curent alternativ sinusoidal este inversul:
- **A:** impedanţei
- **B:** rezistenţei
- **C:** reactanţei
- **Technical and ABC/linguistic assessment:** A 1/Z is admittance Y, not susceptance alone; B 1/R equals conductance only for pure R; C susceptance is not generally 1/X because Z=R+jX => Y=(R-jX)/(R²+X²), and ImY=-X/(R²+X²). In the B-positive-inductive convention Y=G-jB, B=X/(R²+X²), reducing to 1/X only for R=0.
- **Direct or indexed source:** Electrical Engineering Portal «Admittance» exact equations and sign convention: https://electrical-engineering-portal.com/resources/knowledge/admittance
- **Exam intended interpretation:** C only if pure-reactance model and sign convention clarified. **Blocking condition:** Current imported key C has an intended simplified basis, not universal truth; don't replace or release absent course convention and independent review.
- `approved_for_learning=NO`; independent source/technical/linguistic QA = NOT_RUN; official ANRE exam key, grade edition = NOT_VERIFIED.

### G1-ELE-231 | REAL_QUANTITY_EXCLUSIVITY_FALSE
- Stable unit: `AU-62bf06e215a53d51`; QABC sha256 `62bf06e215a53d515b113a3db53be336c076bcef6b76f8d2890c380152205b59`; grade-ID members: G1-ELE-231, G2-ELEC-367; **original keys preserved**: G1-ELE-231=B, G2-ELEC-367=B.
- **Original question:** Singurele mărimi fizice reale în curent alternativ sunt:
- **A:** mărimile efective de curent sau de tensiune
- **B:** mărimile instantanee de curent sau de tensiune
- **C:** valorile medii de curent sau de tensiune
- **Technical and ABC/linguistic assessment:** A RMS is measurable by heating-equivalent effect and physically meaningful, though derived from instantaneous waveform; B instantaneous i(t),u(t) are directly physical; C time-averages over defined intervals are legitimate, but sinusoidal full-cycle mean may be zero. «Singurele» implies falsely that RMS cannot be real.
- **Direct or indexed source:** Tektronix «Fundamentals of AC Power Measurements», RMS and average sections: https://www.tek.com/en/documents/application-note/fundamentals-ac-power-measurements
- **Exam intended interpretation:** B instantaneous intended, «singurele» unsupported. **Blocking condition:** Keep distinction instantaneous vs derived RMS/mean but not assert latter 'unreal'; formal course definition of «reale» and what a period-averaged zero means required.
- `approved_for_learning=NO`; independent source/technical/linguistic QA = NOT_RUN; official ANRE exam key, grade edition = NOT_VERIFIED.

### G2-ELEC-290 | DIMENSIONAL_ERROR_GAMMA_VS_GAMMA_L
- Stable unit: `AU-fd7d308698e05c41`; QABC sha256 `fd7d308698e05c41dc3a89c322bbd1e51748505c537a7bef5dab80986d518bca`; grade-ID members: G2-ELEC-290; **original keys preserved**: G2-ELEC-290=A.
- **Original question:** Mărimea adimensională care reprezintă variaţia pe care o suferă amplitudinea şi faza undei de tensiune sau curent când parcurge 1 km de linie (lungă ) se numeşte:
- **A:** constanta de propagare a liniei
- **B:** constanta de atenuare a liniei
- **C:** constanta de distorsiune a liniei
- **Technical and ABC/linguistic assessment:** A γ=α+jβ represents per-unit-length attenuation and phase, yes name is propagation constant; B α covers attenuation but not phase; C «distorsiune» is not the complex propagation γ. However γ has units 1/length and γ·1km is dimensionless.
- **Direct or indexed source:** Engineering LibreTexts 2.2 «Transmission Line Characteristics» γ in m^-1; https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/02%3A_Transmission_Lines/2.02%3A_Transmission_Line_Characteristics; IEEE Technology Navigator https://technav.ieee.org/topic/propagation-constant/
- **Exam intended interpretation:** A term propagation constant, qualifier adimensional false. **Blocking condition:** Original statement asserts γ itself «adimensională», which conflicts with textbooks. Qualifier is flawed even though imported A is the intended named entity. Direct LibreTexts open failed cache miss; search excerpt exact units plus IEEE index used, limit noted.
- `approved_for_learning=NO`; independent source/technical/linguistic QA = NOT_RUN; official ANRE exam key, grade edition = NOT_VERIFIED.

## Data QA / gates / handoff
- Strict readback of **7/7 original unique unit cards and 13/13 individual grade-ID entries** against all 822 canonical V73 rows: exact question, A/B/C text and original key, 0 discrepancies. Verified original unit IDs and SHA field syntax by reusing CKPT-141/144 original sources; no hash recomputation, no claim of cryptographic rehash.
- Context/scope differences deliberately maintained: AC alternator vs power-electronics inverter; magnetic induction vs generic 'induction electromagnetic field'; 3φ balanced sine vs unconstrained generator; pure reactance vs generic R+jX; source propagation constant γ vs dimensionless product γL; RMS physical vs instantaneous vs average.
- 7 cases remain formally **BLOCKED_FINAL_SIGNOFF** (not 7 learner-approved); no nonindependent simulation masquerading as distinct reviewers. 2026 exam bibliographic source and official original grading key NOT_VERIFIED. **No canonical changes.**
- Next priority: other existing blocked ELE cases in CKPT-141/142/145/148/153, especially risk of motor/transformer source transfer and GIS schematic-dependent options. Do not infer switching procedure from generic schematics. CKPT-182 (10 I7) + CKPT-183 (6 I7) + this (7 ELE) = **23 distinct pre-existing units with fresh adjudication notes** this turn, plus separate prior CKPT-181 (NOR066/NOR094) from previous turn. Counts are QA passes, not certified resolutions of 50.
