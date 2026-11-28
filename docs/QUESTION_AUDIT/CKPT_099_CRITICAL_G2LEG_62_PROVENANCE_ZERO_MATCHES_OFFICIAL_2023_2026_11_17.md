# CKPT-099 | CRITIC: G2-LEG 62 itemi din trainer versus XLSX ANRE Grad II mai 2023 | 17.11.2026

## Dovada sursei, ce s-a verificat efectiv
- Din **Library-ul utilizatorului** au fost materializate trei copii ale workbook-ului `LEGISLATIE-GR.-2-05.2023(1).xlsx`, `(1)(1).xlsx`, `(1)(2).xlsx`; toate **24.725 bytes și același SHA256**: `725323d136481e7ad5643251e2b89a19bd57a471527cbeec847a5fe7f32f2662`. Copiile sunt identice între ele. **Nu s-a verificat hash-ul serverului ANRE**: accesul direct la https://anre.ro/wp-content/uploads/2023/05/LEGISLATIE-GR.-2-05.2023.xlsx a dat unsupported content-type în web și accesul container la internet a fost indisponibil. Prin urmare spunem «copie atribuită fișierului oficial», nu «integritate ANRE criptografic atestată».
- Workbook citit local cu `artifact_tool.SpreadsheetFile.import_xlsx`: **Sheet1 A1:D110**; rândul 6 conține enunț/variante a,b,c, iar rândurile 7–110 conțin **104 enunțuri nevidate**. Originalul este o fișă de întrebări ANRE Grad II legislație din mai 2023, NU fișier de bibliografie.
- Separat, s-a materializat `ANRE_Trainer_DOCUMENT_AUDIT_COMPLET_V2.csv` din biblioteca utilizatorului (**822 ID-uri**) și s-au selectat **62 ID-uri G2-LEG** din grupurile 001–009, 067–083, 100–135. Acest registru de audit, creat în septembrie 2026, are câmpul `Excel_ANRE` **gol pentru toate cele 62** și `Status_audit=NECONFIRMAT PUNCTUAL`. Nu este o verificare independentă, dar confirmă că proveniența nu fusese certificată anterior.
- Algoritm determinist: Unicode NFKD, litere mici, eliminarea diacriticelor, păstrarea doar a literelor/cifrelor, colapsarea spațiilor; s-a comparat fiecare text `Intrebare` G2-LEG cu **toate cele 104 enunțuri** din workbook. **0/62 potriviri textuale exacte normalizate**. Similaritate maximă SequenceMatcher sub **0,85** pentru toate 62; doar 4/62 au similaritate >0,70 cu cel mai apropiat enunț, dar **similaritatea nu înseamnă identitate**.
- **Teste pozitive de control** în același workflow: G1-LEG-001 → rândul 11 din workbook; G1-LEG-002 → rândul 35; G1-LEG-003 → rândul 14; G1-LEG-050 → rândul 108. Deci comparatorul poate recunoaște întrebări reale comune gradelor, nu produce doar «0» prin eroare de normalizare.
- În `MASTER_UNIT_CARDS_568.csv` de pe ramura de audit s-au recitit cele 62 identități canonice, cu 62 unit_id distincte / 62 member_ids, toate risc P1. **Toate 62 au barem importat «A»**, al doilea indiciu (NU dovadă definitivă) de întrebări pedagogice cu opțiunea corectă pusă sistematic prima.

## Interpretarea corectă a rezultatului
- **Confirmat față de copia XLSX 05.2023 din Library:** aceste 62 de enunțuri G2-LEG nu există textual printre cele 104 întrebări ANRE Grad II din workbook. Afirmația «toate 62 sunt întrebări oficiale ANRE din XLSX de mai 2023» este contrazisă de test.
- **NU este demonstrat:** că aceste 62 de întrebări sunt incorecte tehnic, că n-au existat într-o ediție oficială diferită, ori că informațiile din ele nu sunt în bibliografia ANRE 05.2023. Numeroase variante A se potrivesc **bibliografiei oficiale**, dar asta este altă clasă de dovadă decât proveniența întrebării.
- **Risc de produs:** dacă trainerul le amestecă fără etichetă cu întrebările ANRE autentificate, utilizatorul poate învăța un format pedagogic diferit de testul real și poate presupune fals că acestea sunt grile oficiale. Recomandare QA fără mutație: marcați `OFFICIAL_QUESTION_PROVENANCE=NOT_FOUND_IN_ANRE_G2_LEG_05_2023`, `DERIVED_PRACTICE_ITEM=POSSIBLE`, `LEARNER_APPROVAL=NO`, `MODEL_ANSWER_A_UNREVIEWED_AS_OFFICIAL` până la revizie.

## Registru de identități afectate (toate prezente în master)
```text
G2-LEG-001
G2-LEG-002
G2-LEG-003
G2-LEG-004
G2-LEG-005
G2-LEG-006
G2-LEG-007
G2-LEG-008
G2-LEG-009
G2-LEG-067
G2-LEG-068
G2-LEG-069
G2-LEG-070
G2-LEG-071
G2-LEG-072
G2-LEG-073
G2-LEG-074
G2-LEG-075
G2-LEG-076
G2-LEG-077
G2-LEG-078
G2-LEG-079
G2-LEG-080
G2-LEG-081
G2-LEG-082
G2-LEG-083
G2-LEG-100
G2-LEG-101
G2-LEG-102
G2-LEG-103
G2-LEG-104
G2-LEG-105
G2-LEG-106
G2-LEG-107
G2-LEG-108
G2-LEG-109
G2-LEG-110
G2-LEG-111
G2-LEG-112
G2-LEG-113
G2-LEG-114
G2-LEG-115
G2-LEG-116
G2-LEG-117
G2-LEG-118
G2-LEG-119
G2-LEG-120
G2-LEG-121
G2-LEG-122
G2-LEG-123
G2-LEG-124
G2-LEG-125
G2-LEG-126
G2-LEG-127
G2-LEG-128
G2-LEG-129
G2-LEG-130
G2-LEG-131
G2-LEG-132
G2-LEG-133
G2-LEG-134
G2-LEG-135
```

## Consecințe pentru status și politica de proiect
- CKPT-092–098 rămân cercetări de context valoroase: **nu li se anulează creditul documentar**, dar **nu sunt aprobări de barem sau de proveniență**. Cumul din CKPT-098 rămâne **293/568 unități și 348/822 ID-uri** cu fișă contextuală; 0/822 aprobate pentru învățare. Acest CKPT099 are **delta coverage 0**.
- Necesare: confirmarea originilor pentru fiecare dintre cele 62 (eventual altă ediție/întrebări sintetice); compararea exactă A/B/C cu un original oficial dacă există; control juridic/tehnic/lingvistic independent; segregarea viitoare între `OFFICIAL_EXAM_QUESTION` și `DIDACTIC_PRACTICE`. NU promovăm un fapt bibliografic la dovadă de proveniență de grilă.
- Acesta este un audit efectiv efectuat în această sesiune, **nu** un reviewer independent și nu un benchmark de model. Fără modificări în bareme, enunțuri, master CSV, HTML, APK, main, merge, release. PR #7 Draft păstrat.
- Nu este necesară intervenția utilizatorului acum; întrebările se discută cu utilizatorul doar dacă persistă ambiguitate cu dovezi complete, iar corecțiile canonice necesită aprobarea explicită ulterioară.
