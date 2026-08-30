# Build Rules

## 1. Revenue-First Development
Every feature must tie directly to:

- P0,
- a live prospect,
- a production bug,
- a sales blocker,
- compliance.

## 2. Small Changes
Prefer one task = one coherent change.

Do not perform broad refactors while implementing unrelated functionality.

## 3. Test Every Functional Change
Minimum expectation:

- unit tests for state/qualification logic
- webhook tests
- duplicate/idempotency tests
- failure-path tests

## 4. Deterministic Before Agentic
Do not use an LLM for logic that can be represented safely and cheaply with rules/state.

## 5. No Hidden Business Logic in Prompts
Business-critical rules should live in code/configuration where possible.

## 6. Human Escalation Always Exists
If confidence is low, rules are unclear or a customer requests a human, escalate.

## 7. Never Invent
The system must not invent:

- price
- appointment availability
- guarantees
- regulatory claims
- technical diagnosis
- emergency advice beyond approved business text

## 8. Secrets
Use environment variables. Keep `.env` ignored.

## 9. Documentation Is Source of Truth
After material progress:

- update `CURRENT_STATE.md`
- update `NEXT_TASK.md`
- record major decisions in `DECISIONS.md`

## 10. Build Stop Rule
At end of Day 7, feature development stops except for bugs or sales-required changes.
