# CKPT-015 | DEEP-NOR-01 + DEEP-LEG-01 | 40-case source/ABC triage | 2026-11-11

**Repo:** AcoBenny/ANRE_Trainer. **PR #7 Draft**. **Branch:** `audit/anre-v8-priority-17-20261109`. Continues CKPT014, preserving CKPT011 routing, CKPT012 recovery and CKPT013 partial initial investigations.

## Real work this session
1. `DEEP-NOR-01`: **20/20 pre-review source+ABC research records**, 16P0+4P1, source/edition/option-specific caveats. QA structural **PASS 20/20**. See [CKPT014](CKPT_014_DEEP_NOR_01_ALL20_RESEARCH_TRIAGE_AND_QA_2026_11_11.md) and [NOR20 CSV](DEEP_EXECUTION_2026_11_11/DEEP_NOR_01_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv).
2. `DEEP-LEG-01`: **20/20 pre-review source+ABC research records**, 10P0+10P1. **NEW deterministic QA actually executed** after GitHub commit: all20 have unique IDs, exact original question/A/B/C/keys vs V73, correct AU+SHA/manifest batch/P0/P1, complete source locator/ABC reasoning/next gate, 22 columns each, all `independent_review=NOT_RUN` and `approved_for_learning=NO`. **PASS 20/20**. [LEG20 CSV](DEEP_EXECUTION_2026_11_11/DEEP_LEG_01_ALL_20_PRE_REVIEW_SOURCE_ABC_TRIAGE.csv).
3. GitHub PR #7 was read as Draft/unmerged and canonical HTML SHA remains `bc5b5a61954ba138cf83987bfc932eca517f3b21`. Only audit documentation changed, not question/ABC/key/HTML/APK.

## Major findings from official indexed texts, NOT yet legally finalized

| ID | Stored key | Research finding | Gate |
| --- | --- | --- | --- |
| G1-LEG-015 | B | Legea123 art92(1) says unauthorized modification of components of energy installations (B) is **criminal**, not a contravention. A may be contravention, requires art93 exact actor/situation | Legal2026 exact + distinct reviewer |
| G1-LEG-019 | C | Legea123 art93(1) expressly includes failure to comply with ANRE technical norms as **contravention B**, not merely `abatere` C | Legal2026 exact + reviewer |
| G1-LEG-026 | C | Legea123 art92(2) categorizes clandestine installations for direct hookup as **infracțiune B**. `Contravenție sau infracțiune după caz` overgeneralizes that specific offense | Legal2026 exact + reviewer |
| G1-LEG-034 | B | Reg66/2023 art37(e) requires obeying project (**A**); participation in reception/PIF required **if requested** art37(h), while B wrongly says even without request | Current regulation + reviewer |
| G1-LEG-048 | A | Legea123 art57(2) says household clients may choose among payment methods offered by supplier (**B**); cannot impose any method not offered | Legal2026 exact + reviewer |
| G1-LEG-017/032 | B/B | Previous CKPT012/013 identified theft/termination and 5y visa vs4y contradictions, now indexed within LEG20 data | Current edition/complete sanctions + reviewer |
| G1-LEG-002 | B | Theft proven by judgment is a legal termination ground, **but** option C about a 30-day overdue unpaid bill may also enter broader nonpayment ground | Semantic exclusivity and 2026 procedure |
| G1-LEG-020/028 | A/B | Appeals of ATR and location of individual meters have edition, technical scope, or procedural ambiguity | Applicable regulations, type of housing, independent review |

**Source openings:** Portal Legislativ `/DetaliiDocument/300063` etc generally indexed but direct full article opens could fail502 in this environment. Earlier CKPT012 visually checked official gazette hosted by PPC regulation, not July2026 consolidated law. The **exact full selected legal consolidation as of 26.07.2026 has not been verified**. Reuse earlier evidence with its edition; do not label old source 2026 verified.

## Correcting previous reasoning, not source data
- **NOR032**: original stored B supported by PE155/1992 §3.2.10 for 15m horizontal branch-column boxes. Historical V33 selected generic I7 §5.2.12.3.10 for25m pulling boxes and incorrectly concluded no option. Retain this source mismatch as Avengers QA negative benchmark.
- **NOR029**: 2.5m is exception for homes in I7 §5.3.3.21 (candidate C) but 2m and 2.3m can also fit the literal `not exceed`; answer is not uniquely established without revised wording.
- **NOR089**: I7 §5.1.4.3.3 directly supports single phase-wire color with both ends identified (candidate B vs stored A).
- **G2-NOR-137/141/145**: answer options give codes, while stem asks approval act. Prior V41 finding still unresolved. No credit double counted.

## Exact QA/approval status
- **40 source+option triage records** cover the complete **two 20-unit first batches**, but **0 batches closed**, **0 units independently certified this session**, **0 questions approved for training**.
- Mechanical QA ran and PASSed for both 20-record CSVs, not for physical/technical/legal correctness. Deep validator `deep_audit_execution.py validate` intentionally **not run** because independent reviewer and full edition/exam sources are absent; this is correct gate behavior.
- No separate persistent AI reviewers were actually launched. Avengers specialist roles operated as expert review lenses within one assistant, not genuinely independent agents or human certification.

## Next actions (no new setup)
1. Assign true distinct review to all 40 records (first priority NOR089,NOR029,NOR032,NOR027; LEG019,026,034,048,015), reopening the *exact* technical and legal source, and record verified source date/edition and comparison of every A/B/C. Source/edition blockage remains blockage.
2. Obtain legally applicable 2026 Art92/93, Art57/58 and Reg59/Reg66 texts in verified full form, plus PE155/PE102 authenticated edition; adjudicate ambiguous multiple-true questions and apply exact corrections **only after user approval**.
3. Build complete `DEEP-NOR-01.json` / `DEEP-LEG-01.json` **after separate review** with real reviewer evidence, run structural validator. Continue `DEEP-ELE-01`, `DEEP-ELE-02` and remaining batches; do not silently mark queue COMPLETED.
4. All 822 questions remain barred from learner release pending final quality gates. No main merge or APK/HTML changes.
