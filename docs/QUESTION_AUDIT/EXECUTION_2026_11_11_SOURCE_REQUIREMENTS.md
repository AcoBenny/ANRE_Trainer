# Cerințe de surse pentru execuția aprofundată | 2026-11-11

**Plan operațional, nu audit nou.** Bază: CKPT-010/V95; referințele de mai jos descriu accesul documentat în loturile anterioare, fără o nouă verificare a accesului în această pregătire. Nu promite închiderea auditului într-o zi. Nu schimbă chei, aplicație, priorități sau aprobări.

## Intrarea auditorului și ordinea de lucru

1. Citește `CKPT_010_V99_SOURCE_RECHECK_AND_SEPARATE_AI_QA_2026_11_11_HANDOFF.md`, apoi rândurile țintă din `V95_ALL_822_MASTER_AFTER_FOCUSED_RECHECKS_AND_SEPARATE_AI_QA.csv`. Ia textul/ABC original din V73 sau sursa canonică, nu din rezumate.
2. Deschide numai lotul autorului indicat în V95 și review-ul separat V89/V93/V97/V98/V99 aferent. V83/V78 rămân istorie; un vechi NOT_RUN nu anulează review-ul separat ulterior. `SUPPORTED_WITHIN_SCOPE` nu certifică răspunsul integral.
3. Închide mai întâi sursele/terminologia lipsă și edițiile; apoi cele34 P0 cu focus anterior dar fără review AI separat. Continuă coada neaprofundată:213 P1 și518 P2. Aceste numere sunt trase din CKPT-010, nu o nouă numărătoare.

## Surse reutilizabile: acces documentat anterior

| Domeniu | Fișiere de citit țintit | Document/locator reutilizabil | Limită păstrată |
|---|---|---|---|
|Norme I7|V85,V90; V89,V97,V98|[I7 consolidat oficial](https://legislatie.just.ro/Public/FormaPrintabila/00000G01BLZ812IXGEN16BYPVD5MO6U4): 8.1.1.3.3/tabel8.1;8.1.1.3.5;5.1.7.2(a);5.5.3.5;5.3.4.3.1.2;5.2.6.6 inclusiv excepții;5.2.12.2.11–13; locatori individuali în CSV|Versiune consolidată cu [Ordin959/2023](https://legislatie.just.ro/Public/DetaliiDocument/271142), artII tranziție. Nu există certificare exhaustivă a tuturor modificărilor până în2026. NOR028 nu este interdicție fără excepții.|
|Norme/tematică|V94|[Bibliografie ANRE05.2023](https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf): fizicp2 I7, p3 item29 PE155/1992|Confirmă navigația și bibliografia istorică, nu clauzele PE155 și nici un barem.|
|Manevre electrice|V81, apoi V95 ID-uri țintă|[NTE009/10/00](https://legislatie.just.ro/Public/DetaliiDocument/122751), art29(2–4)|Include excepțiile/procedurile; schema efectivă și ediția aplicabilă rămân condiții.|
|Racordare|V86;V89|[Regulament59/2013 consolidare310640](https://legislatie.just.ro/Public/DetaliiDocumentAfis/310640), art5/art9 și anexa3 pct2.3/context2.2|LEG024/028: păstrează domeniul rețelelor publice și data bibliografiei.|
|Electricieni autorizați|V86;V89/V98|[Regulament66/2023](https://legislatie.just.ro/Public/DetaliiDocument/288046), art9,18,30,37,41,43; forma printabilă exactă înV86|LEG032 necesită lanț contravenție–sancțiune, nu deducție din simpla obligație profesională.|
|Legea123|V91,V86;V89/V98|[Forma accesată înV91](https://legislatie.just.ro/Public/FormaPrintabila/00000G0CDOUQ5TXYOEU0X4Y9QAXWNAF7): art92(1–2),93(1)pct3/28,57(2)|Nu substitui această versiune țintei exacte26.07.2026. V86/202403 este istorică19.07.2018.|
|Electrotehnică: formule|V80,V82,V87;V93/V99|Tatum§5.7 delta/stea; OpenStax11.4,16.1,15.6,7.2,15.2; Schneider reactive power/disconnector. URL/pasaj exact în CSV|Rămân definițiile românești, ipotezele, schema, regimul și convenția semnelor. O derivare nu este barem ANRE.|
|Mașini/protecții|V87,V92;V93/V99|NPTEL§4 pp14–15; DOE AppendixA pA-2/fizic36; ABB2018 p6; ANEVAR2022 p32/fizic37; manual Schneider AutoRestart. URL și hash-uri înV99|Review-ul anterior este parțial: nu dovedește exact Q=dW/dt, comparația completă curent/cuplu, selecția istorică a motoarelor ori convenția energetică PIF.|

## Ce lipsește efectiv și când poate fi depășit blocajul

| Țintă | Lipsă/dependeță reală | Criteriu de depășire |
|---|---|---|
|NOR030/031|Text primar autentic PE155/1992§3.2.1/3.2.3; pagina legislativă152201 doar îl menționează|Documentul autentic integral ori paginile cu antet/ediție/proveniență și clauzele, comparate cu fiecareABC. Nu este nevoie de încă o grilă cu răspunsuri.|
|NOR023/027/090|Pentru023 lipsește clauza cu același domeniu al aparatelor;027 necesită identificarea tehnică «șurub contact»;090 necesită condiția intenționată|Pasaj exact/același domeniu, respectiv desen/nomenclator autentic, respectiv context care separă B deC. Acces suplimentar la aceeași pagină I7 singur nu rezolvă lipsa de context.|
|LEG017/032 șiV91|[Consolidarea exactă311821](https://legislatie.just.ro/Public/DetaliiDocument/311821) și regulamentul furnizării [264611](https://legislatie.just.ro/Public/DetaliiDocumentAfis/264611) nu au fost recuperate integral; lanț sancțiuneLEG032 incomplet|Formă/data selectată vizibilă, articole relevante și modificatoare comparate; motiv de reziliere separat de deconectare; sancțiune cu temei complet. Eșecul502/timeout nu dovedește abrogare.|
|ELE088|Manual HitachiMSM revR, URL înV87, p98 nu a putut fi redeschis de reviewerV99 (404/403)|Același manual autentic sau document primar echivalent privind compartimentareaGIS; toateABC verificate, nu doar riscul de pierdere de gaz.|
|ELE028/ELEC177|Figura lipsește din datele aplicației. PDF-ul istoric existent `979902894-Captura-de-ecran-din-2024-11-09-la-14-15-06.pdf`, Library ID `libfile_2e5c4a90b8f0819181b339819291ffcd`, fizicp10/rând28, a fost inspectat vizual de autor și reviewer înV88/V89; nu trebuie cerut din nou utilizatorului|Reutilizează figura istorică existentă pentru adjudecarea tehnică și clarifică proveniența/ediția. Asocierea în aplicație și dreptul de redistribuire se verifică în implementarea autorizată; nu bloca cercetarea ca și când PDF-ul ar lipsi. Nu reconstrui schema din cheie.|
|ELE018/ELEC170;ELE102/ELEC245|Definiția exactăCs și contextul schemei cu bare; contradicții între chei identice|Definiție/schemă primară și adjudecare separată; apoi aprobare explicită înaintea oricărei schimbări de barem.|
|ELEC252/264/293/298/314/335|Sursele existente sunt prea generale/parțiale pentru convenția energetică, schemaHV, comparație motor, epocă, definițieQ, armonice rotor|Manual/standard/articol primar cu pasaj exact pentru afirmația rămasă, urmat de review separat. Nu relua tot lotulV87 pentru a completa o singură dependență.|

## Ieșirea fiecărui lot aprofundat

Înregistrează ID+hash/proveniență canonică, toateABC, URL/articol/pagină, ediție/data aplicabilă, excepții și ipoteze; leagă rândul nou de dovezile vechi fără a le număra din nou. Reviewerul distinct redeschide sursa și verifică afirmația și omisiunile. Păstrează separat `source_retrieval`, `scoped_AI_review`, `qualified_human_signoff`, `approved_for_learning`. Nici pregătirea de față, nici existența unui URL nu depășesc vreun gate. Commitul pe ramura de audit și actualizarea checkpointului sunt responsabilitatea coordonatorului; cheile/HTML/APK/merge/release rămân în afara acestui pas.
