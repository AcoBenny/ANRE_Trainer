import assert from "node:assert/strict";
import { classifyContinuation } from "../qa_statement_completion.mjs";
const fixtures=[
  {
    "id": "B_HISTORICAL",
    "stem": "Conductorul neutru (N) trebuie să aibă aceeaşi secţiune cu conductorul de fază:",
    "options": {
      "A": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază",
      "B": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 16 mm²Cu sau 25 mm²Al",
      "C": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm² Cu sau 35 mm² Al"
    },
    "rule": {
      "edition": "I7-02",
      "source_locator": "§5.1.8",
      "mono_conductors": 3,
      "copper_mm2": 16,
      "aluminium_mm2": 25
    },
    "expectStatus": "ONE_COMPLETION_CANDIDATE",
    "expectLetter": "B"
  },
  {
    "id": "CURRENT_2011_SCOPE_DIFF",
    "stem": "Conductorul neutru (N) trebuie să aibă aceeaşi secţiune cu conductorul de fază:",
    "options": {
      "A": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază",
      "B": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 16 mm²Cu sau 25 mm²Al",
      "C": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm² Cu sau 35 mm² Al"
    },
    "rule": {
      "edition": "I7-2011",
      "source_locator": "§5.2.4.6.1",
      "mono_conductors": 2,
      "copper_mm2": 16,
      "aluminium_mm2": 25
    },
    "expectStatus": "SOURCE_EDITION_SCOPE_MISMATCH",
    "expectLetter": null
  },
  {
    "id": "MULTIPLE_MATCH",
    "stem": "Conductorul neutru (N) trebuie să aibă aceeaşi secţiune cu conductorul de fază:",
    "options": {
      "A": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază",
      "B": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 16 mm²Cu sau 25 mm²Al",
      "C": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 16 mm2 Cu sau 25 mm²Al"
    },
    "rule": {
      "edition": "I7-02",
      "source_locator": "§5.1.8",
      "mono_conductors": 3,
      "copper_mm2": 16,
      "aluminium_mm2": 25
    },
    "expectStatus": "MULTIPLE_MATCHING_COMPLETIONS",
    "expectLetter": null
  },
  {
    "id": "SWAP_ABC",
    "stem": "Conductorul neutru (N) trebuie să aibă aceeaşi secţiune cu conductorul de fază:",
    "options": {
      "A": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 16 mm²Cu sau 25 mm²Al",
      "B": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază",
      "C": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm² Cu sau 35 mm² Al"
    },
    "rule": {
      "edition": "I7-02",
      "source_locator": "§5.1.8",
      "mono_conductors": 3,
      "copper_mm2": 16,
      "aluminium_mm2": 25
    },
    "expectStatus": "ONE_COMPLETION_CANDIDATE",
    "expectLetter": "A"
  },
  {
    "id": "NO_RULE_LOCATOR",
    "stem": "Conductorul neutru (N) trebuie să aibă aceeaşi secţiune cu conductorul de fază:",
    "options": {
      "A": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază",
      "B": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 16 mm²Cu sau 25 mm²Al",
      "C": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm² Cu sau 35 mm² Al"
    },
    "rule": {
      "edition": "I7-02",
      "source_locator": "",
      "mono_conductors": 3,
      "copper_mm2": 16,
      "aluminium_mm2": 25
    },
    "expectStatus": "BLOCKED_SOURCE_EDITION_OR_RULE",
    "expectLetter": null
  },
  {
    "id": "NOT_COMPLETION",
    "stem": "Care sunt secțiunile admise?",
    "options": {
      "A": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază",
      "B": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 16 mm²Cu sau 25 mm²Al",
      "C": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm² Cu sau 35 mm² Al"
    },
    "rule": {
      "edition": "I7-02",
      "source_locator": "§5.1.8",
      "mono_conductors": 3,
      "copper_mm2": 16,
      "aluminium_mm2": 25
    },
    "expectStatus": "NOT_STATEMENT_COMPLETION_STEM",
    "expectLetter": null
  },
  {
    "id": "WRONG_DIMENSION",
    "stem": "Conductorul neutru (N) trebuie să aibă aceeaşi secţiune cu conductorul de fază:",
    "options": {
      "A": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază",
      "B": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 16 mmCu sau 25 mmAl",
      "C": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm² Cu sau 35 mm² Al"
    },
    "rule": {
      "edition": "I7-02",
      "source_locator": "§5.1.8",
      "mono_conductors": 3,
      "copper_mm2": 16,
      "aluminium_mm2": 25
    },
    "expectStatus": "NO_SUPPORTED_COMPLETION",
    "expectLetter": null
  },
  {
    "id": "BAD_ABC",
    "stem": "Conductorul neutru (N) trebuie să aibă aceeaşi secţiune cu conductorul de fază:",
    "options": {
      "A": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază",
      "B": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 16 mm²Cu sau 25 mm²Al"
    },
    "rule": {
      "edition": "I7-02",
      "source_locator": "§5.1.8",
      "mono_conductors": 3,
      "copper_mm2": 16,
      "aluminium_mm2": 25
    },
    "expectStatus": "BLOCKED_ABC_MISSING",
    "expectLetter": null
  },
  {
    "id": "NO_VALID_OPTION",
    "stem": "Conductorul neutru (N) trebuie să aibă aceeaşi secţiune cu conductorul de fază:",
    "options": {
      "A": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază",
      "B": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm² Cu sau 35 mm² Al",
      "C": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm² Cu sau 35 mm² Al"
    },
    "rule": {
      "edition": "I7-02",
      "source_locator": "§5.1.8",
      "mono_conductors": 3,
      "copper_mm2": 16,
      "aluminium_mm2": 25
    },
    "expectStatus": "NO_SUPPORTED_COMPLETION",
    "expectLetter": null
  },
  {
    "id": "DIACRITICLESS",
    "stem": "Conductorul neutru (N) trebuie sa aiba aceeasi sectiune cu conductorul de faza:",
    "options": {
      "A": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază",
      "B": "in circuitele monofazate cu trei conductoare si in circuitele polifazate ale caror conductoare de faza au sectiunea mai mica sau egala cu 16 mm²Cu sau 25 mm²Al",
      "C": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm² Cu sau 35 mm² Al"
    },
    "rule": {
      "edition": "I7-02",
      "source_locator": "§5.1.8",
      "mono_conductors": 3,
      "copper_mm2": 16,
      "aluminium_mm2": 25
    },
    "expectStatus": "ONE_COMPLETION_CANDIDATE",
    "expectLetter": "B"
  },
  {
    "id": "NUMERIC_MONO",
    "stem": "Conductorul neutru (N) trebuie să aibă aceeaşi secţiune cu conductorul de fază:",
    "options": {
      "A": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate indiferent de secţiunea conductoarelor de fază",
      "B": "în circuitele monofazate cu 3 conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 16 mm²Cu sau 25 mm²Al",
      "C": "în circuitele monofazate cu trei conductoare şi în circuitele polifazate ale căror conductoare de fază au secţiunea mai mică sau egală cu 25 mm² Cu sau 35 mm² Al"
    },
    "rule": {
      "edition": "I7-02",
      "source_locator": "§5.1.8",
      "mono_conductors": 3,
      "copper_mm2": 16,
      "aluminium_mm2": 25
    },
    "expectStatus": "ONE_COMPLETION_CANDIDATE",
    "expectLetter": "B"
  }
];
for(const f of fixtures){
 const o=classifyContinuation({stem:f.stem,options:f.options,rule:f.rule});
 assert.equal(o.status,f.expectStatus,f.id+" status");
 assert.equal(o.candidate_letter,f.expectLetter,f.id+" letter");
 assert.equal(o.approved_for_learning,false,f.id+" approval");
}
console.log(fixtures.length+" statement-completion fixture PASS; independent source/answer verification NOT_RUN");
