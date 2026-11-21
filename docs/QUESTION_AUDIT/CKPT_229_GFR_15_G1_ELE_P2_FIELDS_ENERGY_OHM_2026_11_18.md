# CKPT-229 | GFR 15 more P2 electrotechnics preliminary proof/reasoning | 2026-11-18

## Fidelity gate
- Canonical 822 V73 file original Git blob `c027d417a8e4e605c830b2016fb55b099b8d130b`, exact original question/three options plus graded original key copied mechanically. Selected 15 P2 prior preliminary cards not in CKPT227/228. 2026 ANRE official key and bibliography-specific technical source not verified; independent technical / linguistic / negative QA actor NOT_RUN. Generic manufacturer pages explicitly downgraded; not presented as exact manufacturer proof.
- No canonical changes to answer key, original, HTML/APK, main, PR#7 draft or release.

### G1-ELE-050 | DIRECT_POYNTING_VECTOR
- Question original: Energia transmisă de undele electromagnetice cu intensitatea câmpului electric E şi intensitatea câmpului magnetic H se propagă după un vector:
- A: S=E+H
- B: S=HxE
- C: S=ExH
- Imported key **C**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `57`.
- Technical reference: https://openstax.org/books/university-physics-volume-2/pages/16-key-equations
- A/B/C counterfactual and exact model: Poynting flux vector S=E×H (for vacuum H=B/mu0), C. A sum of vectors E+H dimensionally invalid; B H×E=-E×H reverses propagation. Source uses E×B/mu0 which is equivalent in vacuum; in media proper E×H.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-052 | DIRECT_CAPACITIVE_PHASE_LEAD_CURRENT
- Question original: Dacă printr-un condensator circulă un curent alternativ sinusoidal, la bornele sale se produce o cădere de tensiune:
- A: defazată cu 90 de grade în urma curentului
- B: defazată cu 90 de grade înaintea curentului
- C: în fază cu curentul
- Imported key **A**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `59`.
- Technical reference: https://openstax.org/books/university-physics-volume-2/pages/15-summary
- A/B/C counterfactual and exact model: Ideal sinusoidal capacitor: i=C dv/dt so I leads voltage by 90°, voltage follows/lags current 90° -> A. B describes inductor-like relation, C purely resistive. Linear capacitive steady state assumed; parasitic ESR can shift angle.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-054 | DIRECT_ZNO_SURGE_ARRESTER_PURPOSE
- Question original: Descărcătoarele cu oxid de zinc protejează echipamentele din reţele împotriva:
- A: supratensiunilor
- B: supracurenţilor
- C: solicitărilor mecanice
- Imported key **A**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `61`.
- Technical reference: https://www.se.com/us/en/work/support/resources-and-tools/technical-faqs/
- A/B/C counterfactual and exact model: ZnO metal oxide surge arrester clamps transient overvoltages A; B overload/short circuit protected by fuse/breaker, C mechanical strength unrelated. Direct manufacturer page is generic, not a pinpoint data sheet, so SOURCE_PINPOINT_MISSING despite physical-function confidence.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-055 | DIRECT_ZNO_SURGE_ARRESTER_PURPOSE
- Question original: Descărcătoarele cu oxizi de zinc sunt echipamente destinate:
- A: protecţiei personalului de exploatare împotriva electrocutării
- B: protecţiei împotriva supratensiunilor
- C: protecţiei împotriva supracurenţilor
- Imported key **B**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `62`.
- Technical reference: https://www.se.com/us/en/work/support/resources-and-tools/technical-faqs/
- A/B/C counterfactual and exact model: B overvoltage. A direct human electric shock prevention not surge arrester main protective purpose, C overcurrent clearing not its role. Same basic factual unit as 054, but QABC options differ: do not count identical question.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-056 | DIRECT_SERIES_VOLTAGE_SUM
- Question original: Diferenţa de potenţial la bornele a n baterii de condensatoare montate în serie este egală cu:
- A: suma diferenţelor de potenţial la bornele fiecărui condensator
- B: diferenţa de potenţial la bornele fiecărui condensator în parte
- C: diferenţa de potenţial a unui condensator împărţită la n
- Imported key **A**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `63`.
- Technical reference: https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel
- A/B/C counterfactual and exact model: For n ideal series capacitors Vtotal=sum(Vi), so A. B one capacitor voltage applies only n=1 or uncommon special supply; C Vsingle/n reverses rule; identical capacitors mean total n*Vsingle.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-059 | DIRECT_STAR_THREE_PHASE_LINE_VOLTAGE
- Question original: În cazul conexiunii în stea la transformator:
- A: tensiunea de linie este egala cu tensiunea de faza
- B: curentul de linie este egal cu ~1,73 x curentul de faza
- C: tensiunea de linie este egala cu ~1,73 x tensiunea de faza
- Imported key **C**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `66`.
- Technical reference: https://www.electrical-installation.org/enwiki/Three-phase_electrical_power
- A/B/C counterfactual and exact model: Balanced symmetric star/Y: Uline=sqrt(3)*Uphase, so C; A equality only in delta or special nonstandard definition, B 1.73*Iphase describes delta, while Y line current equals phase current. Balanced sinusoidal basis; source URL may be general text needing direct pinpoint confirmation.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-062 | CONDITIONAL_REACTIVE_ENERGY_TERM
- Question original: Energia electrica reactiva:
- A: este o energie electrica complementara, care serveşte la magnetizarea bobinajelor
- B: se poate transforma în energie mecanica
- C: se poate transforma în energie luminoasa
- Imported key **A**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `69`.
- Technical reference: https://openstax.org/books/university-physics-volume-2/pages/15-3-rlc-series-circuits-with-ac
- A/B/C counterfactual and exact model: A intended: reactive energy exchanges periodically with magnetic fields in inductive windings (and capacitors' electric fields). B mechanical work and C light represent active energy conversion; in general electromagnetic energy can eventually transform via systems, so 'reactive energy' described as complementary is an AC accounting convention, not a new stored form of energy.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-063 | DIRECT_INDUCTOR_ENERGY_SQUARE
- Question original: Energia magnetostatică produsă de curentul i care parcurge un circuit care conţine o inductanţă L este egală cu:
- A: 1/2 L i
- B: 1/2 Li2
- C: Li
- Imported key **B**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `70`.
- Technical reference: https://openstax.org/books/university-physics-volume-2/pages/14-3-energy-in-a-magnetic-field
- A/B/C counterfactual and exact model: Stored magnetic U=1/2 L i² -> B. A 1/2 Li lacks current factor, C Li also wrong dimensions. L constant linear model assumed.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-064 | DIRECT_CHARGED_CONDUCTOR_ENERGY
- Question original: Energia electrostatică a unui conductor izolat în spaţiu, încărcat cu o sarcină q şi aflat la un potenţial V este egală cu:
- A: 1/2 q V
- B: q V
- C: 2 q V
- Imported key **A**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `71`.
- Technical reference: https://openstax.org/books/university-physics-volume-2/pages/8-key-equations
- A/B/C counterfactual and exact model: Electrostatic energy U=1/2 qV of isolated linear conductor charged gradually from 0 to V -> A. B qV double this, C 2qV quadruple; q and V final values. Other charge configurations/reference require scope.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-065 | DIRECT_FAULT_CURRENT_GENERAL
- Question original: În cazul producerii unui scurtcircuit într-o instalaţie, are loc următorul fenomen:
- A: creste tensiunea de alimentare a instalaţiei
- B: creste impedanţa echivalenta a instalaţiei
- C: creste curentul de alimentare a instalaţiei
- Imported key **C**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `72`.
- Technical reference: https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law
- A/B/C counterfactual and exact model: Short circuit presents low impedance fault, often substantially increases supply fault current C; A supply terminal voltage increases not characteristic, B impedance increases opposite. Source generic Ohm law, not exact short-circuit network test; current limited by source/internal impedance/protection and some fault configurations require more detail.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-066 | DIRECT_CHARGE_CONSERVATION
- Question original: Enunţul "sarcinile electrice nu pot fi create și nici distruse, ci doar mutate" reprezintă o consecință pentru:
- A: legea conservării sarcinii electrice
- B: legea lui Coulomb
- C: legea lui Laplace
- Imported key **A**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `73`.
- Technical reference: https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules
- A/B/C counterfactual and exact model: A charge conservation direct interpretation; B Coulomb law force inverse square, C Laplace electromagnetic force is different. Charged particles may be created/annihilated only in net-charge conserving processes: quote is introductory conservation of net charge.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-067 | DIRECT_KIRCHHOFF_LOOP
- Question original: Enunţul "suma algebrică a tensiunilor electromotoare dintr-o buclă a unei reţele electrice este egală cu suma algebrică a căderilor de tensiune din buclă" reprezintă:
- A: Prima lege a lui Kirchhoff
- B: a doua lege a lui Kirchhoff
- C: Legea Joule -Lenz
- Imported key **B**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `74`.
- Technical reference: https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules
- A/B/C counterfactual and exact model: B Kirchhoff voltage loop second theorem sums EMFs equal drops; A current junction node law, C Joule Lenz heating unrelated. Lumped/quasistatic circuit; time-varying linked magnetic flux requires induced emf accounting.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-068 | DIRECT_AMPERE_FORCE_DIMENSIONS
- Question original: Expresia B x i x l , unde i este intensitatea curentului care străbate un conductor de lungime l, situat perpendicular pe câmpul de inducţie magnetică de mărime B, reprezintă:
- A: o forţă
- B: o tensiune
- C: o rezistenţă
- Imported key **A**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `75`.
- Technical reference: https://openstax.org/books/college-physics-2e/pages/22-7-magnetic-force-on-a-current-carrying-conductor
- A/B/C counterfactual and exact model: Force magnitude F=B*I*l (sin theta=1 when perpendicular), in newtons -> A. B voltage and C resistance wrong dimensions; magnetic field must be perpendicular specified.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-069 | DIRECT_OHM_LAW_FOR_LINEAR_RESISTOR
- Question original: Expresia matematica a legii lui Ohm pentru o porţiune de circuit este:
- A: I = U / R
- B: I = UxR
- C: I = U - R
- Imported key **A**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `76`.
- Technical reference: https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law
- A/B/C counterfactual and exact model: A I=U/R for ohmic circuit segment with resistance R; B I=U*R dimensional false, C U-R mixes V and Ω. For nonlinear branches Ohm form uses state-dependent resistance and 'Ohm law' as fixed R fails; original 'porțiune de circuit' convention assumes ohmic resistance.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

### G1-ELE-070 | DIRECT_AMMETER_SHUNT
- Question original: Extinderea domeniului de măsurare la ampermetre se realizează cu:
- A: rezistente adiţionale
- B: shunturi
- C: bobine înseriate
- Imported key **B**, UNCHANGED. Original source `ELECTROTEHNICA-09.2024-2.xlsx` row `77`.
- Technical reference: https://openstax.org/books/university-physics-volume-2/pages/10-4-electrical-measuring-instruments
- A/B/C counterfactual and exact model: B parallel low-ohmic shunt bypasses excess current around galvanometer to extend ammeter measuring range. A series additional resistor commonly voltmeter, C series inductor frequency-dependent and not normal DC range extension. For modern transformer clamps different measuring principles.
- `official_ANRE_exam_2026=NOT_VERIFIED`, `independent_QA=NOT_RUN`, `approved_for_learning=NO`.

## Reproducible model checks and handoff
- Poynting S=E×H vector sign (H×E flips direction).
- Ideal C: capacitor voltage lags current by π/2 and sum series voltage equals supplied terminal voltage.
- Three-phase star balanced Uline/Uphase=√3, Iline/Iphase=1.
- Inductor W=0.5 L i², conductor capacitor W=0.5 qV.
- Wire force B I l, perpendicular field; Kirchhoff V-loop and charge node.
- P2 verdicts are documentary and model checks, NOT exam-key approvals or human QA. Future check exact source for ZnO and reactive energy terminology; don't double count any cross-grade question duplicate. PR#7 Draft, no merge/release.
