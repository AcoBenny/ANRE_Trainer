# CKPT-235 | GFR 2026-11-18 P2 evidence sweep, audited readback summary

## Initial and ending ledger
- Baseline `V106_GFR_822_ID_P1_EVIDENCE_RECONCILED_CKPT224_226_2026_11_18.csv` blob `06b6dd9ac8478a7c91f53074a4756033780a3307`.
- Final audited `V114_GFR_P2_15_MORE_PHYSICAL_QABC_EXACT_GRADE_REUSE_2026_11_18.csv` blob `110f1ce427953cc239a92c768682047fef339a49`.
- Programmatic **row-by-row comparison of the two 822-ID registers against V73 original**:
  - **193 previously unfocused Grade-specific IDs now with evidence linkage.**
  - **98 previously unfocused Grade I unique QABC received newly written per-card focused source/math/linguistic checks** in CKPT-227,229,230,231,232,233,234.
  - **4 historically reviewed but still listed unfocused Grade I cases now linked to old detailed source investigations** (CKPT-184/189/217), NOT new source checks.
  - **91 Grade II grade-record references reused matching exact original (question,A,B,C,imported key)** or history, NOT genuine separately performed independent source reviews. Direct per-grade source reopen was not performed by this reuse.
  - **325 P2 Grade IDs without focused evidence**, comprising Grade I **136**, Grade II **189**; previously **518**. The rest of ledger has documentary or historical reference statuses and must not be labeled automatically "learner approved".
  - **822 distinct grade IDs, 0 imported barem/key differences vs V73, 0 modified risk priorities, 0 approved-for-learning rows, 0 key-change-authorized rows.**
- Earlier `V107` overlay was incorrectly joined by a numeric G1-to-G2 offset. **V107 invalidated and superseded by V108**, as documented in CKPT-228. V108 onward reconstructed from clean ledger and requires matching exact QABC **and** key; no canonical data ever changed.

## Material source/answer risks newly surfaced
- G1-ELE-005 / G2-ELEC-158: independent Kirchhoff loops L-N+1 require graph **connectedness**, otherwise L-N+k.
- G1-ELE-007: slip 0..1 applies ordinary motor mode, not generator or plugging modes.
- G1-ELE-049: AC proximity-effect crowding at outside conductor edges; stem does not specify AC so literal DC counterexample.
- G1-ELE-099: imported A says automatic restart for all short-circuit-rotor motors on voltage return, without specifying **control/contactors/undervoltage interlocks**, and is not generally safe or true. Keep blocked.
- G1-ELE-100: imported A presupposes bypass/coupler scheme absent from stem; no unique operation verdict without station single line.
- G1-ELE-104: imported A says dielectric oil **only** electrical insulation; oil circuit breakers can use oil to quench arcs. Stem does not identify apparatus; alternate B contextually also true, no key signoff.
- G1-ELE-118: 3-phase fault generally largest but low zero-sequence impedance may allow SLG fault larger; `de regulă` matters.
- G1-ELE-120: 100V resistor and 70V ideal inductor in series -> 122.065V phasor result, only if inductor is pure and waveform assumptions hold.
- G1-ELE-127: P=4kW Q=3kVAr -> pf=4/sqrt(16+9)=0.8.
- G1-ELE-130: R=5Ω, U=100V -> I=20A.
- G1-ELE-115: flux linkage λ=NΦ, self-inductance L=λ/I not single-turn Φ/I without turns.

## Evidence integrity and release gate
- Original CKPT cards retain original question/options and key, provenance and one or more academic/technical/official evidence URLs. The source class ranges from official I7/legal primary text to open textbooks/manufacturer equipment docs to secondary articles; **never equate them with ANRE official examination answer key**.
- "Source checked" means a targeted source and A/B/C/model comparison by the **same assistant**. It does **not** mean independently cross-validated by a second expert/human or that the current examination bibliography edition is authenticated.
- No edits to app HTML/APK, canonical question/answer source, main, or any PR merge/release.
- PR #7 should remain **Draft, open, unmerged**. A separate real Android app QA and integration phase is suspended per user until the entire QABC bank is independently approved.
- Next phase: keep selecting disjoint remaining P2 distinct QABC in batches <=15, use exact source-object/edition gate, resolve material key conflicts before anyone studies from the app. Do not send per-lot approvals to user; collect only actual decisions that cannot be settled from evidence.
