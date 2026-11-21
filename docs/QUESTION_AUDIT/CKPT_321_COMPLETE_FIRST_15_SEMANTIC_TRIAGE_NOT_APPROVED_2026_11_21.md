# CKPT-321 | First 15 nonstrict semantic-hold cases: candidate technical/context triage | 2026-11-21

## QA scope
- Parent `154cd8863893ff3f7603705081bfae220665bef1`. Queue V242 was constructed from V241, no duplication. First 15 nonstrict records in V242 are QABC-0013, 0019, 0024, 0025, 0036, 0044, 0046, 0050, 0065, 0069, 0080, 0082, 0091, 0092, 0096.
- **CKPT-320** reopened external sources for 0013, 0024, 0025, 0065, 0082. **This CKPT-321** performs source/counterexample **triage** for the other 10. The **full first 15** now have a *new focused source-readiness disposition*, but **NONE** have qualified independent source+technical+linguistic approval or authenticated ANRE scored key.
- Triage statuses below are conservative. An authoritative product page can demonstrate a model/counterexample without authenticating a QABC grade-specific exam answer or offering a normative applicable-2026 clause.
- No app, original workbook question/options, imported keys or grade routes modified. PR #7 stays Draft.

## Remaining ten QABC: exact wording hazards, option distinctions, source readiness

### QABC-0019 / G1-ELE-020, G2-ELEC-172: monopolar GIS enclosure
- Original A (both grades imported) says monopolar encapsulation **completely eliminates** possibility of interphase short-circuits. Separate single-phase enclosures can isolate phase conductors within the enclosed GIS zone; this alone does **not** prove that a phase-to-phase fault is impossible at external terminations, connections, or elsewhere in an installation.
- B gas-loss rate and C cheaper installation are not guaranteed by phase enclosure; construction-specific. Manufacturer confirms single-phase-encapsulated GIS exists, but does not certify universal zero interphase faults.
- Reference: https://www.hitachienergy.com/uk-ie/en/products-and-solutions/high-voltage-switchgear-and-breakers/gas-insulated-switchgear/gis-for-72-5-1200-kv/gis-blf-pass-up-to-170-kv
- **Disposition** `HOLD_ABSOLUTE_TOTAL_FALSE_SCOPE_P0_SOURCE_MODEL_INCOMPLETE`. Require exact equipment configuration, definition of “eliminarea totală”, and manufacturer failure-mode evidence. No signoff.

### QABC-0036 / G1-ELE-043, G2-ELEC-189: generator stator current `I`
- Imported A says stator current grows **directly proportionally** to line-to-line voltage. Balanced steady three-phase apparent power satisfies `|S|=√3 U_LL I` and `|S|=√(P²+Q²)`. At *fixed S*, current is **inversely** proportional to voltage. At fixed voltage, both P and Q contribute; B’s “numai cu puterile active” excludes Q. C can be conditionally true in limited models but not a direct universal law if P varies.
- Textbook context: Springer chapter on three-phase AC power https://link.springer.com/chapter/10.1007/978-3-031-69856-9_8 . Need separate generator impedance/excitation and constant-variable hypotheses for physical device.
- **Disposition** `HOLD_MISSING_CONDITIONS_NO_UNIVERSAL_DIRECT_PROPORTIONALITY`, imported A retained, not validated.

### QABC-0044 / G1-ELE-051, G2-ELEC-197: reciprocity of passive network
- Imported B (current I transferred on interchange of source and measurement) follows the **reciprocity theorem in reciprocal linear networks**, with consistent port references; it does not follow merely from the word “rețea pasivă”.
- Bell Labs describes an ideal **passive gyrator that violates reciprocity**, a positive counterexample to passivity implying reciprocity. A negative current requires reference conventions; C I/2 cannot be inferred either.
- Source: https://www.nokia.com/bell-labs/publications-and-media/publications/the-ferromagnetic-faraday-effect-at-microwave-frequencies-and-its-applications-the-microwave-gyrator/
- **Disposition** `HOLD_PASSIVE_NOT_EQUIVALENT_TO_RECIPROCAL`. Need source or syllabus explicitly delimiting passive bilateral R/L/C networks and port orientations. No signoff.

### QABC-0046 / G1-ELE-053, G2-ELEC-199: three-phase transformer “operating on two phases”
- Original A overheating, B overload, C less transferred power; imported A. The event depends on whether one primary supply conductor opens, primary connection (delta/wye), secondary loading, upstream/downstream protections and delay. Overheating, winding overload and lower total transferable power are not mutually exclusive outcomes. Generic single-phasing references concern 3-phase systems, not necessarily the exact transformer.
- Candidate context, **NOT direct exact-scope proof:** https://www.jsdpower.com/news/News/Technical-Guide/What-happens-to-a-3-phase-transformer-when-one-supply-phase-is-lost.html
- **Disposition** `BLOCKED_EXACT_TRANSFORMER_CONNECTION_AND_SOURCE_SCOPE`: cannot exclude B and C under all regimes. Do not promote generic motor single-phasing data to transformer source authority.

### QABC-0050 / G1-ELE-057, G2-ELEC-203: harmonic sinusoidal signals and period ratios
- Imported A “ratio of periods integer” may describe nth harmonic if first/second sequence and fundamental choice are specified. But B “same period” is already n=1 (first harmonic), and C T1/T2=1/2 is the reciprocal ordering of a 2:1 harmonic period pair. The three alternatives are not necessarily logically disjoint.
- Source: university physics harmonic expansion and n=1 first harmonic https://mochizuki-tus.github.io/UnivPhys_Textbook_EN/ch17_superposition_fourier.html ; additional definition https://www.uwgb.edu/fenclh/problems/waves/standing-waves/2/
- **Disposition** `HOLD_HARMONIC_DIRECTION_AND_NONEXCLUSIVE_OPTIONS`. Need precise convention for “armonice între ele” and whether fundamental n=1 included.

### QABC-0069 / G1-ELE-077, G2-ELEC-222: force on a current-carrying conductor in B field
- Imported A “forță electromagnetică (Laplace)” directly matches established field-force `F=I l×B` for straight wire, with orientation. B “forță electrodinamică” sometimes denotes forces between interacting current circuits, potentially overlapping in certain terminology; C “forță magnetomotoare” concerns magnetic excitation, not mechanical force.
- Sources: Politecnico di Milano research https://re.public.polimi.it/handle/11311/1233539 ; OpenStax §11.4 https://openstax.org/books/university-physics-volume-2/pages/11-4-magnetic-force-on-a-current-carrying-conductor . These demonstrate physical relation, **not Romanian exam term-uniqueness**.
- **Disposition** `HOLD_TERMINOLOGY_LAPLACE_VS_ELECTRODYNAMIC`. Need edition-specific Romanian engineering glossary.

### QABC-0080 / G1-ELE-088, G2-ELEC-233: GIS compartmentalization and defect incidence
- Imported A says compartments limit **possibilities of producing a fault**; actual segmentation may isolate *location/consequences* of an internal arc rather than unconditionally decrease fault initiation probability. B leak risk may increase with added seals but depends on quality; C more gas handled per isolated compartment is not necessarily true.
- Hitachi technical monitoring describes identifying **which gas compartment** contains a detected internal arc, evidence of localization, not of guaranteed lower fault initiation: https://www.hitachienergy.com/in/en/products-and-solutions/high-voltage-switchgear-and-breakers/monitoring-and-controlled-switching/modular-switchgear-monitoring-msm
- **Disposition** `HOLD_FAULT_PROPAGATION_VS_PRODUCTION_MODEL_SCOPE`. Source exact model and interpretation of “producere” required.

### QABC-0091 / G1-ELE-099, G2-ELEC-242: asynchronous motor automatic restart after voltage loss
- Imported A “autopornesc, indiferent de tipul rotorului” is **not universally true** after supply restoration; actual restart depends on contactor/control circuit, undervoltage protection, permissive logic, inertia/load and restoration timing. B “necesită dispozitiv de pornire” is true for some starter circuits; C double-cage rotor “numai” is an unjustified exclusive claim.
- Actual Schneider motor controllers offer configurable automatic restart and selectable timeouts: https://www.productinfo.schneider-electric.com/tesys_t_user_guides/doca0127-tesys-t-ltmr-motor-management-controller-user-guide/English/BM_TeSys%20T%20LTMR%20User%20Guide_53457272_T001010654.xml/%24/CHP_MotorProtectionFunctions_53457272_T001010712 . Two-wire starter without hold-off may auto-restart on restoration, but this is not every installation: https://www.se.com/uk/en/faqs/FA147367/
- **Disposition** `HOLD_RESTART_DEPENDS_ON_CONTROL_NOT_ONLY_ROTOR`. Need the original syllabus's assumed starter/control regime and safety exceptions.

### QABC-0092 / G1-ELE-100, G2-ELEC-243: both busbars energized, expected advantage
- Imported A emphasizes reduced time for bypassing a circuit breaker. Original B concerns loss of supply in one bus fault, C shorter work when a busbar is maintained. Without a specified bypass/transfer-bus topology and protection scheme, the alternatives are not all falsified by the generic statement “two energized busbars”.
- Manufacturer technical engineering handbook documents materially different **double-busbar** and **transfer-bus** arrangements, showing why exact same topology must be established before answering: https://library.e.abb.com/public/7dca4ffad2206d36c1257be30048d4be/DAHandbook_Section_3_Power_distribution_systems_757959_ENa.pdf . A third-party design article also distinguishes bus fault/transfer consequences: https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/
- **Disposition** `HOLD_DOUBLE_BUS_VS_TRANSFER_BUS_CONFIGURATION`. No inference that a particular advantage is unique for unspecified bus arrangement.

### QABC-0096 / G1-ELE-104, G2-ELEC-247: insulating oil, electrical functions, key-risk escalation
- Original A “asigură **doar** izolarea părților sub tensiune”, B “stinge arcul electric care apare în întrerupătoare”, C mechanical lubrication. Both grade imported keys **A**. The *unqualified* “doar” of A is particularly problematic if the field includes **oil-filled circuit breakers**, where insulating oil is also an arc-quenching medium. The literal B is a valid electrical function **in the specified type of breakers**; not a universal claim about all switches.
- IEEE Technology Navigator, topic “Oil insulation”, explicitly describes mineral insulating oil in high-voltage equipment, transformers and **circuit breakers**, around both energized parts and arc-quenching contacts: https://technav.ieee.org/topic/oil-insulation/ . IEC 60422:2024 metadata/source description lists dielectric insulation, cooling and arc-quenching functions: https://www.standards.iteh.ai/catalog/standards/iec/3d40aa70-83c0-4000-82e3-61486cb21885/iec-60422-2024
- **Disposition** `P0_CANDIDATE_LITERAL_IMPORTED_A_CONTRADICTED_BY_OIL_BREAKER_SOURCE_B`. This is an **escalation within the existing semantic 136**, NOT a claim that the historic six strict-count has been formally enlarged. Verify exact “ulei electroizolant” intended equipment scope, original wording, authentic exam scored key and qualified reviewer before any key change.

## First nonstrict-batch readout, no approval
- **15 / 15 source-readiness triage records** handled across CKPT-320 and CKPT-321 (initial five plus ten above). This means *risk categorization and candidate-source reopening*, **NOT independent final validation**.
- Existing 136 total semantic holds and 6 historic strict holds remain; 15 of the 130 nonstrict subset now have updated source-readiness dispositions. **115 of the nonstrict 130 are not yet newly screened in this session.**
- Priority queue V242 is preserved as historical snapshot. Any follow-up checkpoint must refer to this delta, not blindly claim those 15 “awaiting first review”.
- Important new *candidate escalation*: QABC-0096 oil-arc dual electrical role; do not alter historic strict six until independent adjudication or validated taxonomy change.
- Remaining 115 source-ready queue in V242 begins with the next batch after priority #21. All **0/822** final approved, no app/HTML/APK/keys changed.
- Context display requirement stands: same source edition, **before → focus (bold) → after**, exact locator; keep A/B/C editorial reasons separately, no fabricated source excerpt.
