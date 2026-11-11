# CKPT-020 | Pilot Perplexity + Avengers | 2026-11-11

**Scop:** evaluare obiectivă dacă Perplexity găsește **dovezi primare suplimentare** pentru 20 de întrebări P0 distincte, fără să dubleze cercetarea și fără să afecteze baza canonică.

## Lucru efectiv executat
- Au fost selectate 20 ID-uri P0 distincte din V73/V78/V95 și verificate prin `ID_ROUTING_822.csv`, câte o unitate exactă QABC distinctă (20/20). 10 electrotehnică, 5 legislație, 4 norme Grad I, 1 norme Grad II. Toate cele 20 chei originale sunt păstrate.
- Baseline documentar: redeschidere reală a 3 pagini publice relevante pentru 4 ID-uri (DOE pentru G1-ELE-029; Legea123 art92/93 pentru G1-LEG-026/019; Reg66/2023 art37 pentru G1-LEG-034), acoperind **4 ID-uri**. Pentru G1-NOR-089 sursa I7 apare în index, dar pagina directă a returnat 502: **search index only**. Celelalte 15 ID-uri păstrează doar istoric de cercetare, nu înseamnă că nu au dovezi anterioare.
- Comparare explicită A/B/C şi verificare de ediţie pentru fiecare ID: **neînchise**; dovada pentru patru ID-uri este un indiciu specific, nu un verdict de barem.
- Test real Perplexity: **NOT_RUN**. Nu există connector/plugin Perplexity în acest chat şi încărcarea paginii de căutare directă a eşuat; fără token API şi fără execuţie externă. Nu inventăm scor de câştig sau răspunsuri.
- Au fost pregătite 4 runde x5 întrebări şi tabelele necesare pentru completarea/QA a experimentului. Folosirea Free web este posibilă, dar rezultatele necesită exportul sesiunii sau o rulare browser autorizată.

## Artefacte
- `INPUT_20_P0.csv`: întrebările şi variantele originale + ID de unitate, cheie istorică, blocaj preexistent.
- `BASELINE_20_P0.csv`: numai provenienţă explicită a accesării surselor din această sesiune; separă `DIRECT_OPENED` / `SEARCH_INDEX_ONLY` / `PRIOR_EVIDENCE_ONLY`.
- `RESULTS_SCORECARD_TEMPLATE.csv`: toate rezultatele Perplexity încă `NOT_RUN` + câmpuri clare de control al dovezilor.
- `PROMPT_PERPLEXITY_4X5.md`: 4 runde standardizate şi criterii de surse, editii, răspunsuri multiple, grade.
- `CKPT_020_PERPLEXITY_20_P0_BASELINE_2026_11_11.md`: handoff.

## Exemple documentate, fără schimbare de barem
- `G1-LEG-019`: Legea123 art93(1)(3) indică contravenţie B; barem C (abatere); necesită verificarea consolidării2026/QA juridic.
- `G1-LEG-026`: Legea123 art92(2) indică infracţiune B; barem C condiţional; aceeaşi poartă de ediţie/QA.
- `G1-LEG-034`: Reg66 art37(e) susţine A, art37(h) condiţionează participarea la recepţie de solicitare; barem B rămâne neaprobat.
- `G1-ELE-029`: DOE demonstrează invertorul DC-AC ca un contraexemplu la „numai inducţie”, dar nu stabileşte ce sens restrâns a fost intenţionat în examen.
- `G1-NOR-089`: I7 §5.1.4.3.3 apare în index ca suport pentru B, direct502; nu îl marcăm ca sursă redeschisă.

## Metodă de scor, după rularea reală
- `N_primary_useful_new`: URL-uri distincte de sursele existente, redeschise şi cu articol/pagină, ediţie şi grad potrivite.
- `N_conflicts_reduced`: număr de blocaje închise efectiv după QA independent, nu număr de răspunsuri Perplexity.
- `N_false_leads`: surse 404/paywall, versiuni incorecte, obiect/scope greşit sau citări inventate.
- `coverage`: 20 întrebări alocate / 20, dar **Perplexity executed = 0/20**, **approved for learning = 0/20**.
- Se compara acelaşi set cu sursele deja documentate, nu cu o căutare web fictivă. Reviewerul trebuie să redeschidă efectiv fiecare sursă şi să constate accesul şi condiţiile.

## Reguli
- 2026 edition match, ANRE grade match, obiect/condiţii exacte, A/B/C individual, QA independent de autor; fără niciun merge/release şi fără modificări QABC, chei, HTML, APK.
- Regresiile obligatorii NOR032, NOR027 şi capcanele „numai”/„poate” rămân active.
- Baza globală CKPT019: 7/30 loturi preliminare (140/568 unităţi, 186/822 ID-uri); 0/822 aprobări; pilotul NU avansează artificial aceste numere.

## Limitarea de acces
Browserul din acest chat nu poate executa o căutare în contul Perplexity prin pagina web publică, iar API-ul Perplexity este separat de un abonament consumer. Nu s-a folosit o soluţie ocolitoare nesigură, un serviciu „proxy” sau un scraper anti-bot.
