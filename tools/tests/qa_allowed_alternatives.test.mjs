import assert from 'node:assert/strict';
import {classifyDoorbellOptions} from '../qa_allowed_alternatives.mjs';
const cases=[
  {
    "id": "G1_NOR_048",
    "stem": "Alimentarea transformatorului de sonerie sau soneriei de 220(230) V se face:  .",
    "options": {
      "A": "dintr-un circuit de iluminat normal, dintr-un circuit de prize sau direct din tabloul de distribuție",
      "B": "numai dintr-un circuit de iluminat normal",
      "C": "numai dintr-un circuit de prize"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "I7-2011 §5.4.13",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "ONE_VALID_EXAM_OPTION",
    "candidate": "A"
  },
  {
    "id": "G1_NOR_049",
    "stem": "Alimentarea transformatorului de sonerie sau soneriei de 220(230) V se face:  .",
    "options": {
      "A": "numai direct din tabloul de distribuţie",
      "B": "dintr-un circuit de iluminat normal",
      "C": "numai dintr-un circuit de prize"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "I7-2011 §5.4.13",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "ONE_VALID_EXAM_OPTION",
    "candidate": "B"
  },
  {
    "id": "THREE_POSSIBILITIES_IF_NO_ONLY",
    "stem": "Alimentarea transformatorului de sonerie sau soneriei de 220(230) V se face:  .",
    "options": {
      "A": "dintr-un circuit de iluminat normal",
      "B": "dintr-un circuit de prize",
      "C": "direct din tabloul de distribuție"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "I7-2011 §5.4.13",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "MULTIPLE_VALID_OPTIONS",
    "candidate": null
  },
  {
    "id": "ALL_FALSE_EXCLUSIVES",
    "stem": "Alimentarea transformatorului de sonerie sau soneriei de 220(230) V se face:  .",
    "options": {
      "A": "numai dintr-un circuit de iluminat normal",
      "B": "numai dintr-un circuit de prize",
      "C": "numai direct din tabloul de distribuție"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "I7-2011 §5.4.13",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "NO_VALID_OPTION",
    "candidate": null
  },
  {
    "id": "BAD_EXTRA_OPTION",
    "stem": "Alimentarea transformatorului de sonerie sau soneriei de 220(230) V se face:  .",
    "options": {
      "A": "dintr-un circuit de iluminat normal",
      "B": "dintr-un circuit de iluminat de siguranță",
      "C": "numai dintr-un circuit de prize"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "I7-2011 §5.4.13",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "MANUAL_REVIEW_UNKNOWN_OR_COMPLEX_OPTION",
    "candidate": null
  },
  {
    "id": "NO_LOCATOR",
    "stem": "Alimentarea transformatorului de sonerie sau soneriei de 220(230) V se face:  .",
    "options": {
      "A": "dintr-un circuit de iluminat normal, dintr-un circuit de prize sau direct din tabloul de distribuție",
      "B": "numai dintr-un circuit de iluminat normal",
      "C": "numai dintr-un circuit de prize"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "BLOCKED_SOURCE_SCOPE",
    "candidate": null
  },
  {
    "id": "MISSING_OPTION",
    "stem": "Alimentarea transformatorului de sonerie sau soneriei de 220(230) V se face:  .",
    "options": {
      "A": "dintr-un circuit de iluminat normal, dintr-un circuit de prize sau direct din tabloul de distribuție",
      "B": "numai dintr-un circuit de iluminat normal"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "I7-2011 §5.4.13",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "BLOCKED_ABC",
    "candidate": null
  },
  {
    "id": "DIFFERENT_OBJECT",
    "stem": "Alimentarea motorului de 220(230) V se face:",
    "options": {
      "A": "dintr-un circuit de iluminat normal, dintr-un circuit de prize sau direct din tabloul de distribuție",
      "B": "numai dintr-un circuit de iluminat normal",
      "C": "numai dintr-un circuit de prize"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "I7-2011 §5.4.13",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "BLOCKED_OBJECT_OR_STEM",
    "candidate": null
  },
  {
    "id": "REVERSED_ABC",
    "stem": "Alimentarea transformatorului de sonerie sau soneriei de 220(230) V se face:  .",
    "options": {
      "A": "dintr-un circuit de iluminat normal",
      "B": "numai dintr-un circuit de prize",
      "C": "numai direct din tabloul de distribuţie"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "I7-2011 §5.4.13",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "ONE_VALID_EXAM_OPTION",
    "candidate": "A"
  },
  {
    "id": "MISLEADING_AND",
    "stem": "Alimentarea transformatorului de sonerie sau soneriei de 220(230) V se face:  .",
    "options": {
      "A": "dintr-un circuit de iluminat normal și dintr-un circuit de prize",
      "B": "numai dintr-un circuit de prize",
      "C": "numai direct din tabloul de distribuție"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "I7-2011 §5.4.13",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "MANUAL_REVIEW_UNKNOWN_OR_COMPLEX_OPTION",
    "candidate": null
  },
  {
    "id": "VALID_PLUS_DUPLICATE",
    "stem": "Alimentarea transformatorului de sonerie sau soneriei de 220(230) V se face:  .",
    "options": {
      "A": "dintr-un circuit de iluminat normal",
      "B": "direct din tabloul de distribuție",
      "C": "numai dintr-un circuit de prize"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "I7-2011 §5.4.13",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "MULTIPLE_VALID_OPTIONS",
    "candidate": null
  },
  {
    "id": "NEGATED_OPTION",
    "stem": "Alimentarea transformatorului de sonerie sau soneriei de 220(230) V se face:  .",
    "options": {
      "A": "nu dintr-un circuit de iluminat normal",
      "B": "dintr-un circuit de prize",
      "C": "numai direct din tabloul de distribuție"
    },
    "source": {
      "object": "doorbell_primary_supply",
      "locator": "I7-2011 §5.4.13",
      "allowed_routes": [
        "normal_lighting",
        "socket_circuit",
        "distribution_board"
      ],
      "source_uri": "https://legislatie.just.ro/Public/FormaPrintabila/00000G06RYEO88RN4ZO14S89GD4J90SH"
    },
    "expected": "MANUAL_REVIEW_UNKNOWN_OR_COMPLEX_OPTION",
    "candidate": null
  }
];
for(const c of cases){const v=classifyDoorbellOptions({question:c.stem,options:c.options,source:c.source});assert.equal(v.status,c.expected,c.id);assert.equal(v.candidate_letter,c.candidate,c.id);assert.equal(v.approved_for_learning,false,c.id);}
console.log(cases.length+' deterministic alternative-exclusivity fixtures pass (not independent source QA)');
