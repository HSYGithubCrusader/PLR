# Decision Log

Record important decisions chronologically.

## D-001 — Project success is revenue, not product completion
Status: Accepted

The first project ends successfully only when at least one customer has paid.

## D-002 — Initial niche is UK plumbing/heating
Status: Accepted

Focus on small domestic plumbing/heating companies, particularly firms exposed to missed inbound calls.

## D-003 — Product wedge is missed-lead recovery, not generic AI receptionist
Status: Accepted

Commodity receptionist products exist. We sell configuration, qualification, routing, follow-up, reporting and support tied to lead recovery.

## D-004 — Do not replace existing field-service software
Status: Accepted

The system should sit in front of ServiceM8/Tradify/Powered Now/etc. Integrations are deferred until justified by a live client.

## D-005 — Deterministic state machine first
Status: Accepted

Use LLM capabilities only where they materially improve messy-language understanding or bounded classification.

## D-006 — Production core should not assume centrally hosted n8n
Status: Accepted

n8n may be used for prototyping. Production direction is lightweight Python + PostgreSQL unless client-specific deployment/licensing justifies otherwise.

## D-007 — FastAPI for the initial Python web service
Status: Accepted

FastAPI chosen over Flask for the Day 1 repository baseline.

Reasoning:

- Architecture centres on Twilio webhooks and structured JSON payloads; FastAPI provides first-class request/response validation via Pydantic with minimal boilerplate.
- Built-in async support suits inbound webhook handling without adding framework complexity later.
- `TestClient` integrates cleanly with pytest for the Day 1 health-check test.
- Flask would be sufficient for a health endpoint alone but offers no advantage for the webhook-heavy path already specified.

Scope of this decision: framework choice and minimal app skeleton only. No Twilio, PostgreSQL, or product logic is introduced.

## D-008 — Day 2 calls are commercial discovery + validation
Status: Accepted

The Day 2 human-validation calls are **commercial discovery + validation**, not laboratory-style pure research.

The caller must be transparent that the research concerns a system being built for small plumbing businesses. Required opening:

> "Hi, I'm Francisco. I'm researching a system I'm building for small plumbing businesses around missed customer enquiries. Could I ask you one quick question about how you currently handle them?"

If organic interest develops, the caller may continue a commercial conversation. Do not force a pitch merely because the business answered.

Recorded in Human Validation Protocol V2 (`docs/HUMAN_VALIDATION_PROTOCOL.md`).
