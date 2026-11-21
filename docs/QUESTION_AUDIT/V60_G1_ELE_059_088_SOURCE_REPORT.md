# V60 | ANRE Trainer | G1-ELE-059–088 (30 întrebări, electrotehnică)
**Data:** 2026-11-11. **PR:** #7 Draft. **Canon:** V10.29, prin V21 paritate crossgrade și V59 chei/rânduri. Fără editări barem sau aplicație.

## Control efectuat
- 30/30 ID-uri G1 distincte existente; 30/30 au perechi G2 cu text și ABC identice în `V21_G1_204_CROSSGRADE_PARITY.csv`. Am comparat în V59 și cheile G1/G2, rândurile sursă (în toate cele 30: concordanță). **Nu** este un nou audit independent al blobului HTML și nici o dovadă că sursa inițială e oficială.
- Pentru fiecare există nota tehnică și avertizare de unicitate/condiție în `V60_G1_ELE_059_088_SOURCE_LING_RECHECK.csv`.
- **Explicații calculatorice suportate:** 059 tensiune linie stea ≈√3 U_fază; 063 energie ½Li²; 064 energie ½qV cu referința de potențial; 068 forța Biℓ; 072 R/L (factor atenuare) ≠L/R (constanta de timp); 075 f=np/60 cu p perechi poli; 076 |e|=Bℓv pentru orientări perpendiculare; 080 F/l ∝1/r; 081 F=qE; 082 f=1/T.
- **Întrebări cu risc sporit**:
  - `G1-ELE-073` (G2-ELEC-218): dacă fluxul e `E`, `Φ_E=q/ε0` în vid; dacă e `D`, `∮D·dA=q_free`. Originalul nu precizează câmpul, dar cheia B afirmă q. **Ambiguitate de definiție/unități, nu corecție automată**. OpenStax §6.3 documentează explicit fluxul câmpului E.
  - `G1-ELE-077`: „forță electromagnetică (Laplace)” și „forță electrodinamică” pot desemna fenomen apropiat, posibilitatea a două variante semantice necesită lingvist + profesor.
  - `G1-ELE-088`: compartimentarea limitează mai ales extinderea/consecințele defectului, în timp ce cheia A vorbește despre scăderea posibilității de *producere* a lui; sursă GIS exactă lipsă.
  - `G1-ELE-085`: suprasarcina transformatorului se poate accepta temporar numai în limite de încărcare/temperatură, după ghid IEC/fabricant, nu nelimitat.
  - `G1-ELE-061`: explicația efectului pelicular presupune verificarea diferenței dintre curenți paraziți și autoinducție; B „numai” este excluziv.
  - `G1-ELE-079`: Faraday cere derivata fluxului în timp; simpla diferență de flux nu este dimensional echivalentă.
  - `G1-ELE-070/071`: șunt și rezistență adițională se potrivesc aparatelor clasice, dar pentru instrumentație AC există și transformatoare de măsurare.
- **Surse publice punctuale accesate**:
  - OpenStax §6.3 `https://openstax.org/books/university-physics-volume-2/pages/6-3-applying-gausss-law`
  - OpenStax §8.3 `https://openstax.org/books/university-physics-volume-2/pages/8-3-energy-stored-in-a-capacitor`
  - OpenStax §10.4 `https://openstax.org/books/university-physics-volume-2/pages/10-4-electrical-measuring-instruments`
  - OpenStax §11.4 `https://openstax.org/books/university-physics-volume-2/pages/11-4-magnetic-force-on-a-current-carrying-conductor`
  - OpenStax §13.1 `https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law`
  - OpenStax §14.2 `https://openstax.org/books/university-physics-volume-2/pages/14-2-self-inductance-and-inductors`
  - OpenStax §14.3 `https://openstax.org/books/university-physics-volume-2/pages/14-3-energy-in-a-magnetic-field`
  - Nu a fost confirmată pagina exactă pentru fiecare echipament (cuple, GIS, linii, transformator etc.); câmpul sursei rămâne gol când nu există verificare punctuală. Niciun standard cu acces restricționat nu a fost reprodus.

## QA și limite
- Verificare automată: 30 ID unice, paritate G1-G2 și cu V59, 30 rânduri CSV citite înapoi, 0 modificări cheia originală.
- **QA independent tehnic/lingvistic: NOT_RUN. Paginile normativ-tehnice exacte încă PENDING la rândurile desemnate. Nu se declară 30 „corecte la examen”**.
- Contabilizare V61: **274/822** cu fișă individuală preliminară, **548/822** doar triaj/inventar, **0 independent signoff**, **0 aprobări de folosire a aplicației**.
- Nu s-au schimbat enunțuri, ABC, chei, HTML, APK, main și nu s-a făcut merge/deploy.

**Următorul lot:** G1-ELE de după 088, doar ID-uri existente, din registrul V61. Verifică înainte checkpoint-uri mai noi, pentru a evita dubluri între conversații.
