# CKPT-382 | GFR QABC-0143: "adimensională" source-native unit conflict, propagation constant

2026-11-22. Continued from CKPT-381/V292. Read-only research; no source, canonical answer, HTML/APK, or PR merge changes.

## Exact physically reopened original and IDs

User's original source binary `ELECTROTEHNICA-09.2024-2(1)(3).xlsx`, SHA-256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`, cell row 159:

> Mărimea **adimensională** care reprezintă variaţia pe care o suferă amplitudinea şi faza undei de tensiune sau curent când parcurge 1 km de linie (lungă ) se numeşte:

- A = `constanta de propagare a liniei`
- B = `constanta de atenuare a liniei`
- C = `constanta de distorsiune a liniei`.

Source route G1-ELE-152, canonical `QABC-0143`, imported A. Its **app canonical stem** changed **„adimensională”** to **„caracteristică”**. Original same source row and options also occur in G2-ELEC-290, *different canonical* `QABC-0568`, imported A, without stem rewrite. Source equivalence != canonical QABC identity.

This is already a known *material text difference* from V140 and P0 strict original-original mismatch from V283. New addition here is the **direct dimensional countercheck with university technical source and full A/B/C logic**, not a newly discovered data mutation or professional approval.

## Reopened university source with neighboring context

Virginia Tech ECE3105, *Chapter II, Transmission Lines – Wave Equations*, **chapter physical insight**:
https://www.courses.ece.vt.edu/ece3105/chp2.html

- Preceding mathematical context gives voltage waves `V(z)=V+e^{-γz}+V−e^{+γz}` and `γ=α+jβ=sqrt((R'+jωL')(G'+jωC'))`.
- Exact-dimension section directly identifies `γ` as the **complex propagation constant, m^-1**, `α` as attenuation in `Np/m`, `β` as phase constant `rad/m`.
- Following context explicitly applies `γ` to reflection and propagation over length `l`. The product `γ·l` in the exponential **is dimensionless**, but the *propagation constant `γ` itself* is not. This resolves the source's wording trap.
- More detailed adjacent explanation: https://courses.ece.vt.edu/ece3105/chp2_lssn2.html, `γ=α+jβ` (section "Physical Implications", before and after the definition).

Dimensional independent calculation: `R'+jωL'` has units Ω/m; `G'+jωC'` S/m; `sqrt((Ω/m)(S/m))=1/m`. For a 1-km route, `γ×(1 km)` is a dimensionless complex exponent; it is **not** a reinterpretation that makes `γ` dimensionless.

## Every original answer and mutual contrasts

- **A, preferred intended term**: propagation constant `γ=α+jβ` describes **both amplitude change** via `α` and **phase advance** via `β` per distance. The phrase "adimensională" in the original question conflicts with the technical *unit* of the named constant; it does not imply B/C are better.
- **B, rejected as the complete description**: attenuation constant `α` governs amplitude decay only and lacks the separate phase term `β`. Partial component of A, not sufficient for amplitude+phase.
- **C, rejected without stronger exact-scope technical definition**: "distortion constant" is not the standard single complex propagation coefficient combining attenuation and phase. Distortion across frequencies can result from frequency-dependent `α` and `β`, but it is not an exact synonym of `γ` in the cited lecture.
- A/B: B partial, missing phase; A/C: distortion a different multi-frequency concept; B/C: attenuation vs distortion not the full complex propagation rate. The original dimensional adjective makes the *stem* internally inconsistent; classify as **LINGUISTIC_AND_DIMENSIONAL_TRAP**, not an automatic wrong-key proof.

## Didactic card draft, **paraphrase**, not licensed original quote

- Context before: In a distributed transmission line, voltage/current vary with distance; their forward/backward wave solutions involve an exponential `e^{±γz}`.
- **Central focus:** **`γ=α+jβ`; `γ` is measured in inverse length, `α` attenuates amplitude and `β` changes phase. Thus answer A names the full parameter, but the original adjective `adimensională` is physically inaccurate.**
- Context after: Only the **product `γ·z`** inside the exponential is dimensionless. The source's fixed 1 km is not a license to delete the inverse-length unit of `γ`.

No source license permissions for long verbatim passages are asserted. Original exam Q/A remains untouched; explanatory text is original paraphrase.

## Gate / state

- Original XLSX provenance **REOPENED**; candidate answer A **TEXTBOOK_SUPPORTED_WITH_STEM_UNIT_AMBIGUITY**.
- Technical and linguistic **independent professional reviewer NOT RUN**; applicable ANRE 2026 exam edition and official scored key **NOT VERIFIED**.
- Same original row in G1/G2 must not be double-counted as an independent physical source verification.
- A, B, C imported choices unchanged; user interpretation not demanded at this preliminary scientific level.
- All 822 learner approvals still 0. PR #7 remains Draft. CKPT-381 and V292 are retained, not superseded.
