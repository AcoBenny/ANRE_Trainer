# ANRE Trainer | Audit-first release gate (owner decision, 2026-11-08)

## Decision
The owner explicitly requested **no more HTML, APK, UI, runtime data, or question-bank implementation until the didactic-document audit and complete mapping are finished**. Avoid premature integration and rework. This supersedes earlier suggestions to run development work in parallel with content audit.

## Mandatory order: didactic corpus first (owner clarification, 2026-11-08)

The owner clarified that the *full set of didactic manuals must be indexed and audited BEFORE systematic validation of individual exam questions and answer keys*. Earlier question-first source mapping is retained as **preliminary exploratory evidence only**, not a release-certified mapping.

**Phase A: full manual/normative source catalog.** Analyze all 14 uploaded manual PDFs, identify exact duplicates and equivalent editions, scan/OCR limitations, document version and authority; index chapters, subchapters, concepts, formulas and physical PDF page ranges with provenance. Cover all source domains and log gaps. Official law and normative-currentness checks are separate from technical textbooks. A table of contents or word hit is not proof that a paragraph establishes a fact.

**Phase B: source coverage review.** Audit completeness and quality of the didactic catalog against the ANRE topic taxonomy, identify technical gaps, superseded regulations, unclear figures and offline redistribution/copyright permissions; seek additional authorized materials for unresolved topics. Record coverage at subject/concept level, not by counting questions already matched.

**Phase C: question and answer audit.** Only after A/B map the 822 stable IDs and historical question sets to the indexed didactic concepts and exact paragraphs/pages, check full A/B/C question wording, technical/normative truth, historical conflicts, duplicates, AGENT-031 language traps and independent QA. Treat previous 150 question-specific exploratory mappings as tentative candidates to re-evaluate from the source catalog; do not discard them or declare them approved.

**Phase D: implementation (still frozen).** Only after source and question audits pass and the owner explicitly approves, integrate permitted offline instructional content, then real HTML/Android E2E tests.

**Immediate next action:** index all didactic manuals and source taxonomy systematically. Pause new 50-question mapping batches and independent answer-key adjudication until manual index and coverage inventory are complete. Critical already-discovered correctness issues remain documented and not silently changed.

## Allowed in the audit phase
- Read and verify user-uploaded technical/normative manuals and historical question sets, subject to source rights.
- Write metadata-only inventories, source-page mapping tables, QA reports, conflict registries, and audit-only scripts/checks.
- Triage technical ambiguity, linguistic traps (AGENT-031), answer-key conflicts and outdated law; preserve raw evidence.
- Record research findings in docs and issues, without falsely claiming independent autonomous agent runs.

## Not authorized yet
- Modifying standalone or Android HTML, JavaScript, UI, actual exam/learning behavior, database or stored answer keys.
- Including new questions, manuals or reproduced textbook chapters in shipped offline assets.
- Releasing any new APK/HTML build from this audit.
- Spending on external API/model services without separate approval.

## Gates to reopen implementation
1. All 822 stable question IDs have a reviewed disposition: verified didactic evidence with exact source + page/paragraph; or explicitly documented and accepted unresolved exception. User wants **total mapping**, so exceptions are blockers unless approved.
2. Source version and technical correctness verified, question-bank provenance distinguished from instructional textbooks, current normative references checked where relevant.
3. AGENT-031 linguistic QA for traps and ambiguous terms; contradictory source keys adjudicated, with an exact changelog.
4. Copyright / offline-document reuse permission determined per source. Metadata and independently written explanation are not blanket redistribution rights.
5. Independent content QA + source identity check, with 0 unchecked source-card cross-links (76 prior wrong cross-ID candidates remain quarantined).
6. Only then owner approves implementation work, standalone tests and Android APK tests.

## Checkpoint frequency
Keep CKPT-ANRE-20261108-02 as the latest accepted checkpoint until 2–3 substantial validated audit batches, an actual release/handoff or a major risky transition. Interim audit files and issues are sufficient.

## QA statements
A text-layer page anchor, a topic similarity score, a model-assisted reading or GitHub deterministic CI alone **never equals independent final content certification**.
