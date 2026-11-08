# ANRE Trainer | Note didactice originale, versiune de audit, NU pentru publicare

**6 subteme lipsă din sursele locale:** aceste rezumate sunt explicații proprii construite pe baza surselor externe indicate. Ele NU sunt pasaje extrase din manualele utilizatorului, nici verificări independente de inginer sau aprobări ANRE. Originalul de 822 de întrebări rămâne nemodificat.

## SUB-002 | Câmp magnetic fără surse

**Idee centrală.** Legea lui Gauss pentru magnetism afirmă că fluxul total al inducției magnetice prin orice suprafață închisă este zero, `∮ B·dA = 0`; în formă locală `∇·B=0`. Liniile fluxului magnetic nu se termină într-o sarcină magnetică izolată în electrodinamica clasică. **Capcană:** nu înseamnă `B=0` sau că magnetul nu poate crea câmp.

**De demonstrat:** aplicabilitatea formei diferențiale (câmp suficient de regulat), exemple vizuale și distincția față de Gauss electric.
**Surse externe de verificat:** https://openstax.org/books/university-physics-volume-2/pages/16-1-maxwells-equations-and-electromagnetic-waves

**QA:** sursă externă identificată, verificare inginerească independentă `NOT_RUN`, folosire offline `NEAPROBAT`

## SUB-003 | Vector Poynting și flux energetic

**Idee centrală.** Fluxul energetic electromagnetic are densitate vectorială `S=E×H` în W/m², în convenția SI; pentru unda în vid, `H=B/μ0`, deci `S=(E×B)/μ0`. Orientarea rezultă din produsul vectorial. **Capcană:** modulul instantaneu nu este același cu intensitatea medie a unei unde sinusoidale.

**De demonstrat:** convențiile de fazori și medii disipative pentru probleme specifice; formule vizual confirmate MIT PDF p.57 tipărită, captura paginii prin web indisponibilă.
**Surse externe de verificat:** https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/d3be4ea78b036a6362230fb41780cf54_MIT6_013S09_notes.pdf; https://openstax.org/books/university-physics-volume-2/pages/16-3-energy-carried-by-electromagnetic-waves

**QA:** sursă externă identificată, verificare inginerească independentă `NOT_RUN`, folosire offline `NEAPROBAT`

## SUB-005 | Fotovoltaice: efect, panouri și invertor

**Idee centrală.** Semiconductorii fotovoltaici convertesc radiația solară în energie electrică. Celulele sunt conectate în module, apoi în câmpuri; ieșirea modulelor este DC, iar invertorul poate furniza AC.

**Limită:** protecțiile DC/AC, anti-insularizare, invertorul compatibil cu rețeaua și procedurile românești de racordare NU sunt documentate suficient prin această sursă de principiu.
**Surse externe de verificat:** https://www.energy.gov/cmei/systems/solar-photovoltaic-technology-basics; https://www.energy.gov/cmei/systems/solar-photovoltaic-system-design-basics

**QA:** sursă externă identificată, verificare inginerească independentă `NOT_RUN`, folosire offline `NEAPROBAT`

## SUB-006 | Eolian: rotor, generator și conectare

**Idee centrală.** Forțele aerodinamice pun rotorul eolian în mișcare; cuplul este transmis unui generator fie direct, fie prin transmisie mecanică. Energia cinetică a vântului devine energie mecanică și apoi electrică.

**Limită:** principiul generatorului nu stabilește automat sincronizarea și calitatea energiei la punctul de racordare; trebuie o sursă separată pentru convertizoare, sisteme de control și protecții.
**Surse externe de verificat:** https://www.energy.gov/cmei/systems/how-do-wind-turbines-work; https://www.energy.gov/cmei/systems/wind-energy-basics

**QA:** sursă externă identificată, verificare inginerească independentă `NOT_RUN`, folosire offline `NEAPROBAT`

## SUB-012 | Fascicularea conductoarelor și efectul Corona

**Idee centrală.** În linii de înaltă tensiune, împărțirea unei faze în două sau mai multe subconductoare apropiate crește raza electrică echivalentă și reduce gradientul câmpului la suprafața conductorului, diminuând probabilitatea descărcărilor Corona.

**Limită:** efectul depinde de tensiune, geometrie, starea suprafeței și condiții meteo. Fascicularea nu elimină universal efectul Corona; formulele GMR/inductanță sunt în sursă dar figurile și licența necesită audit separat.
**Surse externe de verificat:** https://archive.nptel.ac.in/content/storage2/courses/108104051/chapter_1/1_10.html; https://my.ece.utah.edu/~ece3600/Notes_TransmissionLines_F23.pdf

**QA:** sursă externă identificată, verificare inginerească independentă `NOT_RUN`, folosire offline `NEAPROBAT`

## SUB-015 | Tranzitoriu RC, încărcare și descărcare

**Idee centrală.** La un circuit simplu rezistor-condensator cu variație treaptă, constanta de timp `τ=RC`. La încărcare, `q(t)=C·V·(1−e^(−t/RC))`; la descărcare, `q(t)=q0·e^(−t/RC)`. După o constantă de timp, încărcarea atinge aproximativ 63,2% din valoarea finală și la descărcare rămân 36,8%.

**Limită:** dacă există mai multe rezistențe, folosește rezistența echivalentă văzută de condensator. Pentru circuite de ordin mai mare, o singură `τ=RC` nu caracterizează întregul răspuns.
**Surse externe de verificat:** https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits; https://circuits.mit.edu/F25/psets/04/rc_tutorial

**QA:** sursă externă identificată, verificare inginerească independentă `NOT_RUN`, folosire offline `NEAPROBAT`
