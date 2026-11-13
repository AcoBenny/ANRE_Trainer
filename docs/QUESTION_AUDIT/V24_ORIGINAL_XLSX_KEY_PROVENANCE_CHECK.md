# V24 | Control de proveniență a baremelor în XLSX originale

**Data:** 2026-11-09. **Statut:** audit determinist de structură, fără aprobare de barem. **Sursa canonică aplicație:** V10.29, blob GitHub `bc5b5a61954ba138cf83987bfc932eca517f3b21`.

Am deschis direct fișierele încărcate anterior de utilizator și disponibile în Library: `LEGISLATIE-GR.-1-05.2023 (1).xlsx` (Sheet1) și `ELECTROTEHNICA-09.2024-2.xlsx` (Sheet1). Nu au fost redistribuite sau comise aceste cărți de lucru.

## Legislație G1, rânduri originale

| ID | Excel rând | A/B/C (prezență) | Valoare col. I | Status |
|---|---:|---|---|---|
| G1-LEG-024 | 31 | toate | 1 | **Nu** înseamnă automat A |
| G1-LEG-028 | 35 | toate | 3 | **Nu** înseamnă automat C |
| G1-LEG-032 | 39 | toate | celulă goală | Cheie absentă în I |
| G1-LEG-034 | 41 | toate | celulă goală | Cheie absentă în I |
| G1-LEG-048 | 55 | toate | celulă goală | Cheie absentă în I |

**Control critic:** între I1:I57, singurele valori nenule observate sunt: `I31=1, I34=2, I35=3, I46=4, I54=5`. Fiind o **secvență 1–5 care include 4 și 5**, nu poate reprezenta fidel o coloană standard de barem A/B/C. Fără legenda originală, semnificația coloanei I este necunoscută. Sunt invalide afirmațiile „I31=1 dovedește cheia A” sau „I35=3 dovedește cheia C”.

Foile păstrează enunțurile și opțiunile sursei istorice. Confirmarea literei corecte necesită evidența baremului propriu-zis sau comparația cu actul normativ, cu ediția aplicabilă și interpretarea corectă a capcanelor. Pentru G1-LEG-024/028/032/034/048 rămân separate cele două chei deja evidențiate în V13/V14, fără editări.

## Electrotehnică

`ELECTROTEHNICA-09.2024-2.xlsx`, Sheet1, rândul 25: întrebarea despre `capacitatea de serviciu Cs`, opțiunile `Cs=3 C`, `Cs=C/3`, `Cs=C`; acest tabel A:D nu conține o coloană separată de răspuns. Nu se poate adjudeca de aici singur conflictul `G1-ELE-018` versus `G2-ELEC-170`.

## Concluzie / gate

- S-au verificat **existenta textului și opțiunilor, nu chei oficiale de răspuns**.
- Nicio adnotare laterală fără legendă nu trebuie convertită automat în cheie.
- Verificare tehnică/juridică independentă `NOT_RUN`; QA de verificare a sursei normative per-ID necesar; **zero** schimbări în HTML, APK sau bareme.
