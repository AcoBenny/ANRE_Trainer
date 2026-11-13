// Synthetic prototype: exact table row before comparing units/material. Never a source validation.
function normalizeRo(s){return String(s??"").normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase().replaceAll("²","2").replace(/\s+/g," ").trim();}

export function exactTableMinimum({question,options,table}){
 const out=(status,detail={})=>({status,candidate_letter:null,approved_for_learning:false,source_edition_verified:false,independent_QA:"NOT_RUN",...detail});
 if(!table?.source_locator||!Array.isArray(table.rows)||table.rows.length===0)return out("BLOCKED_SOURCE_TABLE_MISSING");
 const q=normalizeRo(question), matches=table.rows.filter(r=>q.includes(normalizeRo(r.question_scope)));
 if(matches.length!==1)return out("SOURCE_OBJECT_MAPPING_REQUIRED",{matched_rows:matches.map(x=>x.row_id)});
 if(Object.keys(options??{}).sort().join(",")!=="A,B,C")return out("BLOCKED_OPTIONS");
 const row=matches[0], classifications=Object.entries(options).map(([letter,option])=>{
  const regex=/(\d+(?:[.,]\d+)?)\s*mm2\s*(cupru|aluminiu)/g;
  const mentions=[...normalizeRo(option).matchAll(regex)].map(m=>({value:Number(m[1].replace(",",".")),material:m[2]}));
  if(mentions.length===0)return {letter,classification:"NO_PARSEABLE_MATERIAL_SECTION"};
  const tests=mentions.map(({value,material})=>{
   const min=row.minimums[material];
   if(min===null||min===undefined)return {material,value,status:"NOT_SPECIFIED_IN_SOURCE_ROW"};
   if(Math.abs(value-min)<1e-9)return {material,value,status:"MATCH"};
   return {material,value,status:"WRONG_ROW_MINIMUM"};
  });
  return {letter,classification:tests.every(t=>t.status==="MATCH")?"EXACT_ROW_MINIMUM":tests.some(t=>t.status==="NOT_SPECIFIED_IN_SOURCE_ROW")?"MATERIAL_NOT_SPECIFIED_ON_THIS_ROW":"WRONG_VALUE_FOR_THIS_ROW",tests};
 });
 const good=classifications.filter(x=>x.classification==="EXACT_ROW_MINIMUM");
 if(good.length===1)return out("ONE_ROW_SPECIFIC_CANDIDATE",{candidate_letter:good[0].letter,row_id:row.row_id,option_audit:classifications});
 if(good.length>1)return out("MULTIPLE_ROW_SPECIFIC_CANDIDATES",{row_id:row.row_id,option_audit:classifications});
 return out("NO_ROW_SPECIFIC_OPTION",{row_id:row.row_id,option_audit:classifications});
}
