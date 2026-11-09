# ANRE Trainer | V11 G2-ELEC-228–277 first-pass audit

Date 2026-11-09. Direct extraction from canonical GitHub blob `bc5b5a61954ba138cf83987bfc932eca517f3b21` `const DATA`: exact 50 existing IDs; enunțurile, ABC, răspunsurile și sursa originală incluse în CSV. Model-assisted technical/linguistic screen only; `independent_QA=NOT_RUN`, source page `NOT_VERIFIED`, 0 modifications.

Classes: PRINCIPLE=7; SAFETY_SOURCE=13; CONDITIONAL=12; FORMULA_CHECK=11; AMBIGUITY=7. Classes are review queue, **not approval**.

## Critical independent review gates

- **G2-ELEC-242:** „ele autopornesc, indiferent de tipul constructiv al rotorului” cannot guarantee restart regardless of load/protection/supply duration; highly conditional answer A.
- **G2-ELEC-247:** question says „În echipamentul electric, uleiul electroizolant, din punct de vedere electric”; option A „asigură doar izolarea” versus B „stinge arcul electric care apare în întrerupătoare”. For appropriate oil circuit breakers both are functions; original key A requires historical context, exact text and SME resolution.
- **G2-ELEC-266:** original key A contains exclusivity „numai”; option C may be possible in tests of isolated busbar; do not fix key without operating procedures and reviewed single-line diagram.
- **G2-ELEC-268:** „circuit monofazat cu caracter inductiv” voltage leads current by **angle φ ∈ (0,90°]**, not necessarily exactly 90°; original option A says 90°. A may be defensible only for ideal purely inductive circuit.
- **G2-ELEC-264:** option A's „doar” may omit isolating functionality; option B could also characterize use, requiring technical context.
- **G2-ELEC-262:** independent arithmetic check: `sqrt(100^2 + 70^2) = 122.0656 V` for ideal R+L series voltage phasors, matches rounded option C=122 V.
- **G2-ELEC-267:** `P=4 kW, Q=3 kVAr, S=5 kVA; cosφ=0.8`, matches A.
- **G2-ELEC-270:** `I=U/R=100/5=20 A`, matches A.
- **G2-ELEC-261:** DC RL charging current is `I(t)=U/R*(1-exp(-Rt/L))`, approaches U/R asymptotically, not instantaneously. Direct educational support: OpenStax *University Physics Vol. 2* §14.4 https://openstax.org/books/university-physics-volume-2/pages/14-4-rl-circuits . (Web source inspected; not a Romanian ANRE normative replacement.)
- **G2-ELEC-235:** `întotdeauna` in Kirchhoff must be scoped to lumped circuits; `G2-ELEC-274` uses `integral` despite finite leakage; `G2-ELEC-230` transformer overload only permissible under restrictions.

## Pending gate

Exact official technical/normative paragraphs and versions not confirmed for 50/50; source labels from XLSX are provenance, NOT technical proof. Independent electrical specialist and offline HTML/APK QA NOT_RUN. Nothing changed in original keys/app. Next nominal lot 278–327. All labels provisional.
