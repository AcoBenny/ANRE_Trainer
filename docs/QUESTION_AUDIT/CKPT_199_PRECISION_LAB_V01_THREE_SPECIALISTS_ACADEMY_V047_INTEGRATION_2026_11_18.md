# CKPT-199 | Correction: Precision Lab v0.1.0 is the three-specialist Academy integration | 2026-11-18

## User correction / supersession
- The user explicitly clarified that **TinyFish was NOT the requested new three-agent plugin**. TinyFish is only a separate potentially interesting browser automation tool.
- Supersedes the **plugin identity and intended integration target** described in `CKPT_198_TINYFISH_GATED_ACADEMY_ANRE_RESEARCH_ADAPTER_2026_11_18.json`. Preserve CKPT-198 as historical preliminary exploration, not the requested Academy integration. No TinyFish connection or live test was performed.
- The desired three-specialist package is **Avengers Precision Lab v0.1.0** (independently installed plugin). It contains `prompt-architect`, `docs-intelligence`, `architecture-visualizer`. These are skills/workflows, not three independently launched model processes.

## Actual Academy integration, checked
- Avengers Asamble private plugin was updated to **v0.4.7**, release `pluginrel_6afd6ebe40108191a550148cecb34924`, at https://chatgpt.com/plugins/plugins_6aeee75a94cc819195c0aeb3a9649391 .
- Modified source: `skills/agent-router/SKILL.md`, new `skills/agent-router/references/PRECISION_LAB_V01_BRIDGE.md`, plus synthetic test `skills/agent-router/tests/test_precision_lab_bridge.py` and synchronized manifest/compat overlay.
- After save, plugin source readback confirmed v0.4.7 in both manifests, complete `40` preserved core roles, bridge present and linked, benchmark script retained, prompts retained.
- Local static integration checks: **10/10 PASS**, all synthetic text/routing invariants; **NO live independent specialist execution/benchmark proven**, NO real ANRE source accuracy signoff. 40 core roles remain separate; three specialists are optional external overlay and do not require duplicated skill code.

## Intended ANRE dispatch (no default all-three invocation)
1. `docs-intelligence`: for source/legislation editions, exact normative object and neighboring original context, tied to `anre-source-audit`, no duplicate source research. Prefer first on legal/source question cases.
2. `prompt-architect`: for contradictory requirements, ambiguity, missed constraints or repeated user format failures; reuse established protocol rather than re-question user.
3. `architecture-visualizer`: only for actual editable diagrams/traceability/system design tasks, not routine legal multiple-choice adjudication.

## User's ANRE documentation presentation contract, reinforced
- Present unchanged original question and alternatives A/B/C.
- Original source material, as an **uninterrupted verbatim passage** covering the relevant paragraph plus at least one complete paragraph before and one after, retaining all numbering and spelling, and highlight only original words without changing them **when access and quotation permission allow**. Do not interleave the assistant's explanations or split into before/after summaries.
- When an external source cannot lawfully be quoted in full or cannot be read, be transparent; give the allowed exact excerpt and official source link. No synthesized text disguised as verbatim.
- **Only afterward** present separately labeled technical/legal interpretation, exact scope/era issues, and option analysis; avoid influencing the user's independent reasoning before they read.
- Preserve original QABC and grading key; no source research alone establishes official ANRE 2026 answer, human QA, or learning approval.

## No-change gates
- `original_QABC_or_keys_changed=NO`; `HTML_or_APK_changed=NO`; `ANRE_learning_approval=NO`; `independent_technical_source_linguistic_QA=NOT_RUN`; `PR_7=Draft_UNMERGED`.
- Next: use the now-installed Precision Lab Docs Intelligence workflow for new source-specific ANRE research, with source link/edition and user formatting constraints; record real-use feedback and negative cases as test evidence, not invented agent training.
