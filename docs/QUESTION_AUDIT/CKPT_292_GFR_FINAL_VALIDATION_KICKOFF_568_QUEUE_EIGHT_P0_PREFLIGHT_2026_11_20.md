# CKPT-292 | Final-validation kickoff: 568-QABC workqueue, eight original-source P0 preflights | 2026-11-20

## Outcome / user scope
- User asked to **start** the final validation without restarting ANRE auditing. **Actually executed:** V149 baseline structural audit, created V151 complete read-only final-review queue, reopened actual original electrotechnics XLSX for eight cases, obtained source-conditioned technical counterexamples, created V152 eight-case structured review cards, ran 15 deterministic assertions on actual re-fetched GitHub contents, all PASS. **No independent qualified reviewer ran.** Therefore preflight started; *content final signoff has not been achieved*.
- Exact baseline `V149_568_QABC_FINAL_GATE_PROVENANCE_BIAS_AND_CHALLENGE_2026_11_20.csv` blob `ee2ac5536c78eb06a0461243be34c117e257188f`, counted **568 unique QABC, 822 unique grade IDs**. Existing baseline fields `technical_qa=NOT_RUN`, `linguistic_qa=NOT_RUN`, `source_qa=NOT_RUN`, `human_signoff=NOT_RUN`, `approved_for_learning=NO` in **all 568**. These fields faithfully report that the prior source research does not equal independent QA.
- Existing 6 strict blockers / 9 grade placements retain their version-separated source research in `V150_SIX_STRICT_BLOCKERS_CKPT289_291_VERSIONED_RESEARCH_OVERLAY_2026_11_20.json` (no original or imported keys changed). Technical research of these six does not resolve their *official scoring* and human-review dependencies.

## New V151 | complete working queue
- [V151 568 QABC final validation read-only CSV](V151_568_QABC_FINAL_VALIDATION_READONLY_WORKQUEUE_2026_11_20.csv) Git blob `a233c6744a68af16ed434a0b1574ed33ba53061e`.
- 568 records, 822 ID placements, all original imported letters and source-workbook locator fields **identical to V149**. Each has an explicit validation lane, prior research state, outstanding review step and unmodified learner gate.
- **Mutually exclusive queue lanes (count in distinct QABC groups):**
  - L0: 6 **strict source/version/key adjudication holds**, remain blocked from learner approval.
  - L1: 8 **actual original-source source-conditioned pilot cases**, not approved.
  - L2: 55 **remaining P0** for independent professional option/linguistic review.
  - L3: 1 **numeric cell type only** source-import issue, still requires technical review.
  - L4: 348 **ordinary exact-copy** cases pending independent review.
  - L5: 150 **nonworkbook didactic/provenance** practice cases to establish original author and correct edition before review, including position-bias challenge.
- **Lane counts are not the same as original provenance classes**: the 153 nonworkbook cases include 3 prioritized P0 cases in L2 and 150 in L5. Original exclusive provenance classes stay **408 exact source-copy, 6 strict, 1 numeric-type, 153 nonworkbook** = 568. This distinction prevents accidentally reporting 150 as the full didactic item count.
- `P0` includes 65 groups total in V149: six original strict blockers intersect P0, pilot eight and remaining L2 55 grouped by explicit lane; lane classification is priority plus provenance, not answer approval.
- No new original 2026 answer-key source discovered on the official public ANRE exam information page. Official exam page **publishes syllabus and examples** but does not directly authenticate each imported answer letter in our master: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ .

## New V152 | eight actual original-source cards
- [V152 first eight P0 source/model/negative-test cards](V152_EIGHT_P0_FINAL_VALIDATION_PRELIMINARY_SOURCE_CARDS_2026_11_20.json) Git blob `81310d1245a4dce93b251b6ea695c8f9b26f34b7`.
- Reopened original user-uploaded file `ELECTROTEHNICA-09.2024-2(2).xlsx` from conversation container, unchanged SHA-256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`. Verified actual A:D values at rows 120,135,187,196,227,229,236,252. V152 stores exact originally imported A/B/C and grade IDs from pinned V149, not guessed source text. Original workbook has no scored key field.
- **8 QABC / 16 grade IDs**: `0104` Joule heat vs ambient (C conditional), `0119` RL non-pure phase (`phi=45°` counterexample, stored A only ideal-L), `0169` eddy losses (B practical construction, A/C potentially mitigating too), `0178` electrostatic potential (A direct work/charge unit support), `0209` conventional AC instrument transformers and modern DC device terminology (A scoped), `0211` susceptance (generic B=-X/(R²+X²), not 1/X), `0218` fuse overcurrent protection (B concept but instantaneous-prevention wording inaccurate), `0234` unity power factor (input can be resistive at RLC resonance despite L+C elements; A depends on *equivalent input* versus pure-R components).
- **Math negative tests actually run**:
  1. RL `R=XL=1Ω -> atan(1)=45°`, not mandatory 90°.
  2. Susceptance `R=X=1Ω -> B=-1/(1+1)=-0.5S`, not `1/X=+1S`.
  3. Resonant series `R=10Ω, XL=XC=5Ω -> PF=cos(atan(0/10))=1` despite reactive components.
  4. Joule `I=2 A, R=5Ω -> I²R=20W`.
- External technical evidence for each original source/card is linked **inside V152**. No PDF material or textbook copyrighted content redistributed into repository.
- Eight cards are **one assistant's source-conditioned technical/linguistic research plus deterministic negative cases**, NOT distinct agent executions, authenticated source edition or independent qualified reviewer signoff. `independent_technical_QA=NOT_RUN`, `independent_linguistic_QA=NOT_RUN`, `approved_for_learning=false` on all eight.

## Verified QA on current repository content
- **15/15 true, 0 failures**, performed with explicit assertions against freshly fetched **V149, V151 and V152 GitHub blobs**, not just checking commit successful:
  1. V149 count 568;
  2. V151 count 568;
  3. V151 822 distinct grade IDs;
  4. all imported keys identical to V149;
  5. all source workbook locators identical to V149;
  6. all V151 learner approvals still NO;
  7. all V151 technical/linguistic QA still NOT_RUN;
  8. pilot 8 cards;
  9. pilot 16 grade ID placements;
  10. each pilot source row/question/A/B/C/key exactly equals matching V149;
  11. no pilot learner approval and no independent technical/linguistic signoff claimed;
  12–15. four actual physics/arithmetic calculations listed above.
- **Scope of tests:** structural, provenance integrity and numerical falsification. They do **not** certify ANRE key correctness or official bibliography edition, and are **not GitHub CI tests**.

## Next shortest independently useful path
1. Continue **L2 remaining P0, batches of 8–12**. Reopen a distinct existing analysis/source per QABC and check its grade/edition, then run actual independent technician+linguistic reviewer with A/B/C and negative tests; preserve any contestable preflight until source authenticated. Do not re-count V152 as final review.
2. Separately ask an authentic authority/reviewer for the **six L0 original version/key mismatches**. Where official grade answer cannot be authenticated, keep original exam-sample item unapproved, even if a pedagogical correction is technically clear. The researcher can work on other lanes in parallel to that human gate, but no autonomous background claim.
3. Once all required original-source QA/release gates are independently signed, update the master via explicitly authorized, reviewed versioned changes (not silently now). Then test HTML/APK offline; no merge/release without user approval.

**Frozen invariants: 568 original QABC, 822 grade IDs, key/option order intact, no HTML or APK modifications, no GitHub merge, 0 learning approvals, PR #7 and PR #13 Draft.**
