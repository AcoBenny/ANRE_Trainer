# CKPT-231 | GFR close 12 remaining legacy-only P2 by source + historic crossgrade reuse | 2026-11-18

## Nonduplication strategy
- Full exact V73 original SHA `c027d417a8e4e605c830b2016fb55b099b8d130b`. These 12 still had `PREVIOUS_INDIVIDUAL_PRELIMINARY_NO_SIGNOFF` in source stage and no focused progress marker in V110. **Seven** have already investigated related question-level evidence elsewhere (explicit CKPT references) and are reconciled, not re-claimed as new independent source passes. **Five** cases newly examined with source/model comparisons and explicit limitations. All 12 still `approved_for_learning=NO`, `independent_QA=NOT_RUN`, imported keys not touched.
- No app, HTML, APK, main, PR merge/release. PR#7 Draft.

### G1-ELE-005 | EXISTING_CROSSGRADE_EVIDENCE_REUSE_CKPT216
- Original: A doua teoremă a lui Kirchhoff, pentru o reţea electrică cu N noduri şi L laturi (L diferit de N), ne furnizează, pentru analiza unui circuit electric:
- A: L+N-1 ecuaţii distincte
- B: L-N +1 ecuaţii distincte
- C: N-L+1 ecuaţii distincte
- Imported key **B** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `12`.
- Evidence/provenance: G2-ELEC-158, CKPT216.
- Source/model/negative alternative and missing-qualifier analysis: Connected graph: independent loops L-N+1; if disconnected with k components L-N+k. No change B; missing connected qualifier. A L+N-1 and C N-L+1 wrong under normal connected graph.
- Exact crossgrade QABC members: G1-ELE-005=B, G2-ELEC-158=B.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

### G1-ELE-010 | EXISTING_TECHNICAL_EVIDENCE_REUSE_CKPT217
- Original: Cele mai des utilizate pentru serviciile interne ale centralelor electrice sunt:
- A: motoarele de curent continuu
- B: motoarele sincrone
- C: motoarele asincrone
- Imported key **C** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `17`.
- Evidence/provenance: G2-ELEC-162, CKPT217.
- Source/model/negative alternative and missing-qualifier analysis: C asynchronous/induction auxiliary motors commonplace; A DC and B synchronous are special applications. 'Cele mai des' needs timeframe and plant equipment distribution; not universally counted.
- Exact crossgrade QABC members: G1-ELE-010=C, G2-ELEC-162=C.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

### G1-ELE-014 | EXISTING_BLOCKED_CASE_REUSE_CKPT184
- Original: Câmp fără surse este
- A: numai un câmp de curenţi de conducţie în regim staţionar
- B: câmpul electric
- C: câmpul de inducţie electromagnetică
- Imported key **C** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `21`.
- Evidence/provenance: CKPT184 source-scope.
- Source/model/negative alternative and missing-qualifier analysis: C induction electromagnetic field source-free in a specific Maxwell sense, A conduction steady current field uses a source in governing equation, B electric field not always without charge sources. Ambiguity induction vs electrostatic fields and fields in vacuum; no unique literal model authenticated.
- Exact crossgrade QABC members: G1-ELE-014=C, G2-ELEC-166=C.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

### G1-ELE-015 | EXISTING_CROSSGRADE_EVIDENCE_REUSE_CKPT217
- Original: Bobinele montate pe plecari radiale limiteaza curentii de scurtcircuit
- A: atat inainte, cat si dupa punctele lor de racordare la barele statiei;
- B: inainte de punctele lor de racordare la barele statiei;
- C: dupa punctele lor de racordare la barele statiei.
- Imported key **C** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `22`.
- Evidence/provenance: G2-ELEC-167, CKPT217.
- Source/model/negative alternative and missing-qualifier analysis: Feeder outgoing series current-limiting reactor limits fault current downstream. A both sides false, B only before reactor false, C after connection correct under line topology. Not a field switching instruction.
- Exact crossgrade QABC members: G1-ELE-015=C, G2-ELEC-167=C.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

### G1-ELE-021 | NEW_MATERIAL_COMPARISON_CONDITIONAL
- Original: Care dintre materialele electrotehnice admit o densitate de curent mai mare:
- A: aluminiu
- B: cupru
- C: ambele admit aceeaşi densitate de curent
- Imported key **B** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `28`.
- Evidence/provenance: https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance.
- Source/model/negative alternative and missing-qualifier analysis: Copper has greater electrical conductivity/lower resistivity vs aluminium and often permits higher allowable J at equivalent geometry/temperature/construction B intended. But 'admit density' is not a single intrinsic current density without thermal design, cooling, installation and loss criteria; A aluminum lower typical, C equal not general; source compares conductivity not cable ampacity tables.
- Exact crossgrade QABC members: G1-ELE-021=B, G2-ELEC-173=B.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

### G1-ELE-026 | NEW_SWITCHGEAR_COST_SCOPE_BLOCKED
- Original: Utilizarea unei cuple cu functiuni multiple se prefera atunci cand dorim
- A: scurtarea duratei manevrelor
- B: cresterea continuitatii  in alimentare
- C: reducerea investitiei in echiparea statiei.
- Imported key **C** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `33`.
- Evidence/provenance: https://eepower.com/technical-articles/substation-componentspart-5-busbar-configurations/.
- Source/model/negative alternative and missing-qualifier analysis: C multi-function bus coupler can in some topology avoid duplicated breakers/isolators/investment, but A maneuver duration and B continuity may also improve depending interlocks and scheme. The source is a general busbar article, not exact multifunction-coupler economics; no unique answer certified.
- Exact crossgrade QABC members: G1-ELE-026=C, G2-ELEC-175=C.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

### G1-ELE-031 | NEW_PREFAB_CUBICLE_SAFETY_CONDITIONAL
- Original: Celulele prefabricate monobloc se caracterizează în principal prin:
- A: securitate ridicată a persoanelor;
- B: gamă largă de configuraţii ale schemei de conexiuni;
- C: eliminarea totală a posibilităţii de producere a unui scurtcircuit între faze
- Imported key **A** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `38`.
- Evidence/provenance: https://www.ellevio.se/globalassets/content/materialspecifikationer/natstationer/prefabricated-secondary-substations-up-to-800-kva-and-switching-stations--general.pdf.
- Source/model/negative alternative and missing-qualifier analysis: A prefabricated monobloc switchgear constructed with barriers/interlocks can improve operating personnel protection; B wide configurations not always primary for monobloc modular units; C total removal of interphase faults is impossible. However 'mainly' not a measurable universal characteristic. Specification is product-family-specific, not proof of all prefabricated cubicles.
- Exact crossgrade QABC members: G1-ELE-031=A, G2-ELEC-180=A.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

### G1-ELE-051 | EXISTING_BLOCKED_RECIPROCITY_REUSE_CKPT189
- Original: Dacă o tensiune electromotoare E, montată în latura AB a unei reţele pasive, produce în latura CD a reţelei un curent I, montarea t.e.m. E în latura CD va produce în latura AB:
- A: un curent - (minus) I
- B: un curent I
- C: un curent I/2
- Imported key **B** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `58`.
- Evidence/provenance: CKPT189 source and reciprocity theorem.
- Source/model/negative alternative and missing-qualifier analysis: B reciprocity same transimpedance holds for *linear bilateral reciprocal* networks with consistent terminal orientations; original 'rețea pasivă' alone does not guarantee reciprocity, e.g. passive nonreciprocal gyrators. A negative sign depends orientations, C half unsupported. Key B not universally source-certified.
- Exact crossgrade QABC members: G1-ELE-051=B, G2-ELEC-197=B.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

### G1-ELE-053 | EXISTING_CROSSGRADE_SOURCE_REUSE_CKPT217
- Original: Funcţionarea în doua faze a unui transformator trifazat are ca efect:
- A: supraîncălzirea acestuia
- B: suprasarcina
- C: reducerea puterii tranzitate
- Imported key **A** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `60`.
- Evidence/provenance: G2-ELEC-199, CKPT217.
- Source/model/negative alternative and missing-qualifier analysis: A three-phase transformer with phase lost can overheat, but B overload of remaining phases and C transmitted capacity reduction can also be true depending connection/loading. No literal one-answer universal; linked expert case is conditional.
- Exact crossgrade QABC members: G1-ELE-053=A, G2-ELEC-199=A.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

### G1-ELE-057 | EXISTING_BLOCKED_SEMANTIC_CKPT184
- Original: Două funcţii periodice sinusoidale sunt armonice între ele dacă:
- A: raportul perioadelor lor este un număr întreg oarecare
- B: au aceeaşi perioadă
- C: raportul perioadelor lor este egal cu 1/2
- Imported key **A** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `64`.
- Evidence/provenance: CKPT184 harmonics.
- Source/model/negative alternative and missing-qualifier analysis: A periods integer ratio is a common harmonic definition but B equal periods also a ratio 1 and C 1/2 can describe octave harmonic pair (depending ratio orientation). Logical overlap: cannot certify A as only true response. No key changes.
- Exact crossgrade QABC members: G1-ELE-057=A, G2-ELEC-203=A.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

### G1-ELE-086 | NEW_EXACT_FARADAY_TRANSFORMER
- Original: Funcţionarea transformatoarelor electrice are la bazã:
- A: fenomenul inducţiei electromagnetice
- B: efectul termic al curentului electric
- C: curenţii turbionari
- Imported key **A** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `93`.
- Evidence/provenance: https://openstax.org/books/university-physics-volume-2/pages/15-6-transformers.
- Source/model/negative alternative and missing-qualifier analysis: A electromagnetic induction transfers voltage between transformer coils. B Joule heating dissipates power rather than transformer action, C eddy currents generally parasitic heating (cores laminated to reduce). Ideal core and changing flux; real DC transformer not sustained.
- Exact crossgrade QABC members: G1-ELE-086=A, G2-ELEC-231=A.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

### G1-ELE-087 | NEW_EXACT_HENRY_INDUCTANCE
- Original: Henry este unitatea de măsură pentru:
- A: fluxul magnetic
- B: inductanţă
- C: inducţia magnetică
- Imported key **B** unchanged. Source workbook `ELECTROTEHNICA-09.2024-2.xlsx` row `94`.
- Evidence/provenance: https://openstax.org/books/university-physics-volume-2/pages/14-1-mutual-inductance.
- Source/model/negative alternative and missing-qualifier analysis: B henry H is SI unit of inductance L/M, 1 H=1 V·s/A. A magnetic flux measured weber, C magnetic flux density tesla. Three alternatives dimensionally exclusive.
- Exact crossgrade QABC members: G1-ELE-087=B, G2-ELEC-232=B.
- Status NOT approved for learner, independent source/linguistic/technical review NOT_RUN, 2026 ANRE exam key NOT_VERIFIED.

## Aggregate ledger and scope gates
- 12 previously preliminary grade cards progressed to explicit evidence review or historical reuse. Of these, **5 newly source/model reasoned, 7 preexisting historical/crossgrade links** (not new audit work). Actual new bank questions=0, approved learner QABC=0, changed keys=0.
- Four dangerous ambiguity/scope risks: network connected for loop count, 'pasiv'≠reciprocal, 'armonic' overlapping B/C, transformer failure phases multiple outcomes. Do not silently mark such questions correct for exam training.
- Next: 446 remaining unfocused P2 grade ID entries from model note/crossgrade reuse; dedupe exact tuples before focused source checks to avoid inflated work, then independent QA and permission for grading changes. No app work.
