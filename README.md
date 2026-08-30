# Plumber Lead Recovery — First Paying Client Project

## Mission
Build and sell a simple missed-lead recovery system to at least one UK plumbing/heating company within 30 days.

This repository is organised around one rule:

> Revenue is the project. Software is only a means to that end.

## Agent Orchestration Rule

**ChatGPT is the project orchestrator.**

The user begins each project day with ChatGPT. ChatGPT reads the current repository state and daily plan, breaks the day's objective into human / ChatGPT / Cursor / Claude tasks, determines the order in which agents are used, and provides handoff instructions.

The user should not need to independently determine which agent handles the next task. Follow `docs/NEXT_TASK.md` for the current day, status, and agent sequence.

## Start Here
Read these files in order before making any material change:

1. `docs/PROJECT.md`
2. `docs/SCOPE.md`
3. `docs/ARCHITECTURE.md`
4. `docs/BUILD_RULES.md`
5. `docs/AI_OPERATING_MODEL.md`
6. `docs/SALES_PLAYBOOK.md`
7. `docs/PROSPECTING.md`
8. `docs/MARKET_AND_SOFTWARE.md`
9. `docs/COMPLIANCE.md`
10. `docs/30_DAY_PLAN.md`
11. `docs/DAILY_OPERATING_RULE.md`
12. `docs/DECISIONS.md`
13. `docs/CURRENT_STATE.md`
14. `docs/NEXT_TASK.md`

## Mandatory Build Behaviour
Before coding, every AI or human contributor must:

1. Read `docs/CURRENT_STATE.md` and `docs/NEXT_TASK.md`.
2. Check the requested work against `docs/SCOPE.md`.
3. Reject or defer work that is not required for P0, a live prospect, or a demonstrated sales blocker.
4. Make the smallest coherent change that advances the current task.
5. Add or update tests for any functional change.
6. Update `docs/CURRENT_STATE.md` after meaningful progress.
7. Record irreversible or important choices in `docs/DECISIONS.md`.
8. Follow the `AGENT SEQUENCE` in `docs/NEXT_TASK.md`. ChatGPT closes each project day and replaces `docs/NEXT_TASK.md` with the next day's tasking.

## Repository Shape

```text
/app        Production application code
/tests      Automated tests
/scripts    Local/dev/admin scripts
/docs       Product, project, sales and operating truth
/prompts    Reusable prompts for ChatGPT, Claude and Cursor
```

Do not create additional top-level directories unless there is a concrete need.

## Prospect Tracker
`prospects.csv.example` is the committed template (header/schema only). Copy it to `prospects.csv` for local prospect data. The real `prospects.csv` is local-only and must not be committed.

Field definitions for `online_booking`, receptionist penalty, and `owner_answers_calls` are in `docs/PROSPECTING.md`.

## Technology Direction
Initial production direction:

- Python
- PostgreSQL
- Twilio for phone/SMS integration
- Lightweight web service
- Deterministic state machine first
- LLM API only where it materially improves understanding
- n8n allowed for prototyping, not assumed as the commercial production core

## Definition of Success

```text
PAYING_CLIENTS >= 1 within 30 days
```

Secondary operating targets are documented in `docs/PROJECT.md`.

## Anti-Scope-Creep Rule
After Day 7, no development task should be accepted unless the answer to this question is clear:

> Which current prospect, production failure, or demonstrated sales blocker requires this?

If the answer is “none”, do not build it.
