# CKPT-416 | Pilot B: 3 strict conflicts with direct I7/physics clauses

Date 2026-11-23 | Parent CKPT-415 | Audit branch PR #7 Draft | **Do not restart V371 re-index queue**.

| QABC | Imported key unchanged | Direct-source A/B/C verdict (NOT official scoring key) | Owner/reviewer gate |
|---|---|---|---|
| QABC-0236 | G1 B, G2 B | ORIGINAL B «inducţie electromagnetică» is not electrostatic polarization. TRAINER B «inducţie electrostatică» describes polarization, not necessarily net charging. OpenStax §5.2 Figs 5.10–5.13. | Mark source-original ill-posed vs corrected unofficial Trainer, decide policy; independent review |
| QABC-0362 | G1 A | OFFICIAL I7 §5.4.13 explicitly accepts lighting, socket, or panel. ORIGINAL A «numai direct» is invalid; ORIGINAL C is allowed; TRAINER A lists all three and is supported. | Approve explicit key-conflict annotation for ORIGINAL, not silent key change |
| QABC-0386 | G1 B | OFFICIAL I7 §5.5.2.3 requires individually disconnectable AND only with tool. ORIGINAL B says without tool (contradicted), ORIGINAL C true partial; TRAINER B complete, TRAINER C true partial too. | Mark source-original key conflict and Trainer B/C overlap; owner and independent QA |

## Real-source evidence and surrounding context
- `QABC-0236`: OpenStax University Physics Vol 2 §5.2, neutral conductor polarizes under an external electric field (Fig 5.10); Fig 5.12 shows two conductors need separation to retain net charges; Fig 5.13 grounding and removal are an alternative. Link in JSON. Not equivalent to electromagnetic induction.
- `QABC-0362`: [Official government I7 point 5.4.13](https://legislatie.just.ro/Public/DetaliiDocument/286763), immediately after point 5.4.12 environmental routing exceptions and before point 5.4.14 multi-circuit routing. The rule lists all three bell power options.
- `QABC-0386`: same official I7, §5.5.2.1 lists conductors, §5.5.2.2 specifies connection grouping, §5.5.2.3 is exact mandatory tool-only per-conductor disconnection, and §5.5.3.1 enumerates PE arrangements.

## Before → after and whether this experiment beats the loop
**Pilot A CKPT-415 + Pilot B CKPT-416 = six previously known strict QABC, six decision-ready packets** (3 in each; 9 grade placements in aggregate). The previous V371 batches only marked source pointer trace as recovered. These pilots add explicit source-backed **version-specific verdicts (original vs Trainer), exact grade key contradictions, named source-scope blockers and who must decide**. However **not one previously known technical fact is claimed as a new discovery**, **zero conflicts independently closed, zero keys changed and 0/822 learner-approved**. There is actual useful decision packaging, but formal validation is blocked by exam provenance and independent specialist QA. Therefore **do not continue producing 568 identical packets automatically.**

## Stop point
Two pilots are complete. **STOP AND REPORT**, no GFR 371.6/371.7 or third batch automatically. For QABC-0362 and QABC-0386, ask owner to decide which variant (official original vs unofficial corrected Trainer) should be presented during training, while retaining old source and imported key until evidence-based change approval. Alternative: source grade-specific official answer key and qualified independent technical/linguistic review. Existing bank, keys, HTML/APK, PR, and release unchanged.

Detailed per-grade A/B/C, source excerpts and source-version limitations: `docs/QUESTION_AUDIT/DECISION_PILOT/CKPT_416_STRICT_3B_EXACT_I7_AND_PHYSICS_PROOF_PACKETS_2026_11_23.json`.
