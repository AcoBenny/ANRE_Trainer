# CKPT-385 | GFR: two source-native orphan electrotechnics cases researched, no keys changed

Date 2026-11-22. Follows CKPT-384, V296 source completeness index. Source original XLSX SHA256 `2175d2c30ac8e2f149b28edd9ac00c233789bc0a3987ba779d6efed7afad920c`, rows **39 and 65** read directly with artifact_tool from user's private workbook. Neither currently has a QABC mapping in V141, so **do not assign an invented QABC ID** or count as 822 final approvals.

## Source original Excel row 39 | Ampere magnetostatic circulation

Stem: `Circulaţia câmpului magnetic pe un contur închis este egală cu:`
- A: `suma algebrică a curenţilor care străbat conturul`.
- B: `zero`.
- C: `suma căderilor de tensiune            de-a lungul conturului`.

**Physical object and action:** circulation `∮ H·dl` of *magnetic field strength* H around oriented closed contour, currents crossing a spanning surface; right-hand rule determines algebraic signs. It is not magnetic flux `∮ B·dS`, nor a Kirchhoff voltage sum.

**Primary educational source reopened:** Physics LibreTexts / Ellingson §7.4 *Ampere's Circuital Law (Magnetostatics) — Integral Form*, exact formula `∮ H·dl=I_encl`. https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electromagnetics_I_%28Ellingson%29/07%3A_Magnetostatics/7.04%3A_Amperes_Circuital_Law_%28Magnetostatics%29_-_Integral_Form

**Before / context:** Faraday-Ampere contour and an oriented open surface. **Focus:** `∮ H·dl = Σ I_enclosed` **ONLY IN MAGNETOSTATICS**. **After / exception:** for time-varying fields displacement current contributes; exact Maxwell-Ampère law is `∮H·dl=I_c+∫(∂D/∂t)·dS` per Ellingson §8.9, https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism/Electromagnetics_I_%28Ellingson%29/08%3A_Time-Varying_Fields/8.09%3A_Displacement_Current_and_Amperes_Law .

**Alternatives:** A is affirmative in magnetostatic limit; B applies only when net enclosed current is zero (special case), not all paths; C is voltage-loop concept not magnetic circulation. A/B differ in the nonzero-current counterexample; A/C are different physical integrals; B/C not the general relation. **Provisional source A only with magnetostatic scope; missing time regime makes universal question overbroad.**

## Source original Excel row 65 | Two three-phase phasor sets with common tips, different origins

Original stem: `Două sisteme de fazori trifazaţi oarecare, care au vârfuri comune şi origini diferite care se descompun în componente simetrice:`
- A: `au numai aceleaşi componente directe (pozitive)`.
- B: `au aceleaşi componente inverse (negative)`.
- C: `au aceleaşi componente homopolare (zero)`.

**Geometry:** if the two systems share all corresponding phasor endpoints and differ by a common origin translation `d ≠ 0`, they are `V'a=Va+d; V'b=Vb+d; V'c=Vc+d`. For the symmetrical component operator `a=e^{j2π/3}`, `1+a+a²=0` and
- `V0=(Va+Vb+Vc)/3`; `V'0=V0+d` (**changes**),
- `V1=(Va+aVb+a²Vc)/3`; `V'1=V1` (**positive sequence unchanged**),
- `V2=(Va+a²Vb+aVc)/3`; `V'2=V2` (**negative sequence unchanged**).

**University source reopened:** James Kirtley/MIT via Engineering LibreTexts, *Introduction to Electric Power Systems*, §4.1, *The Symmetrical Component Transformation*, exact positive/negative/zero matrix and interpretation. https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Introduction_to_Electric_Power_Systems_%28Kirtley%29/04%3A_Introduction_to_symmetrical_components/4.01%3A_The_Symmetrical_Component_Transformation

**Before:** common translation of all three phasor vectors is identical vector d. **Focus:** positive and negative sequence components **both** remain identical; only zero-sequence is shifted by d. **After:** original A says **`numai`** (= ONLY same positive component), invalidated because negative sequence is ALSO the same; B is affirmatively true and does not falsely exclude others; C false for nonzero origin shift. If the exam intended A by omitting `numai`, that would create multiple correct answers, so literal original wording is essential.

**Provisional unique original-language answer: B** (NOT an ANRE scored key, not added to app). Numerical negative test with arbitrarily selected complex three-phase vectors and common `d=2−3j`: `ΔV0=d`, `ΔV1≈0`, `ΔV2≈0` (floating roundoff <1e−15). The property is algebraic and applies to any arbitrary original triplet with a common translation, not just balanced positive phase systems.

## Gates / permitted next work

- These are **2/11 original Electrotehnică source rows formerly unmapped**, newly provided with reasoned technical alternatives, not new certified learner questions and **not part of current 822**.
- **9 figure-dependent original source rows still need faithful vector interpretation**, direct original score keys and user-approved scope/grade mapping. The DrawingML content exists (V296).
- Current editions/bibliography/official exam scoring keys still need qualified independent review. Source file A/B/C, canonical bank, grade keys, HTML and APK untouched; PR #7 Draft/unmerged.
