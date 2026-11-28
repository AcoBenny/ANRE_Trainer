# CKPT-320 | First remaining-semantic source reopens (5 cases) | 2026-11-21

## Boundaries and basis
- Parent commit `d2f7d40aa14dcd57cf84e864a80914ab4515e616`. Queue: `V242_136_UNIQUE_SEMANTIC_HOLD_PRIORITY_QUEUE_AFTER_CKPT319_2026_11_21.json`. Editorial source: V188 (QABC-0013), V198 (QABC-0024) and V199 (QABC-0025, QABC-0065, QABC-0082).
- **FIVE** QABC cases were newly reopened against external scientific/engineering reference material in this pass: QABC-0013, QABC-0024, QABC-0025, QABC-0065 and QABC-0082. These are a subset of the 15-member first nonstrict batch; its other 10 records remain queued for fresh source verification and cannot be reported as done.
- These records are NOT independent qualified reviews and do not establish official exam keys. All original question/ABC/grade key fields remain intact. All five remain semantic HOLD; **0/822 learner-approved**.

## QABC-0013 / G1-ELE-014, G2-ELEC-166: source-free field vs term «electromagnetic induction»
**Original ANRE 2024 editorial reference:** “Câmp fără surse este”, C “câmpul de inducţie electromagnetică”; both grade keys imported C.
- Maxwell Gauss magnetism: `∇·B=0` (equivalently closed-surface magnetic flux 0), whereas electric field E has `∇·E=ρ/ε0` for vacuum charges. This supports “inducția **magnetică B**” as source-free field in the divergence sense. It does **not** authenticate “câmpul de inducție **electromagnetică**” as synonymous with B. Wording differs from some secondary exam editions.
- A “numai un câmp de curenți de conducție în regim staționar”: `∇·J=0` holds for steady current, so there can be a source-free current field but “numai” makes A nonexclusive. B “câmpul electric” is source-free only in charge-free subregions, not a universal property.
- **Next context window:** OpenStax Maxwell §16.1, before: electric Gauss/source charge; focus: Gauss magnetic `∮ B·dA=0`; after: Faraday induction and distinctions. This is a *textbook context candidate* not a verbatim ANRE key or quotation.
- Verified references: https://openstax.org/books/university-physics-volume-2/pages/16-1-maxwells-equations-and-electromagnetic-waves ; https://openstax.org/books/calculus-volume-3/pages/6-5-divergence-and-curl .
- **Disposition:** `HOLD_ORIGINAL_TERM_EM_INDUCTION_NOT_EQUIVALENT_TO_B`; separate literal ANRE original from conceptual pedagogical exercise and authenticate official scoring.

## QABC-0024 / G1-ELE-028, G2-ELEC-177: omitted circuit figure
**Original question:** asks which short-circuit current limitation method is preferable for “schema de mai sus”; imported B increases reactance between source and fault.
- Analytical distinction: increasing source-to-fault impedance decreases prospective short circuit current under `I_sc≈U/Z` in simplified fixed-source model; higher breaker interrupting rating handles but does NOT itself lower prospective fault current. Lower excitation can alter source contribution. Hence B is **plausible conceptually**, but it cannot be endorsed as preferred for a particular **unavailable diagram**.
- Reopened exact original text in V198 and its provenance; the source diagram is NOT preserved within that text card. No authentic graphic was obtained in this source pass. Engineering reference candidate: https://www.electrical-installation.org/enwiki/3-phase_short-circuit_current_%28Isc%29_at_any_point_within_a_LV_installation
- **Source scope gate:** explicitly **BLOCKED_MISSING_AUTHENTIC_FIGURE**. Before/focus/after *visual* context needs the original diagram and adjacent prompt/caption, not invented circuit details. **No candidate key approval.**

## QABC-0025 / G1-ELE-029, G2-ELEC-178: exclusive «numai»
**Original:** “Curentul electric alternativ poate fi produs numai prin fenomene”; A thermal, B chemical, C electromagnetic induction; imported C.
- DOE explains that a semiconductor inverter converts **DC to AC by rapid electrical switching**. This is a positive counterexample to the claim that AC can **only** be produced by electromagnetic induction in an alternator. C describes a classic method, not all possible mechanisms.
- Source reopened: https://www.energy.gov/cmei/systems/solar-integration-inverters-and-grid-services-basics and https://www.energy.gov/cmei/systems/solar-systems-integration-basics .
- **Source window plan:** DOE surrounding explanation of PV-supplied DC and inverter function, focus on DC-to-AC switching, then grid integration. Textbook evidence is not an official exam key.
- **Disposition:** `HOLD_EXCLUSIVE_NUMAI_FALSE_IN_GENERAL`; if ANRE intended a restricted generator context it must be sourced or the wording defect acknowledged, not silently added as premise.

## QABC-0065 / G1-ELE-073, G2-ELEC-218: ambiguity E versus D
**Original:** “Fluxul electric total, produs de o sarcină electrică ... printr-o suprafaţă închisă” A=2q, B=q, C=q/2; imported B.
- In vacuum Gauss law for **electric field E**: `∮E·dA = q/ε0`; for **electric flux density D** in its applicable macroscopic free-charge convention: `∮D·dA = Q_free`. Therefore B=q maps to the D-flux convention, **not** to a universal unqualified E-flux equation.
- Independent *reference sources* were reopened (NOT reviewer independence): https://openstax.org/books/university-physics-volume-2/pages/6-2-explaining-gausss-law and https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Book%3A_Electromagnetics_I_%28Ellingson%29/05%3A_Electrostatics/5.05%3A_Gauss_Law_-_Integral_Form .
- **Disposition:** `HOLD_FLUX_QUANTITY_NOT_DEFINED`. Need original course's definition of “flux electric” and convention, including medium and free/total enclosed charge, before endorsing B. Context before/focus/after must anchor E versus D definitions.

## QABC-0082 / G1-ELE-090, G2-ELEC-234: resonance and energy accounting
**Original:** “În cazul apariţiei fenomenului de rezonanţă într-un circuit de curent alternativ ... sursa furnizează” A=only active, B=active and reactive, C=only reactive; imported A.
- In ideal linear **series RLC** sinusoidal steady-state at `X_L=X_C`, the net reactive power at source terminals cancels while average active power dissipates in R. Inductor and capacitor still exchange stored energy internally; this distinction is central. “Numai energie activă” is a statement about the **net source power exchange under a model**, not that reactive field energy ceases to exist.
- References: https://openstax.org/books/university-physics-volume-2/pages/15-5-resonance-in-an-ac-circuit ; https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit ; https://openstax.org/books/university-physics-volume-2/pages/15-key-equations .
- **Disposition:** `HOLD_RESONANCE_MODEL_AND_NET_ACTIVE_ONLY`. Need verify if exam question assumes sinusoidal ideal RLC steady state or alternative resonance, and whether “furnizează energie” refers to average/net power or instantaneous exchange.

## Bounded QA and next batch
- 5/130 remaining-semantic cases given fresh source-focused analysis; **125/130 still await first fresh source pass** after CKPT-319. The 6 strict cases were reviewed previously, separately and remain blocked.
- No case transferred to independent approval. The previous historical editorial coverage (568/568) is preserved; fresh source reopening here is not counted as new card creation.
- First batch nonstrict IDs still awaiting fresh source pass: `QABC-0019`, `QABC-0036`, `QABC-0044`, `QABC-0046`, `QABC-0050`, `QABC-0069`, `QABC-0080`, `QABC-0091`, `QABC-0092`, `QABC-0096`.
- Next: reopen remaining batch with exact scope and sources, prevent false universal claims, look for original embedded figure for QABC-0024; preserve the user-approved excerpt requirement before / **focus bold** / after for the future card integration.
- No barem, question, A/B/C, app HTML, APK or PR release changes.
