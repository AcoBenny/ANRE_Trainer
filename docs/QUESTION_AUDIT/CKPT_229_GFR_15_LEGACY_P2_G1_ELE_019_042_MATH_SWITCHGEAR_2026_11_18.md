# CKPT-229 | GFR 15 next legacy P2 electrotechnics QABC, formulas and safety scope | 2026-11-18

## Controls
- 15 **new individual focused** P2 QABC from canonical V73 blob `c027d417a8e4e605c830b2016fb55b099b8d130b`, original source workbook `ELECTROTEHNICA-09.2024-2.xlsx`. No overlap with CKPT-227 G1 items or historic CKPT-184 G1-ELE-014. Exact question/alternatives and original key preserved. Pair mapping later ONLY by exact question/A/B/C/key, no numeric offsets (CKPT-228 regression).
- Source classes: published OpenStax academic textbooks, primary equipment manufacturer, manufacturer engineering design guides, nonofficial educational secondary Romanian coupler source, open research, and IEC-related engineering guidance. State assumptions and exceptions per original physical question. No separately running independent agent, no ANRE examiner signoff, no learner approval.
- Arithmetic/model check: 2 equal series C→C/2; 2 A in 10Ω gives 40W for 10 h = **400Wh**; isolated neutral SLG healthy voltage grows **sqrt(3) ≈ 1.732**; `|Z|=sqrt(3²+4²)=5Ω`, `220V/5Ω=44A`; `τ=RC` time dimension; `F∝1/r²`.

### G1-ELE-019 | DIRECT_SERIES_CAPACITANCE
- Original: **Capacitatea echivalentă a 2 condensatoare, fiecare având capacitatea C, montate în serie este egală cu:**
- A: 2 C
- B: C/2
- C: C
- Imported key **B** unchanged, source workbook row 26; pair: G1-ELE-019=B, G2-ELEC-171=B.
- Three-alternative and physical/linguistic assessment: Equal capacitors in series: 1/Ceq=1/C+1/C=2/C -> Ceq=C/2. A=2C is parallel result, C=C ignores second capacitor. Ideal lossless series model.
- Supporting technical source: https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel.
- QA gate: `DIRECT_SERIES_CAPACITANCE`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-021 | CONDITIONAL_EQUAL_GEOMETRY_AND_TEMPERATURE
- Original: **Care dintre materialele electrotehnice admit o densitate de curent mai mare:**
- A: aluminiu
- B: cupru
- C: ambele admit aceeaşi densitate de curent
- Imported key **B** unchanged, source workbook row 28; pair: G1-ELE-021=B, G2-ELEC-173=B.
- Three-alternative and physical/linguistic assessment: Copper has lower resistivity and at equal area/insulation/installation allowable current density generally exceeds aluminium. A Al not higher at same conditions; C equal false generically. But bare question omits section, temperature rise, insulation/installation, so does not state a universal independent material constant for J_limit.
- Supporting technical source: https://www.electrical-installation.org/enwiki/Conductor_sizing%3A_methodology_and_definition.
- QA gate: `CONDITIONAL_EQUAL_GEOMETRY_AND_TEMPERATURE`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-022 | CONDITIONAL_LINEAR_DIELECTRIC
- Original: **Care dintre relaţiile următoare este adevărată:**
- A: inducţia electrică = permitivitatea x intensitatea câmpului electric
- B: inducţia electrică = intensitatea câmpului electric/ permitivitate
- C: inducţia electrică=sarcina x intensitatea câmpului electric
- Imported key **A** unchanged, source workbook row 29; pair: G1-ELE-022=A, G2-ELEC-174=A.
- Three-alternative and physical/linguistic assessment: For linear homogeneous isotropic dielectric D=εE, A. B E/ε is dimensionally wrong, C charge·E gives electric force (units N), not displacement D (C/m²). In general polarizable/nonlinear media D=ε0 E+P and ε may be tensor or field-dependent; A not fully universal without media definition.
- Supporting technical source: https://www.mdpi.com/1996-1944/18/18/4282.
- QA gate: `CONDITIONAL_LINEAR_DIELECTRIC`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-026 | SECONDARY_SOURCE_COST_MODEL_ONLY
- Original: **Utilizarea unei cuple cu functiuni multiple se prefera atunci cand dorim**
- A: scurtarea duratei manevrelor
- B: cresterea continuitatii  in alimentare
- C: reducerea investitiei in echiparea statiei.
- Imported key **C** unchanged, source workbook row 33; pair: G1-ELE-026=C, G2-ELEC-175=C.
- Three-alternative and physical/linguistic assessment: Multifunction bus coupler can combine switching roles of separate sectional/transverse couplers and reduce installed breaker count/investment, making imported C plausible. A reducing switch-operation time not necessarily and B supply continuity can be worse vs dedicated couplers; source is Romanian secondary educational material, no product-specific engineering tradeoff/official scoring key. Strong safety-context qualifier.
- Supporting technical source: https://licentiada.org/proiectarea-circuitelor-electrice-principale-ale-unei-cet-echipata-cu-doua-grupuri-turbogeneratoare-de-30-mw-311383-e7da9c75/.
- QA gate: `SECONDARY_SOURCE_COST_MODEL_ONLY`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-027 | DETERMINISTIC_ENERGY_CALC
- Original: **Care este energia consumata de o rezistenta electrica r = 10 Ω, prin care trece un curent de 2 A timp de 10 ore:**
- A: 200 Wh
- B: 400 Wh
- C: 800 Wh
- Imported key **B** unchanged, source workbook row 34; pair: G1-ELE-027=B, G2-ELEC-176=B.
- Three-alternative and physical/linguistic assessment: P=I²R=(2A)²·10Ω=40W; E=P·10h=400Wh =0.4kWh =1.44MJ, B. A=200Wh (half), C=800Wh (double). Inputs fixed, resistive heating assumption.
- Supporting technical source: https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power.
- QA gate: `DETERMINISTIC_ENERGY_CALC`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-030 | CONDITIONAL_ALL_VOLTAGES_WORDING
- Original: **Scheme cu un sistem de bare colectoare şi un întreruptor pe circuit sunt folosite**
- A: numai pentru staţii de conexiuni de 6 kV
- B: pentru toate treptele de tensiune din reţelele de distribuţie
- C: numai pentru staţii de conexiuni de medie tensiune până la 6o kV
- Imported key **B** unchanged, source workbook row 37; pair: G1-ELE-030=B, G2-ELEC-179=B.
- Three-alternative and physical/linguistic assessment: Single busbar / one-breaker per circuit scheme is used at multiple distribution voltage levels; A only 6kV and C only MV up to typo '6o kV' overrestrict. B 'toate treptele' as applicability is possible conceptually but not a rule to install at EVERY distribution voltage, as reliability/voltage-dependent designs differ. Treat as intended but universal overstatement.
- Supporting technical source: https://electrical-engineering-portal.com/bus-configurations-substations-345-kv.
- QA gate: `CONDITIONAL_ALL_VOLTAGES_WORDING`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-031 | CONDITIONAL_PRODUCT_SPECIFIC_SAFETY
- Original: **Celulele prefabricate monobloc se caracterizează în principal prin:**
- A: securitate ridicată a persoanelor;
- B: gamă largă de configuraţii ale schemei de conexiuni;
- C: eliminarea totală a posibilităţii de producere a unui scurtcircuit între faze
- Imported key **A** unchanged, source workbook row 38; pair: G1-ELE-031=A, G2-ELEC-180=A.
- Three-alternative and physical/linguistic assessment: Prefabricated metal-enclosed monobloc switchgear emphasizes enclosure, interlocks and internal arc protections to improve personnel safety, A. B a broad range of freely configurable schemes can be less true for monobloc units vs modular systems; C 'total elimination' of phase-to-phase short circuit impossible. Actual safety is product/IAC/operating procedure-specific, not automatically guaranteed by 'prefabricated'.
- Supporting technical source: https://productinfo.se.com/doca0483en-00_dnf7_ioms/doca0483en-00_dnf7_ioms/English/DOCA0483EN_DNF7_IOMS_DD01459658.xml/%24/SwitchgearEnclosure-3D64907D.
- QA gate: `CONDITIONAL_PRODUCT_SPECIFIC_SAFETY`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-033 | CONDITIONAL_DRY_TYPE_FIRE_CLASS
- Original: **Comparativ cu cele imersate, transformatoarele uscate prezintă :**
- A: o bună rezistenţă la foc;
- B: risc redus de poluare acustică a mediului ambiant;
- C: necesitatea unor amenajări speciale la instalare
- Imported key **A** unchanged, source workbook row 40; pair: G1-ELE-033=A, G2-ELEC-181=A.
- Three-alternative and physical/linguistic assessment: Dry-type/cast resin transformers avoid bulk mineral insulating oil and generally lower fire and spill hazards, imported A intent. B sound emission is design-specific not automatically lower, C oil-immersed units often have special containment not dry. Dry units can still burn; some ester/silicone liquid units are fire-resistant, so 'bună rezistență la foc' only relative to conventional oil type and certified design.
- Supporting technical source: https://www.se.com/uk/en/product-subcategory/3610-dry-type-distribution-transformers/.
- QA gate: `CONDITIONAL_DRY_TYPE_FIRE_CLASS`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-034 | DIRECT_IDEAL_ISOLATED_NEUTRAL_SLG
- Original: **Daca la un circuit al unei staţii de 6 sau 20 kV care funcţionează cu neutrul izolat apare o punere monofazatã netã la pământ, tensiunea fata de pământ a celorlalte doua faze:**
- A: scade de 1,41 ori
- B: rămâne constanta
- C: creste de 1,73 ori
- Imported key **C** unchanged, source workbook row 41; pair: G1-ELE-034=C, G2-ELEC-182=C.
- Three-alternative and physical/linguistic assessment: On bolted phase-to-earth fault with isolated neutral, faulted phase-earth drops to 0, two healthy phase-earth voltages rise from U_phase to U_line=√3 U_phase≈1.732 U_phase: C. A decrease by 1.41 and B constant are false in model. Severe transients/overvoltages can differ from steady ideal result.
- Supporting technical source: https://www.electrical-installation.org/enwiki/IT_system_-_Fault_protection.
- QA gate: `DIRECT_IDEAL_ISOLATED_NEUTRAL_SLG`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-035 | DIRECT_COMPARTMENTALIZATION_PURPOSE
- Original: **Compartimentarea unei celule electrice se utilizează**
- A: în scopul evitării extinderii avariilor;
- B: numai  în scopul protejării personalului de exploatare;
- C: protecţiei la supratensiuni
- Imported key **A** unchanged, source workbook row 42; pair: G1-ELE-035=A, G2-ELEC-183=A.
- Three-alternative and physical/linguistic assessment: Walls/partitions between switchgear cells limit spread of arcs, hot gases or damage between equipment; A. B says personnel protection *only*, which is not sole purpose, C overvoltage protection different surge protection apparatus. Compartment design/arc performance must be rated/verified.
- Supporting technical source: https://productinfo.se.com/0100db2301_elecdistfunddesignguide/viewer?docidentity=PowerDistributionEquipment-A630D34D&extension=xml&lang=en&manualidentity=DocumentTypeProductCategoryRangeNam-A482E1D1.
- QA gate: `DIRECT_COMPARTMENTALIZATION_PURPOSE`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-038 | CONDITIONAL_MOTORING_POSITIVE_SEQUENCE
- Original: **Componenta simetrică directă produce, în cazul unui motor electric:**
- A: cuplul util
- B: cuplul de frânare
- C: oscilaţii ale rotorului
- Imported key **A** unchanged, source workbook row 45; pair: G1-ELE-038=A, G2-ELEC-184=A.
- Three-alternative and physical/linguistic assessment: Positive-sequence 3-phase flux rotates in normal forward direction and produces positive driving torque at motoring slip, imported A. B braking torque belongs negative sequence or generating/other braking regimes; C rotor oscillations not primary positive-sequence torque. In generation negative slip positive-sequence electromagnetic torque resists rotation, so 'produce cuplul util' is didactic motoring model not universal operating modes.
- Supporting technical source: https://cms-cdn.selinc.com/assets/Literature/Publications/Technical%20Papers/6779_NegativeSequence_NM_20170209_Web3.pdf?v=20171110-231733.
- QA gate: `CONDITIONAL_MOTORING_POSITIVE_SEQUENCE`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-039 | DIRECT_COULOMB_INVERSE_SQUARE
- Original: **Conform Legii lui Coulomb, forţa de atracţie sau de repulsie care se exercită între sarcinile electrice este:**
- A: direct proporţională cu pătratul distanţei
- B: invers proporţională cu pătratul distanţei
- C: direct proporţională cu distanţa
- Imported key **B** unchanged, source workbook row 46; pair: G1-ELE-039=B, G2-ELEC-185=B.
- Three-alternative and physical/linguistic assessment: For point charges at fixed charge/dielectric F=k|q1q2|/r²: B inversely proportional to square of distance. A directly proportional r² and C to r contradict. Model presumes electrostatic point charges and homogeneous medium; interaction can be more complex with conductors/boundaries.
- Supporting technical source: https://openstax.org/books/university-physics-volume-2/pages/5-3-coulombs-law.
- QA gate: `DIRECT_COULOMB_INVERSE_SQUARE`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-040 | DIRECT_RC_TIME_CONSTANT
- Original: **Constanta de timp a unui circuit format dintr-un rezistor de rezistenţă R înseriat cu un condensator de capacitate C, este:**
- A: RC
- B: R/C
- C: 1/(RC)
- Imported key **A** unchanged, source workbook row 47; pair: G1-ELE-040=A, G2-ELEC-186=A.
- Three-alternative and physical/linguistic assessment: For ideal single series resistor R and capacitor C, τ=RC (seconds because ΩF=s), A. B R/C has wrong units, C 1/(RC) is inverse time / characteristic frequency not time constant.
- Supporting technical source: https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits.
- QA gate: `DIRECT_RC_TIME_CONSTANT`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-041 | DIRECT_CELL_PARTITION_FAULT_CONTAINMENT
- Original: **Delimitările prin pereţi între celulele unei staţii electrice de interior se utilizează în principal în scopul:**
- A: asigurării unui acces mai comod la aparataj;
- B: limitării zgomotului în corpul de conexiuni;
- C: evitării extinderii avariilor.
- Imported key **C** unchanged, source workbook row 48; pair: G1-ELE-041=C, G2-ELEC-187=C.
- Three-alternative and physical/linguistic assessment: Walls between indoor substation bays chiefly reduce consequences and propagation of an internal arc/fire/fault to neighboring bays; C. A convenient access can be secondary, B noise isolation not principal electrical safety rationale. Source manufacturer notes compartmentation reduces internal fault propagation, but exact historical exam topology unspecified.
- Supporting technical source: https://productinfo.se.com/0100db2301_elecdistfunddesignguide/viewer?docidentity=PowerDistributionEquipment-A630D34D&extension=xml&lang=en&manualidentity=DocumentTypeProductCategoryRangeNam-A482E1D1.
- QA gate: `DIRECT_CELL_PARTITION_FAULT_CONTAINMENT`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

### G1-ELE-042 | DETERMINISTIC_AC_IMPEDANCE
- Original: **Curentul care circula printr-un circuit de curent alternativ, având rezistenta r=3 Ω, reactanţa x= 4 Ω si la bornele căruia se aplica o tensiune de 220 V este:**
- A: 31,5 A
- B: 44 A
- C: 53,4 A
- Imported key **B** unchanged, source workbook row 49; pair: G1-ELE-042=B, G2-ELEC-188=B.
- Three-alternative and physical/linguistic assessment: Single series equivalent impedance magnitude |Z|=sqrt(R²+X²)=sqrt(3²+4²)=5Ω; I_rms=U_rms/|Z|=220/5=44A -> B. A31.5 and C53.4 not consistent. Model assumes 220 V RMS phasor, passive linear one-port series R/X; without explicit 'series' or convention, question uses textbook series equivalent simplification.
- Supporting technical source: https://openstax.org/books/college-physics/pages/23-section-summary.
- QA gate: `DETERMINISTIC_AC_IMPEDANCE`; `independent_technical_linguistic_QA=NOT_RUN`, `ANRE_2026_exam_key=NOT_VERIFIED`, `approved_for_learning=NO`.

## Result and next
- Distinct original QABC = 15, grade entries = 30 with source-identical Grade I/II pairs, but **NOT 30 independent source checks**. No new questions, no answer-key edits, no learner approval. High-context cases: ELE021 thermal/rating control, ELE022 dielectric linearity, ELE026 station coupler configuration and secondary-only source, ELE030 all-voltage qualifier, ELE031 IAC device, ELE033 fire class, ELE038 motoring regime, ELE042 series/RMS model.
- Next GFR pass: remaining legacy P2 prechecks, reconcile P2 paired Grade II using exact matching method in CKPT-228. Do not resume application/HTML/APK or merge PR#7.
