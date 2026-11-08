# ANRE Trainer | Audit didactic Batch003, no implementation | 2026-11-08

**Current gate:** [audit first, implementation frozen](AUDIT_FIRST_RELEASE_GATE_2026-11-08.md). No changes to 822 data records, official keys, HTML, APK or PDF assets. No new checkpoint: [LATEST](CHECKPOINTS/LATEST.md) remains CKPT-002.

## Verified scope and progress
- Continued from [Batch002](DIDACTIC_AUDIT_BATCH002_NO_IMPLEMENTATION_2026-11-08.md), where 100 actual Grade II electrotechnics IDs had initial audit.
- **50 more actual IDs** `G2-ELEC-178..227` were inspected for likely original didactic PDF pages.
- Of these new 50: **17** model-inspected page principles (A), **11** page-plus-assumption/derivation (B), **13** topical-only candidates (C), **9** with NO adequate local page (U). No A/B/C is independently approved source proof.
- **Cumulative 150/822** IDs reviewed; **138** have local source page candidate or multi-page derivation, **12** remain unlocated/insufficient, **672** not yet mapped. **Independent source approvals: 0.**
- A previous topical reference for `G2-ELEC-012` was corrected to actual **PREG PDF page 132**, where `f=1/T` is written explicitly. Same direct reference found for `G2-ELEC-227`.
- For `G2-ELEC-208` `W=LI²/2` at PREG p.63 and `G2-ELEC-204` `U_line=√3·U_phase` at UTCN p.66, formulas were visually inspected, as the PDF text extraction was lossy.

## High-priority previous blockers
- `G2-ELEC-177`: **original diagram RECOVERED** in *user-uploaded* `979902894-Captura-de-ecran-din-2024-11-09-la-14-15-06.pdf`, **physical PDF p.10, question 28** (SHA256 `5df037a939b3bfc67a720a4a9face80520e266222c3ed6f1641c366ffbbaa8aa`). Shows generator, bus and three outgoing circuits, with fault mark. Marked choice **B** in user-provided historical PDF. Local technical textbook `337393907-Cartea-Electricianului-Din-Statii-Si-PT-uri12.pdf`, **physical PDF p.373**, explains increasing reactor impedance to limit short-circuit current. Diagram is still MISSING from app DATA; do NOT modify app during freeze. PDF marking is not independently certified official answer key.
- `G2-ELEC-170`: candidate **conditional technical derivation** from PREG p.89 (`Xc=1/(ωC)`), UTCN p.66 star (`U_l=√3 U_f`) and p.68 delta (`I_l=√3 I_f`). With three equal phase-phase capacitances and no earth influence, `I_l=√3·(ω C U_l)=3ω C U_f` → equivalent `Cs=3C`. Local evidence now exists as a *multi-source derivation*, not an actual textbook paragraph stating that formula. Requires independent review of assumptions/definition. External university context: https://cadredidactice.ub.ro/mihaipuiuberzuntiu/files/2012/05/BethSLP.pdf (2013 Bacău electrotechnics, §1.3.3 capacități în serviciu).
- `G2-ELEC-166`: **external** university source, not one of uploaded manuals: https://www.fizica.unibuc.ro/Fizica/Studenti/Cursuri/Docs/SA_Electrostatica%20-%20Cursuri%201-3.pdf . Explains Gauss law for magnetism `div B = 0`; magnetic field has no isolated polar sources. Neither an official ANRE answer key nor licensed offline material.
- `G2-ELEC-172`: **external** technical descriptions of isolated-phase GIS. IEC 62271-203:2022 identifies single-phase separate enclosures; Siemens explains prevention of phase-to-phase faults **within the enclosed equipment**. `eliminarea totală` may be overbroad outside this scope; keep linguistic QA flag. Sources: https://standards.iteh.ai/catalog/standards/clc/69ec8103-3522-4394-9ad8-6ddf96b05d9/en-iec-62271-203-2022 ; https://www.siemensgovt.com/assets/documents/white-papers/isolated-phase-medium-voltage-switchgear.pdf . No redistribution rights confirmed.
- `G2-ELEC-161`: **potential scope conflict**. Current key C excludes the resistor as voltage-regulation equipment *in power networks*, while PREG p.42 explicitly treats a variable-voltage resistor/potentiometric circuit and PREG p.184 uses resistor-based excitation rheostats for generator voltage regulation. Distinguish power-system network control from generator excitation. Do not change key without a specific source and technical reviewer.

## New 50 ID / page / QA-tier crosswalk
Tiers: A page directly supports principle in model-assisted review; B requires explicit hypothesis/calculation; C is only same topic; U exact local source unavailable. Full original-answer text, OCR candidate scores and per-ID notes stay in conversation audit package, NOT committed here. Source page refers to 1-based physical PDF page of user upload.

| ID | Candidate source PDF page | Status |
|---|---|---|
| G2-ELEC-178 | PREG 86 | B: word 'numai' overgeneralizes source |
| G2-ELEC-179 | PREG 214 | C |
| G2-ELEC-180 | I7 179 | C |
| G2-ELEC-181 | MAS 10 | B |
| G2-ELEC-182 | STATII 274 | B |
| G2-ELEC-183 | STATII 590 | C |
| G2-ELEC-184 | MAS 115 | C |
| G2-ELEC-185 | PREG 23 | A: Coulomb 1/r² |
| G2-ELEC-186 | — | U: τ=RC needs exact transient-circuit text |
| G2-ELEC-187 | STATII 590 | C |
| G2-ELEC-188 | PREG 89 | B: Z=5Ω, I=44A |
| G2-ELEC-189 | — | U: generator stator current claim depends on load |
| G2-ELEC-190 | — | U: incandescent lifetime vs voltage not found |
| G2-ELEC-191 | — | U: convection current definition missing |
| G2-ELEC-192 | IEC 224 | B: nonlinear load harmonics, exact case pending |
| G2-ELEC-193 | PREG 87 | C |
| G2-ELEC-194 | PREG 87 | C |
| G2-ELEC-195 | — | U: current proximity effect missing |
| G2-ELEC-196 | — | U: Poynting vector S=E×H missing |
| G2-ELEC-197 | UTCN 74 | C |
| G2-ELEC-198 | PREG 88 | A: capacitor phase angle |
| G2-ELEC-199 | PREG 207 | C |
| G2-ELEC-200 | STATII 302 | B: generic arresters; ZnO specificity pending |
| G2-ELEC-201 | STATII 302 | B |
| G2-ELEC-202 | PREG 50 | B: KVL applied to series capacitors |
| G2-ELEC-203 | — | U: exact harmonic function definition missing |
| G2-ELEC-204 | UTCN 66 | A: balanced star relation visually checked |
| G2-ELEC-205 | IEC 416 | C |
| G2-ELEC-206 | MAS 220 | C |
| G2-ELEC-207 | PREG 209 | C |
| G2-ELEC-208 | PREG 63 | A: W=LI²/2 visually checked |
| G2-ELEC-209 | PREG 31 | C |
| G2-ELEC-210 | STATII 373 | B |
| G2-ELEC-211 | PREG 23 | A: conservation of electric charge |
| G2-ELEC-212 | PREG 50 | A: Kirchhoff 2 |
| G2-ELEC-213 | PREG 57 | A: electromagnetic force BIl |
| G2-ELEC-214 | PREG 40 | A: I=U/R |
| G2-ELEC-215 | PREG 137 | A: ammeter shunts |
| G2-ELEC-216 | PREG 135 | A: voltmeter additional resistors |
| G2-ELEC-217 | — | U: RL attenuation factor missing |
| G2-ELEC-218 | PREG 32 | A: electric flux Gauss |
| G2-ELEC-219 | — | U: bundled conductors and corona losses not sourced locally |
| G2-ELEC-220 | MAS 66 | B: n=60f/p rearranged |
| G2-ELEC-221 | PREG 63 | B: Faraday general, specific e=Blv pending |
| G2-ELEC-222 | PREG 57 | A: electromagnetic force |
| G2-ELEC-223 | PREG 58 | A: electrodynamic force between conductors |
| G2-ELEC-224 | PREG 63 | A: Faraday induction law |
| G2-ELEC-225 | PREG 58 | A: force inverse to conductor separation |
| G2-ELEC-226 | PREG 30 | A: F=qE |
| G2-ELEC-227 | PREG 132 | A: f=1/T |

## Next actions and QA
- AGENT-031 linguistic warning candidates: `G2-ELEC-161` (“nu se folosește”), `172` (“eliminarea totală”), `178` (“numai”), `189` (“direct proporțional”), `192` (“întotdeauna” vs “depinde”). Nothing is automatically proven an intentional trap.
- Confirm exact physics and answers where source page is A or B, review external-source licensing/version, and consider requesting additional teaching manuals once gaps are enumerated.
- Continue next existing IDs after 227, no fictional ID fill-ins, no key changes, no UI/standalone/APK.
- Independent electrical QA: **NOT_RUN**; independent language model/agent QA: **NOT_RUN**; rights clearance: **NOT_CLEARED**; actual offline app runtime: **NOT_TESTED**; cost increase: **0 lei**.
