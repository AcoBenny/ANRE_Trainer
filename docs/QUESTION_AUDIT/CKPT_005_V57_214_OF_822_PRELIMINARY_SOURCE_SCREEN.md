# CKPT-005 | ANRE Trainer | audit P0: întrebările înaintea aplicației
**Data:** 2026-11-11. **Branch:** `audit/anre-v8-priority-17-20261109`; **PR #7 Draft**.

## Numărătoare controlată
- **822 ID-uri canonice** V10.29 `bc5b5a61954ba138cf83987bfc932eca517f3b21`, 414 G1 + 408 G2, fără renumerotare și fără modificări.
- Etape V33–V40 dinaintea sesiunii: **73 ID-uri unice** cu control individual preliminar.
- În sesiunea actuală V41–V56: **147 fișe/înregistrări controlate** (15 G2 normative-bibliografie; 50 G1 legislație; 62 G2 legislație-bibliografie/admin; 20 G1 electrotehnică).
- **6** ID-uri se suprapun cu auditul anterior: G1-LEG-024,028,032,034,048, G1-ELE-018; **141** ID-uri noi.
- **214/822 ID-uri unice** au acum fișe de reevaluare individuală (pe text normativ/legislativ, explicație tehnică sau verificare bibliografică), **608/822** încă doar la inventar/triaj anterior.
- **0/822 aprobări independente** electrotehnic + lingvistic + legal/surse și **0/822 aprobări de folosire în aplicația finală**. Nu echivala `214 source screened` cu `214 correct answers verified`.
- Registrul unificat: `docs/QUESTION_AUDIT/V57_822_MASTER_COVERAGE_AFTER_V56.csv` (822 rânduri). A fost generat prin combinarea a 17 registre de lot, cu control ID/număr/duplicate.

## Constatări noi critice din sesiune
### Grade II: autenticitate și întrebări invalide
- 77 ID-uri non-electrotehnice G2 = 62 G2-LEG + 12 G2-NOR-136–147 + 3 G2-NORM-001–003, **toate au cheia canonică A**.
- 60/77 întrebări sunt construite ca recunoaștere de document/tematică din **tabelul ANRE 2023** (45 G2-LEG+15 G2-NOR/NORM); 17 G2-LEG sunt construite din pagina informativă oficială ANRE. În registre sunt clasificate ca fapt bibliografic/administrativ, **NU proveniență demonstrată din întrebări oficiale de examen**.
- `G2-NOR-137`, `G2-NOR-141`, `G2-NOR-145` sunt **fără opțiune care să răspundă la întrebarea „prin ce act [aprobat]?”**: toate A/B/C sunt indicative de documente, nu actele aprobatoare. Nu modifica cheia A cu o altă literă; necesită refacerea enunțului/opțiunilor sau excluderea după aprobarea utilizatorului.
- `G2-LEG-081`, `082` conțin valori de tarif cu dependență temporală; actualizarea tarifelor după Ordin 118/2023 rămâne `PENDING`.

### Grade I Legislație: avertizări de barem
- `G1-LEG-019`: canonic C „abatere”; Legea 123/2012 art.93 indică **contravenție**, B candidat.
- `G1-LEG-026`: canonic C „contravenție sau infracțiune”; art.92(2) califică executarea/folosirea instalațiilor clandestine drept **infracțiune**, B candidat.
- `G1-LEG-015`: canonic B „modificarea fără drept” este **infracțiune**, nu contravenție în art92(1); altă variantă nu este încă validată.
- `G1-LEG-020`: canonic A „organe ierarhice”; Ord 74/2014 art2 alin2–3 descrie comisia operatorului emitent, B candidat.
- `G1-LEG-017` și cazurile V34 păstrează `LEGAL_CONTEXT_OR_VERSION_PENDING`, nu se promovează o opțiune conjecturală.

### Grade I Electrotehnică: rezultate și limitări
- `G1-ELE-004` B, (C_{eq}=100+50+100=250\mu F); `G1-ELE-017` A, sarcina egală în serie; `G1-ELE-019` B, doi condensatori identici în serie (C/2): calcul și OpenStax `https://openstax.org/books/university-physics-volume-2/pages/8-2-capacitors-in-series-and-in-parallel`.
- `G1-ELE-005` B, număr de ochiuri independente L-N+1 **numai pentru rețea conexă**, conform teoriei grafurilor; condiția nu e specificată explicit în enunț.
- `G1-ELE-007` A, alunecarea 0–1 **în regim de motor**, nu și regim generator/frânare.
- `G1-ELE-018` A vs duplicat G2-ELEC-170 cu canonic C, conflict existent; deducția (C_s=3C) sub echilibru, pagina academică exactă încă de verificat independent.
- `G1-ELE-014` „câmp fără surse” și `G1-ELE-020` „eliminare totală” cer verificare de definiție/schemă și a afirmației absolute; alte întrebări de practică au `SOURCE_TO_FIND` în registru, NU au trecut QA didactic complet.
- ID `G1-ELE-008` **nu există în canon**, nu inventa o întrebare și nu renumerota. V55 are 001–007+009–011, V56 012–021.

## Surse și QA efectiv
- Documente 2023: ANRE tabel tematic/bibliografic 4 pagini (p1–3 accesate textual/vizual): https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf ; pagina ANRE de autorizare: https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/ .
- Legislație oficială: Legea 123/2012, Ordin ANRE 5/2023, 59/2013, 74/2014, 66/2023, articole exacte în CSV-uri. Ediție 05.2023 și versiune curentă 11.2026 NU au primit toate controalele temporale/excepțiile.
- Fizică electrotehnică: OpenStax University Physics vol2 §8.2, deducții matematice și surse industriale unde există; `SOURCE_TO_FIND` desemnează lacună reală, nu sursă inventată.
- În această sesiune **147 rânduri** au fost citite înapoi din GitHub și validate prin parser CSV cu suport pentru virgule / câmpuri citate, comparate exact cu originalul la ID, enunț, A/B/C, cheie și rând XLSX când există; 0 diferențe, 0 dubluri între noile rânduri. Fișierul V57 are 822 intrări și exact 214 ID-uri unice marcate recontrolate.
- **NU** au fost executate: expert uman independent, expert legal independent, lingvist independent, test Android, comparație exhaustive acte curente, verificare XLSX G2 oficial (linkul binar nu a fost disponibil).
- Fără GitHub Actions, fără editare barem/HTML/APK, fără merge/release. `main` neatins; PR #7 Draft.

## Handoff imediat
1. Continuă **G1-ELE-022 înainte** și în paralel decide un protocol pentru sursele didactice autentice ale celor 595 întrebări de electrotehnică. Nu confunda deducție generală cu confirmarea paginii reale.
2. Verifică proveniența G2: compară efectiv cele 77 întrebări non-electrotehnice cu exemplarele XLSX **oficiale**, dacă devin disponibile; marchează `DERIVED_NOT_OFFICIAL_SAMPLE` unde numai bibliografia e sursă. Cele 3 fără opțiune corectă nu se publică fără aprobare de rescriere.
3. Continuă loturi pe același PR Draft până la 822, documentează conflictele și versiunea temporală, cere aprobare pentru corecții **numai după dovezi**.
4. Respectă <https://github.com/AcoBenny/ANRE_Trainer/issues/10>: **întâi întrebările, abia apoi aplicația**; automatizările ANRE sunt dezactivate la cererea utilizatorului. Fără promisiune de muncă continuă după terminarea sesiunii.
