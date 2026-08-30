# Next Task

## CURRENT DAY
1

## PROJECT DAY STATUS
NOT STARTED

## START WITH
ChatGPT

## TODAY'S OBJECTIVE
Freeze project scope and establish repository baseline.

## AGENT SEQUENCE
1. ChatGPT — lead session / decisions
2. Cursor — repository implementation
3. Claude — scope red-team
4. Cursor — approved corrections
5. ChatGPT — verify Day 1 completion

## DO NOT
- Begin Day 2
- Build product features
- Expand scope

---

## ChatGPT Handoff (Step 1)
Confirm Day 1 is aligned with `docs/30_DAY_PLAN.md` and `docs/SCOPE.md`. Record any final scope-freeze decisions in `docs/DECISIONS.md`. When ready, provide Cursor with the Step 2 handoff below.

## Cursor Handoff (Step 2)
Repository baseline only — not P0 product features.

1. Read all root/docs files.
2. Choose FastAPI or Flask for the initial Python service and record the decision in `docs/DECISIONS.md`.
3. Create the smallest runnable application skeleton under `/app`.
4. Create a test skeleton under `/tests`.
5. Confirm `.gitignore` covers Python, environment, IDE and secret exclusions.
6. Confirm `.env.example` contains names only, no secrets.
7. Add dependency configuration appropriate to the chosen Python workflow.
8. Add one health-check endpoint and one test proving it works.
9. Do not add Twilio, PostgreSQL or qualification implementation yet unless required merely to establish interfaces.
10. Update `docs/CURRENT_STATE.md` and set `PROJECT DAY STATUS` to reflect progress.

Do not replace this file until ChatGPT verifies Day 1 completion (Step 5).

## Claude Handoff (Step 3)
Review the Day 1 diff against `docs/SCOPE.md`, `docs/BUILD_RULES.md` and `docs/ARCHITECTURE.md`. Red-team for scope creep, missing tests, and unnecessary complexity. Rank findings by severity. Do not rewrite the application.

## Cursor Handoff (Step 4)
Apply only approved corrections from Claude's review. No new features.

## ChatGPT Handoff (Step 5)
Verify Day 1 definition of done. Update `docs/CURRENT_STATE.md`. Replace this file with Day 2 tasking (customer research) or adjust sequencing per `docs/30_DAY_PLAN.md`.

## Definition of Done
- scope frozen and recorded
- local app starts
- health endpoint responds
- test suite runs
- no secrets committed
- decision log updated
- current state updated
- Claude review completed
- next task points to Day 2 customer research or Day 3 telephony foundation depending on project sequencing
