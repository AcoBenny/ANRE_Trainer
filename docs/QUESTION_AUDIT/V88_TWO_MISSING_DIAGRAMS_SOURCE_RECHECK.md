# V88 | G1-ELE-028 / G2-ELEC-177 | 2026-11-11

Scope: source recheck after CKPT-009, not application modification or approval. Two IDs share the exact original question and ABC; the technical evidence is assessed once and explicitly linked to both IDs, not counted as two independent experiments.

## Provenance and fresh observations
- Baseline HEAD `ceea23837613cb4a8bcd7d34aa39ae3dfe6c4433`; canonical application blob `bc5b5a61954ba138cf83987bfc932eca517f3b21` unchanged. Local HTML SHA256 `95be80e0dee42518ec821abc96e45777cbf32c4e2180a08da6b4f974e96c55d9` identifies the repository HTML, not the separately packaged standalone HTML hash quoted in older records.
- Historical user PDF `979902894-Captura-de-ecran-din-2024-11-09-la-14-15-06.pdf`, Library ID `libfile_2e5c4a90b8f0819181b339819291ffcd`, SHA256 `5df037a939b3bfc67a720a4a9face80520e266222c3ed6f1641c366ffbbaa8aa`. Physical page 10 rendered and visually inspected in this session. Row 28 includes a generator symbol feeding one busbar and three downward branches; the fault symbol is on the right branch. The question and ABC align semantically with both canonical IDs, source XLSX row35. Historical highlights are answer-bank annotations, NOT didactic proof or official ANRE certification. Printed date/edition of the underlying bank remains unestablished; filename is not edition proof. PDF/image not redistributed in GitHub.
- Both canonical DATA records contain no image/figure field. This is static data inspection, not an executed UI/device test; do not claim every renderer/runtime path was tested.

## Fresh primary didactic evidence
Schneider Electric Electrical Installation Guide, `Generator protection`, section `Short-circuit current protection`, subsections `Subtransient phase`, `Steady state phase`, `Calculating the short-circuit current`: https://www.electrical-installation.org/enwiki/Generator_protection (revision displayed 2026-08-05, oldid29798; accessed 2026-11-11). It distinguishes excitation, circuit impedance and subtransient/transient/synchronous reactances; field action is time-dependent. This does not prove an optimal network design for every generator.

Schneider Electric Electrical Installation Guide, `3-phase short-circuit current (Isc) at any point within a LV installation`, opening equation and `Method of calculating ZT`: https://www.electrical-installation.org/enwiki/3-phase_short-circuit_current_(Isc)_at_any_point_within_a_LV_installation (live unnumbered web edition, accessed 2026-11-11). It gives Isc=U20/(sqrt(3)ZT), ZT=sqrt(RT²+XT²), series reactances add. Source scope is LV method; extrapolation to unspecified voltage/optimal design is an engineering inference, not a normative rule.

## ABC and language adjudication (preliminary)
- A: reducing generator excitation can influence sustained fault current, but is not an immediate universal solution to the first subtransient peak; source distinguishes time periods. Cannot reject all physical effect of A. Wording asks what is preferable for the depicted circuit, not whether a method has any effect.
- B: inserting/increasing positive series inductive reactance between source and fault reduces prospective current for fixed source voltage, R and topology; follows from the equations. B is the supported candidate in the ordinary radial inductive-network reading. No quantitative optimum established and missing learner-facing diagram still blocks approval.
- C: increasing breaker breaking rating changes the capacity to interrupt a given current; it does not itself increase network impedance or reduce prospective fault current. Do not confuse rating with a separately specified current-limiting device's let-through performance.
- Triggers: `schema de mai sus`, `de preferat`; missing referent and comparative engineering criterion. Status `MISSING_FIGURE / CONDITIONAL_B_CANDIDATE`, canonical B retained for both.

## Remaining gates
Attach a provenance-approved diagram only in a later authorized implementation; independently review engineering preference, source scope and intended voltage; verify learner-facing rendering offline on HTML/APK when authorized. Independent model QA is a separate record V89 if executed. No human SME signoff, no official answer approval, no app/answer edits.
