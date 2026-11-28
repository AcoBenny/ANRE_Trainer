# V84 | ANRE Trainer | Source QA evidence update 2026-11-11 (not release approval)
## Proveniență, scope și integritate
- Baseline V73: **822/822** enunțuri + A/B/C + cheie + sursă/rând + proveniența fișei de audit; **274 audituri individuale preliminare**, 548 reconcilieri de note anterioare, nu validări independent confirmate.
- V76: scanare deterministă cu parser CSV quote-aware a celor 822 rânduri. 414 Grad I, 408 Grad II; 595 electrotehnică, 112 legislație, 115 norme. 822 ID unice, 0 câmpuri esențiale lipsă, 0 mismatch între barem și textul variantei A/B/C stocate. 254 grupuri duplicate Q+ABC, dintre care **2 perechi cu chei contradictorii**; 18 familii același enunț, alte variante, unele capcane.
- V77: 18 cazuri riscante trecute prin verificare tematică a formulelor/actelor și discriminatori lingvistici, cu sursă sau gap explicit. V80: 4 pe cele două perechi de chei contradictorii. V81: 10 ordine de manevre și cuple transversale confruntate cu NTE 009/10/00 art29/34/38. V82: 9 cazuri electrotehnice cu surse de principiu/fabricant.
- **41/822 întrebări unice** cu fișă de recontrol focalizat în acest lot V77–V82, dintre care **34/72 P0**. Sunt **38 P0** în V78 fără acest nou nivel focalizat (au totuși triaj și uneori audit mai vechi); nu le declara lipsă integrală de dovezi.
- **P0 72, P1 228, P2 522** după ridicarea G1-NOR-042 (inițial P1) în V78. Cele 41 fișe noi sunt **SCREENING PRELIMINAR CU SURSE**, nu signoff pentru învățare.

## Semnale cu impact mare
1. Opt candidați de corectat un barem, **fără editare:** G1-LEG-015 A, -019 B, -020 B, -026 B, -048 B, G1-NOR-029 C, -042 A, -089 B. Necesită verificarea versiunii de reglementare și review independent per întrebare.
2. Patru întrebări fără variantă corectă conform interpretării literale și fragmentelor disponibile: G1-NOR-032 și G2-NOR-137/141/145.
3. Perechea Cs=3C G1-ELE-018 A / G2-ELEC-170 C: sursă didactică University of Victoria Tatum §5.7, transformare delta/stea, 3C pentru C12=C23=C31=C. **A preliminar** pentru ambele; definiția exactă „capacitate de serviciu” și expertul independent lipsesc. Cele 2 chei au fost păstrate.
4. Perechea G1-ELE-102 A / G2-ELEC-245 C: „de preferat în regim normal” în stație cu bare duble depinde de schemă și condiții operative. NTE 009 definește cupla în rezervă caldă, nu recomandă universal o singură opțiune; conflictul se păstrează.
5. NTE 009/10/00 art29(2-4): susține succesiunea tipică de conectare `separator bare → separator linie → întreruptor`, deconectare inversă. Cazurile G1-ELE-129/137, G2-ELEC-269 și G1-ELE-131/138, G2-ELEC-271 corespund cheilor lor **în condițiile procedurii normale**; alin4 admite excepții de siguranță. Nu sunt QA independent aprobate.
6. I7 G1-NOR-042: Art5.2.4.6.1(a) neutralul în monofazat cu două conductoare are aceeași secțiune indiferent de mărime (A); cheia stocată B citează condiții și praguri incongruente cu alineatul. **Nou P0 de adjudecare**, nu corecție automată.
7. G2-ELEC-247: manual ABB/Brown Boveri SBS cu ulei, §4 p.11 (pagina 9 în captura PDF web) arată stingerea arcului de ulei, contrazicând „doar izolație” din A; B candidat condiționat de echipament.
8. G2-ELEC-268 (90° doar L ideal), -358 (susceptanță inversa reactanței doar în element pur), -381 (PF 1 la rezonanță chiar cu L și C), -392 (E vs D), -316 (multiple metode de reducere eddy loss), -365 (siguranța întrerupe după depășire, nu previne orice supracurent), plus G1-ELE-043/G2-ELEC-189 (curent generator fără condiții).

## Auditul realist al surselor în V73
- Câmpul `legacy_source_article_or_page`: **586/822 gol**, **183/822 text exact `NOT_VERIFIED`**, **6/822 indică explicit `NOT_LOCATED` ori `NO_EXACT`**, **47/822 indicii istorice de pagini/articole, dar NU certificate 2026**. Sumă 822.
- În V77+V80+V81+V82 au fost înregistrate **38 URL-uri** la 41 ID-uri; 3 întrebări fără actul real au doar un verdict lingvistic „no valid option”. Adăugarea URL-urilor nu validează restul de 781 de rânduri, nici nu dovedește data aplicării.
- Toți cei **227** itemi de legislație și norme (112+115) au `2026_legal_currentness_verified=NO` în baseline; nu susține actualitatea completă 2026.
- Registru unificat de gate fără modificarea baseline: `V83_822_FOCUSED_EVIDENCE_QA_GATE_MASTER_AFTER_V82.csv` (822 rânduri, 41 marcate V77–V82, toate cu QA/approval `NOT_RUN`/`NO`).

## Surse principale, înregistrate, fără redistribuire copyright
- Portalul Legislativ: Legea 123/2012 art57/92/93; Ordin 74/2014 art2; I7 articolele 5.1.4.3.3, 5.2.4.6.1, 5.2.12.3.10, 5.3.3.21.
- Ordin ANRE 25/2010 / NTE 009/10/00, Regulamentul General de Manevre art29,34,38: https://legislatie.just.ro/Public/DetaliiDocument/122751 .
- University of Victoria, Jeremy Tatum §5.7: https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electricity_and_Magnetism_%28Tatum%29/05%3A_Capacitors/5.07%3A__Delta-Star_Transform .
- OpenStax University Physics vol2 §§6.2, 13.5, 15.3, 15.4.
- Schneider Electric, Electrical Installation Guide: definiția puterii reactive și aparate de comutație.
- BBC/Brown Boveri manufacturer's instruction: https://library.e.abb.com/public/422ae06775599d40c125728700595042/Instruction_Oil_CB_SBS12_SBS24_AG90234.pdf ; recontrol vizual PDF p9 (tipărit 11). **Link, nu copie a manualului**.

## Safety / gates
- **0/822 independent QA electric**, **0/822 independent QA lingvistic**, **0/822 independent source/legal signoff**, **0/822 app-approved**. Nu e permis verdict „822 corecte”, iar aplicația nu este gata de folosit pentru examen.
- Fără modificare enunț, A/B/C, cheie, HTML, APK, `main`, fără build/release/merge. Toate fișierele noi sunt numai documentare în Draft PR #7.
- Pentru release real: 72 P0 adjudecate + 228 P1 și 522 P2, sursă didactică/normativă exactă și data ediției per rând, control de proprietate a sursei și test offline Android/HTML după aprobarea explicită a corecțiilor.
