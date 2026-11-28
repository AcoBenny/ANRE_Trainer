# V23 | ANRE Trainer 822-ID coverage QA and release gate

**Date:** 2026-11-09. **PR:** #7 Draft; branch `audit/anre-v8-priority-17-20261109`. Canonical V10.29: GitHub `app/src/main/assets/anre_trainer.html`, blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`; 822 unique original IDs (G2=408, G1=414). No barem/HTML/APK or release changed.

## Audit coverage by evidence maturity
| Tier | Count | Interpretation |
|---|---:|---|
| G2 and first 50 G1 electrotechnic original-question technical/linguistic model screens | 381 | **Preliminary** physical reasoning, with many exact source pages missing |
| G2 legal/norm historical-version preflight | 77 | Text, category, legal edition, distractor flags; **not** every legal article independently confirmed |
| G1 exact cross-grade text+ABC parity, inherited evidence | 204 | Textual equivalence only, no fresh technical/source approval. One contradictory answer group within these 204 |
| G1 other language/source-risk preflight | 160 | 100 norms, 50 legislation, 10 distinct electrotechnics; **not** proof of correctness |
| **Total** | **822** | **Coverage complete, validation incomplete** |

Deterministic QA: V20 ledger 822 rows, V21 204, V22 160; V21 and V22 sets disjoint, neither overlaps 458 previously screened IDs, exactly fill 364 gaps; V23 822-row ledger read back from GitHub. Strict per-ID independence signoff **0**, release-ready **0**. Source version/page for many IDs pending. Type-safe comparison preserves numeric `A=1, B=0` for G2-ELEC-292 (CSV uses string render); no data edit.

## Critical conflicts/risks
1. Cross-grade exact enunț+ABC but different answer: `G1-ELE-018` A=3C vs `G2-ELEC-170` C=C. Scribd educational course *Rețele Electrice Cursuri Examen* page 36 (text index, non-official) derives equivalent capacity `Cs=3 C_ff+C_p` in balanced regime; with ground neglected implies 3C **if** C12 et al mean same partial phase-to-phase capacitance. Must verify original publication, definition/diagram, teacher SME; no edit: https://fr.scribd.com/document/569579955/Retele-Electrice-Cursuri-Examen
2. Cross-grade identical `G1-ELE-102` A=one busbar live/other cold reserve vs `G2-ELEC-245` C=both busbars live/coupler warm reserve. A historical `ELECTROTEHNICA-09.2024` question sheet (text index) favors A, but both are possible station configurations; „de preferat” needs design objective, one-line diagram and normative procedure. Historical source: https://www.scribd.com/document/844724316/ELECTROTEHNICA-09-2024 ; definition of warm/cold reserve: https://legislatie.just.ro/Public/FormaPrintabila/00000G34SH9QJKVGLBH05IRU059X7NKC
3. Six V13 tracker-vs-canonical key conflicts `G1-LEG-024/028/032/034/048`, `G2-ELEC-170` remain in quarantine. Some official law sources favor the old tracker, but neither workbook key nor original app changed.
4. G2-ELEC-358: susceptance `B=-X/(R²+X²)` rather than general `1/X`. Exact academic reference https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electricity_and_Magnetism_%28Tatum%29/13%3A_Alternating_Current/13.06%3A_Admittance .
5. Missing referenced figures G1-ELE-028 and G2-ELEC-177; do not approve learner-facing UI.
6. Strong answer-position leak: 77/77 G2 legislation/norm and 50/50 early G2 electrotechnical concept questions have original A keys. Quiz randomization should preserve answer mapping and needs explicit product approval before implementation.
7. G1-NOR 100 questions require item-specific I7-2011 **with 2023 changes** (Official Order 959/2023: https://legislatie.just.ro/Public/DetaliiDocument/271142 ); historical 2011 source alone may be stale. Also G2-LEG-081/082 tariff-date-sensitive.

## Team and independent QA honesty
Romanian Language Reviewer role applies mandatory `anre-question-bank-qa` checklist, Electrical Engineer/Normative Source Auditor applies `anre-source-audit`, data QA uses deterministic ID/key/option checks. These **are roles/checklists coordinated in this model**, not real separately executed subagents. Independent human or separate model QA is NOT_RUN. Actual HTML/APK offline integration checks were NOT_RUN.

## Next sequence without user loop
- Resolve 2 cross-grade contradictions with source editions and independent specialist; reconcile V13 six conflicts without touching barem.
- Link every candidate to didactic exact passage including edition/page and offline rights. Prioritize safety-critical G1 norms, electrical faults/relay procedures, and questions with absent figures.
- Then independent QA of per-item conclusions and execute actual HTML/APK offline regression; gate user approval for any barem/app edits or merge/release.
- Continue documentation/checkpoints in PR #7 only, maintaining source and key immutable until explicit approval.

**Nothing here authorizes a changed answer or production release.**
