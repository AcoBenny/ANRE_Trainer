# QA independent al pregătirii execuției aprofundate

Data: 2026-11-11. Reviewer: subagent `qa_independent`, distinct de autorul pregătirii. Acesta este controlul pregătirii și al structurii, **nu un nou audit al răspunsurilor**. Nicio întrebare sau explicație nu primește aprobare pentru învățare prin aceste verificări.

## Verificări executate

| Control | Rezultat observat |
|---|---|
| Rutare canonică | 822 rânduri, fiecare ID exact o dată; fără lipsuri sau dublări |
| Grupare exactă Q+A+B+C | 568 unități distincte, fără normalizare; toate ID-urile din fiecare grup au exact același text și ordine ABC |
| Duplicate și conflicte | 254 grupuri cu mai multe ID-uri; 2 grupuri au chei contradictorii |
| Loturi | 30, maximum20 unități per lot |
| Prioritate P0 | DEEP-ELE-01, DEEP-NOR-01, DEEP-LEG-01 și DEEP-ELE-02 acoperă toate72 ID-uri P0 |
| Decizii pregătite | Toate unitățile NOT_ADJUDICATED, toate ID-urile NOT_ADJUDICATED și approved_for_learning=NO |
| Export efectiv | Comanda batch executată cu succes pentru toate30 loturile; 568 unități exportate,568 unit_id distincte |
| Explicații existente | Ultimul exporter include Explicatie exactă per ID, egală cu datele canonice |
| Rezultate goale | validate respinge results=[] cu exit2/Batch coverage mismatch |
| Director final gol | final-check respinge folderul fără loturi cu exit2/All30batches required exactly once |

Exporturile și probele JSON au fost păstrate numai în memorie sau director temporar în afara repository-ului, șters automat după probe. Nu s-au introdus rezultate sintetice în registrele de audit.

## Gate de corectat înainte de închideri structurale

Un test sintetic a furnizat pentru unitatea exactQABC G1-ELE-018/G2-ELEC-170 `VERIFIED_AS_STORED`, `single_answer_demonstrated=true` și cheile originale diferite A/C. Toate câmpurile structurale erau completate cu valori marcate explicit sintetice; celelalte19 unități ale lotului aveau status BLOCKED_SOURCE. Validatorul a returnat exit0 și structure=PASS. Acesta este un contraexemplu de consistență structurală, nu dovadă de adevăr și nici rezultat real de audit.

Recomandare: o unitate cu `key_conflict=YES` să nu poată primi `VERIFIED_AS_STORED` fără reconciliere explicită. Să rămână BLOCKED sau să ceară CORRECTION_READY_REVIEWED și propunere coerentă per membru. Dacă se admit chei diferite pe exactQABC din cauze reale de ediție/aplicabilitate, justificarea separată și review-ul ei trebuie consemnate explicit, nu deduse dintr-un simplu grade_applicability nevid. Nicio cheie canonică nu se schimbă automat.

Hash cod la proba de mai sus: `bbb24942760c6201152ac5e01f06985cfdb7e83f1d19335896c00d7e5a6ed137`.

## Inspecția gate-urilor de conținut

Validatorul cere pentru închidere sursă, locator, ediție, tip de sursă admis, acces propriu al autorului și reviewerului, aplicabilitate la examen, raționamentABC, unicitate, constatări lingvistice, adjudecare tehnică și referință la dovezile reviewerului. Fiecare membru păstrează cheia originală, are propunere și domeniu, evaluarea explicației existente; corecțiile cer înainte/după și explicația propusă. Autorizarea schimbării cheii și aprobarea învățării rămân NO. Cazurile BLOCKED cer motiv și pas următor și împiedică final-check.

Acestea sunt gate-uri structurale utile, dar booleenii și șirurile de caractere nu autentifică sursele, independența persoanei sau adevărul fizic/juridic. README și scriptul păstrează explicit această limită; nu afirmă că exportul celor30 loturi reprezintă auditarea lor.

## Distincția figurii existente

Registrul surselor a fost citit în versiunea actualizată: pentru ELE028/ELEC177 **există PDF-ul istoric** și pagina10/rând28 inspectată în V88/V89. Lipsește asocierea figurii în datele aplicației; nu se cere încă o dată PDF-ul utilizatorului și nu se blochează cercetarea ca și cum materialul ar lipsi. Proveniența/ediția și o eventuală integrare autorizată rămân aspecte separate.

## Verdict

Rutare/export/negative checks: PASS. Remedierea gate-ului de consistență a fost executată de autor și verificată separat, conform addendumului. Nicio modificare făcută de reviewer în cod, registre sau aplicație; fără commit/merge. Zero răspunsuri noi auditate și zero aprobări pentru învățare în această pregătire.

## Addendum: remediere și reexecutare independentă

Autorul a modificat codul, reviewerul nu. Același contraexemplu sintetic A/C pe unitatea conflictuală a fost reexecutat: VERIFIED_AS_STORED este acum respins cu exit2. A doua probă, CORRECTION_READY_REVIEWED păstrând propuneri A/C diferite pe exactQABC, este tot respinsă cu exit2. Astfel conflictul original nu poate fi închis ca intact, iar o unitate închisă cere o singură cheie propusă pentru toți membrii. Diferențele de aplicabilitate trebuie investigate și separate explicit înainte de închidere. Nu există promovare automată a unei litere sau modificare a datelor canonice.

Hash cod recontrolat: `ef23157b75f0102b5fac836a2c72ec01866684349809b8b3e1a6c4c08f225fdd`. Verdict final al pregătirii: PASS în domeniul structural testat. Adevărul răspunsurilor rămâne pentru execuția aprofundată;0 răspunsuri auditate prin acest control.
