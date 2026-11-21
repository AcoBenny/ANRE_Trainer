# CKPT-236 | GFR | 3 distinct QABC + 3 exact cross-grade references | 2026-11-18

Baseline: V114 SHA `110f1ce427953cc239a92c768682047fef339a49`. Three original Grade I questions and matching Grade II records checked for exact Q+A+B+C+key against V73. Only evidence and status documentation, NO imported key, original QABC, HTML, APK or app edits. Source reopening done by same assistant, NOT an independent reviewer, NOT exam official-key certification.

## G1-ELE-140 / G2-ELEC-278
- Original Q: La funcţionarea în gol a unei linii electrice tensiunea la capăt:
- A: creşte faţă de tensiunea la sursă proporţional cu pătratul lungimii liniei
- B: scade faţă de tensiunea la sursă proporţional cu lungimea liniei
- C: nu se modifică
- Imported key UNCHANGED: A
- Source/option analysis: Efectul Ferranti: capătul receptor al unei linii CA lungi, în gol, poate avea tensiune mai mare decât sursa. Creșterea aproximativ proporțională cu lungimea la pătrat se deduce în aproximația liniei cu pierderi neglijabile și beta*l mic; NU este o lege universal exactă pentru toate lungimile și regimurile. B și C nu descriu efectul în modelul vizat.
- Direct source: https://www2.iea.lth.se/publications/MS-Theses/Full%20document/5330_full_document.pdf
- Flag: MODEL_LIMITATION_QUADRATIC_APPROXIMATION; grade-II evidence reuse is structural only; edition and independent QA pending.

## G1-ELE-142 / G2-ELEC-280
- Original Q: Teoremele lui Kirchhoff se aplică:
- A: numai circuitelor liniare
- B: numai circuitelor cu elemente neliniare
- C: circuitelor liniare şi circuitelor neliniare
- Imported key UNCHANGED: C
- Source/option analysis: Legile Kirchhoff se bazează pe conservarea sarcinii și pe condițiile circuitului concentrat/quasistatic, nu pe liniaritatea elementelor. A și B introduc restricții exclusive false. C corespunde modelului circuitelor concentrate; nu afirmăm universal valabilitatea unei legi simple a ochiurilor la cuplaj electromagnetic arbitrar.
- Direct source: https://openstax.org/books/college-physics/pages/21-3-kirchhoffs-rules
- Flag: LUMPED_CIRCUIT_ASSUMPTION; grade-II evidence reuse is structural only; edition and independent QA pending.

## G1-ELE-143 / G2-ELEC-281
- Original Q: La o instalaţie cu mai multe condensatoare conectate în serie, căderea de tensiune pe fiecare condensator este:
- A: direct proporţionala cu capacitatea
- B: invers proporţionala cu capacitatea
- C: nu depinde de capacitate
- Imported key UNCHANGED: B
- Source/option analysis: În seria de condensatoare ideale la echilibru, sarcina în modul pe fiecare condensator este aceeași, iar U_i=Q/C_i. De aceea B este susținut; A inversează raportul și C ignoră C_i. Real: curenți de scurgere, tensiuni inițiale și distribuție tranzitorie pot modifica repartizarea; se cere explicit modelul ideal.
- Direct source: https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel
- Flag: IDEAL_STEADY_STATE_ASSUMPTION; grade-II evidence reuse is structural only; edition and independent QA pending.

## QA gates
- 3/3 exact crossgrade matches: question, all options and imported key, checked against original V73.
- Previous unfocused rows 325; remaining 319 after six *grade-specific records* linked, representing 3 original source checks + 3 grade-reuse links; NOT 6 independent source reviews.
- Original 822 grade IDs retained, no imported key changes, no approval for learning, no qualified reviewer approval. PR #7 remains Draft, no merge.
