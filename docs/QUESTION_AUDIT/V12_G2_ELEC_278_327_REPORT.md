# ANRE Trainer | V12 G2-ELEC-278–327 model-assisted audit

2026-11-09. 50/50 existing canonical V10.29 questions extracted directly from GitHub blob `bc5b5a61954ba138cf83987bfc932eca517f3b21`. Source/ABC/key kept intact in versioned CSV. Classification: CONDITIONAL=19; PRINCIPLE=13; FORMULA_CHECK=7; AMBIGUITY=7; SAFETY_SOURCE=4. Categories describe *reviews needed*, not independently validated correctness. All exact textbook pages = NOT_VERIFIED; independent QA = NOT_RUN.

## Highest priority gates

- **G2-ELEC-290:** defines propagation constant as „adimensională” per km, but `gamma=alpha+j beta` conventionally has dimension inverse length; check original edition.
- **G2-ELEC-316:** both B (lamination to limit eddy-current losses) and C (avoid placement of massive metals in varying fields) can reasonably mitigate losses; key B only, potential multiple-choice defect.
- **G2-ELEC-314:** reactive power is not generally identical to time derivative of combined magnetic/electric energy; require rigorous definition and context before accepting C.
- **G2-ELEC-279:** Ohm's law generalization `indiferent de natura circuitului` can be overbroad if considering nonlinear elements; key C conventional but needs qualification.
- **G2-ELEC-282:** asynchronous motor speed depends on supply frequency **and** slip; key B not equivalent to exclusive dependence on frequency.
- **G2-ELEC-298:** synchronous machines on variable-frequency supply can vary speed widely; statement limited to historical line-connected drives.
- **G2-ELEC-304:** cost-of-loss trend versus voltage depends on fixed power and network impedance/cost assumptions, missing here.
- **G2-ELEC-325:** electric potential as work per unit charge depends on sign and external versus field-work convention.
- **G2-ELEC-278:** Ferranti effect approximate quadratic dependence for uniform line and small electrical length; source and conditions necessary.
- **G2-ELEC-307:** source conversion identities `ZY=1` and `J=YE`, key A consistent for Z!=0.
- **G2-ELEC-323:** losses P and Q at constant apparent S scale inverse U², with unchanged line R/X.
- **G2-ELEC-324:** at fixed active P, raise cosφ .8 to .9 decreases current and copper losses.

No edits to answers or application. Gate: obtain pages/editions, independently adjudicate ambiguous cases, test in offline learner UI. Do not merge/release.
