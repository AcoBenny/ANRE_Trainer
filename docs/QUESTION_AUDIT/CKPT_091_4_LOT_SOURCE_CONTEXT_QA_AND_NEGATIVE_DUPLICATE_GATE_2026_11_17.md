# CKPT-091 | Sumar QA de sesiune, 4 loturi AH–AJ și control negativ anti-dublare | 2026-11-17

## Commit și acoperire
- Repo AcoBenny/ANRE_Trainer, branch audit/anre-v8-priority-17-20261109, PR #7 Open/Draft/Unmerged; HEAD verificat înainte de scriere: `0350ec14f245a9da5a22d323c907745c880ab6ac`.
- Baseline CKPT-086 (2026-11-17) **226/568 unități** și **281/822 ID-uri**, 0 learner-approved. CKPT-087 LEG033/044/045/050 +4/+4; CKPT-088 G2-LEG067–073 +7/+7; CKPT-089 G2-LEG074–080 +7/+7; CKPT-090 G2-LEG001–006 +6/+6.
- **Cumul verificat prin readback**: **250/568 unități distincte și 305/822 ID-uri** contextual documentate; delta **24/24** în 4 loturi. **0/822 aprobate pentru învățare**; nicio schimbare de cheie, întrebare, variantă sau aplicație. Acest fișier CKPT091 are delta 0.
- GitHub readback efectiv: 4 fișiere, fiecare card apare o singură dată după heading de ID; 24 × trei opțiuni ABC = 72 opțiuni originale transcrise; fiecare bloc conține sursă primară și argumente A/B/C (verificarea de adevăr a surselor rămâne independentă, NOT_RUN).

## QA evidence per batch
- `CKPT_087_P1_LEG033_044_045_050_OFFICIAL_SOURCE_2026_11_17.md`: `4/4` headings distincte; `12/12` alternative ABC; blob `bda720ba92e05092af40495491ecddea7a44a502`.
- `CKPT_088_P1_LOT_AH_G2_LEG067_073_ANRE_ENROLLMENT_2026_11_17.md`: `7/7` headings distincte; `21/21` alternative ABC; blob `9d9c31637300388b027ba516bebff3cf2b0780c6`.
- `CKPT_089_P1_LOT_AI_G2_LEG074_080_ANRE_VISA_2026_11_17.md`: `7/7` headings distincte; `21/21` alternative ABC; blob `7642fb65b7372cd76c54b8adce7298dc0405eb44`.
- `CKPT_090_P1_LOT_AJ_G2_LEG001_006_ORDERS_2026_11_17.md`: `6/6` headings distincte; `18/18` alternative ABC; blob `5a081741b9ec2461752293ccf55f5dfd810c03e4`.

## Test negativ real de dublare și lecție acumulativă
- Un lot propus cu G1-NOR036–040 a fost **blocat înainte de commit** de verificarea arhivei `ACTIVE_EVIDENCE_INDEX_87`. În aceasta, G1-NOR037/038/039/040 erau deja documentate în CKPT047 și reparate de CKPT048. Ele **nu** au fost recreditate (delta 0). NOR036 rămâne candidat nou pentru un lot ulterior, separat.
- Nu confundați faptul că `MASTER_UNIT_CARDS_568.csv` păstrează context gol cu lipsa unei fișe în arhiva CKPT047–049 sau fișierele CKPT050+. Preflight-ul trebuie să consulte identitatea `unit_id`, `member_ids` și indexul de fișe înainte de orice credit.
- Regressions: **NO_DOUBLE_CREDIT**, **FIELD_ALIGNMENT**, **ALL_KEYS_A_PATTERN**. În G2-LEG-001–006/067–080 toate cheile sunt A, fapt care poate sugera aranjarea artificială a variantelor sau întrebări derivate; nu este prin sine o eroare confirmată. Necesită verificarea originalului XLSX și dacă respectivele enunțuri provin din grile oficiale sau sunt întrebări pedagogice proprii.

## Porți deschise și următorul lot
- Confirmarea bibliografiei grade II sesiune 2026 și a provenienței exacte a întrebărilor, nu doar corectitudinea ordinului de aprobare sau a informației de pe pagina ANRE.
- QA independent sursă/juridic/lingvistic, conflicte P0, imaginea lipsă ELE028, versiunea normative PE155/I7. Pot fi păstrate ca fișe contextuale P1, dar **nu** ca răspunsuri pentru trainer.
- Prioritate viitoare: G1-NOR036 fără duplicare, G2-LEG081–083 numai după verificarea tarifelor oficiale 2026, apoi G2-LEG100+ cu deduplicare semantică și test de proveniență.
- Fără intervenție utilizator acum; cereți clarificare numai după epuizarea contextului de surse și a contraexemplelor, prezentând originalul A/B/C și pasajele relevante. Fără bareme, HTML/APK/main, merge/release.
