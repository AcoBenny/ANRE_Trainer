# ANRE Trainer ↔ Neural Academy / Avengers Asamble | training bridge | 2026-11-19

## Mission and source of truth
Use the **final question adjudication** as a real-case learning laboratory for the Academy while maintaining ANRE correctness as the sole release priority. Do not start a separate duplicate question audit.
- ANRE reference: [finalization plan](PLAN_FINALIZARE_822_CKPT250_2026_11_19.md), [CKPT-250](CKPT_250_GFR_FINAL_23_QABC_37_P2_RECORDS_2026_11_19.md), V129; 822/822 evidence-linked IDs and historically ~568 distinct QABC units; **0/822 learner approved**.
- Academy source: [AGENTS.md](https://github.com/AcoBenny/Avengers-Asamble/blob/main/AGENTS.md), [role registry](https://github.com/AcoBenny/Avengers-Asamble/blob/main/registry/agents.json), [training policy](https://github.com/AcoBenny/Avengers-Asamble/blob/main/docs/TRAINING_EVIDENCE_POLICY.md) and [execution protocol](https://github.com/AcoBenny/Avengers-Asamble/blob/main/training/EXECUTION_PROTOCOL.md).
- Previous ANRE Academy work: [CKPT-199](CKPT_199_PRECISION_LAB_V01_THREE_SPECIALISTS_ACADEMY_V047_INTEGRATION_2026_11_18.md) already integrated Precision Lab **skills** into Avengers v0.4.7. Reuse; do not reinstall, relabel TinyFish as the three specialists, or repeat training already evidenced.

## Dynamic roster (roles are not independently executed agents by default)
**Core adjudication, minimal per-case assignment:**
- AGENT-001 Task Orchestrator: stable case queue, risk ordering, checkpoint/handoff, de-duplicate QABC units.
- AGENT-029 Electrical Engineer: physical model/calculations, assumptions, A/B/C and counterexamples.
- AGENT-030 Normative Sources Auditor: original source and edition, official applicability, exact legal/physical object, neighboring context/exception. **Docs Intelligence** (Precision Lab) provides version-aware retrieval when needed; it REPLACES overlapping research, not another independent reviewer.
- AGENT-031 Romanian Language Reviewer: negations, “numai/doar/poate”, question-option bidirectional reasoning, ambiguity and distractor literal truth.
- AGENT-032 Question Bank Data Auditor: exact IDs/QABC, cross-grade equivalence, imported key/provenance, CSV field alignment.
- AGENT-005 Independent QA Auditor: separate reviewer **only when separately executed with actual trace**; challenge scope, exclusion-only reasoning, omitted conditions and false positives. A self-review cannot be promoted to independent QA.

**Supporting on demand, not everyone on every item:**
- AGENT-002 Requirements Analyst + Precision Lab **Prompt Architect** for conflicts, gaps, precise executable prompts; one shared contract, no duplicate requirement elicitation.
- AGENT-004 Evidence Researcher when primary sources are missing; AGENT-008 Memory/Context Curator to version generalized lessons; AGENT-011 Test Automation Architect for deterministic negative/regression fixtures; AGENT-009 Handoff Editor for checkpoints.
- Skeptic/contradictor is a *challenge stage* on the evidence, not a fictitiously independent spawned model; log the actual executor/reviewer identity and whether distinct.
- Precision Lab **Architecture Visualizer** only for an actual diagram/schematic/traceability need. AGENT-033 Android APK QA and AGENT-034 standalone HTML QA are **deferred to the app phase** after question-content gate.
- The router picks normally 2–3 relevant primary specialists plus distinct QA. Other roles are consulted only for special cases.

## One-pass ANRE adjudication + Academy practice
1. **Intake:** retrieve original unchanged Q, A/B/C, imported key, grade, cross-grade twins, source edition, exact scope and prior CKPT. Start with existing conflict queue, do not fabricate source texts or double count duplicates.
2. **Specialist review:** preserve the original and, where accessible/legally quotable, the original contiguous source context (paragraph before + relevant + after). Analyze each A/B/C and both directions (stem→choices, choices→implied model); preserve intended exam key vs technical truth vs officially proven key.
3. **Adversarial review:** skeptic attempts at least one plausible countermodel or exception, wrong-edition and generic-to-specific source substitution; negative fixtures include NOR032 I7 generic 25 m vs PE155 branch-column 15 m. Distinct real reviewer needed for independent signoff.
4. **Result:** write evidence pointers and one of `SOURCE_RESEARCHED`, `INDEPENDENT_OPTION_QA`, `EDITION_VERIFIED`, `BLOCKED`; `LEARNER_APPROVED` only after all required gates, never as inference from structural checks. Keep imported QABC and canonical key unchanged.
5. **Academy lesson:** one compact *redacted* case card: capability and role mapping, failed assumption, context clue, accepted/rejected hypotheses, source pointer/edition, negative test, expected safer behavior and supersession/expiry conditions. Avoid copying copyrighted normative paragraphs or sensitive data to an unrelated repo.
6. **Academy evaluation:** compare same model/tools without and with the skill, 3 baseline + 3 skill-assisted trials per selected case (order alternated); store real response/tool trace/model, prompt hashes, revision, timestamp and costs only when measured. Hold out adversarial cases. A distinct reviewer evaluates semantic correctness, citations, false approvals and source scope.
7. **Promotion:** only with observed improvement, no safety regression, repeatability and external QA evidence, propose versioned Academy rule/skill change on its development branch and PR. Never silently modify Academy main or treat a chat lesson as model fine-tuning. If a model runner or reviewer is unavailable: `ASSIGNED_NOT_EXECUTED` / `INDEPENDENT_QA_NOT_RUN`, not `PASS`.

## Pilot cases (pre-registered, no answers changed)
See [ANRE_ACADEMY_PILOT_CASES_2026_11_19.json](ANRE_ACADEMY_PILOT_CASES_2026_11_19.json).
- Two cross-grade key conflicts, the exclusive-term “doar”, a wrong-scope normative source and an electrical case with an unstated grounding condition.
- For each: success means noticing the actual ambiguity and retaining the source/QA gate; it does **not** mean predicting/endorsing the imported answer.

## Non-negotiable gates and actual status
- Original ANRE QABC/key/HTML/APK: **UNCHANGED** by this bridge. PR #7 Draft: do not merge/release.
- No paid API/model runner invocation, remote RAG upload, third-party installation or source redistribution without explicit consent and source rights. Local read-only repository documentation is permitted.
- This bridge and the pilot case fixtures are **assigned training exercises**, NOT completed real-model trials, measured performance gains, autonomous background agents, independent QA or ANRE learning approval.
- Every batch report: distinct units worked / IDs covered / contradictions open / real QA approvals / blocked, plus 1–2 transferable lessons with evidence and status.
