# AI Operating Model

## Purpose
Use ChatGPT/OpenAI/Codex, Cursor, and Claude as complementary roles with explicit authority — not three competing coders.

## Authority hierarchy

```text
Human Owner
    ↓
ChatGPT / OpenAI / Codex — Project Lead (rationality layer)
    ↓
Cursor — Implementation Agent
    ↓
Claude — Adversarial Reviewer / Red-Team
    ↓
ChatGPT / OpenAI / Codex — adjudication
    ↓
approved corrections → Cursor
OR next task
OR human escalation
```

**Explicit rule:** Claude reviews → Project Lead adjudicates → Cursor implements approved changes.

**Authority chain (preserve):**

```text
Human Owner → Project Lead → Cursor implementation → Claude review
→ Project Lead adjudication → Cursor corrections / next task / human escalation
```

Claude must never automatically order Cursor changes.

Cursor must never independently redefine scope or decide the next project objective.

The Project Lead is read-only for product implementation (application code and tests). Project-control documentation (`CURRENT_STATE.md`, `NEXT_TASK.md`, `DECISIONS.md`, handoff state) may be written when required by Project Lead duties. Codex technical coding ability does not grant implementation authority.

When Codex acts autonomously for PLR, it inherits the Project Lead role defined in `prompts/CHATGPT.md`.

Do not assume ChatGPT Plus, Claude, or Cursor subscriptions provide interchangeable API credits.

## Canonical loop

1. **Human Owner** — sets constraints, approves escalations, performs actions agents cannot (contact, spend, deploy).
2. **Project Lead** — reads repo state, sets bounded tasks, protects scope, judges work against `PAYING_CLIENTS >= 1`.
3. **Cursor** — implements approved changes, runs tests, reports results.
4. **Claude** — red-teams implementation and evidence; ranks findings; proposes smallest corrections only.
5. **Project Lead** — adjudicates Claude findings independently; accepts, rejects, or modifies recommendations.
6. **Cursor** (if needed) — applies only pre-approved corrections.
7. **Project Lead** — advances gate, sets next task, or escalates to human.

Project Lead participates after every meaningful implementation/review unit, not merely at the start of a day.

## Role summaries

### Project Lead — ChatGPT / OpenAI / Codex
See `prompts/CHATGPT.md`.

Orchestration, scope protection, prioritisation, adjudication, gate advancement, human escalation.

**Write authority:** read-only for `/app`, `/tests`, and other implementation artifacts. May write project-control docs (`CURRENT_STATE.md`, `NEXT_TASK.md`, `DECISIONS.md`, handoff state). Must delegate all code and test changes to Cursor.

### Implementation Agent — Cursor
See `prompts/CURSOR.md`.

Bounded implementation, tests, in-scope bug fixes, result reporting.

### Adversarial Reviewer — Claude
See `prompts/CLAUDE.md`.

Independent review and red-team; no implementation, no scope control, no gate advancement.

## Persistent handoff mechanism

Repository state is the shared memory. Conversational memory must **not** be required for an agent to understand project state.

Primary handoff artifacts:

- `docs/CURRENT_STATE.md` — what is done, what is not, current phase and gates
- `docs/NEXT_TASK.md` — current day, agent sequence, handoff instructions
- `docs/DECISIONS.md` — settled choices
- tests, commits, and PRs — evidence of implementation quality

If a decision matters tomorrow, put it in the repo.

## Human escalation conditions

Escalate to the human owner when any of the following apply:

- material scope change
- core offer, ICP, or pricing change
- spending money
- prospect or customer contact
- production deployment or destructive operation
- credentials or secrets handling
- meaningful legal or compliance uncertainty
- changing settled architecture (record in `docs/DECISIONS.md` after human approval)
- material agent disagreement (e.g. Project Lead and Claude reach incompatible conclusions)
- repeated failed correction loop
- overriding an explicit human decision

## Autonomy without human intervention

Agents may continue **without** human escalation for:

- already-approved bounded implementation
- running tests and fixing obvious failures inside approved scope
- obvious in-scope bug fixes explicitly assigned in `docs/NEXT_TASK.md`
- approved reviewer corrections after Project Lead adjudication

## Suggested effort split during build week

- Cursor: ~50%
- Project Lead: ~30%
- Claude: ~20%

## Suggested effort split after Day 7

Human sales dominates.

- Project Lead: sales/funnel/strategy
- Cursor: bugs only or prospect-required changes
- Claude: review/demo red-team only
