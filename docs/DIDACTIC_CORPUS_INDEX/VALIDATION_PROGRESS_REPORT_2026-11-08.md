# ANRE Trainer | Registrul de validare a conceptelor didactice (V1)

**Data:** 8 noiembrie 2026  
**Obiect:** biblioteca didactică ANRE Trainer, nu întrebările și baremele din aplicație.  
**Decizie obligatorie:** fără implementare HTML/APK/DB sau schimbări ale celor 822 de întrebări până la finalizarea auditului surselor și aprobarea utilizatorului.  
**Ultimul checkpoint:** CKPT-ANRE-20261108-02 (nu creăm unul nou pentru acest registru).

## 1. Care este numitorul progresului?

Indexul inițial are **45 etichete**. `produs_referinte_coduri` este metadată comercială, nu disciplină didactică. Au rămas **44 categorii curriculare provizorii**. Acestea nu sunt încă toate conceptele atomice necesare; unele trebuie împărțite. Procentele se referă **strict la versiunea V1 a acestor 44 de categorii**.

### Indicatori măsurați

| Indicator | Număr | Ce măsoară |
|---|---:|---|
| Categorii curriculare V1 | **44** | 45 minus eticheta comercială |
| Categorii cu cel puțin o observație preliminară | **25 / 44 (56,8%)** | Nivel de **explorare**, nu certificare |
| Categorii aprobate final prin QA independent | **0 / 44 (0%)** | Nivel de **validare** în sens strict |
| Categorii prioritare pentru revizuire | **13** | 5 cu risc/lipsă de sursă sau actualitate; 8 cu revizuire de acoperire / granularitate |
| Categorii cu doar indexare, fără eșantion semantic | **12** | Căutări după cuvinte-cheie disponibile, dar fără SQA legat |
| Observații tehnice documentate | **42** | Verificări de pagini/concepte existente (41 legate de categorie, 1 generică neasociată) |
| Subteme speciale propuse spre verificare | **19** | Registru separat; nu amestecăm numărătorii până la adoptarea V2 |

### Distribuție exclusivă a celor 44 de categorii

| Stare | Categorii |
|---|---:|
| Eșantion preliminar, fără risc prioritar cunoscut | 19 |
| Revizuire prioritară (granularitate, scheme, condiții) | 8 |
| Sursă lipsă sau risc de actualitate/autoritate | 5 |
| Neexaminate semantic, doar indexate | 12 |
| **Total** | **44** |

**Atenție:** unele dintre cele 13 categorii prioritare au și observații preliminare. De aceea *25 cu eșantion*, *13 prioritare* și *12 doar indexate* sunt indicatori diferiți, nu categorii care trebuie adunate într-un singur total.

## 2. De ce 0% aprobare finală?

Cele 42 de verificări din prima trecere au fost realizate prin consultarea textului extras și inspectarea unor imagini PDF originale. Au detectat probleme concrete (de exemplu confuzia dintre rezistență și rezistivitate la legea Joule-Lenz în PREG p.52), dar **nu s-a efectuat încă un audit independent**. Prin urmare niciun capitol sau categorie nu poate avea statutul „aprobat definitiv”.

Un concept va primi **APROBAT_FINAL** numai când:

1. are o afirmație tehnică formulată explicit, pagina fizică PDF și paragraful/figura exacte; versiunea și rolul sursei sunt identificate;
2. au fost verificate în imagine originală formulele, indicii, semnele, unitățile, diagramele și ipotezele care pot schimba răspunsul;
3. un revizor tehnic distinct validează afirmația și sursa, iar pentru norme este confirmat textul în vigoare și domeniul de aplicare; folosirea offline se face doar în limitele drepturilor disponibile;
4. nu există conflicte de sursă sau precizări lipsă nerezolvate pentru subtemele relevante.

**O categorie cu un singur exemplu verificat nu este considerată acoperită integral.** Cazul `SQA-021 Conversie energetică` nu a fost atribuit arbitrar unei clase de mașini electrice.

## 3. Cele 13 categorii de control prioritar

`camp_electric`, `camp_magnetic`, `energie_solara_eolian`, `incarcare_vehicule_electrice`, `instalatii_situatii_speciale`, `legislatie_autorizare`, `linii_aeriene`, `masini_asincrone`, `protectie_supratensiune`, `r_l_c_impedanta`, `racordare_furnizare_contracte`, `scheme_relee_automatizari`, `siguranta_muncii`.

**19 subteme candidate** detaliază aceste zone: div B=0; vectorul Poynting; semnul Lenz; RC/RL tranzitoriu; Corona; capacitatea de serviciu LEA; GIS/instalații speciale; moduri de încărcare EV; regimuri ale mașinilor asincrone; protecții de supratensiune; versiuni normative etc. Lista este extensibilă. *Categoria GIS merită verificată și în cadrul subtemei „instalații speciale”; nu este încă un număr suplimentar de întrebare sau aprobare.*

## 4. Fișierele registrului

- **ANRE_Registru_Validare_Concepte_2026-11-08.xlsx**: panou cu indicatori calculați prin formule, 45 etichete (44 incluse), cele 42 de dovezi, 19 subteme și reguli QA.
- **ANRE_REGISTRU_44_CATEGORII.csv**: fișierul sursă, cu status, responsabilitatea verificării și pagini candidate.
- **ANRE_DOVEZI_QA_42_CONECTATE.csv**: legături explicite între 42 de observații și categoriile curriculare. 41 asociate; una generică neasociată.
- **ANRE_SUBTEME_LACUNE_19.csv**: domeniile care necesită materiale/versiuni/diagrame suplimentare.
- **ANRE_REZUMAT_PROGRESS.json**: indicatorii și definițiile verificabile automat.

## 5. Reguli de actualizare

- Indexare structură pagini: **realizată** (3.464 pagini canonice; 3.374 căutabile după OCR).
- Verificare preliminară pe categorii: **25/44**, încă incompletă.
- Validare definitivă: **0/44**, independent QA neexecutat.
- Dacă o categorie se desparte în două sau mai multe subteme, creăm o **versiune nouă a taxonomiei** și consemnăm noul numitor; nu modificăm retrospectiv procentele.
- Rămâne interzisă implementarea și actualizarea baremelor înainte de auditul și aprobarea explicită a utilizatorului.

## Proveniență

Datele provin din `docs/DIDACTIC_CORPUS_INDEX/MANUAL_45_TOPIC_COVERAGE_QA_FIRST_PASS.csv` și `docs/DIDACTIC_CORPUS_INDEX/SOURCE_SEMANTIC_QA_FIRST_PASS_42.csv`, care reprezintă rapoarte de audit ale bibliotecii PDF încărcate de utilizator, **nu o certificare ANRE**. Manualele originale nu sunt redistribuite în GitHub. Nu am efectuat în acest pas noi verificări independente ale celor 3.464 de pagini, nu am rulat un model specializat separat și nu am modificat aplicația.
