# Avengers Academy: regula „enunţ + completare” / variante-capcană | v1 | 2026-11-12

## Provenienţa lecţiei
Caz colaborativ: `G1-NOR-041` (Grad I; barem original B, NEMODIFICAT).
Utilizatorul a observat:
- enunţul are formă de **afirmaţie incompletă** („Conductorul neutru trebuie să aibă aceeaşi secţiune cu faza:”), iar fiecare răspuns îl continuă.
- **A** pare adevărat dacă citeşti doar prima parte, dar adaugă o generalizare greşită;
- **B** conţine condiţia şi pragurile corecte;
- **C** are structură plauzibilă, dar modifică valorile admise;
- nu numai enunţul poate ascunde o capcană: **fiecare variantă** poate avea cuvinte precum „indiferent”, „numai”, „până la”, cifre sau excepţii false.

Interpretarea utilizatorului este `USER_REASONING`, distinctă de dovezile tehnice de mai jos şi de aprobarea finală.

## Ce e verificabil din sursele găsite
**I7-02, §5.1.8** (reproducere HTML, nu facsimil oficial validat):
https://www.rasfoiesc.com/inginerie/electronica/NORMATIV-PENTRU-PROIECTAREA-SI29.php
- conţine **separat** regula pentru „monofazate cu două conductoare, indiferent de secţiune”;
- apoi conţine expres **„monofazate cu trei conductoare şi ... polifazate ... 16 mm² Cu sau 25 mm² Al”**, formulare aproape identică cu B.

**I7-2011 §5.2.4.6.1** (Portal Legislativ indexat; deschiderea directă a returnat 502):
https://legislatie.just.ro/Public/FormaPrintabila/00000G21NAWUB675P0O2JT8X45KA4QZH
- structură diferită: (a) circuite monofazate cu două conductoare; (b) circuite polifazate la pragurile 16 mm² Cu /25 mm² Al; plus alte condiţii pentru armonici/dezechilibru;
- simpla asemănare a pragurilor nu înseamnă că ediţia poate fi schimbată fără a compara exact enunţul. **I7-02 este istoric, nu documentul automat aplicabil examenului actual.**
- NU deduce automat `trei conductoare = L+N+PE` doar ca să faci sursele să pară egale: această sintagmă există literal într-o ediţie anterioară; provenienţa exactă a întrebării din chestionar nu este încă certificată.

**Mică corecţie de unităţi:** 16/25/35 **mm²** sunt secţiuni transversale ale conductorului, nu diametre.

## Logica nouă, testabilă
```text
IF întrebarea este un ENUNŢ DE COMPLETAT:
  FOR each option:
     afirmaţie = enunţ + opţiune
     verifică toate conjuncţiile ("şi", "sau") şi restricţiile
     respinge generalizări nejustificate ("indiferent" la polifazate)
     verifică pragurile distinct pe material: Cu şi Al
     compară numărul de conductoare şi condiţiile cu EDIŢIA exactă
  IF o singură completare reproduce regula contextuală:
     propune candidatul, fără aprobare automată
  ELSE:
     escaladează sursa/versiunea/ambiguitatea reală
```

### Evaluare pentru G1-NOR-041 pe forma normativă I7-02
- A: **OVERBROAD_UNBOUNDED_POLYPHASE**, nu doar „incomplet”: spune „indiferent de secţiune”, deşi reducerea neutrului poate fi permisă în condiţiile normei la secţiuni polifazate mai mari.
- B: **MATCH_RULE** cu 16 mm² Cu şi 25 mm² Al şi expresia „trei conductoare” din I7-02 §5.1.8. **Candidat B** (deja cheie stocată).
- C: **WRONG_MATERIAL_THRESHOLDS**, 25 mm² Cu şi 35 mm² Al nu sunt pragurile acelei propoziţii normative.
- Dacă înlocuieşti sursa cu I7-2011, se produce **SOURCE_EDITION_SCOPE_MISMATCH**, nu alegere forţată. Nu confunda „răspunsul urmărit de vechiul chestionar” cu „dovada că formularea este perfect aliniată normei actuale”.

## Artefacte / regresii
- `tools/qa_statement_completion.mjs`: clasificator îngust de completări conjunctive faţă de o regulă structurată, include parser pentru `trei` şi `3`, `mm²`, `mm2`, delimitarea mono/polifazat, Cu/Al şi `indiferent`; **nu** citeşte automat PDF/norme şi **nu** certifică sursa.
- `tools/tests/qa_statement_completion.test.mjs`: **11 teste sintetice** (original B, conflict 2011, A nelimitat, C supradimensionat, răspuns duplicat, permutare, sursă absentă, enunţ necompletabil, unitate invalidă, ABC incomplet, diacritice/cifre).
- Execuţie efectuată prin **JS runner pe aceleaşi funcţii şi fixtures**: prima încercare a eşuat deoarece parserul suporta `3 conductoare`, nu `trei conductoare`; corectat şi reexecutat **11/11 PASS**. Scriptul Node salvat în GitHub **nu este încă executat separat de CI**. Aceasta este verificare deterministă de parser, nu QA independentă a surselor.
- `APPROVED_FOR_LEARNING=NO`, `INDEPENDENT_QA=NOT_RUN` pentru această nouă verificare. Nu schimbă baremul, variantele, HTML/APK, `main`, nu merge/release.

## Regula de economie a resurselor
În viitoarele întrebări de completare, clasificatorul semnalează imediat *care conjunct* sau *ce prag* strică varianta, fără alt research pe opţiunile deja demonstrabil false; mai multe surse se cer numai când ediţia şi obiectul diferă. Păstrăm capcanele legitime în forma originală.
