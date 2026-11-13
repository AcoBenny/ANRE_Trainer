# Avengers Academy | Permis ≠ exclusiv; opțiuni alternative (v1) | 2026-11-12

## Scop
Accelerăm auditul ANRE reutilizând dovezile din `DEEP-NOR-03`, fără a rescrie întrebările-capcană. Când o normă admite variante alternative (`X sau Y sau Z`), **o variantă singulară fără restricție poate fi corectă**, în timp ce `numai X` este fals dacă sunt permise și Y/Z. Etichetăm fiecare răspuns ca afirmație completă. Acest lucru este diferit de întrebările cu LIMITĂ MAXIMĂ unde trebuie egalat plafonul, nu ales un exemplu permis.

## Două cazuri canonice: alimentare sonerie
Source: **I7-2011 §5.4.13**: alimentarea transformatorului de sonerie sau a soneriei de 220V este admisă (a) din circuit de iluminat normal, (b) din circuit de prize, **sau** (c) direct din tabloul de distribuție.
- Portal Legislativ, text indexat: https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH . Direct `open` produced HTTP502; do not claim full official page opened.
- Reproduction of Monitorul Oficial text, **readable HTML §5.4.13**: https://www.infodosar.ro/monitorul-oficial/ministerul-dezvoltarii-regionale-si-turismului/132763-reglementari-0-2011 . Source-specific article directly read, **not** 5.4.23 which is about *secondary bell pushbutton*, a different object and action.
- `G1-NOR-048`, Grade I, original key **A**: A is complete list of three permissible paths. B (`numai iluminat`) and C (`numai prize`) are false **exclusivity**; preliminary `A_SUPPORTED_EXACT_I7_5_4_13`.
- `G1-NOR-049`, Grade I, original key **B**: A (`numai direct din tabloul`) is false exclusivity, **B** (`din circuit de iluminat normal`) is a permissible **example**, C (`numai prize`) is false exclusivity. Preliminary `B_SUPPORTED_NONEXCLUSIVE_SINGLE_EXAMPLE`.
- Neither question should be rewritten as ambiguous. The previous research was blocked on the missing exact source; **source locator now supplied**. Do **not** convert research classification into final learner signoff: 2026 consolidated changes/grade exam bibliography and independently reopened sources remain outstanding.

## Adjacent case reused, no extra exhaustive research
- `G1-NOR-052` key **A**, alternatives B/C add `numai pentru conductoare Cu` or `numai pentru conductoare Al`. The material qualifier is unsupported: I7-2011 **§5.2.4.6.1(a)** says in monophase two-conductor circuits, neutral (where present) has phase section **irrespective of conductor section**; Annex5.32 notes include monophase N same size as phase. A is an intended non-exclusive general rule, B/C false material-only restrictions. Scope conditions must still be checked (specific monophase arrangement, applicable bibliography), hence `A_SUPPORTED_CONDITIONAL`, **not learner-approved**.
- Readable exact paragraphs in the Monitorul Oficial HTML reproduction above, I7 §5.2.4.6.1 and Annex5.32.

## Quantifier scan for future routing
- Read exact GitHub V73 `822` original placements, plus `ID_ROUTING_822`. Screening A/B/C for `numai|exclusiv|doar` returned **151 question IDs /112 unique QABC units**. Within these, **38 IDs** contain at least two such restrictive options, hence likely higher-yield for evaluating distractor exclusivity. This is **LEXICAL DISCOVERY, NOT WRONG-ANSWER COUNT** and could include false positives. It does not add 151 new units to completed deep pretriage or mean all are ambiguous.
- Priority next: 38 candidate IDs with 2+ restrictions, grouped by unit/batch; avoid reworking the 048/049/052 examples. Formalize only questions with actual matched source and conjunctive statement, not `numai` text alone.

## Deterministic regression
- New source-scoped proof of concept: `tools/qa_allowed_alternatives.mjs`.
- Tests: `tools/tests/qa_allowed_alternatives.test.mjs`. Ran the equivalent JS implementation/fixtures in sandboxed JS tool runner: **12/12 PASS**, including 048=A,049=B, three equally allowed singletons=>genuine multiple-answer, all false exclusives=>no option, case-swap, unknown route, alternate `și`, missing locator, negation, duplicates, wrong object. **Node/CI suite was written but not separately executed**. The classifier is deliberately limited to the doorbell object and supplied 3-path source. It is not an AI/independent source verifier.
- All outputs `approved_for_learning=false` by construction, `independent_source_qa=NOT_RUN`. No original question, answer key, HTML, APK or stable/release branch modified.

## Next collaborative case: G1-NOR-053
- Original stored **A** even though **PE155/92 §1.2.1** defines `branșament` from electric line to subscriber's interior installation; **§1.2.2** defines `racord` from line to **firida de branșament**. The option A appears to copy **racord**, not full branșament. Option C references boundary point / meter terminals; historical PE155 observation says `bornele de ieșire din contor`, but the actual C text omits the `ieșire` qualifier. **Potential C candidate, unresolved scope and exact terminus**.
- Historical reproduced norm PDF (text read; screenshot attempt pages0-1 **cache miss**, NO visual verification): https://electrician365.ro/wp-content/uploads/2019/04/Normativ-instalatii-electrice-Privind-proiectarea-si-executarea-bransamentelor-electrice-pentru-cladiri-civile.pdf
- Current ANRE Regulation59/2013 (2022-revised) definition of `branșament` = low-voltage user connection installation: https://b.colegiul-geodezilor.ro/legislatie/act-complet.php?a=64_ORD-ANRE-59-2013_regulament-racordare . **Do not transfer definition mechanically across document editions and regulated objects.**
- Human interpretation question: "Ce definește enunțul: branșamentul complet sau doar racordul până la firidă? Care variantă ți se pare corectă și de ce?" User insight is `USER_HYPOTHESIS`, not an automatic key correction.
- Independent source/edition/linguistic QA remains open. Preserve prior pretriage `G1-NOR-053=A_HISTORICAL_DEFINITION_NEEDS_TEMPORAL_SCOPE` intact, record new contradiction separately.
