# AI Operating Model

## Purpose
Use ChatGPT, Cursor and Claude as complementary roles instead of three competing coders.

## Orchestration Rule
ChatGPT is the project orchestrator.

Each project day begins with ChatGPT. ChatGPT reads `docs/CURRENT_STATE.md`, `docs/NEXT_TASK.md` and the relevant daily plan, then:

1. states the day's objective,
2. assigns tasks to human / ChatGPT / Cursor / Claude,
3. defines the agent sequence and order,
4. writes handoff instructions for each step.

The user should not need to decide which agent acts next. Agents follow `docs/NEXT_TASK.md` unless ChatGPT updates it during the day.

## Role 1 — ChatGPT: Project Orchestrator / Lead / Research / Sales Strategy
Primary responsibilities:

- daily session orchestration and agent handoffs
- scope control
- current-market research
- product decisions
- prioritisation
- prospect scoring
- pricing
- outreach strategy
- objection analysis
- demo structure
- funnel diagnosis
- deciding whether a proposed feature advances revenue

ChatGPT should not routinely write large implementation patches when Cursor can work directly inside the repository.

### Typical ChatGPT question
“What is the highest-value next action toward the first paying client given CURRENT_STATE, NEXT_TASK and the latest sales evidence?”

## Role 2 — Cursor: Primary Builder
Primary responsibilities:

- implement scoped tasks
- write tests
- fix defects
- integrate APIs
- update schema/migrations
- maintain repo consistency

Before each task Cursor must read:

- `README.md`
- `docs/SCOPE.md`
- `docs/BUILD_RULES.md`
- `docs/CURRENT_STATE.md`
- `docs/NEXT_TASK.md`

Cursor must not add P1/P2 functionality unless the task explicitly satisfies the scope gate.

### Preferred task style
“Implement X according to the repo docs. Write tests. Do not modify unrelated code. Update CURRENT_STATE and NEXT_TASK.”

## Role 3 — Claude: Reviewer / Red Team
Primary responsibilities:

- code review
- architecture review
- security review
- edge cases
- test design
- adversarial conversation testing
- identifying hidden assumptions
- critiquing sales copy/offers when requested

Claude should review completed or proposed work rather than independently rebuild the same feature.

### Typical Claude task
“Review the current diff against SCOPE, BUILD_RULES and ARCHITECTURE. Find defects, unsafe assumptions, missing tests and unnecessary complexity. Rank findings by severity. Do not rewrite the entire system.”

## Default Workflow

```text
ChatGPT defines/validates next task
            |
            v
Cursor implements + tests
            |
            v
Claude reviews / attacks
            |
            v
Cursor fixes legitimate issues
            |
            v
ChatGPT checks business value / next priority
```

## Suggested Effort Split During Build Week

- Cursor: ~50%
- ChatGPT: ~30%
- Claude: ~20%

## Suggested Effort Split After Day 7

Human sales dominates.

- ChatGPT: sales/funnel/strategy
- Cursor: bugs only or prospect-required changes
- Claude: review/demo red-team only

## Shared Context Rule
The repository is the shared memory.

Do not rely on any model remembering unstored decisions.

If a decision matters tomorrow, put it in the repo.
