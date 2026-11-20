# ANRE Academy: Cloudflare AI Gateway + GitHub App (pilot, not deployed)

This integration is an **event-driven GitHub App webhook receiver**, not a manually dispatched GitHub Actions workflow. A Cloudflare Worker accepts signed GitHub `issues.labeled` webhooks and runs a small **read-only** benchmark on the six pre-registered CKPT-256 negative fixtures. It never changes question stems, A/B/C choices, answers, HTML, APK, or PR #7.

## What is actually implemented

- Receives `POST /github/webhook`; validates GitHub's HMAC-SHA256 signature, repository name, issue event, and exact `academy-pilot` label.
- **Disabled by default**: `PILOT_ENABLED=false` results in **zero AI requests**.
- When separately enabled, reads the existing six-fixture JSON from the ANRE audit branch, makes **at most six** AI Gateway calls, and stores unreviewed text and actual usage metadata in a Cloudflare KV report for seven days.
- Uses the fixed Cloudflare dynamic route `dynamic/academy-free-only`; it cannot independently prove that models behind that route are free. The Cloudflare dashboard must enforce *only approved free-tier BYOK providers* and **zero paid fallback**.
- Read-only result retrieval at `GET /reports/{github-delivery-id}`, requiring the separate `REPORT_TOKEN` secret.
- Requests are only evidence for Academy model evaluations. They **are not** qualified independent QA, training model weights, proof of source validity, or ANRE answer approval.

**Not yet completed:** GitHub App registration/installation, Cloudflare account and Worker deployment, gateway route/provider setup, live API testing, reliable scheduling, QA of responses. No independent model has been run by this PR.

## Activation steps (manual initial setup, automatic thereafter)

1. In [Cloudflare dashboard](https://dash.cloudflare.com/), create an AI Gateway named `anre-academy` and a dynamic route named exactly `academy-free-only`. Add only free-tier BYOK provider credentials whose *actual* current quotas are confirmed in your accounts. Configure rate limits, failover on provider 429/5xx, **no paid provider and no Unified Billing paid fallback**. Verify the deployed route version before turning on pilot.
2. Create a Cloudflare KV namespace for reports and deploy the Worker (copy `wrangler.toml.example` to `wrangler.toml`, replace the KV ID, authenticate Wrangler, then run `npx wrangler deploy`). Leave `PILOT_ENABLED=false`.
3. Set **Cloudflare Worker secrets**, not GitHub repository secrets: `GITHUB_WEBHOOK_SECRET` (random shared secret with GitHub App), `CF_API_TOKEN` (Cloudflare API token with the least permissions required for the AI REST API), and `REPORT_TOKEN` (separate strong random token). Set nonsecret vars `CF_ACCOUNT_ID` and `CF_GATEWAY_ID=anre-academy`. `CF_API_TOKEN` belongs to your Cloudflare account; provider API keys should be stored in Cloudflare BYOK where supported, not in code.
4. Under [GitHub Developer Settings: Apps](https://github.com/settings/apps), create a **private GitHub App** with webhooks enabled and URL `https://<your-worker>.workers.dev/github/webhook`. Set its webhook secret to the same value used by the Worker. Grant only **Issues: read** repository permission, subscribe to **Issues** events, then install the App for **ANRE_Trainer only**. No contents-write, secrets access, or repository permissions to modify answers.
5. After checking webhook signature tests, KV, quotas, and provider route, turn on `PILOT_ENABLED=true` in the Cloudflare Worker environment and add the `academy-pilot` label to a dedicated GitHub issue. This creates an event automatically, without manually launching a workflow. The GitHub App webhook deliveries page shows the delivery ID. Use that ID with the authenticated report endpoint.
6. Review outputs **independently** against actual primary sources, then decide whether to expand beyond the initial six fixtures.

## Limits and important security constraints

- Never send the actual API keys in GitHub issues, chats, screenshots, or commits.
- Cloudflare route switching responds to configured errors/limits, **not necessarily** to the upstream provider's remaining free-token balance. The route cannot guarantee zero spend if a paid model or billing path is configured accidentally.
- Cloudflare Workers `ctx.waitUntil` is short-lived and KV writes are not atomic. Retries or simultaneous duplicate deliveries could cause repeated calls; production use requires an atomic queue/lock (Durable Objects, Cloudflare Workflows, or equivalent) and a persisted usage budget.
- The six fixture records are challenge prompts, **not the full original QABC or source excerpts**. Passing them cannot certify any ANRE question or provide independent source review.
- No background worker runs merely because these source files exist in GitHub. You must configure the external Cloudflare account and GitHub App.
- Tests: `node --test integrations/academy-cloudflare/test/*.test.mjs` (Node 20+). Only synthetic, offline tests; never label a live integration verified until a signed event and genuine model call have been observed.
- Keep PR #7 Draft; no merge, no release, no automatic edits to ANRE source material.

Official references: [GitHub Apps and webhooks](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps), [GitHub webhook signature validation](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries), [Cloudflare dynamic routes](https://developers.cloudflare.com/ai-gateway/features/routing/dynamic-routing/), [Cloudflare dynamic route usage](https://developers.cloudflare.com/ai-gateway/features/routing/dynamic-routing/usage/), [Cloudflare AI REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/).
