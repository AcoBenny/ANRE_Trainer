# CKPT-227 | GFR 15 P2 individual legacy QABC: physics, components, exact A/B/C and counters | 2026-11-18

## Evidence and constraints
- Source V73 822-grade master Git blob `c027d417a8e4e605c830b2016fb55b099b8d130b`; focus 15 **previously PRELIMINARY_ONLY** Grade I electrotechnics cards, original workbook `ELECTROTEHNICA-09.2024-2.xlsx`, rows 8–24 (nonconsecutive); imported key never edited. Same QABC may appear in Grade II; **do not count as additional independent checks**.
- OpenStax textbook, academic motor/reactor/graph sources, contemporary vendor/manufacturer and official Romanian AAR functional standard re-opened via public source retrieval in this session; links in each card. Not authenticated as ANRE's official exam scoring key, no independent human/agent signoff, no student approval.
- Internal arithmetic/model check: C_parallel(100,50,100)=250µF; graph cycles L−N+k with example L=5,N=4,k=2 -> 3 loops against connected-formula 2 (respecting L≠N); Joule Q=I²Rt with fixed I, R, t.
- Previously blocked G1-ELE-014 is **not** counted in this fresh batch: see CKPT-184 for existing ambiguity source pass. No QABC edits, app work, merge or release.

### G1-ELE-001 | CONDITIONAL_GRID_OPERATION
- **Original question:** Atunci când se compensează energia electrica reactiva prin baterii de condensatoare, tensiunea în reţeaua electrica:
- **A:** scade
- **B:** nu se modifica
- **C:** creste
- **Imported key:** **C**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `8`; exact QABC grade instances: G1-ELE-001=C, G2-ELEC-154=C.
- **A/B/C model, limitations, negative cases:** Compensating inductive reactive load with local shunt capacitors typically lowers reactive line current and hence voltage drop, so the receiving-end voltage increases (C) with upstream voltage/regulator/load held constant. A decrease is not the normal fixed-network result. B unchanged can happen if an upstream voltage regulator actively maintains a setpoint; 'crește' not universal for all networks.
- **Direct source:** https://electrical-engineering-portal.com/voltage-regulators; locator: Voltage regulation and power-factor correction; normal feeder model; regulator counterexample..
- **Gate:** `CONDITIONAL_GRID_OPERATION`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-002 | DIRECT_PHYSICAL_OBJECT_MATCH
- **Original question:** Bobinele de stingere din staţiile electrice de transformare sunt echipamente pentru:
- **A:** compensarea factorului de putere
- **B:** dotări PSI
- **C:** compensarea curenţilor capacitivi
- **Imported key:** **C**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `9`; exact QABC grade instances: G1-ELE-002=C, G2-ELEC-155=C.
- **A/B/C model, limitations, negative cases:** C arc suppression/Petersen coil compensates capacitive earth-fault currents via inductive neutral current. A power-factor correction as a general load objective is a different capacitor/reactor context. B PSI fire brigade equipment is unrelated; coil can help quench fault arc but is not firefighting inventory.
- **Direct source:** https://www.mdpi.com/2673-4826/4/2/7; locator: Introduction: resonant earth neutral coil to cancel capacitive earth fault current..
- **Gate:** `DIRECT_PHYSICAL_OBJECT_MATCH`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-003 | DIRECT_DISTRACTOR_ELIMINATION
- **Original question:** Câmpul magnetic poate fi produs:
- **A:** numai de magneţi permanenţi
- **B:** numai de electromagneţi
- **C:** de magneţi permanenţi si de electromagneţi
- **Imported key:** **C**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `10`; exact QABC grade instances: G1-ELE-003=C, G2-ELEC-156=C.
- **A/B/C model, limitations, negative cases:** A 'numai' permanent magnets excludes electromagnets and moving charges. B 'numai' electromagnets excludes permanent magnets. C both permanent magnets and electromagnets generate B field; option does not exhaust all possible sources, but stem asks 'poate fi produs', not only by these two.
- **Direct source:** https://openstax.org/books/college-physics-ap-courses/pages/22-2-ferromagnets-and-electromagnets; locator: Magnetism definitions and experiments..
- **Gate:** `DIRECT_DISTRACTOR_ELIMINATION`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-004 | DETERMINISTIC_PARALLEL_CAPACITANCE
- **Original question:** 3 condensatoare având capacitatea C1=100 μF, C2=50 μF, C3=100 μF legate în paralel, au capacitatea echivalentă.
- **A:** 25 μF
- **B:** 250 μF
- **C:** 50 μF
- **Imported key:** **B**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `11`; exact QABC grade instances: G1-ELE-004=B, G2-ELEC-157=B.
- **A/B/C model, limitations, negative cases:** Three capacitors in parallel have same U and equivalent CΣ=C1+C2+C3=100+50+100=250 µF, B. A 25 and C 50 fail direct arithmetic; confirmed in independent arithmetic check.
- **Direct source:** https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel; locator: Parallel capacitors equivalent sum; concrete arithmetic..
- **Gate:** `DETERMINISTIC_PARALLEL_CAPACITANCE`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-005 | CONDITIONAL_CONNECTED_GRAPH_MISSING
- **Original question:** A doua teoremă a lui Kirchhoff, pentru o reţea electrică cu N noduri şi L laturi (L diferit de N), ne furnizează, pentru analiza unui circuit electric:
- **A:** L+N-1 ecuaţii distincte
- **B:** L-N +1 ecuaţii distincte
- **C:** N-L+1 ecuaţii distincte
- **Imported key:** **B**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `12`; exact QABC grade instances: G1-ELE-005=B, G2-ELEC-158=B.
- **A/B/C model, limitations, negative cases:** If the network is CONNECTED, a spanning tree has N−1 edges and the L−(N−1)=L−N+1 independent fundamental loops give B. A L+N−1 overcounts; C N−L+1 wrong sign generally. Stem only gives L ≠ N, not connectedness. For k connected components, number of independent loops is L−N+k, so e.g. L=4,N=4,k=2 gives 2 versus B=1 (here L=N, use e.g. L=5,N=4,k=2 gives 3 vs B=2; the counterexample must respect L ≠ N). The source model thus remains incomplete, not unconditional approval.
- **Direct source:** https://graphcalc.readthedocs.io/en/latest/api/graphs/invariants/cycle_invariants.html; locator: Cyclomatic number formula E−V+c. Explicit L!=N-compatible counterexample..
- **Gate:** `CONDITIONAL_CONNECTED_GRAPH_MISSING`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-006 | DIRECT_OPERATIONAL_PURPOSE
- **Original question:** AAR se utilizează în scopul:
- **A:** limitării curenţilor de scurtcircuit;
- **B:** creşterii continuităţii în alimentare;
- **C:** reducerii pierderilor de energie pe linii.
- **Imported key:** **B**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `13`; exact QABC grade instances: G1-ELE-006=B, G2-ELEC-159=B.
- **A/B/C model, limitations, negative cases:** Romanian AAR (anclanșare automată a rezervei) switches supply to available reserve to improve continuity of electric supply B. A short-circuit limiting is done by protection/reactance devices, C line losses optimized by different measures. Source refers to continuity to station internal customers.
- **Direct source:** https://legislatie.just.ro/Public/FormaPrintabila/00000G1XVHI158QR1MF2P9E8O4I5NEHX; locator: 2012 Romanian technical norm art.178; current 2026 legal applicability of that edition not proven, functional meaning clear..
- **Gate:** `DIRECT_OPERATIONAL_PURPOSE`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-007 | CONDITIONAL_INDUCTION_MOTOR_MODE
- **Original question:** Alunecarea s a unui motor asincron are valori:
- **A:** cuprinse între 1 si 0
- **B:** cuprinse între -1 si 0
- **C:** de regulă, mai mari decât 1
- **Imported key:** **A**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `14`; exact QABC grade instances: G1-ELE-007=A, G2-ELEC-160=A.
- **A/B/C model, limitations, negative cases:** For normally motor-driven asynchronous machine n in [0,n_sync], slip s=(n_sync−n)/n_sync is 1 at standstill and approaches 0 near synchronous, so A intended. B negative s occurs when machine acts as induction GENERATOR, not motoring; C s>1 occurs in plugging/contra-current braking. Stem says motor, but does not explicitly restrict operation to normal motoring, so treat as didactic intended A not all operating states.
- **Direct source:** https://dtmc0945.github.io/L-MCI-BSc-Drive-Technology/InductionMachineEquivalentCircuit.html; locator: Induction machine motoring, generating and plugging speed regimes..
- **Gate:** `CONDITIONAL_INDUCTION_MOTOR_MODE`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-009 | CONDITIONAL_GRID_CONTROL_SCOPE
- **Original question:** Care element nu se foloseşte la reglarea tensiunii în reţelele electrice:
- **A:** bobina de compensare
- **B:** transformatorul
- **C:** rezistorul
- **Imported key:** **C**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `16`; exact QABC grade instances: G1-ELE-009=C, G2-ELEC-161=C.
- **A/B/C model, limitations, negative cases:** Typical feeder regulation uses transformer tap positions or shunt reactors/capacitors to modify voltage and reactive-flow, not a standalone resistor for economical network-wide voltage regulation, intended C. A reactor can affect reactive voltage drop, B transformer tap changes voltage. Counterexample: series resistance changes U=IR and may be used as a dropper in low-power equipment; 'nu se folosește' is too absolute without specifying utility distribution voltage-control hardware.
- **Direct source:** https://electrical-engineering-portal.com/voltage-regulators; locator: Transformer tap and reactive equipment vs resistive drop..
- **Gate:** `CONDITIONAL_GRID_CONTROL_SCOPE`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-010 | SOURCE_COMPATIBLE_NOT_STATISTICAL_CERTIFICATION
- **Original question:** Cele mai des utilizate pentru serviciile interne ale centralelor electrice sunt:
- **A:** motoarele de curent continuu
- **B:** motoarele sincrone
- **C:** motoarele asincrone
- **Imported key:** **C**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `17`; exact QABC grade instances: G1-ELE-010=C, G2-ELEC-162=C.
- **A/B/C model, limitations, negative cases:** For conventional station internal-service fans/pumps/drives the prevalent technology is induction/asynchronous motor C. A DC reserved for particular services, B synchronous for selected duties. Source documents multiple power-plant auxiliary induction motor applications; it does NOT independently establish a numerical frequency comparison for all stations/eras, so 'cele mai des' remains broad.
- **Direct source:** https://www.mdpi.com/1996-1073/17/5/1066; locator: 2024 engineering article listing induction motors at plant auxiliaries..
- **Gate:** `SOURCE_COMPATIBLE_NOT_STATISTICAL_CERTIFICATION`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-011 | DIRECT_REACTOR_IMPEDANCE_MODEL
- **Original question:** Bobinele pentru limitarea curenţilor de scurtcircuit au:
- **A:** rezistenta mare
- **B:** inductanţa mare
- **C:** inductanţa mica
- **Imported key:** **B**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `18`; exact QABC grade instances: G1-ELE-011=B, G2-ELEC-163=B.
- **A/B/C model, limitations, negative cases:** A current-limiting reactor is an in-series high-inductive-reactance element (X_L=2πfL) to increase fault-loop impedance, reducing short-circuit current: B large L. A large resistance is not the normal low-loss reactor design, C small L yields inadequate fault current reduction. Reactor design may specify limiting X and transient recovery effects, not merely 'L mare' in isolation.
- **Direct source:** https://www.mdpi.com/1996-1073/16/2/811; locator: Current limiting reactors series with feeder, equivalent circuit, short-circuit current effects..
- **Gate:** `DIRECT_REACTOR_IMPEDANCE_MODEL`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-012 | DIRECT_ELECTROSTATIC_DEFINITION_WITH_SCOPING
- **Original question:** Câmpul electrostatic este descris
- **A:** prin: intensitatea câmpului electric
- **B:** numai prin inducţia electrică
- **C:** inducţia magnetică
- **Imported key:** **A**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `19`; exact QABC grade instances: G1-ELE-012=A, G2-ELEC-164=A.
- **A/B/C model, limitations, negative cases:** E (electric-field strength/intensity) describes the electrostatic field; A holds. B 'numai D electric displacement' false exclusivity because E and potential also describe it, C magnetic induction is a different B-field quantity. D=εE is material dependent (linear dielectric, specified conditions), so never assert D=εE as universal scalar relation.
- **Direct source:** https://openstax.org/books/university-physics-volume-2/pages/5-4-electric-field; locator: Field strength E from source charges, definitions..
- **Gate:** `DIRECT_ELECTROSTATIC_DEFINITION_WITH_SCOPING`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-013 | CONDITIONAL_OIL_FILLED_INSTALLATION
- **Original question:** Comparativ cu cele uscate, transformatoarele imersate prezintă :
- **A:** o bună rezistenţă la foc;
- **B:** risc crescut de poluare acustică a mediului ambiant;
- **C:** necesitatea unor amenajări speciale la instalare
- **Imported key:** **C**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `20`; exact QABC grade instances: G1-ELE-013=C, G2-ELEC-165=C.
- **A/B/C model, limitations, negative cases:** C oil-immersed transformer can require bund/oil spill/fire provisions at installation that dry type lacks. A superior fire resistance is not generally the point of conventional mineral-oil transformer. B increased noise is model/design dependent, not the defining distinction. Ester-filled vs mineral-oil and exterior installations can change exact provisions, so 'necesitatea' is conditional, not a universal rule for every liquid-filled transformer.
- **Direct source:** https://www.se.com/us/en/faqs/FA275901/; locator: Schneider manufacturer dry vs liquid type, containment and installation conditions; also https://electrical-engineering-portal.com/specifying-transformers.
- **Gate:** `CONDITIONAL_OIL_FILLED_INSTALLATION`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-015 | DIRECT_SERIES_REACTOR_DOWNSTREAM_SCOPE
- **Original question:** Bobinele montate pe plecari radiale limiteaza curentii de scurtcircuit
- **A:** atat inainte, cat si dupa punctele lor de racordare la barele statiei;
- **B:** inainte de punctele lor de racordare la barele statiei;
- **C:** dupa punctele lor de racordare la barele statiei.
- **Imported key:** **C**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `22`; exact QABC grade instances: G1-ELE-015=C, G2-ELEC-167=C.
- **A/B/C model, limitations, negative cases:** A short-circuit on bus or on upstream side of outgoing feeder reactor does NOT pass through its impedance, so A both sides and B upstream are false. Downstream/outgoing radial fault current passes through series inductance and is reduced, C. Current-limiter location must be between source and fault to work.
- **Direct source:** https://www.phasetophase.nl/book/book_1_4.html; locator: Distribution feeder series current limiting reactor..
- **Gate:** `DIRECT_SERIES_REACTOR_DOWNSTREAM_SCOPE`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-016 | DIRECT_JOULE_HEAT_FIXED_R_TIME
- **Original question:** Cantitatea de căldura produsã la trecerea curentului electric printr-un conductor este:
- **A:** direct proporţională cu secţiunea conductorului
- **B:** direct proporţionala cu pătratul intensităţii curentului
- **C:** invers proporţionala cu rezistenta conductorului
- **Imported key:** **B**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `23`; exact QABC grade instances: G1-ELE-016=B, G2-ELEC-168=B.
- **A/B/C model, limitations, negative cases:** Joule heat for resistance R and time t: Q=I² R t, so B dependence on square of current. A direct proportion to conductor section is false if material/length fixed (larger S decreases R and Q for constant I), C inverse proportional to R is false for fixed I but true for fixed V, which the stem does not state. Thus B requires current-controlled assumption or holding R,t constant; flag source current regime.
- **Direct source:** https://openstax.org/books/university-physics-volume-2/pages/9-5-electrical-energy-and-power; locator: Equation P=I²R=V²/R, contrast fixed-I and fixed-V cases..
- **Gate:** `DIRECT_JOULE_HEAT_FIXED_R_TIME`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

### G1-ELE-017 | DIRECT_SERIES_CAPACITOR_CHARGE
- **Original question:** Cantitatea de electricitate cu care se încarcă o baterie de n condensatoare montate în serie, fiecare de capacitate C, este:
- **A:** aceeaşi cu care se încarcă fiecare element component
- **B:** suma cantităţilor cu care se înarcă fiecare element în parte
- **C:** egală cu de două ori cantitatea de electricitate cu care se încarcă fiecare condensator
- **Imported key:** **A**, unchanged. Workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `24`; exact QABC grade instances: G1-ELE-017=A, G2-ELEC-169=A.
- **A/B/C model, limitations, negative cases:** For n ideal capacitors in a series chain under two-terminal excitation, each internal element carries identical charge magnitude Q; total equivalent capacitor terminal charge equals one element's charge, A. B sum nQ double counts separate plate charges, C 2Q only special artifact. Assumes initially uncharged ideal series capacitors with no free trapped intermediate-node charge.
- **Direct source:** https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel; locator: Series capacitances and equal element charge..
- **Gate:** `DIRECT_SERIES_CAPACITOR_CHARGE`; `independent_technical_linguistic_QA=NOT_RUN`; `official_2026_ANRE_exam_key=NOT_VERIFIED`; `approved_for_learning=NO`.

## Audit counts and next gate
- 15 distinct QABC units with exactly **30 grade entries across Grades I and II**, original keys consistent in all 15 pairs. 0 newly added bank questions, 0 modified barems, 0 learner signoffs. Strong context traps G1-ELE-005 connectedness, G1-ELE-007 operating mode, G1-ELE-001 voltage held/regulation, G1-ELE-009 word 'nu', G1-ELE-013 transformer installation, G1-ELE-010 'cele mai des'.
- Do NOT record 30 unique unit reviews from 15 grade-pair copies. Preserve existing CKPT-184 G1-ELE-014 and CKPT-216 G2-ELEC-158 (same QABC G1-ELE-005).
- Resume next disjoint 15 P2 individual prelim in original workbook order; carry grade-pair evidence reuse with no falsely independent specialist count; PR #7 stays Draft.
