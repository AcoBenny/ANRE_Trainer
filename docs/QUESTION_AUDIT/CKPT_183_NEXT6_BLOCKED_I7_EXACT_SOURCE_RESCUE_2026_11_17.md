# CKPT-183 | 6 additional blocked I7 units, direct source rescue and ambiguity QA | 2026-11-17

This is **additive** to CKPT-182 (10 existing units), preserves CKPT-172/173/176 and source-failure history, and does not change canonical QABC, barems, app, release gates or main. I7 full text reopened directly at [searchable text](https://www.arya.ro/legislatie/document.php?slug=normativ-i7-2011); the [official document index](https://legislatie.just.ro/Public/DetaliiDocument/286763) is available through indexing but direct read was HTTP 502 today. 2026 exam edition/key and independent technical/legal review not established.

## Newly surfaced exact-clause repairs
- **NOR025 major source rescue**: same-object primary norm **I7 §5.3.3.19.1** itself supplies **15 mm**. CKPT-173 had incorrectly sent this question to generic §5.3.3.19.2 / STAS7944 as if no matched I7 clause existed. Keep original history and supersede source locator without rewriting the original case or barem.
- **NOR033 major source rescue**: I7 §4.3.7.1 actually gives **two fuse rating steps** as an example. That repairs previous `NO_EXACT_DOCUMENT` finding for intended A, but **«de ex.» does not certify a universally sufficient two-step rule** for all fuse curves.

## Six original QABC cards with source/option QA

### G1-NOR-090 | OVERLAPPING_B_AND_C
- Existing unit `AU-63f2b04cc9d8dd52`, hash `63f2b04cc9d8dd52155179a3e1a6bc7c9face861449048923e2197df164ca59b`; **imported key B, unchanged**; source candidate: C literal; B overlapping, not applied.
- **Original question:** Tuburile şi ţevile metalice
- **A:** nu se pot monta direct pe elementele de construcţie din materiale combustibile.
- **B:** se pot monta direct pe elementele de construcţie din materiale combustibile, condiționat.
- **C:** se pot monta direct pe elementele de construcţie din materiale combustibile
- **ABC:** A absolute prohibition contradicted by §5.2.12.2.12. B conditional permission could be true where extra environment or installation constraints apply. C exactly quotes direct metal-tube permission, but no general practical implication of ignoring other requirements.
- **I7 §5.2.12.2.11–13 and §3.0.3.7 neighboring context:** Clue: metal tubes on combustible building material may be direct per §5.2.12.2.12; neighboring §5.2.12.2.11 stipulates 3cm in AD3/AD4/AF etc and §5.2.12.2.13 separately regulates plastic tubes. Do not import plastic-specific conditions into metal permission.
- **Disposition:** No unconditional single-key approval; ambiguity or missing qualifier retained.

### G1-NOR-016 | TOO_EXCLUSIVE_DOZE_VS_OTHER_ACCESSORY
- Existing unit `AU-c57ec6fca3d0e6f6`, hash `c57ec6fca3d0e6f68afa4e838126740fdca103c8fc6fdc6f0c63a0618f14035c`; **imported key C, unchanged**; source candidate: C intended, not applied.
- **Original question:** Legăturile electrice între conductoare izolate pentru îmbinări sau derivaţii se fac:
- **A:** în interiorul tuburilor sau ţevilor de protecţie
- **B:** în interiorul golurilor din elementele de construcţie
- **C:** numai în doze sau cutii de legătură
- **ABC:** A in-protection-tube splice disallowed. B inside construction void disallowed. C doze/cutii are allowed, but «numai» may exclude other specifically designed accessories.
- **I7 §5.2.6.4–5 neighboring context:** §5.2.6.4 prescribes only specially provided accessories, examples «doze, cutii de legătură etc.»; §5.2.6.5 prohibits free joints in tubes/voids/passes. C is intended by elimination but not an exhaustive literal set of all permitted accessory forms.
- **Disposition:** No unconditional single-key approval; ambiguity or missing qualifier retained.

### G1-NOR-025 | EXACT_15MM_SOURCE_RECOVERED
- Existing unit `AU-250aa31d22a753c4`, hash `250aa31d22a753c4b14e1dd34290f609e6251b17b817b98f9e7c5143f7a3529c`; **imported key B, unchanged**; source candidate: B 15mm, not applied.
- **Original question:** La realizarea tablourilor şi barelor de distribuţie de j.t., distanţa minimă de izolare în aer între piesele fixe sub tensiune ale diferitelor faze, precum şi între acestea şi părţi metalice legate la pământ trebuie să fie de cel puţin:
- **A:** 10 mm
- **B:** 15 mm
- **C:** 20 mm
- **ABC:** A 10mm falls below explicit minimum. B 15mm matches same object: fixed live parts of distinct phases and grounded metal in a switchboard. C 20mm is a stricter clearance, not the specified minimum.
- **I7 §5.3.3.19.1–20 neighboring context:** Critical correction to CKPT-173 source-locator mismatch: §5.3.3.19.1 (not §5.3.3.19.2) explicitly gives ≥15mm in air and ≥30mm creepage between these fixed parts. §5.3.3.19.2 separately sends distance BETWEEN BARS to STAS7944; §5.3.3.20 prefabricated panels to product standard. Exact object scope must match; don't generalize 15mm to all prefab/device clearances.
- **Disposition:** Specific original normative figure directly source-supported; 2026/exam edition and independent QA still open.

### G1-NOR-033 | EXEMPLAR_TWO_STEPS_NOT_UNIVERSAL
- Existing unit `AU-ecfc1c65dfc8ff71`, hash `ecfc1c65dfc8ff71638a68c51c7ec1c3c5d7e0c29ba2fdad280eeaccf13f1e5a`; **imported key A, unchanged**; source candidate: A 2 steps, not applied.
- **Original question:** Pentru asigurarea selectivităţii, între curenţii nominali ai fuzibilelor a două siguranţe consecutive, diferenţa trebuie să fie de cel puţin:
- **A:** doua trepte
- **B:** o treapta
- **C:** trei trepte
- **ABC:** A two steps is the normative example for two consecutive fuses. B one step does not meet the cited exemplar. C three steps is stricter but not the quoted minimum.
- **I7 §4.3.7.1 neighboring context:** I7 §4.3.7.1 requires selective coordination based on protective characteristics and gives two fuse-current steps as «de ex.» illustration, not universal guarantee under all fuse curves, operating conditions or types. Thus barem A has exact text support but statement «trebuie» overstates what the example proves.
- **Disposition:** Source example verified, but absolute/technical sufficiency remains conditional.

### G1-NOR-081 | NO_FULLY_EXPLICIT_ABC_CONJUNCTION
- Existing unit `AU-a605ad5abab07022`, hash `a605ad5abab07022969b067c8b0dc1502c376b970ab460303af160da2fbb5b9a`; **imported key C, unchanged**; source candidate: C intended, incomplete, not applied.
- **Original question:** Montarea în contact direct cu materiale combustibile se admite
- **A:** pentru cabluri cu izolație din PVC
- **B:** pentru toate tuburile şi plintele din materiale plastice
- **C:** pentru cabluri cu întârziere la propagarea flăcării
- **ABC:** A PVC insulation insufficient evidence of fire rating. B all plastic tubes/plinths too sweeping, need approval. C delayed flame spread alone omits source's additional fire-resistance condition.
- **I7 §3.0.3.5–8 neighboring context:** §3.0.3.7 uses **rezistente la foc ȘI cu întârziere la propagarea flăcării** for cables touching combustible material. Here C names only flame retardance. An exam may treat it as characteristic of a fire-resistant cable, but no affirmative universal implication proved. Do not force key.
- **Disposition:** No unconditional single-key approval; ambiguity or missing qualifier retained.

### G1-NOR-082 | NO_FULLY_EXPLICIT_ABC_CONJUNCTION
- Existing unit `AU-36a182d5fe982c52`, hash `36a182d5fe982c521f643aa20fedc352735d018d5bcfb58c4a109f6d2a8a15b2`; **imported key B, unchanged**; source candidate: B intended, incomplete, not applied.
- **Original question:** Montarea în contact direct cu materiale combustibile se admite
- **A:** pentru toate tuburile şi plintele din materiale plastice
- **B:** pentru cabluri rezistente la foc
- **C:** pentru cabluri cu izolație din PVC
- **ABC:** A all plastic tubes fails required approval. B fire resistant cables names one of two simultaneous cable conditions in I7. C PVC insulation alone insufficient.
- **I7 §3.0.3.5–8 neighboring context:** §3.0.3.7 requires both fire-resistance AND flame-retardance. B says only fire resistance and is not proved sufficient as universal requirement by the current evidence. C/A similarly fail; no literal fully complete option.
- **Disposition:** No unconditional single-key approval; ambiguity or missing qualifier retained.

## QA and handoff
- Deterministic **6/6 exact matches** to V73 original question, three options and imported key; 822 canonical grade-ID rows seen. Source section and clause objects checked against exact stem and counterexamples. Existing units only, **0 new unit credit**, **0 approval for learning**, **0 key changes**.
- CKPT-182+183 now cover **16 distinct existing blocked I7 cases** including 2 rescued previously missing direct I7 clauses; this count is **rechecks**, not resolved final certification. CKPT-181 NOR066 separate, not counted again.
- Independent reviewers NOT_RUN; exact official ANRE grading key NOT_VERIFIED; latest exam bibliographic edition NOT_INDEPENDENTLY_SIGNED. Release gates all NO; PR #7 Draft, no merge.
- Next: use the remaining blocked electrical/legislation cards and negative source-scope cases, avoiding repeated I7 work.
