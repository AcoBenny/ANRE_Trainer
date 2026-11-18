# CKPT-202 | G1-LEG-025 official live-source retrieval and fidelity smoke test | 2026-11-18

## Scope and evidence
- Case G1-LEG-025 / AU-950954e2d16b0eb9. Canonical question and A/B/C remain unchanged.
- Official page accessed through live source extraction: https://legislatie.just.ro/Public/DetaliiDocument/311821 (consolidation presented as 26 July 2026). Direct web retrieval can intermittently return a 502; hosted markdown extraction succeeded.
- Legea 123/2012, Title I, Chapter I, Art. 1(2)(b) is the provision for stationary DC sources not connected via inverters to SEN.
- Crucial wording: exemption applies to 'prezentului titlu' (Title I), whereas canonical stem asks about the whole Law 123/2012. This scope mismatch remains unresolved for final legal-quality approval.

## Live real-source extraction and test actually executed
- Retrieved official-page markdown had 850984 UTF-16 JS code units.
- Located anchors: Article 1 header offset 2279; Art. 1(2) offset 3567; letter b offset 4035; Article 2 offset 4208; Article 3 offset 9204.
- Slice Art. 1(2) to before Article 3 had 5637 code units. Grouped lengths 468 / 173 / 4996. Non-cryptographic FNV32 scratch fingerprint: 0b32f91d.
- Six strict equality/order smoke scenarios against actually fetched text passed: unchanged slice accepted; preceding removed, following removed, swapped segments, rewording, and inserted explanation rejected.
- Important limitation: this was a small JS smoke test comparing the fetched string, NOT execution of the installed Python source_fidelity_gate.py on an actual rendered answer. It does not prove model output fidelity.
- HTML-to-Markdown includes editorial modification notes and ellipsis separators. A clean canonical 3-paragraph legal extraction cannot be assumed from raw markdown offsets.

## Outcome and safe next
- Official statute accessible: YES. Relevant official rule identified: YES. Six integrity smoke cases: PASS.
- Full three original consecutive law paragraphs user-visible and verified character-by-character: NOT DONE. Status FULL_VERBATIM_CONTEXT_NOT_DELIVERED.
- Independent review of correct A/B/C for current ANRE exam and unambiguous scope: NOT DONE.
- Imported key B is consistent with exemption from Title I, but not independently certified as a whole-law statement.
- Next: parse official statutory article/paragraph boundaries separately from editorial notes, preserve legal version and text offsets, and then run packaged source_fidelity_gate.py against a permitted full-text presentation. If unable to reproduce, report blocked rather than claim PASS.
- Safety: PR #7 stays Draft; no edit to question, variants, key, HTML, APK; no merge or release.
