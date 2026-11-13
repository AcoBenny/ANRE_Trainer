# ANRE Trainer | Free web source research | 2026-11-11

## Decizie
**Perplexity DEFERRED/NOT COST-EFFECTIVE** după testele limitate în planul gratuit relatate de utilizator. Fără a şterge proiectul de test CKPT020-021, continuarea executată foloseşte căutări web gratuite, Portal Legislativ, surse de inginerie şi registrul existent. **Perplexity NOT_RUN in aceasta sesiune**; niciun scor comparativ sau avantaje de timp inventate.

## Ce s-a executat
- CKPT-021 (anterior): 5 din cele 20 unităţi QABC ale pilotului, web-only.
- CKPT-022 (acest pas): celelalte **15/15 unităţi QABC** (rundele 2, 3, 4), aceleaşi 15 ID-uri P0 extrase din `INPUT_20_P0.csv`. Detalii A/B/C, referinţe exacte, acces, blocaje şi candidaţi în `ROUND2_WEB_EVIDENCE_5.csv`, `ROUND3_WEB_EVIDENCE_5.csv`, `ROUND4_WEB_EVIDENCE_5.csv`. Total pilot web analizat preliminar **20/20 unităţi**, NOT 20 aprobări.
- Verificare automată efectivă după GitHub reopen: **15 rânduri,15 ID-uri distincte,15 unităţi distincte, exact grade/unit/batch/barem/riscuri identice cu V73, ID_ROUTING_822 şi INPUT_20_P0; A/B/C + surse+blocaj completat; 0 nepotriviri, PASS**. QA este structural, nu revizie tehnică independentă.
- Nu au fost rulaţi alţi agenţi independenţi, nu există semnătură specialist uman, nu au fost modificate variante/chei HTML/APK şi nu s-a făcut release sau merge.

## Constatări prioritare, fără aprobare de barem
1. **Legal, 2026:** Portalul Legislativ `https://legislatie.just.ro/Public/DetaliiDocument/300063` a fost deschis direct şi afişează ultima consolidare **26.07.2026**. `G1-LEG-019` Legea 123 art93(1) pct3 susţine **B / contravenţie**, stocat C. `G1-LEG-026` art92(2) susţine **B / infracţiune**, stocat C. Sunt dovezi specifice mai bune decât indexul istoric, dar review juridic separat/condiţii examen încă nu sunt confirmate.
2. **Legislaţie art37:** `G1-LEG-034` A proiect respectat, B recepţie doar *dacă i se solicită* (contrazice originalul). `G1-LEG-032` regula vizării la5 ani nu transformă vechimea4 ani în contravenţie; A e condiţional la tipizarea legală. `G1-LEG-017` Reg furnizare ANRE5/2023 art18(3)(a) susţine A furt constatat judiciar, legea123 art58(6) indică doar deconectare pentru refuz garanţie, nu reziliere automată; regulamentele actualizate ale furnizării nu au fost redeschise direct (HTTP502).
3. **I7/PE155:**
   - `G1-NOR-027` I7 §5.3.4.3.1.2 confirmă conductorul de fază la **contactul central al soclului**; traducerea în „şuruburile de contact” A necesită desen al soclului, B stocat este suspect.
   - `G1-NOR-029` I7 §5.3.3.21 2,3m general / **2,5m** excepţie locuinţe; C intended, dar A/B/C pot fi literal sub limita maximă, de aceea ambiguu.
   - `G1-NOR-032` PE155/92 §3.2.10 **15 m pentru coloanele orizontale**; B stocat este susţinut specific, iar norma generică I7 invocată în V33 nu poate substitui PE155.
   - `G1-NOR-089` I7 §5.1.4.3.3 permite o singură culoare cu marcaj la ambele capete (**B**); cheia păstrată A conflict.
   - `G2-NOR-137` I7-2011 este **indicativ**, nu *act de aprobare*; acesta este Ordin 2741/2011. Niciuna dintre A/B/C nu numeşte actul, deci chestionarul necesită rescriere ori excludere, nu schimbare forţată de literă.
4. **Electrotehnică:** ABB §3.14.1.3-.4 distinge transfer bar/bypass de schema double bus obişnuită, aşa că `G1-ELE-125` şi `G2-ELEC-266` rămân condiţionate de topologie. Manualul ABB ZX1.2 §4.1 şi IET2026 susţin regula separatoarelor fără sarcină pentru `G1-ELE-137/138`; ordinea precisă mai cere schema şi procedura locală. IIT Madras §3 confirmă gamma=alpha+jbeta, unitate m^-1, pentru `G2-ELEC-290` enunţul „adimensională” este eronat.
  
## Acces şi QA corect documentate
- HTML Portal Legislative Legea123 şi Reg66: accesat direct în această sesiune. I7 text Portal oficial doar prin index (open502), dar o copie PDF declarată din Portal a fost deschisă **ca text PDF**; **screenshot PDF = cache miss**. PE155 copie textuală PDF de pe baluna.ro deschisă, screenshot PDF cache miss. ABB PDF text deschis, screenshot cache miss. NU se pretinde verificare vizuală când lipseste.
- Sursele NON-ANRE nu certifică automat ediţia de examen, obiectul exact şi gradul; regulile avengers source-scope au fost aplicate descriptiv, nu ca review independent.
- 20/20 pilot web research != 822/822 validated. Starea inventarului: **7/30 loturi cercetate preliminar, 140/568 unităţi, 186/822 ID-uri, 0/822 aprobări pentru învăţare**. Întrebările pilot sunt subseturi deja cercetate (fără dublă numărare).

## Următorul handoff
1. QA cu reviewer distinct şi surse redeschise pentru corecţiile juridice/normative cele mai solide (G1-LEG-019/026/034, G1-NOR-089, G1-NOR-032); păstrare NO_APPROVAL până la închidere verificabilă.
2. Întrebări de topologie G1-ELE-125/G2-ELEC-266 şi terminologie G1-NOR-027/G2-ELEC-290 către expert domeniu.
3. Continuitate pe 23 loturi încă fără cercetare aprofundată pre-QA, cu economisire de muncă la duplicate.

**Rămâne interzis:** schimbarea baremelor, QABC, HTML/APK, merge main/release fără aprobare. Nu există worker async.
