# QA independent al sincronizării CKPT-043–049

Data: 2026-11-16. Reviewer: subagent `qa_independent`, separat de coordonatorul importului. Scop: integritate arhive, reconciliere schema/câmpuri, identitate QABC/chei și numărătoare fără dublare. **Nu este reverificarea semantică a surselor, edițiilor și tuturor răspunsurilor.** Nu s-a executat cod din arhive; JSON/CSV/MD și intrările ZIP au fost tratate numai ca date.

## Baza de comparație

Worktree verificat: `/workspace/scratch/dcb221b51b62/ANRE_SYNC_CKPT043_049`, HEAD `64ce1f4` (CKPT-042), ramura de audit. Blobul canonic al HTML este `bc5b5a61954ba138cf83987bfc932eca517f3b21`, SHA256 `95be80e0dee42518ec821abc96e45777cbf32c4e2180a08da6b4f974e96c55d9`. Bytes sunt identici cu baza canonică folosită în comparațiile automate locale. Nu s-au schimbat bareme, texte, aplicație sau alte fișiere de către reviewer.

## Integritate și structură

| Control executat | Rezultat |
|---|---|
| MANIFEST_SHA256: cele8 fișiere enumerate | 8/8 SHA256 și8/8 dimensiuni exacte |
| Cele3 ZIP principale | CRC fără erori;47 are7intrări,48are12,49are9 |
| ZIP-ul nested `CKPT047_PLUGIN_RECOVERED_47.zip` din048 | CRC fără erori;4 JSON de lot |
| CKPT047 loturiA/B/C/D |12+11+9+15=47fișe,47ID-uri unice |
| CKPT048 loturi reparate |47fișe cu exact aceleași47ID-uri;35reparări,12fără rotație |
| CKPT049 loturiE/F/G |13+11+12=36fișe,36ID-uri unice |
| CKPT049 variante individuale |108 texte de opțiuni din option_analysis coincid exact cu A/B/C original |
| QABC/cheie047 și048 |47/47 și47/47 identice cu canonul repository;0diferențe |
| QABC/cheie049 |36/36 identice cu canonul;0diferențe |
| CKPT046 |4fișe/8ID-uri de grad: text/ABC și cheia fiecărui membru identice cu canonul;0diferențe |

Schemele au fost inspectate distinct:046 are cards cu stem/members/old_key;047/048 au cards cu obiectul original;049 are liste de rânduri cu id/question/original_key și option_analysis. Nu s-au tratat rezumatele sau fiecare JSON auxiliar drept fișe noi.

## Recuperarea câmpurilor din048

Pentru toate35fișele schimbate, am comparat direct perechile brute047→048. Transformarea verificată este:

- old exact_source.locator → repaired A_research;
- old A_research → repaired B_research;
- old B_research → repaired C_research;
- old C_research → repaired context_romanian;
- old context_romanian → repaired exact_source.locator.

Zero abateri de la această inversare. Cele12fișe ale lotuluiA nu au acea rotație. Originalul QABC/cheie rămâne identic în toate47. Payloadurile din ZIP-ul nested recuperat și copiile reparate top-level coincid după excluderea metadatelor de proveniență `field_alignment_repair`/`CKPT048_recovery`; acestea sunt două reprezentări ale aceleiași reparații, nu47fișe suplimentare. Nu s-au rerulat cele12teste declarate în raportul istoric; această sesiune a executat propria comparație directă a câmpurilor și datelor.

**048 nu înseamnă47întrebări noi și nici35răspunsuri corectate.** Repară35fișe explicative în copia documentară a celor47din047. Originalul047 trebuie păstrat ca dovadă de regresie, iar048 folosit pentru citirea explicațiilor.

## Numărătoare și suprapuneri

| Set | Număr unic și relație |
|---|---|
|047 vs048 |47ID-uri comune integral;zeroID-uri noi în048 |
|047/048 vs049 |zeroID-uri și zero unități QABC comune;049adaugă36unități preliminare |
|046 vs047/048/049 |zero suprapuneri de unități;046adaugă4unități/8ID-uri de grad |
|Unități nou documentate046+047(reparat048)+049 |4+47+36=87unități;8+47+36=91ID-uri de grad |
|MasterCKPT042 contextual existent |15unități/25ID-uri de grad; niciuna dintre cele87nu suprapune aceste15 |
|Uniune contextuală documentară după reconciliere |102unități/116ID-uri de grad, fără a implica validare sau aprobare |
|043/044/045 |follow-up de interpretare pe NOR028 șiNOR023 deja în cele15;nu se numără drept3unități noi |

CKPT049 conține7candidate neaplicate de nepotrivire: NOR053 A→C,054 A→B,058 B→C,060 B→C,061 A→B,062 A→B,066 B→A. Acestea sunt metadate de cercetare, **nu autorizări sau rezultate tehnice independente confirmate**.

## Limite și verdict

PASS pentru integritatea/schemele/alinierile numerice și QABC în domeniul verificat. Fișele reparate păstrează approved_for_learning=false și câmpurile separate QA ca nerulate în sesiunea lor;049manifest declară0aprobări și cercetare preliminară. Absența conflictelor de identitate nu demonstrează adevărul explicațiilor, autenticitatea unei copii ARYA/PE155, ediția aplicabilă2026 sau eliminarea corectă a distractorilor. QA structural actual nu se înscrie drept QA tehnic/lingvistic/sursă de închidere pentru aceste fișe.

Mențiunea istorică048 despre plugin v0.4.4 nepublicat trebuie păstrată ca istorie, fără a fi prezentată drept stare curentă a pluginului. Importul documentar trebuie să păstreze arhivele originale și să marcheze048ca superseding repair al047. Fără commit/push făcut de reviewer; starea GitHub și publicarea sunt responsabilitatea coordonatorului.
