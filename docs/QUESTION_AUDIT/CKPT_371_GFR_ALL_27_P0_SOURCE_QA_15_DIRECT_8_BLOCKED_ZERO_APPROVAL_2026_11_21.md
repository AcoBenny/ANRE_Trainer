# CKPT-371 | GFR Punctul 1: toate cele 23 P0 QABC / 27 trasee cercetate pe Excel original | 2026-11-21

## Rezultat executat acum, nu intenție

- Au fost refăcute verificările de obiect, condiții, textul original A/B/C și sursă pentru **toate cele 23 QABC / 27 trasee P0**, fără a folosi formulările rescrise în aplicație drept autoritate a examenului.
- Dosarul [V284](./V284_GFR_23_P0_SOURCE_NATIVE_OPTION_QA_AND_ADVERSARIAL_LETTER_LOCK_2026_11_21.json) conservă **69 evaluări între enunț și opțiuni**, câte un test negativ pentru fiecare întrebare, candidați de sursă și limite.
- Dosarul [V285](./V285_GFR_23_P0_BIDIRECTIONAL_69_PAIRWISE_QA_8_FORMAL_BLOCKERS_2026_11_21.json) adaugă **69 de comparații pereche A/B, A/C, B/C** la cele 23 QABC, refuză concluziile nejustificate, și detaliază cele 8 blocaje.
- **15 QABC / 16 trasee**: au o alegere provizorie susținută direct de citatul sursei în obiectul și contextul cercetat; acestea NU sunt cheia oficială și NU sunt validate pentru învățare.
- **8 QABC / 11 trasee**: au rămas explicit condiționate, incomplete sau nesusținute ca item cu răspuns unic fără probe suplimentare, după cum urmează:

| QABC | Grade routes | Motivul exact al reținerii finale |
|---|---|---|
| QABC-0017 | G1-ELE-018, G2-ELEC-170 | În modelul simetric fază-neutru Cs=3C (A), dar Grade II importat C; convenția de definire a lui Cs și baremul autentic necesită reconciliere |
| QABC-0094 | G1-ELE-102, G2-ELEC-245 | Două sisteme de bare și cuplă în funcțiune ori rezervă caldă sunt moduri reale diferite; nu rezultă o preferință universală fără condiții de sistem; import A/C diferit între grade |
| QABC-0143 | G1-ELE-152 | A = constanta de propagare este intenția probabilă, dar în Excel original „adimensională” e eronat pentru gamma cu unitate 1/km; app a schimbat enunțul |
| QABC-0236 | G1-ELE-247, G2-ELEC-383 | În Excel original B spune „inducție electromagnetică”, nu electrostatică; niciuna dintre opțiunile originale nu denumește exact polarizarea unui conductor în câmp electrostatic; app a schimbat opțiunea |
| QABC-0288 | G1-LEG-024 | Ordin ANRE 59/2013 art.11 cere cerere pentru fiecare loc nou indiferent de durată/putere, dar asta nu certifică absolutul din C „ATR obligatoriu pentru orice”; trebuie separate cerere, ATR și certificat/actualizare |
| QABC-0341 | G1-NOR-027 | PE102/1986 art.4.6.3 susține A dar este **NU în bibliografia Grad I 2023**. Am redeschis textul I7 din fișierul utilizatorului, **pagina PDF 67, §5.3.4.3.1.2**: faza se leagă la *contactul central al soclului siguranței cu filet*. Această sursă este relevantă pentru Grad I; trebuie dovedită corespondenta „șuruburile de contact” cu „contactul central”, fără a confunda componentele |
| QABC-0367 | G1-NOR-053 | PE155/1992 diferențiază branșament/racord, C este cea mai bună alternativă; în Excel, C omite „bornele **de ieșire** ale contorului”, condiția exactă de delimitare |
| QABC-0386 | G1-NOR-072 | Originalul C „deconectabil individual” este adevărat, dar norma cere în plus „numai cu sculă”; B din Excel spune explicit „fără sculă”, opus normei. Versiunea rescrisă a aplicației face B și C simultan adevărate |

## Descoperire critică QA: adversarial AI nu poate înlocui maparea literelor

Un model extern a citit texte legale corecte pentru cele **7** QABC de legislație, dar a produs **7/7 litere greșite**, de fiecare dată întorcând litera deja *importată în aplicație* în locul opțiunii A/B/C pe care o justificase chiar el. Rezultatul `resp_5ea01537-b269-42f9-a7e9-f0e73b7fd842` a fost **RESPINS** integral ca verificare independentă a răspunsurilor, nu tratat ca un al doilea vot. V284 conține matricea exactă literă originală ↔ text ↔ sursă și cele șapte rezultate fals-pozitive. Modelul de cercetare electrotehnică `resp_3d8d8881-bb9d-45db-8a08-7a93332812b9` a confirmat mai multe distincții, dar nici el nu reprezintă un inginer evaluator certificat.

## Surse redeschise / limite

- I7/2011 completat la 22.09.2023, utilizator, SHA256 **`4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`**, inclusiv §5.3.4.3.1.2, §5.5.2.3, §5.4.13 și celelalte articole specifice
- [Legea energiei electrice 123/2012, formă pe Portal Legislativ](https://legislatie.just.ro/Public/DetaliiDocument/294442) art.57/92/93
- [Regulamentul autorizării electricienilor aprobat prin Ordin ANRE 66/2023](https://legislatie.just.ro/Public/DetaliiDocument/288046), art.37 e/h/i
- [Regulamentul racordării aprobat prin Ordin ANRE 59/2013, formă consolidată](https://legislatie.just.ro/Public/DetaliiDocument/310640), art.5/11 și anexa 3 pct **2.3**, nu pct 2.1
- [IP71/2015 document tehnic, copie publică](https://stoianconstantin.wordpress.com/wp-content/uploads/2024/11/1.e-ip-71-2015-statii-de-conexiuni-si-de-transformare.pdf) §5.2.4.3–3.1, investiție prin reducerea numărului de celule de cuplă, cu dezavantaje de complexitate/fiabilitate
- Bibliografia examenului este în prezent afișată pe site-ul [ANRE, Energie electrică](https://anre.ro/participanti-la-piata-de-energie/persoane-fizice/energie-electrica/) cu titlu 2023; ediția aplicabilă fiecărei situații concrete de examinare în 2026 încă necesită autentificare. Nu s-au găsit chei oficiale punctuale pentru cele 23 QABC în materialele accesate.
- Pentru PE155, PE102, IP71 unele PDF-uri de la terți nu au fost certificate vizual cu pagini oficiale. Citatele cercetate sunt provizorii.

## GFR „Punctul 1”: ce este și ce nu este închis

**ÎNCHEIAT:** tratarea/revizuirea tehnică preliminară, individualizată, a **27/27 trasee P0**, cu 23 dosare QABC, 138 verificări opțiuni/perechi și 23 teste negative documentate. Nu mai există caz P0 fără o propunere bazată pe sursă **sau fără o cauză precisă de blocaj**.

**NU ECHIVALEAZĂ cu încheierea validării finale a punctului 1:** 8 QABC rămân cu probleme semantice sau de sursă, toate 27 necesită verificarea independentei de specialitate și autentificarea baremului pentru a fi declarate acceptate. Vocabular de status corect: `P0_SOURCE_RESEARCH_DOSSIER_COMPLETE_NOT_APPROVED`, nu `P0_FINAL_KEYS_VALIDATED`.

**Status rămas:** 136/136 diagnostic semantic identificat, 136 grupuri încă release-blocate; **0/822** trasee certificate pentru învățare. Nicio modificare la Excel original, A/B/C sau baremele canonice, HTML, APK, main; PR #7 rămâne Draft, fără merge/release.

**Următor pas:** obținerea dovezilor necesare pentru cele 8 cauze exacte, recenzori independenți calificați pentru 27/27, validarea ediției/baremului și apoi aplicarea explicit aprobată. Dacă aprobarea externă nu este disponibilă, nu pretindem trecerea acestei porți și nu amânăm automat restul QA documentar.
