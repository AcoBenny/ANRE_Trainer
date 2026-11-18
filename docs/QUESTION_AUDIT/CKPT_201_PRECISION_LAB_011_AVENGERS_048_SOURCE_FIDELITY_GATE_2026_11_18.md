# CKPT-201 | Original-source fidelity implementation + Academy upgrade | 2026-11-18

## Exact goal
User said "Okie start" after approving a correction to the recurring ANRE source-presentation failure: they want the **unaltered original documentation, continuous, with a complete paragraph before, the central paragraph, and a complete paragraph after**, without any assistant interpretation interspersed. In the prior G1-LEG-025 pilot, the exact text was not delivered even though the stated procedure was present in skill instructions. The user also asked to exercise the 3-specialist Precision Lab v0.1 workflow in Avengers Academy.

## Changes actually applied to private account plugins
1. **Avengers Precision Lab v0.1.0 -> v0.1.1**, user-owned private plugin ID `plugins_6afd563d3ba48191b6d2efa1010c443d`, published release `pluginrel_6afd749b54cc8191ad922de46886a9f1`. Updated `skills/docs-intelligence/SKILL.md` with original-source-first mode and added `skills/docs-intelligence/references/contiguous-original-source.md`. Exact context, provenance, permitted quoting, user-supplied sources and blocked status are explicit.
2. **Avengers Asamble v0.4.7 -> v0.4.8**, private plugin ID `plugins_6aeee75a94cc819195c0aeb3a9649391`, published release `pluginrel_6afd74a8b7e88191801aee1f6c7c72e2`. Updated `skills/agent-router/references/PRECISION_LAB_V01_BRIDGE.md`. Added `skills/agent-router/scripts/extract_original_context.py` and `skills/agent-router/scripts/source_fidelity_gate.py` with unit test files in `skills/agent-router/tests/`.
3. Plugin readback VERIFIED for both stored releases: version aligned across root and .codex manifests; default prompts preserved; all new files present; previous core `agent-router/SKILL.md` still installed. They are skills and Python helpers, not independent agent processes or plugin tools with autonomous runtime.

## What the two Python components do
- Extractor reads an **already accessible local UTF-8 source**, finds a unique original paragraph by a needle phrase, extracts the **entire original predecessor + target + successor** without paraphrasing, and reports the original file's SHA256. It refuses no-match, multi-match, and absent neighbors. The output has `extraction_verified=false` by default; external source/page authenticity, official edition, source scope and copyright are NOT certified.
- Fidelity verifier checks the **actual rendered Markdown reply**, unchanged exam question and exact A/B/C order, exact three consecutive paragraphs (with optional Markdown bold), source title, edition, locator and a link; it returns `PASS_FORMAT_ONLY`, `FAIL`, `BLOCKED_SOURCE_REPRODUCTION` or `BLOCKED_UNVERIFIED_SOURCE`. It does not authenticate user-provided source fixtures or accept exam answers.

## Actual test results
- Command: `python -m unittest discover -s skills/agent-router/tests -p 'test_*py' -v` on staged helper scripts: **21/21 deterministic tests PASSED** (15 verifier tests and 6 extractor tests), including negative cases for missing before/after, rewording, out-of-order fragments, interleaved assistant explanation, missing edition/link and rights constraints.
- Full *synthetic fictional* pipeline: run extractor over three fictitious legal paragraphs, compare against the known artificial input, then run fidelity gate on displayed sample Markdown: **PASS_FORMAT_ONLY**.
- The first end-to-end attempt detected a **trailing-newline mismatch** in the final paragraph (false FAIL); extractor amended to remove separator/terminal newline, without altering internal text; repeat was PASS. This regression lesson is part of the release evidence.
- Artifact ZIP SHA256 (local staging): Precision Lab v0.1.1 `6977b8e85030f91cb3b7cbec004f53fe9352478b0c805462fed82359a04196e8`; Avengers v0.4.8 rebuilt `4c6fd9e8d8b67355421d8348573c6acb8687061ff3020adfcfee80f0ae6703ee`.
- Local test outputs are from deterministic fixtures and **do not establish real model competence**, actual ANRE source extraction success or independent reviewer validation.

## Explicitly NOT yet solved
- **G1-LEG-025 real law full-context display in chat remains BLOCKED/NOT_TESTED**. The relevant edition of the entire Legea nr.123/2012 has not been verified as a user-supplied, local full-text source for unrestricted reproduction in the current conversation, so we cannot claim the three real original legal paragraphs have already been shown. No workaround to tool copyright limits, no pretending a summary is original.
- Original question remains `G1-LEG-025` (unit `AU-950954e2d16b0eb9`) with imported candidate B UNCHANGED. Different text scope 'Legea nr. 123/2012' vs 'prezentul titlu' remains a separate source-scope flag.
- Official applicable 2026 ANRE exam bibliography and answer-key authenticity NOT independently certified. No human/legal/linguistic independent QA executed.
- **No changes** to original question bank, any A/B/C, barem, HTML, APK, main branch, or release. PR #7 stays Draft.

## Safe next acceptance test
When an exact eligible statute document is available (user-uploaded/readable local text with correct edition and rights), choose a single art.1 passage covering the full preceding and following original paragraph, compare to the original page, flag extraction as verified only with evidence, render one contiguous block in chat, and run `source_fidelity_gate.py`. That real case, rather than the synthetic tests, will establish whether the user-visible format requirement is finally satisfied.
