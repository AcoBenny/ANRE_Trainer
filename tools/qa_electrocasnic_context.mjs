// ANRE Academy source-context candidate classifier v1. Narrow semantics ONLY.
// Never certifies normative edition, installation design, or learner answers.
const normalize = s=>String(s??"").normalize("NFD").replace(/[\u0300-\u036f]/g,"").replaceAll("²","2").toLowerCase().replace(/\s+/g," ").trim();
export function contextFromDomesticAppliance({question,options,source}){
 const result=(status,context,more={})=>({status,context,candidate_letter:null,approved_for_learning:false,independent_QA:"NOT_RUN",normative_edition_certified:false,flags:[],...more});
 if(!source||source.section!=="5.4.7"||source.table!=="5.32"||source.minimum_socket_cu_mm2!==2.5) return result("BLOCKED_EXACT_NORM_SOURCE","unknown");
 const q=normalize(question);
 if(!/\belectrocasnic\b/.test(q)||!/\bmonofazat\b/.test(q)||!/\bpeste\s*2(?:[.,]0+)?\s*kw\b/.test(q))return result("NOT_TARGET_SEMANTIC_CASE","unknown");
 if(/\b(?:racordare directa|alimentare fixa|conectare fixa|hardwired)\b/.test(q))return result("NO_AUTOMATIC_SOCKET_MAPPING","fixed_connection",{flags:["DOMESTIC_APPLIANCE_NOT_NECESSARILY_SOCKET"]});
 if(/\b(?:industrial|atelier industrial)\b/.test(q))return result("BLOCKED_SCOPE_MISMATCH","non_dwelling");
 const socketExplicit=/\b(?:priza|prize|locuinta|locuinte)\b/.test(q);
 if(Object.keys(options??{}).sort().join(",")!=="A,B,C") return result("BLOCKED_OPTIONS","unknown");
 const numWithMaterial=s=>[...normalize(s).matchAll(/(\d+(?:[.,]\d+)?)\s*mm2\s*(cupru|aluminiu)/g)].map(x=>({mm2:Number(x[1].replace(",",".")),material:x[2]}));
 const inspected=Object.entries(options).map(([letter,value])=>({letter,tokens:numWithMaterial(value)}));
 const matches=inspected.filter(x=>x.tokens.length===1&&x.tokens[0].material==="cupru"&&x.tokens[0].mm2===2.5);
 if(matches.length!==1)return result("OPTIONS_NEED_MANUAL_REVIEW",socketExplicit?"explicit_socket":"inferred_from_examples",{flags:["NO_UNIQUE_EXACT_SOCKET_CU_OPTION"]});
 return result(socketExplicit?"CANDIDATE_EXPLICIT_SOCKET_CONTEXT":"CANDIDATE_INFERRED_DOMESTIC_SOCKET_CONTEXT",socketExplicit?"explicit_socket":"inferred_from_electrocasnic_gt2kw",{candidate_letter:matches[0].letter,flags:[...(socketExplicit?[]:["INFERRED_NOT_LOGICALLY_FORCED"]), "MINIMUM_NORMATIVE_NOT_CABLE_POWER_RATING", "ACTUAL_CABLE_SIZING_REQUIRED"]});
}
