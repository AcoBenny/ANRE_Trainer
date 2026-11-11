# ANRE Trainer | sursă secundară: chestionare-anre.ro | pilot 2026-11-11

## Scop şi statut
Acest pilot adaugă **indicii externe** pentru auditul existent, nu întrebări canonice, nu bareme şi nu aprobări pentru învăţare. Sursă terţă: https://chestionare-anre.ro/ (platformă independentă; declară că întrebările sunt inspirate/adaptate din exemple ANRE, actualizări afişate 2024). Gradele I/II sunt vizibile; testele randomizează întrebările şi variantele, iar explicaţiile complete sunt uneori disponibile doar în aplicaţia comercială.

**PROVENIENŢĂ:** pagini publice şi rezultate indexate inspectate la 2026-11-11; unele deschideri directe au întors pagină anti-bot, iar alte accesări au dat un set diferit de 25. Nu există permalinks verificate pe întrebare; observaţiile din index pot reflecta un snapshot mai vechi. Comentariile utilizatorilor sunt alerte, nu autoritate. Nu s-a folosit un export complet al site-ului, nu s-au copiat întrebările sale în bancă.

## Comparaţie pilot
Registru: [PILOT_CROSSWALK.csv](PILOT_CROSSWALK.csv). **10 ID-uri din banca de 822** identificate ca posibile suprapuneri pe **6 familii tematice**, dintre care 6 ID-uri au corespondent cu aceeaşi întrebare şi opţiuni (ordonarea răspunsurilor pe site diferă); 4 sunt doar legături de enunţ/comentariu şi NU trebuie tratate ca matching complet. Cifrele sunt doar acoperire de comparare; **0 ID-uri validate tehnic/juridic sau pentru învăţare**.

Indicii prioritare:
- G1-LEG-027: site-ul indică 12 luni, consistent cu C din bancă; regulamentul din 2026, cauzele alternative şi formularea trebuie verificate independent.
- G1-LEG-039: explicaţia secundară enunţă 30 zile fără restricţie JT/MT, în timp ce varianta B din bancă menţionează MT. Păstrăm ca verificare de domeniu, nu conflict decis.
- G1-ELE-100/G2-ELEC-243: o variantă referitoare la manevrele de ocolire a întreruptorului coincide cu baremul existent, dar geometria şi interblocajele rămân nedemonstrate.
- G1-ELE-206/G2-ELEC-342: reglarea puterii reactive prin excitaţie este confirmată orientativ; lipsesc sursa primară şi review-ul separat.
- G1-ELE-124/G2-ELEC-266/G1-ELE-125: discuţii despre cupla transversală. **G2-ELEC-266 şi G1-ELE-125 sunt P0**. Comentariile site-ului nu au aceleaşi opţiuni validate şi nu rezolvă restricţiile „numai” ori schemele.
- G1-LEG-047: un comentariu din 2026 contestă definiţia ATR, dar opţiunile menţionate de comentator **diferă** de variantele noastre canonice. Doar lead legislativ.

## Reguli Avengers de integrare
1. Potrivirea se face după **enunţ + semantica tuturor opţiunilor**, nu după litere; alege `STEM_OPTIONS_REORDERED`, `STEM_FAMILY_COMMENT_ONLY` sau `SAME_STEM_DIFFERENT_OPTIONS_COMMENT`. Gradele şi duplicatele se verifică separat.
2. Site-ul este **SURSĂ SECUNDARĂ / DISCOVERY ONLY**. Nu poate închide `BLOCKED_SOURCE`, `BLOCKED_EDITION`, `BLOCKED_DIAGRAM`, `BLOCKED_AMBIGUITY` şi nu oferă `approved_for_learning`.
3. Pentru fiecare candidat deschide **norma primară** cu paragraful, obiectul, condiţiile, ediţia, gradul şi confirmă toate A/B/C + capcanele lingvistice; apoi QA distinctă cu propria redeschidere. În caz de ecran anti-bot sau explicaţie doar în aplicaţie, consemnează limitarea, nu ocoli protecţia.
4. Respectă drepturile conţinutului terţ: păstrează URL, temă, diferenţe argumentate şi metadate, nu republica în masă banca site-ului.
5. Prioritizează variantele P0 afectate şi reutilizează munca din CKPT-018; integrarea site-ului **nu** creşte artificial numărul celor 7 loturi preliminare sau acoperirea de 186 ID-uri.

## Ce NU s-a făcut
Nu s-au rulat agenţi independenţi, nu s-au aprobat răspunsuri sau grade, nu s-a validat versiunea integrală a legilor în vigoare la 11.11.2026 şi nu s-a verificat fiecare întrebare publicată pe platforma terţă. Nicio modificare la Q/A/B/C, barem, HTML, APK, `main`, release sau PR merge.
