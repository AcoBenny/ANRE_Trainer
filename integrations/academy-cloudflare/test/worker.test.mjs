import test from "node:test";
import assert from "node:assert/strict";
import { webcrypto } from "node:crypto";
import worker, { validGithubSignature } from "../worker.mjs";

if (!globalThis.crypto) globalThis.crypto = webcrypto;
const secret = "offline-test-secret-strong-value";
const enc = new TextEncoder();
const body = JSON.stringify({
  action: "labeled", label: { name: "academy-pilot" },
  repository: { full_name: "AcoBenny/ANRE_Trainer" },
  issue: { number: 81 }
});

async function signedRequest(content = body, extraHeaders = {}) {
  const key = await crypto.subtle.importKey(
    "raw", enc.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]
  );
  const mac = new Uint8Array(await crypto.subtle.sign("HMAC", key, enc.encode(content)));
  const signature = "sha256=" + Array.from(mac, x => x.toString(16).padStart(2, "0")).join("");
  return new Request("https://academy.example.test/github/webhook", {
    method: "POST",
    headers: {
      "x-hub-signature-256": signature, "x-github-event": "issues",
      "x-github-delivery": "offline-test-delivery-01", ...extraHeaders
    },
    body: content
  });
}

test("valid GitHub signatures accepted; tampered body refused", async () => {
  const req = await signedRequest();
  assert.equal(await validGithubSignature(body, req.headers.get("x-hub-signature-256"), secret), true);
  assert.equal(await validGithubSignature(body + "x", req.headers.get("x-hub-signature-256"), secret), false);
  assert.equal(await validGithubSignature(body, "sha256=bad", secret), false);
});

test("missing signature rejected without AI calls", async () => {
  const response = await worker.fetch(new Request("https://academy.example.test/github/webhook", {
    method: "POST", body
  }), { GITHUB_WEBHOOK_SECRET: secret }, {});
  assert.equal(response.status, 401);
});

test("valid event remains inert while pilot is disabled", async () => {
  let jobs = 0;
  const response = await worker.fetch(await signedRequest(), {
    GITHUB_WEBHOOK_SECRET: secret, PILOT_ENABLED: "false"
  }, { waitUntil() { jobs++; } });
  assert.equal(response.status, 202);
  assert.equal((await response.json()).model_calls, 0);
  assert.equal(jobs, 0);
});

test("other repositories cannot start the pilot", async () => {
  const payload = JSON.stringify({
    action: "labeled", label: { name: "academy-pilot" },
    repository: { full_name: "someone/other" }, issue: { number: 1 }
  });
  const response = await worker.fetch(await signedRequest(payload), {
    GITHUB_WEBHOOK_SECRET: secret, PILOT_ENABLED: "true"
  }, { waitUntil() { throw Error("must not run"); } });
  assert.equal((await response.json()).status, "ignored");
});

test("report endpoint requires its own secret", async () => {
  const response = await worker.fetch(
    new Request("https://academy.example.test/reports/delivery-12345678"),
    { REPORT_TOKEN: "report-token" }, {}
  );
  assert.equal(response.status, 401);
});

test("health check does not start AI requests", async () => {
  const response = await worker.fetch(
    new Request("https://academy.example.test/health"),
    { PILOT_ENABLED: "false" }, {}
  );
  assert.equal(response.status, 200);
  assert.equal((await response.json()).model_calls_made_by_health, 0);
});
