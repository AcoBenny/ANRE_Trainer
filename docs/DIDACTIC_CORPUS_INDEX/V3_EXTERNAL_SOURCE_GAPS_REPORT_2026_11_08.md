# ANRE Trainer | Completare bibliografică externă pentru șase lacune, V3

Data audit: 2026-11-08. **Audit exclusiv, fără modificare HTML/APK/bareme.** Ultimul checkpoint acceptat: CKPT-002.

## Rezultate

- În baza celor **19 subteme** prioritare, **6** au fost anterior clasificate drept fără paragraf local didactic adecvat. S-au identificat **surse externe educaționale precise pentru toate cele 6**. Asta NU înseamnă că lipsurile bibliotecii locale au fost eliminate sau că s-au integrat offline.
- **4/6** au explicație explicită pentru principiul specific: `SUB-002`, `SUB-003`, `SUB-012`, `SUB-015`.
- **2/6** au explicat doar funcționarea de bază: `SUB-005` (PV) și `SUB-006` (eolian). *Racordarea, protecțiile și integrarea în rețea rămân insuficient acoperite.*
- **0/6** au fost verificate independent de un specialist, **0/6** au fost autorizate pentru copiere integrală/offline în aplicație, **0/44** categorii părinte au primit aprobare finală.
- **Registrul V2 și numitorul 44 au rămas neschimbate**; fișierul V3 doar adaugă surse și limite la 19 subteme.

## Dovezi externe cu locator

| Subtemă | Locator autoritativ | Nivelul real al dovezii |
|---|---|---|
| `SUB-002` | OpenStax, University Physics Volume 2, §16.1 Maxwell’s Equations and Electromagnetic Waves | PRINCIPIU_EXPLICIT |
| `SUB-003` | MIT OCW, Electromagnetics and Applications, §2.7.1, p.57 tipărită, eq. (2.7.12) | PRINCIPIU_EXPLICIT |
| `SUB-005` | U.S. Department of Energy, Solar Photovoltaic Technology Basics (PV cell/module/array) | PRINCIPIU_DIDACTIC_DOAR; RACORDARE_NEPROBATA |
| `SUB-006` | U.S. Department of Energy, How Do Wind Turbines Work? | PRINCIPIU_DIDACTIC_DOAR; RACORDARE_NEPROBATA |
| `SUB-012` | NPTEL, Power System Analysis, Chapter 1, Modelling Power System Components, secțiunea 1.10 Bundled Conductors | PRINCIPIU_EXPLICIT; CALCULE_NEVALIDATE |
| `SUB-015` | OpenStax, University Physics Volume 2, §10.5 RC Circuits, eq. 10.8–10.12 | PRINCIPIU_EXPLICIT |

## Limite esențiale

1. **Document didactic vs barem ANRE:** OpenStax, MIT, NPTEL și DOE nu sunt norme românești și nu aprobă singure răspunsuri de examen.
2. **Licențe:** OpenStax și MIT OCW folosesc CC BY-NC-SA 4.0 pentru materialele lor aplicabile; utilizarea necomercială, atribuirea și ShareAlike trebuie respectate. Fișierele NPTEL/Utah și materialele DOE cu elemente terțe nu sunt declarate automat redistribuibile. Niciun PDF extern nu a fost publicat în GitHub sau adăugat în aplicație.
3. **Capturi PDF:** paginile PDF MIT și Utah au putut fi citite textual în căutarea publică, dar instrumentul web de captură a eșuat (cache miss). Păstrăm marcajul `PDF_TEXT_ONLY_VISUAL_PENDING` pentru aceste pagini, nu afirmăm verificare vizuală. OpenStax și DOE au fost consultate ca pagini HTML.
4. **Granularitate:** relațiile `S=E×H` și `S=(E×B)/μ0` sunt compatibile numai cu distincția dintre `B` și `H` (a doua este forma în vid). De asemenea, `τ=RC` cere un model echivalent RC de ordinul întâi.
5. **Surse locale:** 11 lucrări distincte, 3.464 pagini din catalogul anterior; aceste șase concepte nu au fost declarate nou descoperite în manualele locale prin această etapă.

## Ce rămâne înainte de încheierea auditului bibliotecii

- Căutarea unor cursuri și fragmente reutilizabile offline în condiții de licență clare, sau validarea unor note didactice originale (draft separat).
- Surse specifice pentru **racordare/protecții PV și eoliene în România**, inclusiv verificarea edițiilor normative aplicabile.
- QA tehnic independent asupra formulelor și afirmațiilor din toate cele 19 subteme; separarea lor de toate cele 44 de categorii părinte.
- Nicio modificare a celor 822 întrebări până la auditul didactic finalizat și aprobarea utilizatorului.

**Fișiere:** `ANRE_6_LACUNE_SURSE_EXTERNE_V3.csv`, `ANRE_SUBTEME_19_REGISTRU_V3.csv`, `ANRE_NOTE_DIDACTICE_ORIGINALE_6_SUBTEME_DRAFT.md`.
