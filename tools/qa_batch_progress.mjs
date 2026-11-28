// Read-only end-of-batch progress gate for ANRE / Avengers Asamble.
// No legal-source, official-key, human reviewer or UI-runtime authentication.
import {readFileSync,writeFileSync} from "node:fs";
import {pathToFileURL} from "node:url";
export const DEFAULT_STAGES = Object.freeze(["BACKLOG","TRIAGED","SOURCE_RESEARCHED","REVIEW_READY","INDEPENDENTLY_REVIEWED","APPROVED","INTEGRATED","QA_PASSED"]);
function fail(message){throw new Error(`INVALID_BATCH: ${message}`);}
function nonEmpty(value,label){if(typeof value!=='string'||!value.trim())fail(label);return value.trim();}
function uniqueStrings(xs,label){if(!Array.isArray(xs))fail(`${label} must be array`);const c=xs.map((x,i)=>nonEmpty(x,`${label}[${i}]`));if(new Set(c).size!==c.length)fail(`${label} contains duplicates`);return c;}
function state(value,name,stages){if(!value||typeof value!=='object'||!Array.isArray(value.items))fail(`${name}.items`);const m=new Map();for(const [i,item] of value.items.entries()){if(!item||typeof item!=='object')fail(`${name}.items[${i}]`);const id=nonEmpty(item.id,`${name}.items[${i}].id`),stage=nonEmpty(item.stage,`${name}.${id}.stage`);if(!stages.includes(stage))fail(`${name}.${id}: unknown stage ${stage}`);if(m.has(id))fail(`${name}: duplicate item id ${id}`);m.set(id,{id,stage,gates:uniqueStrings(item.open_gates??[],`${name}.${id}.open_gates`),refs:uniqueStrings(item.evidence_refs??[],`${name}.${id}.evidence_refs`),approval:item.approval??null});}return m;}
function stats(items){let g=0,a=0,r=0;for(const x of items.values()){g+=x.gates.length;if(['APPROVED','INTEGRATED','QA_PASSED'].includes(x.stage))a++;if(x.stage==='REVIEW_READY')r++;}return {items:items.size,open_gates:g,approved:a,review_ready:r};}
function proofGate(now,old,id){return now.refs.some(ref=>!old?.refs.includes(ref))?null:`${id}: no new per-item evidence_refs`;}
export function evaluateBatch(batch){
 if(!batch||typeof batch!=='object')fail('input must be object');
 const batchId=nonEmpty(batch.batch_id,'batch_id'),taskId=nonEmpty(batch.task_id,'task_id'),project=nonEmpty(batch.project,'project'),stages=uniqueStrings(batch.stage_order??DEFAULT_STAGES,'stage_order');
 if(stages.length<3)fail('stage_order needs >=3 states');
 const before=state(batch.before,'before',stages),after=state(batch.after,'after',stages);
 const advanced=[],gateClosed=[],newItems=[],regressions=[],claimErrors=[],evidenceOnly=[];
 for(const [id] of before)if(!after.has(id))regressions.push(`${id}: item disappeared`);
 for(const [id,now] of after){
  const old=before.get(id);
  if(!old){if(stages.indexOf(now.stage)>0){const error=proofGate(now,null,id);if(error)claimErrors.push(error);else newItems.push(id);}continue;}
  const from=stages.indexOf(old.stage),to=stages.indexOf(now.stage),closing=old.gates.filter(g=>!now.gates.includes(g)),reopened=now.gates.filter(g=>!old.gates.includes(g));
  if(to<from)regressions.push(`${id}: stage fell ${old.stage} -> ${now.stage}`);
  if(reopened.length)regressions.push(`${id}: gates newly opened [${reopened.join(', ')}]`);
  if(to>from||closing.length){const error=proofGate(now,old,id);if(error)claimErrors.push(error);else{if(to>from)advanced.push({id,from:old.stage,to:now.stage});if(closing.length)gateClosed.push({id,gates:closing});}}
  else if(now.refs.some(ref=>!old.refs.includes(ref)))evidenceOnly.push(id);
 }
 for(const [id,now] of after){
  if(!['APPROVED','INTEGRATED','QA_PASSED'].includes(now.stage))continue;
  const approval=now.approval;
  if(!approval||approval.independent!==true||!approval.reviewer_ref||!approval.decision_ref)claimErrors.push(`${id}: approval lacks independently reviewable reviewer_ref/decision_ref`);
  if(project.toUpperCase().includes('ANRE')&&(!approval?.exam_key_authentication_ref||approval?.edition_verified!==true))claimErrors.push(`${id}: ANRE approval lacks exam-key authentication and edition verification`);
 }
 const progressIds=new Set([...advanced.map(x=>x.id),...gateClosed.map(x=>x.id),...newItems]);
 const verdict=claimErrors.length?'INVALID_PROGRESS_CLAIM':regressions.length?'REGRESSION':progressIds.size?'PROGRESSED':'NO_PROGRESS_REPEAT';
 const action={INVALID_PROGRESS_CLAIM:'CORRECT_BATCH_EVIDENCE_BEFORE_CONTINUING',REGRESSION:'INVESTIGATE_AND_RECONCILE',PROGRESSED:'CONTINUE_NEXT_UNFINISHED_BATCH',NO_PROGRESS_REPEAT:'STOP_REPEAT_AND_PIVOT_OR_ESCALATE'}[verdict];
 return {schema:'batch_progress_result_v1',project,batch_id:batchId,task_id:taskId,verdict,action,counts:{before:stats(before),after:stats(after)},delta:{distinct_items_advanced:progressIds.size,stage_transitions:advanced,closed_gates:gateClosed,new_processed_items:newItems,evidence_only_items:evidenceOnly,regression_reasons:regressions,invalid_progress_claims:claimErrors},audit_notice:'Structural preflight only. Does not independently verify technical truth, official exam keys, reviewer identity or HTML/APK runtime.'};
}
if(process.argv[1] && import.meta.url===pathToFileURL(process.argv[1]).href){
 const p=process.argv[2];if(!p){console.error("Usage: node tools/qa_batch_progress.mjs batch.json [report.json]");process.exit(2);}
 try{const result=evaluateBatch(JSON.parse(readFileSync(p,"utf8")));const txt=JSON.stringify(result,null,2)+"\n";if(process.argv[3])writeFileSync(process.argv[3],txt);process.stdout.write(txt);process.exit(result.verdict==="PROGRESSED"?0:1);}
 catch(err){console.error(err.message);process.exit(2);}
}
