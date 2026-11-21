# CKPT-378 | Revizie oarbă AI 23 QABC: opt diferențe și verificarea lor în surse

Data: 2026-11-21. Obiect: 23 întrebări P0, 27 trasee G1/G2.

## Rezultat

- Cercetare separată executată pe 23/23 întrebări, fără literele candidate: 15 concordanțe, 8 diferențe brute.
- Șapte diferențe au fost reconcilate prin identificarea exactă a erorii de obiect, calcul, condiție sau text normativ. O diferență, QABC-0094, rămâne nerezolvată pentru că regula nu prescrie un regim universal preferat.
- 0/822 aprobări profesionale independente pentru învățare: al doilea model AI NU este jurist/inginer acreditat și nu confirmă un barem ANRE oficial.

## Divergențe, fără rescrierea variantelor originale

| ID | Model AI orb | Candidat sursă / decizie | Cauza demonstrată |
|---|---|---|---|
| QABC-0017 | C | A | Modelul a împărțit greșit capacitățile între faze la 3; q1=C(V1−V2)+C(V1−V3)=3CV1 în sistem echilibrat, Cs=3C. |
| QABC-0094 | C | Fără alegere universală | NTE definește stările operative fără să stabilească obiectivul universal de exploatare. Ipoteza utilizatorului: A pentru siguranța exploatării. |
| QABC-0279 | NONE | A | Refuzul accesului la contoare este contravenție conform Legea 123 art.93(1) pct28; furtul de energie este infracțiune în condițiile Codului penal art.228. |
| QABC-0292 | B | C | Anexa 3 pct.2.3 Regulament ANRE 59/2013 spune parter/palier pentru ansamblu de blocuri. |
| QABC-0356 | B | A | I7 p55 §5.2.4.6.1(a) indică monofazat cu două conductoare indiferent de secțiune; B are model și praguri greșite. |
| QABC-0362 | NONE | C | A și B includ «numai», C nu; I7 p70 §5.4.13 permite trei trasee fără exclusivitate. |
| QABC-0372 | B | C | I7 p13 §3.0.3.5 are excepția IP33 și materiale rezistente, omisă de AI. |
| QABC-0380 | B | A | I7 p59 §5.2.12.1.4 interzice textual conductoarele electrice în tuburi/țevi din pământ; AI a confundat obiectul cu cabluri subterane corespunzătoare. |

## Surse primare și controale

- PDF I7 furnizat de utilizator, SHA256 `4bc3fc701cb71c937ad166462807423fa505c483783c5c93fe5b8ad03b20f431`: paginile 13, 55, 59, 70, 162 redeschise în această rundă.
- [Portalul Legislativ, Legea 123/2012](https://legislatie.just.ro/Public/DetaliiDocument/294442), art.92 și art.93.
- [Codul penal, art.228](https://lexapp.ro/legislatie/codul-penal/art-228/), energia electrică este bun mobil pentru furt.
- [Regulament ANRE 59/2013](https://legislatie.just.ro/Public/DetaliiDocument/310640), anexa 3 pct.2.2–2.3.
- [ANRE bibliografie electricieni 05.2023](https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf), în continuare publicată pe pagina examenului în noiembrie 2026. PE102 NU la Grad I, DA la Grad II; PE155 DA la ambele.
- [V290](./V290_GFR_SECOND_AI_INDEPENDENT_BLIND_23_SOURCE_RECONCILED_8_CONTRADICTIONS_2026_11_21.json) include toate cele 23 de înregistrări, patru identificatoare de cercetare AI separate, opțiunile originale și cauzele diferențelor.

## Porti pentru aprobare finală (NEÎNDEPLINITE)

- Verificare de specialist competent identificabil pentru fiecare dintre cele 23 de întrebări, separat tehnic/juridic și lingvistic.
- Ediția normativă aplicabilă examenului verificată și acoperită explicit, nu inferată din existența bibliografiei 2023.
- Autentificarea cheilor ANRE sau protocol de tratare documentată a întrebărilor fără răspuns original corect/unic.

PR #7 este Draft. Originalele Excel, baremele, HTML, APK nu au fost modificate. Nicio versiune a aplicației nu a primit aprobarea de utilizare.
