# CKPT-424 | 208/822 educational content validations

Date 2026-11-24 | Parent CKPT-423 | [PR #7](https://github.com/AcoBenny/ANRE_Trainer/pull/7) Draft / unmerged.

**Incremental validated: 4 distinct original groups / 8 new grade routes, 200 → 208 / 822.** Distinct QABC accepted: 103 → 107 / 568. Historical holds unchanged: 200 routes / 136 groups. Unflagged pending: 414 routes / 325 groups.

## Four fresh reviews (no duplicates)
- **QABC-0030 (G1-ELE-035/G2-ELEC-183, key A)** and **QABC-0034 (G1-ELE-041/G2-ELEC-187, key C)**: switchgear partitioning prevents propagation of faults to adjacent bays in manufacturer technical page [ZPUE](https://zpue.com/low-voltage-switchgears/98-oferta/medium-voltage-switchgears), Design/Cubicle compartments. Limitation: source is specific MV cabinet manufacturer, not generic promise of fault prevention.
- **QABC-0061 (G1-ELE-069/G2-ELEC-214, key A)**: [OpenStax Ohm, §9.4](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law) directly states U=IR; I=U/R within ohmic conductor scope; U*R and U-R fail units/formula.
- **QABC-0107 (G1-ELE-116/G2-ELEC-258, key A)**: [OpenStax §5.4](https://openstax.org/books/university-physics-volume-2/pages/5-4-electric-field) F=qE defines E=F/q, not only electrostatic potential-gradient or conductor current U/R.

An external independent **AI** challenger was actually run via Parallel web research, session `resp_03f7776b-7a1e-406b-828b-67fcb7006176`; it reviewed original A/B/C and opened each technical source URL. This is **not** human specialist certification or official ANRE-key proof. Verbatim source context rights and offline app QA are not claimed.

## Deliberate exclusion
- **QABC-0064** (RL factor of attenuation, key A R/L) has technical derivation from OpenStax §14.4 but no directly sourced Romanian definition distinguishing «factor de atenuare» from time constant L/R. Independent reviewer flagged inference; remains pending. No forced conditional approval.

## Data controls and next step
Original G1/G2 imported keys untouched; all 4 validated groups have exactly 2 matching grade routes. Counts reconciled to 568 QABC / 822 grade IDs, previous 200 historical holds unchanged. Only audit documentation updated on PR #7. No barem, original question, HTML, APK, main or merge/release changed. Continue with 414 unflagged pending grade routes, aim 250/822 only when 42 more routes independently sourced and safely adjudicated.
