# CKPT-383 | GFR: three I7-related P0 questions and one same-stem P2 control

Date 2026-11-22; audit branch `audit/anre-v8-priority-17-20261109`; previous checkpoint CKPT-382. Detailed machine-readable source/alternative review: [V293](./V293_4_SOURCE_NATIVE_NOR_G1_I7_DIRECT_PARAGRAPH_OPTION_GATES_2026_11_22.json).

## Evidence physically reopened now

1. User's source original `NORME-TEHNICE-Gr.-1-05.2023(1)(3).xlsx`, **SHA-256 `bed56a32f24d19774ec9dfff8c5b1438176078d0e9c4eb9e8fa1ff1fc98c3092`**, verified from actual Excel bytes and `artifact_tool` cell reads for physical rows **49,55,56,79**. It is the same historically audited source hash. Original answer-key attribution has **not** been verified from official exam scoring material.
2. User's exact I7 PDF `803493174-I7-2011-completat2023(1).pdf`, **SHA-256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`**, reopened at actual pages **55,70,72**; verified visually with Files page images and against parsed paragraph text. It is the same I7 hash used in prior CKPT-378, **not an independent new enactment or expert examination**.
3. ANRE official currently displayed [electrician exam page](https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/) as consulted 2026-11-22 still links [05.2023 ANRE bibliography](https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf), visually verified page 2 of PDF: I7/2011 **DA Grade I and II**. *Caveat*: publication on an official site does **not** prove that no newer amendment exists or that this source is the exact 2026 examination clause/version for each case.

## Four original Excel questions, answer-by-answer primary I7 test

### P0 QABC-0356 / G1-NOR-042, original row 49

Stem: `Conductorul neutru (N) trebuie să aibă aceeaşi secţiune cu conductorul de fază:`
- A: `în circuitele monofazate cu două conductoare, indiferent de secţiunea conductoarelor`.
- B: `în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm2 Cu sau 35 mm2 Al`.
- C: `în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază`.

Primary paragraph **I7 §5.2.4.6.1(a)** exactly requires equal section in *2-wire single-phase* circuits regardless of section, establishing **source-supported A**. **I7 §5.2.4.6.1(b)** uses ≤**16 mm² copper / 25 mm² aluminum** for multiphase, not B's 25/35; B also incorrectly stipulates a three-wire monophase regime as its common case. C incorrectly universalizes multiphase sizing: §§5.2.4.6.2–6.3 handle harmonics and permitted neutral downsizing. Context preceding §5.2.4.5 addresses PE/PEN (not interchangeable with N); following subsections provide exceptions. **Imported B remains unchanged but technically contested**; original-source A preferred provisionally.

### P0 QABC-0362 / G1-NOR-048, original row 55

Original stem is 220(230)V bell or transformer feed. Original **A only direct panel; B only normal-lighting circuit; C from a socket circuit**. I7 **§5.4.13** permits all three source types, and crucially **not exclusively**. Before it §5.4.12 addresses circuit routing through special locations, after it §5.4.14 circuit conductor routing/protection; neither narrows §5.4.13 to exclusively one feed. A/B false by `numai`; C affirmatively allowed. **Original-source candidate C**, app canonical rewrites all options and imports A. Do not project app A onto the original. Source PDF says sonerie 220V while original worksheet says 220(230)V; same function but different era nominal-voltage wording, preserve this fidelity distinction.

### P2 QABC-0363 / G1-NOR-049, original row 56: anti-deduplication regression

**Exactly same source stem as row 55, but A/B/C are NOT equal**. Original **A only direct panel; B from normal-lighting circuit; C only socket circuit**. Under the *same exact* I7 **§5.4.13**, affirmative **B** is uniquely unqualified, A/C false for exclusivity. This matches imported B **as provisional answer research**, no official score or independent expert approval. **Do not deduplicate rows 55 and 56 by stem**. QABC-0362 vs -0363 must remain separate source-native variant sequences even if an educational concept is shared.

### P0 QABC-0386 / G1-NOR-072, original row 79

Original A: `nu este obligatoriu să poată fi deconectat individual` (contradicted); B: `trebuie să poată fi deconectat uşor, fără utilizarea unei scule` (direct contradiction to tool-only condition); C: `trebuie să poată fi deconectat individual` (**affirmative true but not full combined rule**). I7 **§5.5.2.3** requires BOTH individual disconnectability and a safe connection disconnectable **only with a tool**. Preceding §5.5.2.2 concerns conductors connected through main protective conductors; following §5.5.3 begins protective conductor classification. Therefore **original-source candidate C**, while rewritten app option B combines the complete normative text and imported key B belongs to *that rewritten question only*. A separate card must preserve the omitted tool requirement as context. Do not falsely classify C as incorrect simply for not restating every normative qualification.

## Reconciliation and counts

- All four exact grade source rows reopened; **3 P0 QABC + 1 P2 QABC**, no double counting of previous technical research. Prior V290/CKPT-378 had already reached same three P0 source candidates; this checkpoint adds current physical XLSX/PDF revalidation, adjacent I7 context and a second original same-stem P2 control.
- No new official scoring authority, no identifiable independent electrical engineer/jurist or separate linguist endorsement. No professional learner approvals.
- Queue remains **27 P0 / 2 P1 / 793 P2 = 822** routes in V283/V291. The P1 source binary check was closed at CKPT-381 but UI runtime and professional signoff remain pending.
- All original XLSX, canonical bank, options/order, imported keys, HTML, APK unchanged. PR #7 remains **Draft** and is not merged or released.

## Next useful task

Treat remaining **P0 original-key candidate disagreements** as research-stage findings; reopen official full legislative/technical source by exact object, edition and surrounding context, annotate answer alternatives, **then request genuinely independent qualified signoff**, without claiming that this assistant can self-certify those approvals. Inspect original workbook rows using sha-pinned source and preserve source-vs-rewritten grade split. A simple QA checklist or second AI vote is not professional certification.
