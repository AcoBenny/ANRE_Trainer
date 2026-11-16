# CKPT-071 | QA readback: 66/66 P0 cu context și corecția dublei numărări ELE-290 | 2026-11-16

## Verificare efectivă a indexului pe ramură
- Repo `AcoBenny/ANRE_Trainer`; branch `audit/anre-v8-priority-17-20261109`, PR #7 Draft/Open, HEAD verificat pre-write `bbbdecd560650abcc1781a782fecc4d5f7424f70`.
- Au fost citite direct din GitHub `MASTER_UNIT_CARDS_568.csv` (568 de rânduri unice) și **12 fișiere CKPT** (050,060–070), păstrând `unit_id` și `representative_id`; nu s-au creditat simple concluzii dintr-un mesaj.
- În master sunt **66/568 unități P0** (potențial problematic, NU 66 răspunsuri greșite). **10** aveau deja context în master. Celelalte **56** au acum fișe documentare P0, toate identificabile prin AU sau ID în CKPT-050/060–070. **0 P0 fără fișă de context**; acest rezultat NU înseamnă 66/66 adjudecate sau QA independent trecut.
- Pentru auditul contextual P0, un singur **AU** a apărut în două fișe cu analiză completă: `AU-fd7d308698e05c41` / `G2-ELEC-290`. Prima fișă a fost **CKPT-050**, iar **CKPT-065** a revenit cu analiză suplimentară, dar a etichetat greșit unitatea drept „nouă” și a crescut greșit subtotalul cu **+1 unitate/+1 ID**.
- Mai există o **mențiune incidentă** a G2-ELEC-290 în CKPT-064 la „următorul lot”; aceea **nu este analiză nouă**. Regula de QA trebuie să numere unic după `unit_id`, iar ID-urile după `member_ids`, nu aparițiile literale în texte.

## Corecția cumulativă, fără rescriere istorică
| Etapă | Unități context reale | ID-uri context reale | Precizare |
|---|---:|---:|---|
| CKPT-050 | 114/568 | 139/822 | 12 unități și 23 ID-uri documentate atunci |
| CKPT-060 | 116/568 | 143/822 | +2/+4, incl. ELE-066 promovat P2 |
| CKPT-061 | 120/568 | 151/822 | +4/+8 |
| CKPT-062 | 125/568 | 158/822 | +5/+7 |
| CKPT-063 | 128/568 | 164/822 | +3/+6 |
| CKPT-064 | 133/568 | 174/822 | +5/+10 |
| CKPT-065 | **136/568** | **179/822** | +3/+5 reale: ELE-220, ELE-229, ELE-249; ELE-290 era în CKPT-050 |
| CKPT-066 | **141/568** | **184/822** | +5/+5 |
| CKPT-067 | **145/568** | **188/822** | +4/+4 |
| CKPT-068 | **150/568** | **193/822** | +5/+5 |
| CKPT-069 | **155/568** | **198/822** | +5/+5 |
| CKPT-070 | **159/568** | **203/822** | +4/+5 |

**Cumulul verificat după CKPT-070: 159/568 unități și 203/822 ID-uri documentate contextual**, nu 160/568 și 204/822 cum afișau documentele incrementale. Numărările istorice rămân intacte pentru trasabilitatea erorii; **acest CKPT-071 este registrul de reconciliere prioritar** pentru continuare. `0/822` întrebări aprobate pentru învățare; fără bibliografie/exam-grade+edition signoff și fără QA tehnic/lingvistic/sursă independent.

## Distribuția unităților P0 cu fișe de context (fără dublare)
- **10** în MASTER, documentate anterior (ELE-018, ELE-102, ELE-029, ELE-043, ELE-073, ELE-104, NOR-023/027/029/032).
- **12** în CKPT-050 (inclusiv G2-ELEC-290).
- **1** în CKPT-060 (G1-ELE-020; G1-ELE-066 este P2 promovat și nu intră în 66 P0).
- **4** în CKPT-061; **5** în CKPT-062; **3** în CKPT-063; **5** în CKPT-064.
- **3 unice** în CKPT-065; **5** în CKPT-066; **4** în CKPT-067; **5** în CKPT-068; **5** în CKPT-069; **4** în CKPT-070.
- **Sumă 10+12+1+4+5+3+5+3+5+4+5+5+4 = 66 P0 distincte**. Fiecare P0 are cel puțin o fișă, nu orice fișă este perfectă sau semnată.

## Porți P0 rămase deschise, înainte de training
1. Contradicții importate vs surse primare, inclusiv `ELE-124`, `G1-LEG-015/019/026/048/024/034`, `G1-NOR-010/012/042/089`, plus conflicte între grade `ELE-018/102`; verificați **ediția exactă** și noțiunea juridică înainte de orice propunere de corecție.
2. Lipsă diagramă originală `ELE-028`, formulare `G2-NOR-137/141/145` cu **act aprobator** versus **indicativ**, sursă istorică exactă `NOR-030/031`, multe exclusivități „numai”, suprapuneri semantic tehnice.
3. **QA independent** pe opțiuni A/B/C, surse, lingvistică, statutul publicării ca întrebare oficială, condiții de simulare și drepturi offline. `0/822` approvals.
4. Trecerea la **P1/problematic** pentru contextualizare, păstrând P0 conflictele în registrul de escaladare. **Nu** transformați screeningul P0 complet în promisiunea că toate P0 sunt rezolvate; conflictul nu se închide prin numărare.

## Lecția Avengers Asamble, de integrat în QA
**`UNIT_ID_SINGLE_CREDIT`**: înainte de raportarea delta unui lot, comparați exact `unit_id`/hash și toate `member_ids` cu fișele anterioare din repo, nu doar cu coloana `contextual_explanation` a MASTER. Masterul rămâne neschimbat deoarece politica utilizatorului permite numai documentație, deci master gol nu înseamnă lipsă de fișă nouă. Un nou raționament poate merita un CKPT nou **fără credit de coverage**. Test negativ obligatoriu: a doua fișă ELE-290 are delta reală 0.
- Acest control identifică și **corectează** o eroare din activitatea proprie anterioară; nu șterge CKPT-065 și nu modifică baremele, enunțurile, HTML/APK, CSV, main, merge/release.
