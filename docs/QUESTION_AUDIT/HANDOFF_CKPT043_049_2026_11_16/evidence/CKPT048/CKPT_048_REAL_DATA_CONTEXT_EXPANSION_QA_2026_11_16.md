# CKPT-048 | Avengers Asamble / ANRE Trainer | Testare reală a Expansiunii Contextuale
**Data:** 16.11.2026  
**Stare:** REAL DATA + QA STRUCTURAL, NU aprobare a răspunsurilor  
**Plugin publicat:** Avengers Asamble v0.4.3, neschimbat. **Patch v0.4.4:** pregătit local, nepublicat.  
**Repo ANRE:** `AcoBenny/ANRE_Trainer`, PR #7 Draft, **neactualizat în această sesiune**. Nu s-au schimbat baremuri, HTML, APK, `main`, release/merge.

## 1. Rezultatul verificării de date reale

- Am folosit arhiva locală `CKPT_047_4_LOTURI_47_GRILE_2026_11_16.zip` din patru loturi și copia Library `ANRE_Trainer_MAPPING_FINAL_V1.csv` cu **822 ID-uri** (SHA256 `effa386b6e9c4d8e529b313af822c068fea5e0ed0473e40eb2adcd4be8c0a43f`).
- Au fost confruntate efectiv **47/47 ID-uri** cu întrebările, A/B/C și cheile originale. **0 nepotriviri canonice**.
- Defect detectat: **35/47 fișe din loturile B/C/D** aveau următoarea rotație exactă de export:
  1. `exact_source.locator` conținea explicația opțiunii A;
  2. `A_research` conținea explicația B;
  3. `B_research` conținea explicația C;
  4. `C_research` conținea paragraful contextual;
  5. `context_romanian` conținea referința normativă reală.
- Lotul A avea **12/12 fișe fără această eroare**; B **11/11 afectate**; C **9/9 afectate**; D **15/15 afectate**.
- O reparație deterministă și **non-distructivă** a reconstruit 35 fișe într-o copie nouă. Păstrăm originalul CKPT-047 nemodificat ca probă a regresiei. În copia corectată: **47/47 fără semnale de nealiniere**, **47/47 cu enunț/A/B/C/cheie identice cu sursa**.
- Două implementări distincte ale recuperării au fost comparate automat pe **47 fișe × câmpurile critice**: **0 diferențe** (nu este QA tehnic independent).

## 2. Extindere contextuală pe cazuri reale (nu scenarii fictive)

Am produs 8 fișe de *context-expansion* cu ancoră, legătura exactă cu sursa, explicația contextuală, A/B/C, contradicții, limită de căutare și indicatori de încredere. Sunt cazuri din CKPT-047, nu afirmații că modelul a rulat de 8 ori independent.

| Întrebare | Indiciu contextual important | Rezultat de cercetare |
| --- | --- | --- |
| `G1-NOR-010` | Măsurarea izolației față de PE vs doar între active, I7 §8.1.1.3.3 | B original / C candidat, neaprobat |
| `G1-NOR-012` | Condițiile de material vs „întotdeauna”, I7 §5.1.7.2(a) | B original / C candidat, neaprobat |
| `G1-NOR-042` | Monofazat cu două fire vs polifazat cu praguri 16 Cu / 25 Al, §5.2.4.6.1 | B original / A candidat, neaprobat |
| `G1-NOR-089` | Aceeași culoare pentru faze permisă cu identificarea capetelor, I7 §5.1.4.3.3 | A original / B candidat, neaprobat |
| `G1-NOR-090` | Permisiunea de montaj direct §5.2.12.2.12 și condiții speciale §5.2.12.2.11 | B original; C poate reproduce literal regula generală, unicitate încă necertificată |
| `G1-NOR-007` | Prag maxim 2 kW vs orice valoare sub prag, I7 §5.3.2.3 | C original, cercetare neaprobată |
| `G1-NOR-065` | Prize dedicate în locuințe peste 2 kW: alt obiect decât regula generală pentru prize | A original, cercetare neaprobată |
| `G2-NOR-137` | „Prin ce act aprobat” nu înseamnă indicativul I7-2011 | A original; niciun răspuns valid în formularea exactă, cercetare neaprobată |

**QA structural contextual:** 8/8 fișe acceptate drept formă corectă în `context_expansion_gate.py` și 8/8 exemple mutate intenționat pe surse de alt domeniu respinse. **Nu** sunt probe de adevăr normativ: pasajele citate sunt din cercetarea anterioară și indexarea publică; re-deschiderea oficială completă a I7 în această sesiune a returnat HTTP 502. Încă nu este dovedită bibliografia/ediția integral aplicabilă 2026. QA tehnic, de sursă și lingvistic independent: `NOT_RUN`.

Surse orientative pentru redeschidere într-un mediu cu acces oficial: [I7 Portal Legislativ](https://legislatie.just.ro/Public/DetaliiDocument/286763) (§5.2.12.2.11–.12; §5.2.4.6.1; §8.1.1.3.3), [bibliografie ANRE mai 2023](https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf). Nu confundăm rezultatele din indexarea surselor cu o certificare vizuală a ediției complete.

## 3. Automatizare de QA / îmbunătățire propusă

Am creat un patch **Avengers Asamble v0.4.4 (DEV, NU publicat)**:
- `semantic_field_alignment.py scan`: verifică maparea semantică pentru sursă, explicațiile A/B/C, paragraf și barem, cu confruntarea bazei originale;
- `recover`: repară doar tiparul precis de rotație documentat și creează **arhivă nouă**, fără modificarea originalului;
- reguli noi în coordinator, context skill și QA evidence gate;
- `14/14` teste sintetice pe noul validator, `31/31` teste sintetice ale context gate v0.4.3; `47/47` fișe reale validate structural după corecție; `8/8` scenarii de domeniu greșit blocate.

Testul original pe CKPT-047 returnează `BLOCKED_ALIGNMENT` (**35 fișe**) și copia reparată returnează `ALIGNMENT_PREFLIGHT_PASS_NOT_SOURCE_QA` (**47 fișe**, zero probleme de aliniere). Niciuna dintre aceste verificări nu certifică adevărul răspunsurilor.

**Principiul învățat:** verificarea cantității + integrității QABC nu verifică automat și **identitatea semantică a câmpurilor sursă/explicație**. Extinderea contextului trebuie să confirme că dovezile sunt atribuite locului corect, nu numai să adune paragrafe.

## 4. Limite și continuare

- **0/822 răspunsuri aprobate pentru învățare**. Acest checkpoint nu adaugă noi grile cercetate față de CKPT-047, ci repară documentația și extinde QA pe 8 cazuri cu proveniență reală. Nu crește artificial statistica de 66/568 fișe locale documentate anterior.
- **Publicarea v0.4.4 și sincronizarea GitHub sunt blocate intenționat** până la permisiunea corespunzătoare și disponibilitatea instrumentelor. Pluginul efectiv instalat rămâne v0.4.3.
- Următorul lot ANRE: read-open oficial sursă specifică + versiune 2026 + validare A/B/C și reviewer independent; prioritate cazurile cu barem diferit față de sursa aparentă. Fără îmbinarea cercetării preliminare cu certificarea completă.
