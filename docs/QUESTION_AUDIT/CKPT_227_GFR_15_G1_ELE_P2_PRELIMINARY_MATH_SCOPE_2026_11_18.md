# CKPT-227 | GFR 15 PRELIMINARY P2 Grade I electrotechnics original QABC and model scope | 2026-11-18

## Governance
- Selected exactly 15 **existing** G1 P2 technical IDs whose last status in V106 was `PREVIOUS_INDIVIDUAL_PRELIMINARY_NO_SIGNOFF` and `NO_FOCUSED_RECHECK_RECORDED`. Source canonical V73 Git blob `c027d417a8e4e605c830b2016fb55b099b8d130b`.
- Technical-source and mathematical review with exact A/B/C negative alternatives and stated model limitations. External source URLs are public source material, not authenticated 2026 ANRE official scoring key. **One assistant**, not independent AI/human judges; reference quality differentiated. Already investigated G1-ELE-005 and G1-ELE-014 excluded to avoid redundant work.
- No original answer key, question, choice order, source HTML/APK/main, PR merge or release changed. **No question is learner-approved**.

### G1-ELE-001 | CONDITIONAL_NETWORK_VOLTAGE_RISE
- Original: Atunci când se compensează energia electrica reactiva prin baterii de condensatoare, tensiunea în reţeaua electrica:
- A: scade
- B: nu se modifica
- C: creste
- Imported key **C** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `8`. Cross-grade exact QABC: G1-ELE-001=C, G2-ELEC-154=C.
- Source: https://standards.theiteh.com/catalog/standards/iec/fe890289-16a0-4863-846b-a5807cefda65/iec-61921-2017.
- A/B/C and model / wording test: Shunt capacitive reactive compensation may raise load-point voltage on inductive network, as IEC61921 text notes. A 'scade' not typical; B 'nu se modifica' not typical. C expected, but 'creste' not invariant at a strong voltage-controlled source or under regulation/overcompensation. Missing network/control assumptions.
- Gate: `CONDITIONAL_NETWORK_VOLTAGE_RISE`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-002 | DIRECT_PETERSEN_COIL_GROUND_FAULT
- Original: Bobinele de stingere din staţiile electrice de transformare sunt echipamente pentru:
- A: compensarea factorului de putere
- B: dotări PSI
- C: compensarea curenţilor capacitivi
- Imported key **C** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `9`. Cross-grade exact QABC: G1-ELE-002=C, G2-ELEC-155=C.
- Source: https://www.mdpi.com/2673-4826/4/2/7.
- A/B/C and model / wording test: Arc suppression coil in network neutral supplies inductive earth-fault current compensating capacitive network earth-fault current. A overall power-factor compensation not same object, B fire protection unrelated, C correct specific compensation. Nearby distinction: not a reactor whose purpose is short circuit current limitation.
- Gate: `DIRECT_PETERSEN_COIL_GROUND_FAULT`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-003 | DIRECT_MULTIPLE_MAGNETIC_FIELD_SOURCES
- Original: Câmpul magnetic poate fi produs:
- A: numai de magneţi permanenţi
- B: numai de electromagneţi
- C: de magneţi permanenţi si de electromagneţi
- Imported key **C** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `10`. Cross-grade exact QABC: G1-ELE-003=C, G2-ELEC-156=C.
- Source: https://openstax.org/books/university-physics-volume-2/pages/11-2-magnetic-fields-and-lines.
- A/B/C and model / wording test: Permanent magnets and energized electromagnets each generate field -> C. A and B say 'numai' and wrongly exclude other source. The list isn't physically exhaustive (moving charges, Earth magnetic field), so C means both listed, not 'only these'.
- Gate: `DIRECT_MULTIPLE_MAGNETIC_FIELD_SOURCES`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-004 | DIRECT_PARALLEL_CAPACITANCE_ARITHMETIC
- Original: 3 condensatoare având capacitatea C1=100 μF, C2=50 μF, C3=100 μF legate în paralel, au capacitatea echivalentă.
- A: 25 μF
- B: 250 μF
- C: 50 μF
- Imported key **B** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `11`. Cross-grade exact QABC: G1-ELE-004=B, G2-ELEC-157=B.
- Source: https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel.
- A/B/C and model / wording test: Parallel: Ceq=C1+C2+C3=100+50+100=250 microfarads -> B. A=25 and C=50 invalid; no unspecified coupling/parasites in ideal exercise.
- Gate: `DIRECT_PARALLEL_CAPACITANCE_ARITHMETIC`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-006 | DIRECT_AUTOMATIC_TRANSFER_CONTINUITY
- Original: AAR se utilizează în scopul:
- A: limitării curenţilor de scurtcircuit;
- B: creşterii continuităţii în alimentare;
- C: reducerii pierderilor de energie pe linii.
- Imported key **B** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `13`. Cross-grade exact QABC: G1-ELE-006=B, G2-ELEC-159=B.
- Source: https://www.eaton.com/us/en-us/products/low-voltage-power-distribution-control-systems/automatic-transfer-switches/automatic-transfer-switch-fundamentals.html.
- A/B/C and model / wording test: AAR automatic transfer to alternate supply improves continuity to loads when source fails -> B. A reactor/fault-current limitation not this device's purpose, C line I2R loss optimization not intended. Source is analogous ATS and not exact Romanian AAR acronym officially verified, mark terminology equivalence.
- Gate: `DIRECT_AUTOMATIC_TRANSFER_CONTINUITY`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-007 | CONDITIONAL_MOTOR_MODE_SLIP
- Original: Alunecarea s a unui motor asincron are valori:
- A: cuprinse între 1 si 0
- B: cuprinse între -1 si 0
- C: de regulă, mai mari decât 1
- Imported key **A** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `14`. Cross-grade exact QABC: G1-ELE-007=A, G2-ELEC-160=A.
- Source: https://mrcet.com/downloads/digital_notes/EEE/09022024/4.ELECTRICAL%20MACHINES-II%20DIGITAL%20NOTES.pdf.
- A/B/C and model / wording test: s=(ns-n)/ns; normal forward motoring 0<s<1 (at standstill =1), A intended. B negative slip corresponds induction generating and C >1 can occur plugging/braking; question omits 'in regim de motor obisnuit', so A not universal for all operation.
- Gate: `CONDITIONAL_MOTOR_MODE_SLIP`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-009 | CONDITIONAL_NETWORK_CONTROL_AND_THERMAL_RESISTOR
- Original: Care element nu se foloseşte la reglarea tensiunii în reţelele electrice:
- A: bobina de compensare
- B: transformatorul
- C: rezistorul
- Imported key **C** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `16`. Cross-grade exact QABC: G1-ELE-009=C, G2-ELEC-161=C.
- Source: https://openstax.org/books/college-physics-ap-courses/pages/23-11-reactance-inductive-and-capacitive.
- A/B/C and model / wording test: Reactors and transformer taps are standard network voltage control means A/B; ordinary series resistor is not an efficient preferred regulator of power network voltage, intended C. But resistance changes voltage drop in a circuit and can be used in special regulators/loads, so absolute 'nu se foloseste' needs network/device scope; source only directly supports reactance property, not a signed ANRE methods list.
- Gate: `CONDITIONAL_NETWORK_CONTROL_AND_THERMAL_RESISTOR`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-011 | DIRECT_CURRENT_LIMITING_REACTOR_INDUCTANCE
- Original: Bobinele pentru limitarea curenţilor de scurtcircuit au:
- A: rezistenta mare
- B: inductanţa mare
- C: inductanţa mica
- Imported key **B** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `18`. Cross-grade exact QABC: G1-ELE-011=B, G2-ELEC-163=B.
- Source: https://openstax.org/books/college-physics-ap-courses/pages/23-11-reactance-inductive-and-capacitive.
- A/B/C and model / wording test: Higher inductance increases reactance XL=2pi f L and limits short-circuit current at frequency f. B large L; A high resistance creates active loss and is not coil's preferred short-circuit limitation; C small L contradicts purpose. 'mare' relative to typical circuit impedance, no universal inductance numerical threshold.
- Gate: `DIRECT_CURRENT_LIMITING_REACTOR_INDUCTANCE`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-012 | DIRECT_ELECTROSTATIC_E_FIELD
- Original: Câmpul electrostatic este descris
- A: prin: intensitatea câmpului electric
- B: numai prin inducţia electrică
- C: inducţia magnetică
- Imported key **A** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `19`. Cross-grade exact QABC: G1-ELE-012=A, G2-ELEC-164=A.
- Source: https://openstax.org/books/college-physics/pages/18-4-electric-field-concept-of-a-field-revisited.
- A/B/C and model / wording test: E field vector intensity describes electrostatic field, A. B only electric induction D omits E and constitutive medium context; C magnetic induction B refers different physical field. Other electrostatic descriptors potential/charge exist so no assertion E is unique possible descriptor.
- Gate: `DIRECT_ELECTROSTATIC_E_FIELD`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-013 | CONDITIONAL_OIL_TRANSFORMER_INSTALLATION
- Original: Comparativ cu cele uscate, transformatoarele imersate prezintă :
- A: o bună rezistenţă la foc;
- B: risc crescut de poluare acustică a mediului ambiant;
- C: necesitatea unor amenajări speciale la instalare
- Imported key **C** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `20`. Cross-grade exact QABC: G1-ELE-013=C, G2-ELEC-165=C.
- Source: https://www.se.com/us/en/work/support/resources-and-tools/technical-faqs/.
- A/B/C and model / wording test: Oil-immersed transformers normally need oil containment, fire/environment management in suitable installations, making C expected. A better fire resistance false for combustible mineral oil vs dry construction; B noise risk not unique, depends specification. **Source linked is generic manufacturer FAQ, not an exact compared installation clause**; cannot claim normative verification from it. Preserve conditional until actual equipment/manual/standard clause located.
- Gate: `CONDITIONAL_OIL_TRANSFORMER_INSTALLATION`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-016 | DIRECT_JOULE_LAW_I_SQUARED
- Original: Cantitatea de căldura produsã la trecerea curentului electric printr-un conductor este:
- A: direct proporţională cu secţiunea conductorului
- B: direct proporţionala cu pătratul intensităţii curentului
- C: invers proporţionala cu rezistenta conductorului
- Imported key **B** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `23`. Cross-grade exact QABC: G1-ELE-016=B, G2-ELEC-168=B.
- Source: https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power.
- A/B/C and model / wording test: For resistor at fixed R and time t, heat Q=I^2 R t, B. A directly proportional to conductor area is false when fixed length/resistivity imply R~1/S; C inversely proportional to R is false under fixed I (but under fixed voltage Q=V^2t/R, so problem implicitly holds I fixed).
- Gate: `DIRECT_JOULE_LAW_I_SQUARED`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-017 | DIRECT_SERIES_CAPACITOR_CHARGE
- Original: Cantitatea de electricitate cu care se încarcă o baterie de n condensatoare montate în serie, fiecare de capacitate C, este:
- A: aceeaşi cu care se încarcă fiecare element component
- B: suma cantităţilor cu care se înarcă fiecare element în parte
- C: egală cu de două ori cantitatea de electricitate cu care se încarcă fiecare condensator
- Imported key **A** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `24`. Cross-grade exact QABC: G1-ELE-017=A, G2-ELEC-169=A.
- Source: https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel.
- A/B/C and model / wording test: In ideal series all n capacitors bear same charge magnitude Q, so battery equivalent charge same as component Q: A. B erroneously sums separate capacitor charges into terminal charge; C says 2x irrespective of n and false. Fixed terminal voltage yields Ceq=C/n, Q=CV/n.
- Gate: `DIRECT_SERIES_CAPACITOR_CHARGE`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-019 | DIRECT_SERIES_IDENTICAL_CAPACITORS
- Original: Capacitatea echivalentă a 2 condensatoare, fiecare având capacitatea C, montate în serie este egală cu:
- A: 2 C
- B: C/2
- C: C
- Imported key **B** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `26`. Cross-grade exact QABC: G1-ELE-019=B, G2-ELEC-171=B.
- Source: https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel.
- A/B/C and model / wording test: Two equal capacitors C in series 1/Ceq=1/C+1/C=2/C -> Ceq=C/2 B. A 2C is parallel result, C single capacitor.
- Gate: `DIRECT_SERIES_IDENTICAL_CAPACITORS`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-022 | CONDITIONAL_LINEAR_ISOTROPIC_D_E
- Original: Care dintre relaţiile următoare este adevărată:
- A: inducţia electrică = permitivitatea x intensitatea câmpului electric
- B: inducţia electrică = intensitatea câmpului electric/ permitivitate
- C: inducţia electrică=sarcina x intensitatea câmpului electric
- Imported key **A** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `29`. Cross-grade exact QABC: G1-ELE-022=A, G2-ELEC-174=A.
- Source: https://openstax.org/books/university-physics-volume-2/pages/8-1-capacitors-and-capacitance.
- A/B/C and model / wording test: Constitutive relationship D=epsilon E in linear isotropic uniform dielectric -> A. B inverse epsilon and C Q*E not dimensionally applicable. In nonlinear/anisotropic media D is function/tensor of E and free/bound polarization: no universal scalar epsilon. Source provides dielectric capacitance concept but not independent proof of general tensor formula.
- Gate: `CONDITIONAL_LINEAR_ISOTROPIC_D_E`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

### G1-ELE-027 | DIRECT_ELECTRIC_ENERGY_CALCULATED
- Original: Care este energia consumata de o rezistenta electrica r = 10 Ω, prin care trece un curent de 2 A timp de 10 ore:
- A: 200 Wh
- B: 400 Wh
- C: 800 Wh
- Imported key **B** preserved; original workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `34`. Cross-grade exact QABC: G1-ELE-027=B, G2-ELEC-176=B.
- Source: https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power.
- A/B/C and model / wording test: R=10ohm I=2A P=I^2R=4*10=40W; for t=10hours E=40*10=400Wh -> B. A=200 and C=800 inconsistent. A pure resistor constant current assumed.
- Gate: `DIRECT_ELECTRIC_ENERGY_CALCULATED`; edition `ANRE_2026_UNVERIFIED`; independent technical/linguistic/source review `NOT_RUN`; `approved_for_learning=NO`.

## Math test vectors / negative fixtures
- ELE004: 100+50+100=250 microF (parallel); false alternatives 25,50.
- ELE017: Q1=Q2=...=Qn for series ideal; terminal Q=C*V/n, not n times single charge.
- ELE019: 1/Ceq=2/C => Ceq=C/2 (not 2C).
- ELE016: Q=I²Rt, fixed I,R,t; current doubled => heating factor 4.
- ELE027: I²R=4*10=40W; 40W*10h=400Wh; 1Wh=3600J => 1.44MJ.

## Count and unclosed issues
- 15 existing *grade IDs*, verify distinct exact QABC and distinguish cross-grade repeats separately. No added bank items, no modified keys, no learner approvals, no independent signed correctness. **Caveated** intended keys at ELE001/007/009/013/022; reinforce bounds, source specificity and exam edition. Previous independent verification from repository notes remains pending. No app changes. Continue with disjoint prelim P2 before broader model-only grade II.
