# CKPT-052 | G1-ELE-057 / G2-ELEC-203 | Interpretarea B propusă de utilizator versus A istorică

**Data:** 2026-11-16. **Baza:** CKPT-051, `e9ccf0bc46c69ca4a8158535acca51a38288e0c0`, PR #7 Draft. **Stare:** DISPUTĂ DESCHISĂ, USER_INTERPRETATION, NU este schimbare de cheie și NU este aprobare pentru învățare. Zero fișe noi: actualizare a unității `AU-84185dba0d7b87f1` deja documentate.

## Text canonic, nealterat
Întrebare: „Două funcţii periodice sinusoidale sunt armonice între ele dacă:”
- A: „raportul perioadelor lor este un număr întreg oarecare”
- B: „au aceeaşi perioadă”
- C: „raportul perioadelor lor este egal cu 1/2”

Cheie stocată: **A** pentru G1-ELE-057 și G2-ELEC-203. Nu a fost rescrisă.

## Interpretarea formulată de utilizator

Utilizatorul susține **B** și separă:
1. Două mărimi sinusoidale cu aceeași perioadă/frecvență, de fază eventual diferită, dar cu defazaj constant. Pot fi însumate ca o sinusoidă de aceeași frecvență și reprezentate împreună fazorial.
2. O fundamentală și armonica superioară de ordin k, unde frecvențele sunt în raport întreg, dar suma undelor este în general nesinusoidală.

Acesta este un **argument valid despre sinusoide de aceeași frecvență și domeniul metodei fazoriale**, nu o dovadă independentă că expresia „armonice între ele” din enunț se definește *strict* astfel. Interpretarea utilizatorului este păstrată distinctă de surse și de verdictul istoric.

## Dovezi reanalizate independent de afirmarea utilizatorului

- **Mihai Iordache, Bazele electrotehnicii (2008), sec. 3.2–3.3:** pentru două sinusoide cu aceeași pulsație `ω`, defazajul este constant; suma lor rămâne sinusoidală de aceeași frecvență; suma a două mărimi de frecvențe diferite nu este o mărime sinusoidală în general; reprezentarea fazorială comună este definită pentru aceeași frecvență. https://ro.scribd.com/document/51004536/Mihai-Iordache-Bazele-Electrotehnicii-2008 (pasaje din cap. 3; text accesat și citit în sesiune, nu PDF-ul original vizual).
- **Culegere neoficială „Subiecte rezolvate examen autorizare ANRE electricieni 2010 – Electrotehnica”**, rândul 67, pagina PDF 4 (index pagina 3): **varianta A este colorată galben** drept răspuns propus. Pagina a fost inspectată vizual: https://tomaradu.yolasite.com/resources/30749113-Subiecte-rezolvate-examen-autorizare-ANRE-electricieni-2010-Electrotehnica.pdf . Marcat A în culegerea istorică ≠ barem ANRE 2026 certificat.
- **SIEAR/AIIR, volumul conferinței 2006, secțiunea Fourier** (text căutat, captură PDF eșuată cu cache miss): prima armonică = fundamentală, superioare n=2,3,... . https://www.siear.ro/doc/v412006.pdf . Dovada tehnică neconfirmată vizual din această sursă.
- Un alt set didactic secundar explică explicit că raportul multiplu întreg al perioadelor constituie relație armonică și marchează **A**: https://ro.scribd.com/document/460854895/02-electrotehnica-doc . Accesul la pagina respectivă a dat challenge, deci numai rezultat indexat, nu verificare de primă mână.

## Analiza critică A/B/C

- **A:** corespunde noțiunii frecvențelor armonice în raport de multipli întregi atunci când ordinea raportului este aleasă fundamentala/armonică. Dar enunțul nu precizează ordinea. Exemplu: f1=50 Hz, f2=150 Hz; T1/T2=3, dar T2/T1=1/3. Posibilă relație armonică și fără raport integral direct între două armonici de ordine 2 și 3 față de fundamentala comună.
- **B:** este necesar pentru sinusoide sincrone în *aceeași diagramă fazorială* și suficient pentru a avea sumă sinusoidală, dar **nu necesar** pentru relația fundamentală–armonică superioară. Ex. 50 și 150 Hz sunt în relație armonică deși perioadele diferă. Aceeași frecvență nu cere faze inițiale identice, ci menține defazaj constant.
- **C:** `T1/T2=1/2` poate indica raport de frecvență 2, deci descrie un caz armonic în ordinea inversă. Nu este o alternativă universal falsă. A/B/C sunt insuficient delimitate semantic.

**Concluzie provizorie:** istoricul grilei și definiția uzuală a armonicilor sprijină A drept intenție de examen; interpretarea B este corectă pentru regimul sinusoidal de aceeași frecvență. Întrebarea rămâne **NOT_APPROVED / SEMANTIC_AMBIGUITY**, nu se schimbă A în B și nu se declară eroarea utilizatorului. Unitatea nu se recontorizează.

## Lecții transferabile Avengers Asamble

1. **Nu confunda proprietatea unei operații cu definiția relației cerute:** „suma rămâne sinusoidală” ≠ „sunt armonice între ele”.
2. **Nu substitui „sincron/same-frequency” cu „armonic-related integer multiple”** fără o definiție explicită a domeniului.
3. **Sursa istorică de răspuns versus adevăr tehnic:** cheia evidențiată într-o culegere este un indiciu de intenție pedagogică, nu un barem oficial actual.
4. **Test de alternativă inversă și caz particular:** întoarce raportul T1/T2, verifică n=1 și C=1/2; dacă două variante devin adevărate în condiții explicite, păstrează ambiguitatea.
5. **Sursa de domeniu versus glosar generic:** de verificat terminologia exactă în cursul relevant pentru examen înainte de închiderea disputei.

**QA/status:** comparație manuală a textului cu CKPT-051, zero modificări de text/ABC/cheie, zero QA independent tehnic/lingvistic și zero aprobări pentru învățare. Necesită delimitare expresă „armonice între ele” și posibilă interpretare suplimentară a utilizatorului.
