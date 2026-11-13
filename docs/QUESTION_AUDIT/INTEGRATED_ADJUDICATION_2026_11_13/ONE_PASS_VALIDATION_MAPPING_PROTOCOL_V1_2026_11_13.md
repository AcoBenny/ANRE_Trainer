# Avengers Asamble | ANRE One-Pass Validation + Context Mapping | v1.0 | 2026-11-13

## Obiectiv
**O singură trecere de cercetare structurată per QABC unic**, folosind toate celelalte etape în aceeași fișă și reutilizând probele deja disponibile, apoi verificare *independentă reală*. Etapele nu sunt trei ture complete pentru 822 întrebări. Întrebările comune între grade sunt cercetate o singură dată, dar au **porți de aprobare distincte pe ID/grad** și baremele păstrate până la adjudecare.

## Surse de adevăr și fișiere
- **Canonic nemodificat** `V73_ALL_822_EVIDENCE_AND_RELEASE_GATES_MASTER.csv` + `DEEP_EXECUTION_2026_11_11/UNITS_568.csv` + `ID_ROUTING_822.csv`.
- **Fișa unică**, `INTEGRATED_ADJUDICATION_2026_11_13/MASTER_UNIT_CARDS_568.csv`: un singur QABC, original, original-keys pe fiecare membru, sursa, ABC, paragraf context, highlights, drepturi și porți review.
- **Release pe grad/ID** `INTEGRATED_ADJUDICATION_2026_11_13/GRADE_RELEASE_LEDGER_822.csv`: 822 ID-uri, referință la unitatea unică și statutul final separat; inițial toate `NO`.
- **Investigarea istorică** `DEEP_EXECUTION_2026_11_11/DEEP_*_ALL_*.csv`: surse preliminare refolosite ca *piste*, niciodată tratate implicit drept dovadă autentică.
- **Piloți evidență** `P0_PILOT_*_CONTEXT_CARDS*.json`: date structurate, exportabile ulterior în trainer după aprobarea lor.

## Ordinea atomică per întrebare
1. **Recuperează exact** unit ID, SHA QABC, toate ID-urile gradelor, textul și toate variantele A/B/C, baremele originale și conflictele P0/P1/P2. Confirmă sursa originală, nu reconstrui întrebarea.
2. **Deschide sursa țintită și verifică potrivirea obiectului**: regulament/mediu fizic/dispozitiv exact, acțiunea, condiția, nivelul, termenii și contextul. Pentru norme/legi, verifică versiunea originalului, modificările și bibliografia ANRE pentru fiecare grad și data examenului. O dovadă de domeniu general este blocată pentru o întrebare reglementată specific.
3. **Adjudecă simultan A/B/C**, cu raționament, condiții, excepții și contraexemple, marcând termenii lingvistici `numai`, `întotdeauna`, `poate`, `trebuie`, `de preferat`, `maxim`; dacă două opțiuni pot fi adevărate literal, `BLOCKED_AMBIGUITY`. Nu corecta baremul automat.
4. **Mapare în aceeași vizită la sursă**, nu într-o tură ulterioară:
   - Titlul autentic, autor/emitent, **ediția**, articolul/§/pagina/figura/tabelul și linkul la exact fragmentul relevant.
   - **Paragraf contextual amplu** (uzual 4–6 propoziții sau întregul paragraf original, când drepturile permit), care descrie *de ce* și condițiile de aplicare, nu doar 3–4 cuvinte comune cu răspunsul.
   - **Bold selectiv** pentru formula/termenul/trapul de interpretare și condițiile importante. Păstrează contextul, nu evidenția tot textul.
   - Distinge strict `CITAT_VERBATIM` de `PARAFRAZĂ_CONTEXTUALĂ_ORIGINALĂ`. Nu inventa citate. Pentru surse externe protejate, folosește **citat foarte scurt**, parafrază explicativă originală și link precis; folosește fragmente mai lungi numai dacă deținătorul permite explicit sau utilizatorul a furnizat material utilizabil cu drepturi. Nu redistribui PDF-urile/standardele restricționate.
   - Pregătește `highlight_terms`, `contextual_explanation_4_6_sentences_with_BOLD`, `source_quote_short_verbatim`, `source_permission_for_offline` fără duplicare de text între popup și card.
5. **QA independent efectiv** (surse originale, calcule, versiune, limbă, context și unicitatea opțiunii) cu specialiști diferiți/sesiuni separate sau om calificat. Autocontrolul aceluiași model se notează `SINGLE_ASSISTANT_REVIEW`, nu `INDEPENDENT_QA`; testul structural PASS verifică numai consistența. Pentru regula NOR032, `I7 §5.2.12.3.10` generic conduit nu înlocuiește PE155/1992 §3.2.10 coloană branșament.
6. **Release gate atomar pe ID**: doar când sursa/ediția, corectitudinea A/B/C, sursa contextuală/rights, QA independent și lipsa conflictelor trec toate, marchează `approved_for_learning=YES`. Până atunci `NO`; un conflict în baremele originale A/C trebuie rezolvat o singură dată la unitate și raportat ambelor grade.
7. **Check structural automat pentru fiecare lot/commit**, compară master QABC + SHA + original keys + traseu + referințe; apoi check end-to-end pe HTML/APK, navigare, repetiții, popup offline, citat contextual și highlights **doar** după aprobarea datelor. Nicio aprobare fără test real.

## Evitarea muncii duble
- Răspuns/explicație/mapare sunt **un singur pachet de evidență**, nu activități seriale ce redeschid aceeași sursă.
- Dacă sursa sau ediția nu sunt accesibile, scrie exact blocajul și **nu repeta cercetarea generică**. Reîncepe strict când apare originalul/ediția/clarificarea.
- Dacă aceeași QABC apare la Gradele I și II, cercetezi o singură dată **dar verifici separat cerințele bibliografice ale gradului și cheia originală**.
- La contradicții, păstrezi concluziile anterioare și adaugi `superseding_correction` cu dovadă verificabilă, fără a șterge istoricul.
- Nu mai număra `research complete` ca `approved`; afișează permanent două contoare independente: `coverage` și `learner approved`.

## Blocaje/limitări
- În prezent, cei 568/822 sunt acoperiți în tabele și cercetarea preliminară 30/30 loturi a trecut QA de integritate. **Nu este dovada că 822 răspunsuri sunt corecte.**
- PR #7 rămâne Draft pe ramura de audit. Nu modifica baremele, HTML, APK, main, nu face merge fără aprobare explicită.
- Niciun agent independent real nu este inventat și niciun worker asincron nu este activat.

## Lecție transferabilă altor proiecte
**Inventar unic → dovezi exacte → explicație/context + obiect final în aceeași trecere → QA independent → aprobarea punctuală, nu reanalizarea tuturor obiectelor.** Păstrează fiecare eșec și verificare ca istoric, distinge experimentul de certificarea reală și reutilizează constatări compatibile între proiecte.
