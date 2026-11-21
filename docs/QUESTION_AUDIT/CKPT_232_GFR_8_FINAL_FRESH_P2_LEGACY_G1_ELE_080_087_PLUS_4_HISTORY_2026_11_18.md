# CKPT-232 | GFR 8 final new Grade I legacy P2 preliminaries, plus four historical disjoint checks | 2026-11-18

## Scope / hard distinction
- Exact QABC and imported keys copied from [V73] Git blob `c027d417a8e4e605c830b2016fb55b099b8d130b`, workbook `ELECTROTEHNICA-09.2024-2.xlsx`. Eight **new focused** unit source cards below, each same exact QABC/key in Grade II; 4 other Grade I P2 legacy cases already examined in CKPT-184/189/217 and are **historical crossrefs only**. No 2026 official ANRE exam key, independent reviewer or training release gate satisfied.
- Sources: OpenStax physics, NIST dimensional units/period, equipment/training engineering, official I7 safety, IEC transformer loading guide index **without full standard access**. Protect copyright, do not copy a paywalled IEC standard. No field instructions, no app changes.

### G1-ELE-080 | DIRECT_LONG_PARALLEL_WIRE_FORCE_1_OVER_R
- Original: Forţa electrodinamică exercitată între două conductoare filiforme, paralele, lungi, aflate la distanţa r, străbătute de câte un curent:
- A: este direct proporţională cu distanţa r dintre conductoare
- B: este invers proporţională cu distanţa r dintre conductoare
- C: nu depinde de distanţa r dintre conductoare
- Imported key **B** unchanged; original workbook ELECTROTEHNICA-09.2024-2.xlsx:87; Grade II exact QABC/key counterpart G2-ELEC-225.
- A/B/C and conditions: For long parallel wires F/ℓ=μ0 I1 I2/(2πr), so B inversely proportional to r. A directly proportional and C independent of r false. Assumes equal fixed currents and separation r, long thin parallel wires in homogeneous nonmagnetic medium; not generic short/angled wires.
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/12-3-magnetic-force-between-two-parallel-currents
- Gate: `DIRECT_LONG_PARALLEL_WIRE_FORCE_1_OVER_R`, `official_current_ANRE_exam_key=NOT_VERIFIED`, `independent_technical_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-081 | DIRECT_ELECTRIC_FIELD_FORCE
- Original: Forţa F care se exercită asupra unei sarcini electrice q aflată într-un câmp electric de intensitate E are expresia:
- A: F=E/q
- B: F=qE
- C: F=q/E
- Imported key **B** unchanged; original workbook ELECTROTEHNICA-09.2024-2.xlsx:88; Grade II exact QABC/key counterpart G2-ELEC-226.
- A/B/C and conditions: Electric field E defined by F=qE on test charge; B. A E/q and C q/E do not give force dimensions; vector direction for negative q reversed, magnitude |q|E.
- Technical source: https://openstax.org/books/university-physics-volume-2/pages/5-4-electric-field
- Gate: `DIRECT_ELECTRIC_FIELD_FORCE`, `official_current_ANRE_exam_key=NOT_VERIFIED`, `independent_technical_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-082 | DIRECT_PERIOD_FREQUENCY_RECIPROCAL
- Original: Frecvenţa unei mărimi periodice este inversul:
- A: amplitudinii
- B: perioadei
- C: fazei
- Imported key **B** unchanged; original workbook ELECTROTEHNICA-09.2024-2.xlsx:89; Grade II exact QABC/key counterpart G2-ELEC-227.
- A/B/C and conditions: Frequency f=1/T in Hz (1/s), B inverse period. A amplitude inverse dimensionally wrong, C phase inverse unrelated frequency. No need to assume sinusoid, applies any periodic parameter.
- Technical source: https://www.nist.gov/pml/time-and-frequency-division/popular-links/time-frequency-z/time-and-frequency-z-f
- Gate: `DIRECT_PERIOD_FREQUENCY_RECIPROCAL`, `official_current_ANRE_exam_key=NOT_VERIFIED`, `independent_technical_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-083 | DIRECT_INDUCTION_WATTHOUR_EDDY_CURRENT
- Original: Funcţionarea contoarelor de inducţie are la baza:
- A: curenţii turbionari
- B: efectul termic al curentului electric
- C: forţa electrostatica
- Imported key **A** unchanged; original workbook ELECTROTEHNICA-09.2024-2.xlsx:90; Grade II exact QABC/key counterpart G2-ELEC-228.
- A/B/C and conditions: Legacy induction electricity meter has rotating conductive disk with induced eddy currents generating meter driving torque and electromagnetic braking, so A. B thermal effects and C electrostatic force not meter induction operating principle. Does not describe digital/static electronic meter, but original explicitly says induction type.
- Technical source: https://www.eit.edu.au/resources/fundamentals-of-smart-metering-kwh-and-kvarh-meters/
- Gate: `DIRECT_INDUCTION_WATTHOUR_EDDY_CURRENT`, `official_current_ANRE_exam_key=NOT_VERIFIED`, `independent_technical_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-084 | DIRECT_EARTHING_SHOCK_PROTECTION_PURPOSE
- Original: În instalaţiile de joasa tensiune, legarea la pământ este justificatã:
- A: din motive economice
- B: pentru diminuarea suprasolicitărilor echipamentelor electrice
- C: pentru securitatea muncii
- Imported key **C** unchanged; original workbook ELECTROTEHNICA-09.2024-2.xlsx:91; Grade II exact QABC/key counterpart G2-ELEC-229.
- A/B/C and conditions: Low voltage safety grounding/PE and equipotential bonding primarily protects people/animals against electric shock under fault, so C. A purely economics not basis, B limiting equipment stress can be ancillary function but not core protection claim. Need distinguish earthing, bonding, disconnection and network TN/TT/IT details from generic one-line purpose.
- Technical source: https://legislatie.just.ro/Public/DetaliiDocument/286763
- Gate: `DIRECT_EARTHING_SHOCK_PROTECTION_PURPOSE`, `official_current_ANRE_exam_key=NOT_VERIFIED`, `independent_technical_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-085 | CONDITIONAL_TEMPORARY_TRANSFORMER_OVERLOAD
- Original: Funcţionarea în suprasarcinã a unui transformator reprezintă:
- A: un regim de avarie
- B: un regim temporar admisibil
- C: un regim inadmisibil
- Imported key **B** unchanged; original workbook ELECTROTEHNICA-09.2024-2.xlsx:92; Grade II exact QABC/key counterpart G2-ELEC-230.
- A/B/C and conditions: Transformer can tolerate short/limited overload based on ambient, prior load, thermal rise, aging and protection settings, so B `regim temporar admisibil` in supervised conditions. A all overload automatically fault false, C all prohibited false. Does NOT authorize unbounded overload or guarantee safe without transformer loading guide. Specific regime dry vs immersed, IEC 60076-7/12 applicability must be checked.
- Technical source: https://www.iteh.fr/catalog/standards/iec/924f42fe-e556-4197-b0fd-ca0cd3c56f58/iec-60076-7-2005
- Gate: `CONDITIONAL_TEMPORARY_TRANSFORMER_OVERLOAD`, `official_current_ANRE_exam_key=NOT_VERIFIED`, `independent_technical_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-086 | DIRECT_ELECTROMAGNETIC_INDUCTION_TRANSFORMER
- Original: Funcţionarea transformatoarelor electrice are la bazã:
- A: fenomenul inducţiei electromagnetice
- B: efectul termic al curentului electric
- C: curenţii turbionari
- Imported key **A** unchanged; original workbook ELECTROTEHNICA-09.2024-2.xlsx:93; Grade II exact QABC/key counterpart G2-ELEC-231.
- A/B/C and conditions: AC transformer works mutual electromagnetic induction from changing magnetic flux A. B thermal effect is loss, C eddy currents are mostly parasitic core losses (not principle of intended winding transfer). Constant DC steady state gives no normal secondary induced voltage.
- Technical source: https://openstax.org/books/college-physics-2e/pages/23-7-transformers
- Gate: `DIRECT_ELECTROMAGNETIC_INDUCTION_TRANSFORMER`, `official_current_ANRE_exam_key=NOT_VERIFIED`, `independent_technical_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-087 | DIRECT_NIST_SI_HENRY_UNIT
- Original: Henry este unitatea de măsură pentru:
- A: fluxul magnetic
- B: inductanţă
- C: inducţia magnetică
- Imported key **B** unchanged; original workbook ELECTROTEHNICA-09.2024-2.xlsx:94; Grade II exact QABC/key counterpart G2-ELEC-232.
- A/B/C and conditions: SI derived unit henry H measures inductance B. A magnetic flux measured weber Wb; C magnetic flux density (magnetic induction B) tesla T. Dimensional H=V·s/A.
- Technical source: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes
- Gate: `DIRECT_NIST_SI_HENRY_UNIT`, `official_current_ANRE_exam_key=NOT_VERIFIED`, `independent_technical_QA=NOT_RUN`, `approved_for_learning=NO`.

## Four previously reviewed case-source references: zero newly certified units
### G1-ELE-014 ↔ G2-ELEC-166: TERM_NOT_UNIQUE
- Original QABC: Câmp fără surse este | A: numai un câmp de curenţi de conducţie în regim staţionar | B: câmpul electric | C: câmpul de inducţie electromagnetică. Imported key **C**, unchanged.
- Historical source audit `CKPT_184_BLOCKED_ELECTROTECHNICS_7_TERMS_MATH_CONTEXT_2026_11_17.md`; Source-free B induction interpretation vs ambiguous Romanian term. This is a reference to previously performed analysis, **not another independent technical QA pass**, learner approval NO.
### G1-ELE-051 ↔ G2-ELEC-197: PASSIVITY_NOT_SUFFICIENT_RECIPROCITY
- Original QABC: Dacă o tensiune electromotoare E, montată în latura AB a unei reţele pasive, produce în latura CD a reţelei un curent I, montarea t.e.m. E în latura CD va produce în latura AB: | A: un curent - (minus) I | B: un curent I | C: un curent I/2. Imported key **B**, unchanged.
- Historical source audit `CKPT_189_NEXT5_BLOCKED_RECIPROCITY_OHM_MAGNETISM_MANEUVERS_2026_11_17.md`; Passive bilateral network assumption omitted; nonreciprocal passive gyrator counterexample. This is a reference to previously performed analysis, **not another independent technical QA pass**, learner approval NO.
### G1-ELE-053 ↔ G2-ELEC-199: TWO_PHASE_TRANSFORMER_CONDITIONALLY_EFFECT
- Original QABC: Funcţionarea în doua faze a unui transformator trifazat are ca efect: | A: supraîncălzirea acestuia | B: suprasarcina | C: reducerea puterii tranzitate. Imported key **A**, unchanged.
- Historical source audit `CKPT_217_GFR_7_P1_GRADEII_TECHNICAL_QABC_FAULTS_REACTOR_GIS_2026_11_18.md`; Single-phase loss may overheat or cause other effects; not unique without connection/loading. This is a reference to previously performed analysis, **not another independent technical QA pass**, learner approval NO.
### G1-ELE-057 ↔ G2-ELEC-203: HARMONIC_OPTIONS_OVERLAP
- Original QABC: Două funcţii periodice sinusoidale sunt armonice între ele dacă: | A: raportul perioadelor lor este un număr întreg oarecare | B: au aceeaşi perioadă | C: raportul perioadelor lor este egal cu 1/2. Imported key **A**, unchanged.
- Historical source audit `CKPT_184_BLOCKED_ELECTROTECHNICS_7_TERMS_MATH_CONTEXT_2026_11_17.md`; A generic integer ratio, B same fundamental and C half ratio may overlap harmonics. This is a reference to previously performed analysis, **not another independent technical QA pass**, learner approval NO.

## Audit totals and next
- New source-focused original QABC: **8**; associated exact grade I/II occurrences up to 16 (not separate verification). Previously reviewed historical Grade I references 4, not new units. Count gate 0 key changes, 0 release approvals.
- Future GFR next must address remaining **P2 previous-model or crossgrade reuse** question units, not mark entire 822 as validated by inherited notes. Historical contradictions remain in dedicated blocked queue. 
