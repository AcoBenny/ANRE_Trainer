# CKPT-188 | Exact PECS Romanian textbook coupler roles: superseding six existing QABC cases | 2026-11-17

## New decisive source and context
Directly reopened Romanian *Comanescu & Costinas, PECS: Note de curs*, searchable HTML transcription: https://www.academia.edu/25952537/Partea_electrica_a_centralelor_si_statiilor. Relevant §3.5.4 compares multifunction and individual couplers; §3.6.1 treats double main bus with transverse coupler and one breaker per circuit; §3.6.2 treats combined longitudinal-transverse coupler in sectioned main buses. These are distinct objects, and each question is matched to its actual context. Exam applicability 2026 and original official ANRE grading answer keys NOT confirmed.

### Explicit supersession of previous overly broad inference
CKPT-186 hypothesized that bypassing a line breaker through a transverse coupler always needs a distinct bypass/transfer bus, thereby making G1-ELE-126 option B possibly true. PECS §3.6.1 refutes this universal restriction in its exact scheme. That paragraph lists **four functions** (testing isolated-bus insulation by controlled energization, reassigning circuits, parallel energized buses, breaker bypass with brief interruption). Historical CKPT-186 is kept; this record **supersedes only the unjustified universal assumption**. A course source is not an official 2026 ANRE approved answer key, and no live switching instruction is given.

## Six original QABC checks, no editing

### G1-ELE-026 | COUPLER_COMBINED_COST_SOURCE_DIRECT
- Existing unit `AU-da0512acac25df72`, QABC SHA `da0512acac25df7260c2943413ebadcae76c6b5947c2aafb9a8ab7cc1995cc33`, original grade keys G1-ELE-026=C, G2-ELEC-175=C **PRESERVED**.
- **Question original:** Utilizarea unei cuple cu functiuni multiple se prefera atunci cand dorim
- **A:** scurtarea duratei manevrelor
- **B:** cresterea continuitatii  in alimentare
- **C:** reducerea investitiei in echiparea statiei.
- **Source/condition vs ABC:** PECS §3.5.4 compares multiple dedicated couplers with a combined multifunction coupler: reduced operational flexibility in exchange for lower capital investment. A shorter operations possible but no global source guarantee; B greater continuity not demonstrated; C reducing investment directly supported.
- **Exact source and neighbor:** PECS §3.5.4 with neighboring §3.5.3 and §3.6.1. https://www.academia.edu/25952537/Partea_electrica_a_centralelor_si_statiilor
- **Source-supported candidate:** C, NOT_APPLIED; status `SOURCE_SUPPORTED_DIDACTIC_NOT_EXAM_KEY_SIGNOFF`. Corrects earlier provisional interpretation (CKPT138) but retains prior evidence and source limitations.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official ANRE 2026 exam bibliography and graded key NOT_VERIFIED.

### G1-ELE-246 | LONGOTRANSVERSE_BAREM_B_CONFLICT_C_CANDIDATE
- Existing unit `AU-bfa0211e53d3d4a0`, QABC SHA `bfa0211e53d3d4a0058258d83ce3639d129a72f9a577a36025d8cd35a36640c0`, original grade keys G1-ELE-246=B, G2-ELEC-382=B **PRESERVED**.
- **Question original:** Utilizarea unei cuple longo-transversale se preferă atunci când dorim:
- **A:** scurtarea manevrelor;
- **B:** o siguranţă în funcţionare mai mare;
- **C:** reducerea investiţiei în echiparea staţiei.
- **Source/condition vs ABC:** Earlier B higher reliability was plausible only as generic statement, now contradicted as the *reason for choosing a multifunction longitudinal-transverse coupler over separate couplers*: PECS §3.6.2 explicitly notes economy at cost of less flexibility. A shorter maneuvers not stated; B greater operational safety not supported by this comparative reason; C lower capital cost matches.
- **Exact source and neighbor:** PECS §3.6.2 with §3.6.1; scope comparative coupler, not generic longitudinal sectionalization. https://www.academia.edu/25952537/Partea_electrica_a_centralelor_si_statiilor
- **Source-supported candidate:** C, NOT_APPLIED; status `BLOCKED_DIRECT_DIDACTIC_C_VS_IMPORTED_B`. Corrects earlier provisional interpretation (CKPT138) but retains prior evidence and source limitations.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official ANRE 2026 exam bibliography and graded key NOT_VERIFIED.

### G1-ELE-122 | BUSBAR_DISCONNECTOR_ISOLATION_AND_SELECTION
- Existing unit `AU-dac8a21bd3faca36`, QABC SHA `dac8a21bd3faca36f265a1fb2834735d1476c8c95e4f5b5db3684f800544f235`, original grade keys G1-ELE-122=A, G2-ELEC-264=A **PRESERVED**.
- **Question original:** Într-o schemă electrică prevăzută cu mai multe sisteme de bare colectoare, separatorul de bare
- **A:** asigură doar selectarea sistemului de bare pe care urmează a fi conectat circuitul;
- **B:** asigură izolarea unei părţi a circuitului de bara colectoare aflată sub tensiune;
- **C:** comutaţia curentului în regim normal de funcţionare.
- **Source/condition vs ABC:** PECS §3.6.1: busbar disconnector both selects busbar system AND isolates associated circuit. A claims «doar selectarea» and is therefore restrictive; B isolation from energized bus is a function, with proper off-load/interlocked condition; C load-breaking current in regular operation is not its ordinary duty.
- **Exact source and neighbor:** PECS §3.6.1 with §3.5.4; do not confuse simple isolator with circuit breaker. https://www.academia.edu/25952537/Partea_electrica_a_centralelor_si_statiilor
- **Source-supported candidate:** B, NOT_APPLIED; status `BLOCKED_DIRECT_DIDACTIC_B_VS_IMPORTED_A`. Corrects earlier provisional interpretation (CKPT185) but retains prior evidence and source limitations.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official ANRE 2026 exam bibliography and graded key NOT_VERIFIED.

### G1-ELE-124 | TRANSVERSE_COUPLER_INSULATION_TEST_SUPPORTED
- Existing unit `AU-9ad47849152dd1ab`, QABC SHA `9ad47849152dd1ab6b37eee33a7ad703861d878a1209963d357c4538c968b515`, original grade keys G1-ELE-124=A, G2-ELEC-266=A **PRESERVED**.
- **Question original:** Într-o staţie cu două sisteme de bare colectoare, cupla transversală:
- **A:** se poate utiliza numai pentru cuplarea în paralel a celor două sisteme de bare colectoare care sunt sub tensiune;
- **B:** nu se poate utiliza pentru ocolirea unui întreruptor de linie pe durata unei revizii sau reparaţii;
- **C:** se poate utiliza pentru verificarea stării izolaţiei unui sistem de bare colectoare, care până în momentul respectiv a fost scos de sub tensiune.
- **Source/condition vs ABC:** PECS §3.6.1 lists four functions of transverse coupler in the double-bus one-breaker scheme: insulation test of previously isolated bus, reassigning circuits, parallel energized buses, bypassing a circuit-breaker with short interruptions. A says «numai» parallel and thus false; B 'cannot bypass' false for given scheme; C test insulation by energization is true.
- **Exact source and neighbor:** PECS §3.6.1 exact four functions, next paragraph §3.6.2 distinguishes longitudinal-transverse couplers. https://www.academia.edu/25952537/Partea_electrica_a_centralelor_si_statiilor
- **Source-supported candidate:** C, NOT_APPLIED; status `SOURCE_SUPPORTED_C_NOT_EXAM_KEY_SIGNOFF`. Corrects earlier provisional interpretation (CKPT186) but retains prior evidence and source limitations.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official ANRE 2026 exam bibliography and graded key NOT_VERIFIED.

### G1-ELE-125 | TRANSVERSE_COUPLER_BYPASS_SUPPORTED
- Existing unit `AU-9688f38d9257eb2b`, QABC SHA `9688f38d9257eb2b1a9ce8194ceb27480138dd617f37e83957407afa230657ca`, original grade keys G1-ELE-125=B **PRESERVED**.
- **Question original:** Într-o staţie cu două sisteme de bare colectoare, cupla transversală:
- **A:** nu se poate utiliza pentru cuplarea în paralel a celor două sisteme de bare colectoare care sunt sub tensiune;
- **B:** se poate utiliza pentru ocolirea unui întreruptor de linie pe durata unei revizii sau reparaţii;
- **C:** se poate utiliza numai pentru verificarea stării izolaţiei unui sistem de bare colectoare, care până în momentul respectiv a fost scos de sub tensiune.
- **Source/condition vs ABC:** Previous assumption that B requires dedicated transfer bus was too general. PECS §3.6.1 explicitly includes bypassing a line breaker by transverse coupler with short interruptions. A says cannot parallel energized buses, false for suitable synchronized scheme; B bypass possible; C «numai» insulation check contradicts other listed functions.
- **Exact source and neighbor:** PECS §3.6.1 exact object, not a generic switchyard. https://www.academia.edu/25952537/Partea_electrica_a_centralelor_si_statiilor
- **Source-supported candidate:** B, NOT_APPLIED; status `SOURCE_SUPPORTED_B_NOT_FINAL`. Corrects earlier provisional interpretation (CKPT186) but retains prior evidence and source limitations.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official ANRE 2026 exam bibliography and graded key NOT_VERIFIED.

### G1-ELE-126 | TRANSVERSE_COUPLER_PARALLEL_SUPPORTED
- Existing unit `AU-c9c9ff229afe157a`, QABC SHA `c9c9ff229afe157a2f55a7e5f8e62db4c5c5df4bdc0e92aa4bee4d5747850796`, original grade keys G1-ELE-126=A **PRESERVED**.
- **Question original:** Într-o staţie cu două sisteme de bare colectoare, cupla transversală:
- **A:** se poate utiliza pentru cuplarea în paralel a celor două sisteme de bare colectoare care sunt sub tensiune;
- **B:** nu se poate utiliza pentru ocolirea unui întreruptor de linie pe durata unei revizii sau reparaţii;
- **C:** nu se poate utiliza pentru verificarea stării izolaţiei unui sistem de bare colectoare, care până în momentul respectiv a fost scos de sub tensiune.
- **Source/condition vs ABC:** PECS §3.6.1 explicitly permits parallel tie, bypass and insulation check. A parallel buses possible with synchronism/protection; B cannot bypass false in exact described scheme, and C cannot insulation-test false. This replaces CKPT186 generic bypass-bus assumption while retaining old QA.
- **Exact source and neighbor:** PECS §3.6.1 and neighboring §3.6.2. https://www.academia.edu/25952537/Partea_electrica_a_centralelor_si_statiilor
- **Source-supported candidate:** A, NOT_APPLIED; status `SOURCE_SUPPORTED_A_NOT_FINAL`. Corrects earlier provisional interpretation (CKPT186) but retains prior evidence and source limitations.
- `approved_for_learning=NO`; independent technical/source/linguistic QA NOT_RUN; official ANRE 2026 exam bibliography and graded key NOT_VERIFIED.

## Regression and QA
- Original question, A/B/C and imported key strict equality against V73 **6/6 unique units, 10 grade IDs**, zero differences. Original SHA/units inherited, not rehashed. All cases **already inventoried** in the 568/822 research phase, no new question credit.
- New source-specific provisional conflicts: **G1-ELE-246 imported B vs course C; G1-ELE-122 imported A vs course B; G1-ELE-124 imported A vs course C**. Original compatible: G1-ELE-026 C, G1-ELE-125 B, G1-ELE-126 A. No automatic key edits.
- Access: text version of original course readable, printed illustrations/schematics not visually authenticated separately; bibliography/current validity and independent reviewer remain blocked. Preserve and link all prior CKPTs rather than overwriting them.
- All study gates NO, PR #7 Draft; no original QABC, barem, HTML, APK, main, merge or release changes.
