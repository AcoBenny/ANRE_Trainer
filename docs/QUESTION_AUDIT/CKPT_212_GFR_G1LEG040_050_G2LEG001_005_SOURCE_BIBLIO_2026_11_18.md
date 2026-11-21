# CKPT-212 | GFR ANRE legislation 15 QABC: G1-LEG-040..050 + G2-LEG-001..005 | 2026-11-18

## Reproducibility and safety
- Source canonical V73 Git blob `c027d417a8e4e605c830b2016fb55b099b8d130b`; 15 previously unreviewed P1 source bank cards; original QABC and keys mechanically copied from 822-row register. Existing IDs not new additions. Preceding G1-LEG-025 was deliberately skipped because already CKPT-203 user decision despite V100 not showing the historic checkpoint.
- Current primary texts reopened 2026-11-18: [law](https://legislatie.just.ro/Public/DetaliiDocument/311821), [Ordin66 regulation](https://legislatie.just.ro/Public/DetaliiDocumentAfis/288046), [Ordin5 supply regulation](https://legislatie.just.ro/Public/DetaliiDocument/280249), [Ordin59 connection](https://legislatie.just.ro/Public/DetaliiDocument/310640). Official ANRE [2023 exam bibliography PDF](https://anre.ro/wp-content/uploads/2023/05/Tematica-si-bibliografie-pentru-examenul-de-autorizare-electricieni-2023-.pdf) pages 1 and 2 viewed **visually** using the PDF page screenshot, table cells Grade II verified.
- The PDF is explicitly version **May 2023**, hosted on ANRE's current pages. This is evidence of that official bibliography edition, **not proof a newer 2026 examination syllabus/version does not exist**. Original G2-LEG question cards in V73 have a distinct source-file provenance; bibliographic match does not make them official examination wording.
- No application work, canonical QABC/key edits, independent-agent claims, or learner approvals.

### G1-LEG-040 | CONDITIONAL_MISSING_CUMULATIVE_CONDITIONS
- Original question: În calitate de persoană fizică autorizată, electricianul autorizat gradul I poate executa instalaţii electrice interioare
- A: având o putere electrică instalată de maximum 10 kW şi la o tensiune nominală mai mică de 1 kV, numai dacă deţine un atestat emis de ANRE
- B: având o putere electrică instalată de maximum 20 kW şi la o tensiune nominală mai mică de 1 kV, numai dacîă deţine un atestat emis de ANRE
- C: având o putere electrică instalată de maximum 10 kW şi la o tensiune nominală mai mică de 1 kV, fără a deţine un atestat emis de ANRE
- Imported answer **C** untouched. Provenance: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` row `47`.
- Source: Ordin ANRE 66/2023 art. 9 lit. a și art. 35 secț. A lit. a, inclusiv condițiile (i)-(iii).
- Analysis A/B/C: A/B condiționează fals de atestatul operatorului; B greșește și pragul de putere 20 kW; C corespunde pragului 10 kW, sub 1 kV și derogării de la atestat, însă formularea nu include condițiile cumulative ale art.35A(a), inclusiv asociere și alte verificări. O formulare simplă nu autorizează orice titular Grad I să lucreze singur ca PFA.
- Status: `CONDITIONAL_MISSING_CUMULATIVE_CONDITIONS`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G1-LEG-041 | DIRECT_MATCH
- Original question: La încetarea perioadei de valabilitate a contractului de furnizare a energiei electrice, clientul final de energie electrică are dreptul să primească de la furnizor decontul final de regularizare
- A: În termen de maximum 42 de zile de la încetarea contractului de furnizare a energiei electrice
- B: la  încetarea contractului de furnizare a energiei electrice
- C: În termen de maximum 10 de zile de la încetarea contractului de furnizare a energiei electrice
- Imported answer **A** untouched. Provenance: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` row `48`.
- Source: Ordin ANRE 5/2023 regulament furnizare art. 19(1).
- Analysis A/B/C: A 42 zile de la încetarea contractului corespunde exact termenului maxim pentru transmiterea facturii cu decontul final; B scadența instantanee nu este impusă; C 10 zile apar în alte etape/obligații, nu la art19(1).
- Status: `DIRECT_MATCH`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G1-LEG-042 | SOURCE_SCOPE_MISMATCH_BLOCKED
- Original question: Furnizarea energiei electrice se desfăşoară
- A: numai în baza unei licenţe pentru activitatea de furnizare a energiei electrice
- B: fără licență, de către operatori de distribuție neconcesionari către clienţii alimentaţi direct din reţelele electrice pe care aceştia le exploatează
- C: fără licență, de către producători, oricărui client final
- Imported answer **B** untouched. Provenance: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` row `49`.
- Source: Legea 123/2012 art. 10 alin. (2) lit. d/f, alin. (4^2); art.52; dispozițiile de excepție privind distribuția neconcesionară.
- Analysis A/B/C: A este prea absolut dacă se pot acorda drepturi complementare prin licență sau alte excepții; B afirmă FURNIZARE fără licență de către distribuitor neconcesionar, însă art.10(4^2) scutește DISTRIBUȚIA, nu dovedește automat drept de FURNIZARE fără licență. C conține 'oricărui client final', excesiv. B păstrat ca barem importat, dar nu certificat, trebuie act juridic direct care autorizează această activitate distinctă.
- Status: `SOURCE_SCOPE_MISMATCH_BLOCKED`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G1-LEG-043 | CONDITIONAL_WORKING_DAY_UNIT
- Original question: În cazul furnizării energiei electrice în baza unui contract încheiat pe piaţa concurenţială, întreruperea alimentării cu energie electrică pentru nerespectarea obligaţiilor contractuale de către beneficiar se face în cazul clienților noncasnici:
- A: cu un preaviz de minim 5 zile
- B: cu un preaviz de cel puţin10 zile
- C: fără preaviz
- Imported answer **A** untouched. Provenance: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` row `50`.
- Source: Ordin ANRE 5/2023 Regulamentul furnizare art.26 alin.(4)(b), context neplată în contract concurențial.
- Analysis A/B/C: A este valoarea intenționată 5, dar textul oficial cere minimum 5 **zile lucrătoare** pentru client noncasnic în caz de neplată; opțiunea A spune doar '5 zile', fără calificativ, iar întrebarea spune generic 'nerespectarea obligațiilor contractuale' și nu doar neplată. B 10 nu este pragul legal, C fără preaviz nu corespunde acestui caz; comparația nu permite certificarea textuală necondiționată.
- Status: `CONDITIONAL_WORKING_DAY_UNIT`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G1-LEG-044 | DIRECT_MATCH
- Original question: Furnizarea energiei electrice către clientul final se realizează:
- A: fără încheierea contractului de furnizare, pe bază de negocieri
- B: fără încheierea contractului de furnizare, pentru clienții casnici
- C: fără încheierea contractului de furnizare în situaţiile reglementate în mod distinct de către autoritatea competentă.
- Imported answer **C** untouched. Provenance: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` row `51`.
- Source: Legea 123/2012 art.52 alin.(4), art.53 alin.(4).
- Analysis A/B/C: C este excepția permisă de reglementări ANRE de la semnarea unui contract; A nu permite negocierea fără contract în general; B 'fără contract pentru toți casnicii' este fals. Art53(4) exemplifică furnizorul de ultimă instanță fără semnarea prealabilă în condițiile sale.
- Status: `DIRECT_MATCH`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G1-LEG-045 | DIRECT_MATCH_WITH_DOMESTIC_USE
- Original question: Căminele studenţeşti se încadrează în categoria :
- A: clienţilor noncasnici
- B: clienţilor casnici
- C: clienţilor casnici, dar numai dacă au o putere aprobată sub 50 kW
- Imported answer **B** untouched. Provenance: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` row `52`.
- Source: Ordin ANRE 5/2023, regulament art.8 lit.a.
- Analysis A/B/C: A clasifică nejustificat orice cămin ca noncasnic; B este categoria normată pentru cămine studențești în scop de consum casnic; C inventează un prag general sub 50 kW.
- Status: `DIRECT_MATCH_WITH_DOMESTIC_USE`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G1-LEG-046 | DIRECT_MATCH
- Original question: Întreprinderile mici se încadrează în categoria
- A: clienţilor noncasnici
- B: clienților casnici
- C: clienţilor noncasnici, dar numai dacă au o putere aprobată mai mare de 20 kW
- Imported answer **A** untouched. Provenance: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` row `53`.
- Source: Ordin ANRE 5/2023 regulament art.8 lit.b; Legea123 art3 client noncasnic.
- Analysis A/B/C: A întreprinderile mici sunt noncasnice; B greșit casnice; C presupune un prag 20 kW care nu definește categoria.
- Status: `DIRECT_MATCH`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G1-LEG-047 | DIRECT_MATCH
- Original question: Avizul tehnic de racordare constituie:
- A: angajamentul operatorului de reţea de a realiza instalaţia de racordare a utilizatorului;
- B: oferta operatorului de reţea la cererea de racordare a solicitantului;
- C: acceptul operatorului de reţea pentru utilizarea reţelei în anumite condiţii
- Imported answer **B** untouched. Provenance: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` row `54`.
- Source: Ordin ANRE 59/2013 art.24 privind ATR.
- Analysis A/B/C: A confundă oferta de racordare cu obligația fermă de realizare (ulterior contract); B este definiția explicită ATR ca ofertă a operatorului la cerere; C simplifică avizul la autorizare de utilizare, omite conținutul tehnico-economic.
- Status: `DIRECT_MATCH`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G1-LEG-049 | DIRECT_MATCH
- Original question: În cazul unui refuz de constituire a garanţiilor conform Regulamentului de furnizare a energiei electrice la clienţii finali  şi a procedurilor specifice
- A: furnizorul are dreptul să solicite operatorului de distribuţie deconectarea clientului final de la reţea
- B: clientul final poate fi deconectat numai după o decizie a ANRE pentru cazul respectiv
- C: se reziliază contractul de furnizare a energiei electrice
- Imported answer **A** untouched. Provenance: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` row `56`.
- Source: Legea123/2012 art.58(5)-(6); Regulament ANRE5/2023 art26(2)(b).
- Analysis A/B/C: A distinge dreptul furnizorului de a solicita deconectarea de executarea de către operator; B nu cere în general decizie ANRE individuală pentru neconstituirea garanțiilor; C rezilierea automată a contractului nu este efectul art58(6).
- Status: `DIRECT_MATCH`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G1-LEG-050 | DIRECT_MATCH_WITH_AGREEMENT_SCOPE
- Original question: Clientul vulnerabil
- A: nu are dreptul să beneficieze de eşalonarea la plată a facturii
- B: are dreptul să beneficieze de eşalonarea la plată a facturii, la cerere, pe o perioadă de minimum 3 luni
- C: are dreptul să beneficieze de eşalonarea la plată a facturii, la cerere, pe o perioadă de maximum 3 luni
- Imported answer **B** untouched. Provenance: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` row `57`.
- Source: Ordin ANRE5/2023 Regulament furnizare art.7 alin.(1) lit.d.
- Analysis A/B/C: A neagă dreptul vulnerabilului, contrazice art.7; B minimum 3 luni la cerere, sau perioadă convenită între părți, corespunde reglementării; C maximum 3 luni inversează limita. Convenția contractuală poate ajusta durata.
- Status: `DIRECT_MATCH_WITH_AGREEMENT_SCOPE`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G2-LEG-001 | OFFICIAL_BIBLIOGRAPHY_EXACT
- Original question: Care este legea indicată în bibliografia ANRE pentru Gradul II privind energia electrică și gazele naturale?
- A: Legea nr. 123/2012
- B: Legea nr. 50/1991
- C: Legea nr. 10/1995
- Imported answer **A** untouched. Provenance: `Tematica și bibliografia ANRE pentru examenul de autorizare electricieni 2023` row `18`.
- Source: ANRE Bibliografie oficială 05.2023, PDF p.1 (zero-index0), poziția 2, coloana Grad II='DA'.
- Analysis A/B/C: A Legea123/2012 exact actul; B Legea50/1991 și C Legea10/1995 nu corespund obiectului sau poziției din bibliografie. PDF ANRE p.1 verificat și vizual.
- Status: `OFFICIAL_BIBLIOGRAPHY_EXACT`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G2-LEG-002 | OFFICIAL_BIBLIOGRAPHY_EXACT
- Original question: Prin ce ordin ANRE este indicat în bibliografia Gradului II Regulamentul de furnizare a energiei electrice la clienții finali?
- A: Ordinul ANRE nr. 5/2023
- B: Ordinul ANRE nr. 66/2023
- C: Ordinul ANRE nr. 128/2008
- Imported answer **A** untouched. Provenance: `Tematica și bibliografia ANRE pentru examenul de autorizare electricieni 2023` row `26`.
- Source: ANRE Bibliografie oficială 05.2023, PDF p.1, poziția 3, Grad II='DA'.
- Analysis A/B/C: A Ordinul ANRE5/2023 aproba regulamentul furnizare; B 66/2023 reglementează autorizarea electricienilor; C 128/2008 cod distribuție. PDF ANRE p.1 verificat și vizual.
- Status: `OFFICIAL_BIBLIOGRAPHY_EXACT`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G2-LEG-003 | OFFICIAL_BIBLIOGRAPHY_EXACT
- Original question: Ce ordin ANRE este indicat în bibliografia Gradului II pentru Regulamentul privind racordarea utilizatorilor la rețelele electrice de interes public?
- A: Ordinul nr. 59/2013
- B: Ordinul nr. 46/2021
- C: Ordinul nr. 134/2021
- Imported answer **A** untouched. Provenance: `Tematica și bibliografia ANRE pentru examenul de autorizare electricieni 2023` row `34`.
- Source: ANRE Bibliografie oficială 05.2023, PDF p.1, poziția 4, Grad II='DA'.
- Analysis A/B/C: A Ordinul59/2013 aprobă regulamentul racordării; B 46/2021 standard de distribuție; C 134/2021 atestare operatori. PDF ANRE p.1 verificat și vizual.
- Status: `OFFICIAL_BIBLIOGRAPHY_EXACT`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G2-LEG-004 | OFFICIAL_BIBLIOGRAPHY_EXACT
- Original question: Prin ce ordin este aprobat documentul indicat în bibliografie ca „Codul tehnic al rețelelor electrice de distribuție”?
- A: Ordinul ANRE nr. 128/2008
- B: Ordinul ANRE nr. 102/2015
- C: Ordinul ANRE nr. 20/2004
- Imported answer **A** untouched. Provenance: `Tematica și bibliografia ANRE pentru examenul de autorizare electricieni 2023` row `64`.
- Source: ANRE Bibliografie oficială 05.2023, PDF p.2 (zero-index1), poziția 7, Grad II='DA'.
- Analysis A/B/C: A Ordinul128/2008 cod tehnic de distribuție; B Ordinul102/2015 soluții racordare; C Ordinul20/2004 cod de transport (NU pentru Grad II), nu distribuție. PDF ANRE p.2 verificat vizual.
- Status: `OFFICIAL_BIBLIOGRAPHY_EXACT`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

### G2-LEG-005 | OFFICIAL_BIBLIOGRAPHY_EXACT
- Original question: Ce ordin ANRE este indicat pentru Standardul de performanță pentru serviciul de distribuție a energiei electrice?
- A: Ordinul nr. 46/2021
- B: Ordinul nr. 12/2016
- C: Ordinul nr. 103/2015
- Imported answer **A** untouched. Provenance: `Tematica și bibliografia ANRE pentru examenul de autorizare electricieni 2023` row `72`.
- Source: ANRE Bibliografie oficială 05.2023, PDF p.2, poziția 8, Grad II='DA'.
- Analysis A/B/C: A Ordinul46/2021 standard performanță serviciu distribuție; B Ordinul12/2016 privește transportul (NU Grad II); C Ordinul103/2015 cod măsurare (NU Grad II). PDF ANRE p.2 verificat vizual.
- Status: `OFFICIAL_BIBLIOGRAPHY_EXACT`; independent source/technical/linguistic reviewer `NOT_RUN`, `approved_for_learning=NO`.

## Status and handoff
- 15 existing exact grade IDs, 15 case assessments. Source-compatible intended answers 12/15 (including 5 bibliographic matches on ANRE official PDF), **3 conditional or unresolved: G1-LEG-040, G1-LEG-042, G1-LEG-043**. 0 changed keys, 0 final-approved answers.
- P0 correction priority G1-LEG-042: distinguish *distribution without distribution-license* versus *supply without supply-license*. A related rule is insufficient to justify imported B. Require separate exact legal supply exemption and edition.
- Maintain PR #7 Draft and no release. Next process G2-LEG-006..009, 100-series bibliography cards with same ANRE PDF, checking exact grade applicability and document number; no more app QA.
