# CKPT-192 | G1-LEG-017: user's semantic hypothesis, primary law context and correction | 2026-11-17

Documentation ONLY; maintains question, ABC and B (imported). No learning approval or independent external agent review.

## Canonical trace / predecessor
- G1-LEG-017; unit `AU-4b365bd0966b300d`; original QABC sha256 `4b365bd0966b300dae3c29d7f13e0374bb346425e99cc7bfbbd047855d820e70`.
- Previous evidence CKPT-163, CKPT-190, CKPT-191; imported key `B` UNCHANGED; user favors candidate `A` NOT APPLIED.

## User's original observation (preserved as hypothesis, not statutory quote)
> Dupa citit e clar ca raspunsul este A.
> Ca sa poate rezilieze trebuie sa fie deja intrun contract cu furnizorul. Unde B nu prezinta acest stadiu, ba inca se poate oferi un contract acelui individ, si clientul final nu este inca conectat la retea daca nu plateste acea garantie deci este eliminat pe acelasi principiu ca B.

## Primary text and precise scope QA
- Official Romanian source: https://legislatie.just.ro/Public/FormaPrintabila/00000G0UMVX7MM6BAVV320XLVAOEXZ5Q
- Legea nr. 123/2012, art.58(4)(a): electricity theft confirmed by a final court ruling is expressly a ground of *reziliere a contractului*. Candidate A is exact wording/object match.
- Art.58(4)(c) also allows other cases specified by current law, so this paragraph alone does not prove there can be no legally sufficient B circumstance.
- Art.58(5) allows guarantees to be sought of an already existing final client when metering distortion / theft-by-bypass is found; art.58(6) states refusal permits provider to request *deconectare* from network, not directly contractual *reziliere*. Thus user's C 'not connected yet' premise is NOT supported. Stronger C elimination basis is legal effect mismatch.
- Illegal distribution-grid connection does NOT logically entail that no supply contract already exists. A contracted customer could make an illegal bypass; user's B 'no contract' premise is NOT universally established. Article 61 treats contractual noncompliance with possible termination in some cases; exact contractual/legislative nexus for the wording B still NOT AUTHENTICATED.
- Overall: source-supported candidate A, imported B suspect, no automatic correction; current ANRE exam edition / official key NOT independently checked.

## Workflow lesson
- When presenting legal text for user analysis, provide the original, unaltered source with one full neighboring paragraph/alignment before and after highlighted passage where reproduction rights allow; if cannot reproduce, link exact full official text and explicitly state limitation. Put any model reasoning in a fully separate section *after* source text, not between excerpts.
- Preserve user feedback and potential contradictions without asserting user statements as verified facts. A/B/C exception gates and source-era must still pass.

## Release safety
- `canonical_mutation=NO`; `learning_approved=NO`; `independent_legal_QA=NOT_RUN`; `independent_linguistic_QA=NOT_RUN`; `official_ANRE_2026_edition=NOT_VERIFIED`; `PR_7_Draft=YES`.
- `next_action`: verify actual 2026 applicable bibliography/official key; locate exact statutory or contractual clause if any making illegal connection in option B a contractual termination ground; independently QA all three choices before modifying learner content.
