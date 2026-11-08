# ANRE Trainer | Indexarea OCR a manualului scanat (audit didactic, fără implementare)

**Data:** 8 noiembrie 2026  
**Versiune de lucru:** OCR overlay V2, peste indexul structural al celor 11 surse canonice.  
**Decizie utilizator:** mai întâi verificăm manualele, apoi cele 822 de întrebări; nicio modificare a aplicației.

## Rezultate reale

- Scan original: `695172381-Manual-Pentru-Autorizarea-Electricienilor-Instalatori.pdf`, **332 pagini**, SHA-256 `b85057732a71d96d4d217a42f5e2c1e9996f24e0011c5de374e7c878341b110a`.
- PDF OCR: `ANRE_Manual_Electricieni_1995_332pag_OCR_RO_CAUTABIL.pdf`, SHA-256 `1ceac1f2eec5469afdbb561f74060b985146987d9b062f3eb93d98788723702a`.
- **324/332 pagini** au text OCR căutabil; opt pagini albe sau fără text relevant nu au fost transformate în pagini didactice.
- Biblioteca canonică: **3.374/3.464 pagini cu strat text**, față de 3.050 înainte de OCR (plus 324); **90** încă fără text suficient, predominant diagrame/copertă/pagini din alte PDF-uri. Procent căutabil: **97.4%**.
- În manualul istoric, scanarea cu 45 de categorii detectează *termeni* din **35/45** domenii în partea teoretică (pagini fizice PDF **35–146**) și din **41/45** undeva în document. Acești indicatori nu certifică faptul că explicația este completă sau că formula este corectă.
- Șase categorii apar numai în alte părți ale documentului (adesea legislație istorică, securitate sau grile): `linii_aeriene, posturi_de_transformare, iluminat_siguranta, instalatii_situatii_speciale, emc_perturbatii_armonici, siguranta_muncii`. Nu le promovăm drept surse didactice teoretice.
- Patru categorii nu au potrivire pe dicționarul de termeni OCR: `camp_electric, legislatie_autorizare, energie_solara_eolian, incarcare_vehicule_electrice`. **Absența unui cuvânt-cheie nu dovedește absența conceptului.**

## Controale efectuate

- S-a recitit PDF-ul OCR cu PyMuPDF; textul apare pe 324 de pagini; căutarea locală din indexul FTS5 (SQLite) funcționează. Exemple de pagini OCR identificate: `transformatoare` → [4, 73, 80, 99, 100, 101], `electrotehnica` → [3, 26, 35, 36, 37, 38], `coulomb` → [39, 49], `protecție` → [6, 7, 13, 25, 85, 86].
- **12/12** pagini eșantionate au rasterizare pixel cu pixel identică în PDF-ul original și cel cu strat OCR (la factor de randare 0,75). Această verificare arată fidelitatea imaginii, nu calitatea fiecărui cuvânt recunoscut.
- Exemplu de limitare: pagina PDF **99** tratează transformatoarele, dar ecuația raportului de transformare este deteriorată în transcrierea OCR. **Formula se va verifica vizual în scanul original**, nu se va cita din textul OCR.
- Indexul a fost extins cu navigare OCR pentru cele 332 de pagini, o matrice pe cele 45 de concepte și o bază locală FTS5 pentru căutarea în textul OCR al manualului istoric. Restul celor 10 lucrări canonice păstrează indexul anterior; nu s-a repetat inutil extragerea din catalogul mare Schneider 2024.

## Clasificarea autorității și a drepturilor

- Manualul este din **1995**. Explicațiile fizice pot servi drept punct de pornire pentru audit, dar normele, condițiile de autorizare și legislația citate sunt **istorice**, nu sunt dovadă de drept actual.
- Zonele de pagini OCR sunt clasificate orientativ: 1–16 front matter/cuprins; 17–34 autorizare istorică; 35–146 teorie; 147–218 norme/securitate istorice; 219–298 **întrebări de examen, NU material didactic în sine**; 299–332 anexe. Delimitările sunt derivate din cuprins și pot necesita confirmare pentru secțiunile de tranziție.
- Documentul OCR și baza SQLite conțin text aparținând materialului încărcat de utilizator: **se oferă numai ca descărcare privată a utilizatorului**; nu se publică în repository. În GitHub salvăm doar metadatele, codurile de concepte și legăturile către pagini.
- Permisiunea de a redistribui PDF-urile sau extrase lungi în APK **nu este verificată**.

## Ce rămâne pentru „bibliotecă validată”

1. Audit tehnic al formulelor, diagramelor și paragrafelor de pe paginile candidate, inclusiv cele în care OCR a distrus indici/simboluri.
2. Revizuirea celor **90 de pagini fără text** din celelalte surse: identificăm paginile cu diagrame care merită indexate vizual, fără OCR inutil pe pagini albe/catalog.
3. Compararea domeniilor din cele 11 surse cu **tematica oficială ANRE**, și căutarea unor surse suplimentare pentru lacunele reale; reglementările I7 trebuie versionate separat.
4. Audit de proveniență, calitate și drepturi de utilizare. Numai după aceea asociem sistematic sursele cu toate cele 822 de întrebări.

**Status:** `OCR_INDEXING_PASS` / `SOURCE_SEMANTIC_QA_PENDING` / `OFFLINE_RIGHTS_NOT_VERIFIED` / `QUESTION_MAPPING_NOT_RESTARTED` / `INDEPENDENT_QA_NOT_RUN` / `APP_NOT_MODIFIED` / `EXTRA_COST_0_RON`.

**Checkpoint:** CKPT-002 rămâne ultimul; acesta este doar un registru de progres intermediar.

## Următoarea selecție: paginile grafice fără text

După OCR rămân **90 de pagini fără strat text suficient** în cele 11 surse canonice: 20 în *Cartea electricianului din stații și PT-uri*, 51 în catalogul Schneider 2024, 8 în manualul scanat 1995 (pagini goale/aproape goale), 8 în ghidul IEC, 2 în cursul PREG și 1 în catalogul Finder.

- Au fost inspectate vizual un eșantion de **15 pagini** din documentele non-OCR. Paginile Finder p.61 și PREG pp.2,8 apar goale, iar exemple din Schneider și IEC reprezintă copertă/separatoare de capitole. **Nu generalizăm la toate paginile lor**.
- Toate cele **20 de pagini fără text ale sursei STATII** au fost previzualizate într-o planșă de contact. Au fost identificate desene de echipamente, scheme, grafice și tabele, importante pentru catalog. Clasificările sunt generale, fără validarea inginerescă a simbolurilor sau a legendelor.
- Registrul `NON_TEXT_PAGES_VISUAL_TRIAGE_90_2026_11_08.csv` consemnează toate cele 90 de pagini cu priorități candidate; `STATII_GRAPHIC_ONLY_20_VISUAL_INDEX.csv` păstrează etichetele vizuale din planșa de contact. Un grad mare de alb sau lipsa de text nu justifică eliminarea unei pagini tehnice.
- **Fără OCR în masă pentru cele 90**: mai întâi separăm schemele și tabelele de copertă/pagini albe; formularele/drawings necesită verificare vizuală, nu doar transcriere de caractere.
