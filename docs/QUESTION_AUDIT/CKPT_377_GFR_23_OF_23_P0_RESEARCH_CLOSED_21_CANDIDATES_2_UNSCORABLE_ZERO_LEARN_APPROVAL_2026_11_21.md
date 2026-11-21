# CKPT-377 | GFR: 23/23 dosare P0 închise la nivel de cercetare, NU la nivel de aprobare

Data: 2026-11-21. Branch: `audit/anre-v8-priority-17-20261109`. PR #7 rămâne Draft.

## Rezultat verificabil

- 23/23 QABC P0 au enunțul și A/B/C originale, sursă identificată, 3 verificări ale variantelor, 3 verificări pereche și test adversarial.
- 27/27 trasee de grad I/II au fost reconciliate exact cu V283 după ID, sursă, rând și cheia importată, fără diferențe.
- 21/23 au candidat bibliografic provizoriu; două nu au răspuns original necondiționat unic: QABC-0094 și QABC-0236.
- 15/23 au text de sursă direct care indică răspunsul; alte 8/23 au calificări și excepții specifice.
- 4/23 au probleme de fidelitate materială față de sursa Excel în textul Trainer: QABC-0143, QABC-0236, QABC-0362, QABC-0386.
- 0/822 aprobări independente calificabile pentru studiu; dosar de cercetare închis ≠ răspuns certificat de ANRE.

## Cele 23 de concluzii de cercetare (literele NU sunt bareme ANRE autentificate)

| ID | Trasee | Chei importate (neschimbate) | Candidat sursă | Motiv și limită |
|---|---:|---|---|---|
| QABC-0017 | 2 | G1-ELE-018=A; G2-ELEC-170=C | A | Matematica modelului trifazat echilibrat: Cs=3C; cheia grad II=C nu este reconciliată |
| QABC-0094 | 2 | G1-ELE-102=A; G2-ELEC-245=C | niciunul | Utilizator A pentru siguranța exploatării; NTE definește stările dar nu o configurație universal preferabilă; G1=A/G2=C |
| QABC-0143 | 1 | G1-ELE-152=A | A | Constanta complexă de propagare γ=α+jβ are 1/km; doar γL e adimensional. Originalul spune greșit adimensională |
| QABC-0235 | 2 | G1-ELE-246=B; G2-ELEC-382=B | C | Cupla longo-transversală combinată economisește investiția prin reducerea celulelor; o creștere universală a siguranței nu este dovedită |
| QABC-0236 | 2 | G1-ELE-247=B; G2-ELEC-383=B | niciunul | Original 2024 B='prin inducţie electromagnetică'; versiune mai veche doar 'prin inducție'. Nu există A/B/C științific exact pentru simplul E; cardul în trei paragrafe ales de utilizator a fost redactat |
| QABC-0279 | 1 | G1-LEG-015=B | A | Art.93(1) pct.28 refuz acces contor: contravenție; art.92 componente / furt: infracțiuni |
| QABC-0283 | 1 | G1-LEG-019=C | B | Art.93(1) pct.3 nerespectarea normelor ANRE: contravenție, nu infracțiune/abatere generică |
| QABC-0288 | 1 | G1-LEG-024=A | C | Art.5/11 Regulament Ordin59/2013 cerere racordare indiferent putere/durată; art.25 ATR pe soluție; orice ATR nou necesită încă juridic exact-scop |
| QABC-0290 | 1 | G1-LEG-026=C | B | Art.92(2) executare/folosire instalații clandestine: infracțiune |
| QABC-0292 | 1 | G1-LEG-028=B | C | Ordin59/2013, Anexa 3 pct.2.3 blocuri locuințe: centralizat parter/palier; nu pct.2.1 |
| QABC-0298 | 1 | G1-LEG-034=B | A | Ordin66/2023 art.37 e obligă respectarea proiectului; h recepție la cerere; i punere sub tensiune operator |
| QABC-0312 | 1 | G1-LEG-048=A | B | Legea123/2012 art.57(2): client casnic poate alege oricare metodă pusă la dispoziție de furnizor |
| QABC-0324 | 1 | G1-NOR-010=B | C | I7 §8.1.1.3.3, PDF utilizator p162: izolația se măsoară între conductoarele active și PE legat la pământ; conductoarele active pot fi unite |
| QABC-0341 | 1 | G1-NOR-027=B | A | PE102 §4.6.3 explică A textual; I7 §5.3.4.3.1.2 faza la contactul central; șurub terminal și contact central nu sunt automat aceeași piesă; PE102 neaplicabil grad I bibliografie 2023 |
| QABC-0356 | 1 | G1-NOR-042=B | A | I7 §5.2.4.6.1(a) N aceeași secțiune cu faza pentru circuit monofazat cu două conductoare indiferent de secțiune |
| QABC-0362 | 1 | G1-NOR-048=A | C | I7 §5.4.13 acceptă circuit de iluminat, prize sau direct tablou; numai din A/B fals; C adevărat; originalul diferă de textul modificat în Trainer |
| QABC-0367 | 1 | G1-NOR-053=A | C | PE155 §1.2.1–2 racord până la firidă, branșament până la punct delimitare la bornele de IEȘIRE ale contorului; C omite de ieșire |
| QABC-0372 | 1 | G1-NOR-058=B | C | I7 §3.0.3.5 excepție sub zone de condens pentru instalații închise IP33 și materiale rezistente, deci C condiționat |
| QABC-0374 | 1 | G1-NOR-060=B | C | I7 §5.5.3.2 conductele pentru apă nu pot fi utilizate drept conductoare de protecție |
| QABC-0375 | 1 | G1-NOR-061=A | B | I7 §5.2.12.3.4 îmbinarea tuburilor la treceri prin elementele de construcție este interzisă |
| QABC-0380 | 1 | G1-NOR-066=B | A | I7 §5.2.12.1.4 interzice conductoare electrice individuale în tuburi/țevi pozate în pământ; nu confunda cu cabluri subterane adecvate |
| QABC-0386 | 1 | G1-NOR-072=B | C | I7 §5.5.2.3 necesară deconectare individuală, și NUMAI cu sculă; original C adevărat, B 'fără sculă' fals; Trainer a rescris B astfel încât și B și C adevărate |
| QABC-0403 | 1 | G1-NOR-089=A | B | I7 §5.1.4.3.3 permite o singură culoare pentru faze, cu identificare corespunzătoare la ambele extremități |

## Pozițiile utilizatorului păstrate distinct

- QABC-0094: A, pentru „siguranta exploatari”, păstrată ca ipoteză, nu ca adjudecare oficială. Detalii CKPT-373.
- QABC-0236: utilizatorul a ales completarea didactică prin card; cardul înainte / text-cheie îngroșat / după este scris în CKPT-376. Termenii fizici rămân separați și originalul nu este schimbat.

## Probe QA

- Comparat noul V289 cu V283: 27/27 rute P0, aceleași rânduri din Excel, aceleași surse și chei importate.
- Comparat V289 cu V284: 23/23 texte A/B/C originale în aceeași ordine.
- V285: 69 verificări enunț-opțiune, 69 verificări între perechi de opțiuni, 23 teste negative, fără presupunerea unei validări independente.
- I7 din biblioteca utilizatorului, SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`, redeschis inclusiv la §8.1.1.3.3 pagina PDF 162.
- Două verificări externe adversariale punctuale: QABC-0235 `resp_9434639e-bbae-43c6-b5b6-3623f659d35e`; QABC-0341 `resp_1b4692f0-f989-435d-b19b-b1a85c7991c2`. Acestea sunt AI, nu certificări de specialist.

## Ce rămâne într-adevăr pentru validarea finală

- Verificarea independentă profesională a răspunsurilor, a logicii și a formulărilor, inclusiv întrebările cu „orice”, „numai”, neconcordanțe de ediție și de model.
- Autentificarea baremelor pe grad sau stabilirea procedurii de tratare a originalelor defective, fără rescrieri atribuite ANRE.
- Stabilirea ediției aplicabile examenului (pagina oficială accesibilă afișează bibliografie 2023).
- Repararea ulterioară a celor patru divergențe de fidelitate din Trainer prin proces aprobat, nu în această rundă.
- Validarea celorlalte 2 trasee P1 și 793 P2 din coada V283, înainte de folosirea aplicației.

## Delimitări

Închiderea acestei runde este **închidere de investigație și adjudecare provizorie**, nu finalizarea cerinței generale de aprobare 822/822. 0/822 rămâne real și explicit. Excel, întrebări canonice, chei, HTML, APK, release și PR #7 au rămas nemodificate.

## Legături

- [V289 registru complet 23/27](./V289_GFR_ALL_23_P0_RESEARCH_DISPOSITIONS_27_ROUTES_SOURCE_NATIVE_A_B_C_RELEASE_GATES_2026_11_21.json)
- [V285 verificări A/B/C](./V285_GFR_23_P0_BIDIRECTIONAL_69_PAIRWISE_QA_8_FORMAL_BLOCKERS_2026_11_21.json)
- [V287 opt cazuri dificile](./V287_GFR_ALL_8_P0_DEEP_SOURCE_RECONCILIATION_QABC_0236_HISTORIC_VARIANT_DIFF_2026_11_21.json)
- [CKPT-376 card didactic 0236](./CKPT_376_QABC_0236_USER_CHOSEN_DIDACTIC_CARD_BEFORE_FOCUS_AFTER_2026_11_21.md)
