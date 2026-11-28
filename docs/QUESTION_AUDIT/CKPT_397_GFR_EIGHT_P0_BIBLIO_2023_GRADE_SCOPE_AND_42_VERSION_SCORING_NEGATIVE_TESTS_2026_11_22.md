# CKPT-397 | GFR ANRE eight historic P0 blockers: direct ANRE bibliography and source-versus-Trainer negative scoring gates

Date: 2026-11-22. Continues CKPT-396. PR #7 Draft on `audit/anre-v8-priority-17-20261109`. This checkpoint is research and read-only QA documentation. No canonical original XLSX, scoring key, canonical QABC/grade IDs, HTML, APK, main, merge or release modified.

## What was actually completed in this session

### V334 | Source-exact version and score identity preimplementation negative gate
- [V334](./V334_SOURCE_EXAM_TRAINER_7_FIDELITY_DELTAS_42_SHUFFLE_FAIL_CLOSED_2026_11_22.json) reopens **V140** physical source-to-master differentials for **seven grade routes** and compares the original question, original A/B/C, edited trainer stem/options and frozen imported answer letter in six displayed-option permutations for each route.
- **7 routes:** **5 material semantic/text mutations** and **2 numeric-cell datatype-only differences**.
- For **4 material routes**, the selected imported letter denotes **materially different answer-option text in the original source and edited trainer**; the fifth material case changes the stem. These 5 source-vs-trainer differences are structural BLOCKS for direct exact-exam import.
- **42/42 deterministic simulated permutation checks** completed. **30/42** permutations are material-version blocked, and **24/42** have mismatched keyed option text. These test a *reference data identity condition*, NOT the real HTML/APK runtime or truth of either imported key. The remaining 12 datatype-only permutations still need faithful number display/regression and official-key QA.
- Two **exact shared-QABC grade-specific imported-key conflicts** remain: `QABC-0017` G1 A vs G2 C, `QABC-0094` G1 A vs G2 C; same stem and original options in each pair. Never store a globally shared QABC answer letter as if it were authenticated for both grades.
- Mandatory future architecture: `EXAM_ORIGINAL` records the true original workbook stem and A/B/C separately from `DIDACTIC_CORRECTED`; scorer must be keyed by grade route + explicit item version + immutable original choice identity. Neither currently source-authenticated official key nor release permission exists.

### V335 | Direct source-version/grade applicability evidence
- [V335](./V335_OFFICIAL_ANRE_2023_GRADE_I_BIBLIO_PE102_NOT_INCLUDED_PE155_I7_INCLUDED_2026_11_22.json) fetched directly the **official ANRE 05.2023 bibliography PDF** from https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf , PDF content type, HTTP 200, parsed original row table.
- Explicit table entries: **I7-2011 §14 Grade I DA / Grade II DA**, **PE 102/1986 §22 Grade I NU / Grade II DA**, **PE 155/1992 §29 Grade I DA / Grade II DA**. This directly supports an earlier suspected G1 bibliography exclusion for PE102.
- This is verified for the **2023 officially published table as parsed**, not independently certified as the exact **2026 exam** edition. The ANRE electricity landing page (reviewed now) still visibly links the 2023 bibliography under 2026 event notices, but visibility alone does not certify session-specific applicability.
- `G1-NOR-027 / QABC-0341`: direct copied PE102/1986 §4.6.3 text matches original source **A** connecting feeders to contact screws, but **PE102 is not a Grade-I listed 2023 norm**. Relevant Grade-I I7-2011 §5.3.4.3.1.2 says phase to fuse-holder **central contact**. Mechanical terminology equivalence 'șuruburile de contact' ↔ 'contact central' remains unverified; don't convert a related I7 clause to source-exact exam proof.
- `G1-NOR-053 / QABC-0367`: PE155/1992 §1.2.1 source PDF defines whole branșament through customer's internal installation, observation places demarcation at **meter output terminals**; §1.2.2 defines **racord electric** only from line to firidă. This supports source **C** as better exact-object candidate than imported A, but C omits **de ieșire**, and historical official scored key is not proven.
- Both third-party PE PDF texts were retrievable in web PDF index (with line references), but **visual page screenshot returned cache miss**, and direct container network download failed. Do not say their original page images were authenticated. Official ANRE bibliography PDF text table parsed successfully, **its page image also NOT visually checked**.

## Eight preexisting historic P0 research holds remain (no fake closure)

| QABC | Remaining exact gate after this session |
|---|---|
| 0017 | Cs=3C model researched in CKPT-374; G1 A vs G2 C imported keys without official grade-specific score authentication |
| 0094 | One-breaker double-bus operating-policy / preference criterion unresolved; G1 A vs G2 C |
| 0143 | Original 'adimensională' vs edited Trainer 'caracteristică'; gamma has inverse-length units |
| 0236 | Original B 'inducție electromagnetică' vs edited B 'electrostatică'; static E does not imply Faraday magnetic induction |
| 0288 | Request for grid connection at new sites vs obtaining ATR for **every** site, special/exceptional scopes unresolved |
| 0341 | PE102 literal source A, but grade-I 2023 bibliography excludes PE102; I7 contact central vs contact screws needs physical terminal equivalence |
| 0367 | PE155 branșament full vs racord only; missing 'output' qualifier in C and formal key provenance |
| 0386 | Original B 'without tool' contradicts I7 'only with tool'; current Trainer B rewritten, source original C factually true but shorter |

These are **8 QABC groups / 11 grade routes** from CKPT-371, not eight new discoveries. They were all preliminary-source researched before this checkpoint; this session adds fresh source-grade and scoring-version safety evidence. All 28 current P0 routes across 24 QABC remain **unapproved**.

## Counts, safety and next productive finite step

- Legacy canonical: **568 QABC / 822 grade routes**, 0/822 independently approved.
- Staged Grade II original recovery: **157 source candidates**, 0/157 independently approved; still quarantined.
- Existing P0: **28 routes** (27 historical plus one later legal overlay); professionally adjudicated **0/28**.
- App real UI scoring, webview/offline APK test: NOT RUN. Prior 4,932 permutation simulations and current 42 reference version gates do not stand in for app QA. No original key or app data mutated.
- **Next**: secure an actual independent qualified reviewer and original official scoring-key provenance where possible; separately verify specific 2026 exam bibliography and correct source-edition scope. Until then, use V334 version-lock rules for any reversible integration planning, *not* as authority to merge/release. Continue source research on 8 high-risk original P0 as evidence permits, but do not needlessly re-run CKPT-374 mathematical proof.
- Exactly as before: **no merge, no release, no import of 157 candidates, no learning approval, no HTML/APK/key changes.**
