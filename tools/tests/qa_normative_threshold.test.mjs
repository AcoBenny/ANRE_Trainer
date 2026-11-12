import assert from 'node:assert/strict';
import { evaluateNormativeBound } from '../qa_normative_threshold.mjs';
const rule = {
  "ruleType": "maximum",
  "objectKeyword": "tablourile de distributie",
  "defaultMaxMeters": 2.3,
  "exceptions": [
    {
      "scopeKeyword": "locuinte",
      "maxMeters": 2.5
    }
  ],
  "source_locator": "I7-2011 §5.3.3.21",
  "source_url": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
};
const cases = [
  {
    "id": "NOR029_ORIGINAL",
    "q": "Tablourile de distribuţie din locuinţe se pot instala astfel încât înălţimea laturii de sus a tablourilor faţă de pardoseala finită să nu depăşească:",
    "opts": {
      "A": "2 m",
      "B": "2,3 m",
      "C": "2,5 m"
    },
    "expectStatus": "SINGLE_NORMATIVE_BOUND_CANDIDATE",
    "expect": "C"
  },
  {
    "id": "GENERAL_BOUND",
    "q": "Tablourile de distribuţie se instalează astfel încât înălţimea laturii de sus faţă de pardoseala finită să nu depăşească:",
    "opts": {
      "A": "2 m",
      "B": "2,3 m",
      "C": "2,5 m"
    },
    "expectStatus": "SINGLE_NORMATIVE_BOUND_CANDIDATE",
    "expect": "B"
  },
  {
    "id": "DWELLING_EXCEPTION",
    "q": "Tablourile de distribuţie din locuinte se pot instala astfel încât înălţimea laturii de sus a tablourilor faţă de pardoseala finită să nu depăşească:",
    "opts": {
      "A": "2 m",
      "B": "2,3 m",
      "C": "2,5 m"
    },
    "expectStatus": "SINGLE_NORMATIVE_BOUND_CANDIDATE",
    "expect": "C"
  },
  {
    "id": "ADMISSIBLE_EXAMPLES",
    "q": "Care dintre urmatoarele inaltimi ale laturii de sus a tablourile de distributie din locuinte fata de pardoseala finita sunt permise?",
    "opts": {
      "A": "2 m",
      "B": "2,3 m",
      "C": "2,5 m"
    },
    "expectStatus": "MULTIPLE_ADMISSIBLE_EXAMPLES",
    "expect": null
  },
  {
    "id": "DUPLICATED_EQUIVALENT_MAX",
    "q": "Tablourile de distribuţie din locuinţe se pot instala astfel încât înălţimea laturii de sus a tablourilor faţă de pardoseala finită să nu depăşească:",
    "opts": {
      "A": "2,5 m",
      "B": "250 cm",
      "C": "2,3 m"
    },
    "expectStatus": "MULTIPLE_EQUIVALENT_BOUND_CHOICES",
    "expect": null
  },
  {
    "id": "MAX_MISSING",
    "q": "Tablourile de distribuţie din locuinţe se pot instala astfel încât înălţimea laturii de sus a tablourilor faţă de pardoseala finită să nu depăşească:",
    "opts": {
      "A": "2 m",
      "B": "2,3 m",
      "C": "3 m"
    },
    "expectStatus": "SOURCE_OR_OPTIONS_MISMATCH",
    "expect": null
  },
  {
    "id": "UNIT_CONVERSION",
    "q": "Tablourile de distribuţie din locuinţe se pot instala astfel încât înălţimea laturii de sus a tablourilor faţă de pardoseala finită să nu depăşească:",
    "opts": {
      "A": "200 cm",
      "B": "2300 mm",
      "C": "250 cm"
    },
    "expectStatus": "SINGLE_NORMATIVE_BOUND_CANDIDATE",
    "expect": "C"
  },
  {
    "id": "WRONG_OBJECT",
    "q": "Cablurile de distribuţie din locuinţe se pot instala astfel încât înălţimea laturii de sus faţă de pardoseala finită să nu depăşească:",
    "opts": {
      "A": "2 m",
      "B": "2,3 m",
      "C": "2,5 m"
    },
    "expectStatus": "BLOCKED_OBJECT_OR_MEASURE_SCOPE",
    "expect": null
  },
  {
    "id": "UNPARSABLE_ANSWER",
    "q": "Tablourile de distribuţie din locuinţe se pot instala astfel încât înălţimea laturii de sus a tablourilor faţă de pardoseala finită să nu depăşească:",
    "opts": {
      "A": "2 m",
      "B": "2,3 m",
      "C": "depinde"
    },
    "expectStatus": "BLOCKED_OPTIONS_OR_UNITS",
    "expect": null
  },
  {
    "id": "NO_SOURCE_LOCATOR",
    "q": "Tablourile de distribuţie din locuinţe se pot instala astfel încât înălţimea laturii de sus a tablourilor faţă de pardoseala finită să nu depăşească:",
    "opts": {
      "A": "2 m",
      "B": "2,3 m",
      "C": "2,5 m"
    },
    "rule": {
      "ruleType": "maximum",
      "objectKeyword": "tablourile de distributie",
      "defaultMaxMeters": 2.3,
      "exceptions": [
        {
          "scopeKeyword": "locuinte",
          "maxMeters": 2.5
        }
      ],
      "source_locator": "",
      "source_url": "https://legislatie.just.ro/Public/FormaPrintabila/00000G1AGLK3X9HXIS43LTLA4TCXTBR4"
    },
    "expectStatus": "BLOCKED_SOURCE_RULE_MISSING",
    "expect": null
  },
  {
    "id": "OTHER_QUANTIFIER_NOT_COVERED",
    "q": "Tablourile de distribuţie din locuinte au înălţimea laturii de sus fata de pardoseala finita de cel putin:",
    "opts": {
      "A": "2 m",
      "B": "2,3 m",
      "C": "2,5 m"
    },
    "expectStatus": "NOT_AN_EXPLICIT_BOUND_QUESTION",
    "expect": null
  }
];
for (const c of cases) {
 const out=evaluateNormativeBound({question:c.q,options:c.opts,rule:c.rule??rule});
 assert.equal(out.status,c.expectStatus,c.id+' status');
 assert.equal(out.candidate_letter,c.expect,c.id+' candidate');
 assert.equal(out.approved_for_learning,false,c.id+' approval');
}
console.log(cases.length+' normative-threshold regression tests PASS; independent source QA NOT_RUN');
