# CKPT-181 | NOR066 supersession + NOR094 source/context QA (2026-11-17)

## Scope / provenance
Continuation from live branch PR #7 Draft HEAD `dfb08b5730e4e888d8ef68545b85976c77e077ed`. Do **not** re-count as new QABC work: 568/568 research/source-scope entries and 822/822 canonical grade IDs are already inventoried in CKPT-180. This is an **additive, history-preserving** source reopening of 2 **existing** Grade I units, NOT a learner-release approval. Older CKPT-175/177/179 are preserved unchanged.

Sources reopened during this session:
- I7/2011 complete HTML mirror, §§5.2.12.1.3–5 and 5.5.7.9–11, plus §5.5.8: https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011
- Official consolidated regulation identity: https://legislatie.just.ro/Public/DetaliiDocumentAfis/286763 (official portal could be located through search snippets but **direct page reopening returned HTTP 502** during this recheck).
- Official 2023 amendment: Ordin 959/2023 https://legislatie.just.ro/Public/DetaliiDocument/271142 (identity found, direct HTTP 502; cannot claim 2026 consolidated exact clause re-verified).

## G1-NOR-066 | existing conflicting imported key and preserved supersession
- Stable ID `G1-NOR-066`; unit `AU-7d2fe260e4064d75`; QABC SHA256 `7d2fe260e4064d7588e5a2622fd4c14a0f28dcec322d627f0c3fecd6a20d1b99`.
- Exact question: **Instalarea conductoarelor electrice în tuburi sau ţevi pozate în pământ:**
- Unmodified options **A** este interzisă; **B** este admisă; **C** este admisă numai pentru conductoare de cupru.
- Imported key: **B UNCHANGED**. **A source-supported candidate, NOT a key edit**.
- I7 §5.2.12.1.4: **„Se interzice instalarea conductoarelor electrice în tuburi sau țevi pozate în pământ.”** Previous §5.2.12.1.3 allows isolated conductors and/or cables in protection conduits generally; subsequent §5.2.12.1.5 addresses same-circuit conductors and PE in one protective element. These generic neighboring permissions do not override the exact buried-tube prohibition.
- Per option: A directly matches specific prohibition; B conflicts in the specified object/installation; C narrows an otherwise prohibited action to Cu, unsupported.
- Erratum chain: CKPT-175 **conditional generic technical inference** → CKPT-179 **superseding exact-scope prohibition** → CKPT-181 **same-source paragraph and neighbor recheck, no new grade credit**. Retain historical wrong inference rather than silently overwriting it.
- Status **BLOCKED_CANONICAL_KEY_CONFLICT**. Current exact authoritative edition/exam applicability, independently performed technical+linguistic review and official answer key still unresolved. No approval.

## G1-NOR-094 | contextual support, not absolute-answer signoff
- Stable ID `G1-NOR-094`; unit `AU-56400be12641a793`; QABC SHA256 `56400be12641a79302b3a208be104d28d06d44884cdc08234e3ba2906fa56653`.
- Exact question: **Rezistenţa prizei de pământ a unei clădiri, atunci când este folosită numai pentru protecţia împotriva şocurilor electrice, trebuie să fie cel mult**
- Unmodified options **A** 10 Ω; **B** 1 Ω; **C** 4 Ω. Imported key **C UNCHANGED**.
- I7 §5.5.7.11 says for this object/purpose **„Rezistența prizei de pământ poate fi: – cel mult 4 Ω atunci când este folosită numai pentru protecția împotriva șocurilor electrice”**, versus **„cel mult 1 Ω”** when shared with the building lightning protection earthing electrode. Neighbor §5.5.7.10 additionally requires the earthing resistance to permit protection to disconnect within the specified time; §5.5.8 provides a separate common-electrode/transformer spacing context, not interchangeable.
- Option review: A 10Ω is not the specified protection-only upper figure; B 1Ω belongs to combined lightning protection and is more restrictive than the questioned category; C 4Ω is the **source-stated figure and intended key**. Literal QA caveat: question's **„trebuie să fie”** is stronger than source's **„poate fi”**; engineering acceptance also depends on §5.5.7.10. An unnecessarily stricter 1Ω value may still physically satisfy an upper-bound condition, but it does not identify the normative threshold for the specified case.
- Existing CKPT-177 classified this **CONDITIONAL_MODEL_OR_SOURCE** and remains authoritative as historical analysis; this check **confirms supporting source context only**, does not add a new unit, bypass edition checks or mark the item learner-approved.

## QA boundary and handoff
- Exact ID/unit/hash/QABC/key fields compared against existing CKPT-175/177 and CKPT-179 plus V73/822 grade ledger. Both are **existing** units; **0 new unique-unit credit**.
- Direct exact HTML paragraphs and neighboring text opened. Official portal direct accesses failed; this recheck does **not** certify a complete 2026 legal consolidation, ANRE exam-specific version, or official answer key.
- Technical/source/linguistic reasoning here was done within **one assistant session**; genuinely independent reviewers **NOT_RUN**. Canonical question/options/keys, HTML, APK, other checklists and main **NOT_MODIFIED**. `approved_for_learning=NO` for both.
- Next: prioritize remaining **50 blocked +45 older precheck-only** from CKPT-180, without blanket repetition; obtain independent and exam-edition QA before any final approvals. Preserve this erratum evidence chain.

PR #7 remains Draft, no merge/release.
