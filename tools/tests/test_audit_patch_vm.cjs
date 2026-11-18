'use strict';
// ANRE audit_patch.js Node VM regression. Uses actual repo script, simulated DOM.
// Run: node tools/tests/test_audit_patch_vm.cjs
// Negative gate: ANRE_NEGATIVE_NO_SIGNATURE_GUARD=1 node tools/tests/test_audit_patch_vm.cjs
// This is NOT a real Chromium, Android, or full HTML app test.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const crypto = require('node:crypto');
const path = require('node:path');

const source = fs.readFileSync(path.resolve(__dirname, '../../app/src/main/assets/audit_patch.js'), 'utf8');
const script = process.env.ANRE_NEGATIVE_NO_SIGNATURE_GUARD === '1'
  ? source.replace('if(old&&signature===lastSignature)return;', '') : source;
const blobSHA = crypto.createHash('sha1').update('blob ' + Buffer.byteLength(source) + '\0').update(source).digest('hex');
const tasks = [];
const metrics = {inserts: 0, removes: 0, callbacks: 0, dispatched: 0, maxQueue: 0};
let observerCallback = null;
let auditBox = null;
const notify = () => {
  if (observerCallback) {
    metrics.callbacks++;
    observerCallback([{type:'childList'}]);
  }
};
const makeText = initial => {
  let value = initial;
  return {get textContent() {return value}, set textContent(v) {value=String(v); notify()}};
};
const grade = makeText('G1-LEG-025');
const meta = makeText('PRELIMINARY');
const q = makeText('Sursele se supun supun verificării?');
const answer = makeText('se supun supun');
const container = {insertBefore(box) {auditBox = box;metrics.inserts++;notify()}};
q.parentNode=container;
const document = {
  body:{},
  querySelector(selector) {return selector==='.q'?q:null},
  querySelectorAll(selector) {
    if(selector==='.meta .pill')return [grade,meta];
    if(selector==='.answer')return [answer];
    return [];
  },
  getElementById(id) {return id==='audit-runtime'?auditBox:null},
  createElement(tag) {
    assert.equal(tag,'div');
    return {style:{},id:'',className:'',innerHTML:'',remove() {
      if(auditBox===this) {auditBox=null;metrics.removes++;notify()}
    }};
  }
};
const sandbox = {
  document,
  MutationObserver: class {
    constructor(fn){observerCallback=fn}
    observe(body,options){assert.equal(body,document.body);assert.equal(options.subtree,true)}
  },
  setTimeout: fn => {tasks.push(fn);metrics.maxQueue=Math.max(metrics.maxQueue,tasks.length)}
};
function drain() {
  let count=0;
  while(tasks.length) {
    if(count++>60)throw new Error('SELF-SCHEDULING MUTATION LOOP: >60 dispatched callbacks');
    const task=tasks.shift();task();metrics.dispatched++;
  }
}
const tests={};
function check(name,fn){fn();tests[name]='PASS'}
vm.runInNewContext(script,sandbox,{filename:'audit_patch.js',timeout:1500});
check('initial_typo_corrected_only_in_display',()=>{
  drain();assert.equal(q.textContent,'Sursele se supun verificării?');
  assert.equal(answer.textContent,'se supun');
  assert.equal(metrics.inserts,1);assert.equal(metrics.removes,0);
  assert.ok(auditBox.innerHTML.includes('Cross-reference tehnic'));
});
check('observer_settles_without_extra_redraw',()=>{
  notify();drain();assert.equal(metrics.inserts,1);
});
check('navigation_one_redraw_and_linguistic_markers',()=>{
  grade.textContent='G1-LEG-026';
  q.textContent='În cazul testului nu este doar o regulă';
  drain();
  assert.equal(metrics.inserts,2);assert.equal(metrics.removes,1);
  assert.ok(auditBox.innerHTML.includes('negație'));
  assert.ok(auditBox.innerHTML.includes('termen de exclusivitate'));
});
check('metadata_status_change_one_redraw',()=>{
  meta.textContent='VERIFIED';drain();
  assert.equal(metrics.inserts,3);assert.equal(metrics.removes,2);
  assert.ok(auditBox.className.includes('audit-official'));
});
check('identical_text_change_does_not_redraw',()=>{
  const n=metrics.inserts;q.textContent=q.textContent;drain();
  assert.equal(metrics.inserts,n);
});
check('another_question_typo_fix_and_idempotence',()=>{
  grade.textContent='G1-ELE-028';
  meta.textContent='PRELIMINARY';
  q.textContent='Este scurtcirciut la toate cazurile';
  drain();
  assert.equal(q.textContent,'Este scurtcircuit la toate cazurile');
  assert.equal(metrics.inserts,4);
  const n=metrics.inserts;notify();drain();assert.equal(metrics.inserts,n);
});
check('negative_status_must_not_look_official',()=>{
  for(const label of ['NOT_VERIFIED','UNVERIFIED','VERIFIED_PENDING','NOT VERIFIED']) {
    meta.textContent=label;drain();
    assert.ok(!auditBox.className.includes('audit-official'),label+' must not be official');
  }
});
check('explicit_verified_and_i7_tags_still_recognized',()=>{
  for(const label of ['VERIFIED','VERIFICAT CU I7','DOCUMENTAR OFICIAL ANRE']) {
    meta.textContent=label;drain();
    assert.ok(auditBox.className.includes('audit-official'),label+' must be recognized');
  }
});
console.log(JSON.stringify({passed:true,test_count:Object.keys(tests).length,tests,
  source_blob_sha:blobSHA,stats:metrics,
  scope:'actual JS in Node VM simulated DOM/MutationObserver; NOT real browser/APK'},null,2));
