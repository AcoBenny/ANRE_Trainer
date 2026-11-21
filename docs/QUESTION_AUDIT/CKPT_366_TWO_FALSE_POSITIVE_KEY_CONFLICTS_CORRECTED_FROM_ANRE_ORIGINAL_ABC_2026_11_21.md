# CKPT-366 | Critical original ABC option rotation discovered in 19-case key-remediation board | 2026-11-21

## Safety correction verified against user source files
- The superseded V278 19-case review board had 19/19 correct authoritative top-level A/B/C entries from the user ANRE workbook (V149), but a lower-level inherited V249 evidence field silently stored **different alternatives** for QABC-0362 and QABC-0386. The prior source_card candidate letter was computed from the incorrect inherited ABC rather than the actual original choices.
- This is a genuine options/scope rotation defect, NOT a change of the original workbook or application keys.

### QABC-0362 / G1-NOR-048
- **Original imported A stays A.** Original A lists normal lighting OR socket circuit OR distribution board, exactly the three paths permitted by user I7 2023 PDF §5.4.13, p70. Original C says **only** from a socket circuit and excludes other explicitly legal sources. The previous candidate **C was wrong** because its old nested evidence corresponded to a different ordering and sentence. Now source-aligned A for 2023.

### QABC-0386 / G1-NOR-072
- **Original imported B stays B.** Original B says each conductor can be disconnected individually AND the connection is secure and disconnectable **only with a tool**. User I7 2023 PDF §5.5.2.3 p72 mandates both statements. Original C only states the individual-disconnect requirement, omitting the mandatory tool qualifier. The old nested evidence substituted the opposite B, 'without using a tool', so old candidate C was a false conflict.

## Ledger and gates
- [V279 superseding 136-case ledger and exact 17-key-remediation candidate board](./V279_ANRE_ORIGINAL_ABC_FIELD_ROTATION_FIX_17_KEY_CONFLICT_CANDIDATES_136_SOURCE_ROOTS_2026_11_21.json). Source diagnostic 136/136, unresolved source-meaning 0, **17 research-stage imported-vs-source conflict candidates**, **8 sourced-aligned cases**, 2 proven false positives corrected.
- **136 QABC remain release blocked**, learner approvals 0/822. Historical six strict flags retained as historic provenance; source-specific subflags for these two are now correctly marked original-source aligned. Authenticated 2026 ANRE scored keys and qualified independent grading not yet performed.
- Original Excel, original A/B/C, imported grade key, HTML/APK, main, merge/release not modified. Existing V249/V277/V278 left immutable to expose the QA failure and prevent recurrence.
- The next scoring review must compare **authoritative original ABC and inherited source-card ABC letter by letter**, not merely check question count and correct keys. No automatic answer changes from a board even when its source candidate is strong.
