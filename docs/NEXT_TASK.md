# Next Task

## CURRENT DAY
2

## PROJECT DAY STATUS
IN PROGRESS

## START WITH
Human Owner (execute Human Validation Protocol V2)

## TODAY'S OBJECTIVE
Model the customer — build an evidence-backed ICP from real UK plumbing/heating businesses.

## COMPLETED
- research completed: **40** UK plumbing/heating businesses (not 20)
- ICP signals and software clues recorded in local `prospects.csv`
- prospects scored and tiered (A/B/C)
- Claude ICP evidence review: **PASS WITH CORRECTIONS**
- approved corrections applied to local tracker and prospecting documentation
- Human Validation Protocol V1 drafted
- Claude protocol adversarial review: **PASS WITH CORRECTIONS**
- Project Lead adjudication complete
- **Human Validation Protocol V2 frozen** — approved for Human Owner execution (`docs/HUMAN_VALIDATION_PROTOCOL.md`)

## NEXT GATE
Human Owner executes Day 2 Commercial Discovery + Missed-Call Validation Protocol V2 on the six-business cohort. After execution, return to **Project Lead** for final Day 2 verification. **Day 3 not started.**

## HUMAN-VALIDATION COHORT (order)
1. PJS Plumbing & Heating Services
2. T.H.Williams Plumbing and Heating Ltd
3. Heat365
4. John The Plumber
5. RM Plumbing & Electrical Ltd
6. Matt Plumbing & Heating

Cohort preserved unless compliance screening makes an individual business ineligible.

## AGENT SEQUENCE
1. ChatGPT — lead session / research plan — **DONE**
2. ChatGPT + Human — customer research and prospect logging — **DONE**
3. Claude — ICP evidence red-team — **DONE (PASS WITH CORRECTIONS)**
4. Cursor — approved corrections — **DONE**
5. ChatGPT — technical verification of research/review — **DONE**
5b. Cursor — draft Human Validation Protocol V1 — **DONE**
5c. Claude — protocol adversarial review — **DONE (PASS WITH CORRECTIONS)**
5d. Project Lead — adjudicate protocol findings — **DONE**
5e. Cursor — freeze Human Validation Protocol V2 — **DONE**
6. Human Owner — execute Protocol V2 on cohort — **NEXT**
7. Project Lead — final Day 2 verification — **AFTER human execution**

## DO NOT
- Begin Day 3 (telephony skeleton)
- Build product features
- Expand scope
- Commit local `prospects.csv` or `suppression.csv` (local-only data; must never be committed)
- Replace this file with Day 3 tasking until Project Lead completes final Day 2 closeout

---

## Human Owner Handoff (Step 6)
Execute `docs/HUMAN_VALIDATION_PROTOCOL.md` (V2 — frozen) on the six-business cohort above.

Before each call: screen number against TPS, CTPS, and local `suppression.csv` (copy from `suppression.csv.example` if needed).

Record outcomes in local `prospects.csv` and validation evidence locally only. Do not commit `prospects.csv`, `suppression.csv`, or real contact data.

## Project Lead Handoff (Step 7)
After human execution, verify Day 2 definition of done against the frozen validation gate (PASS A / PASS B / REASSESS / WEDGE WEAKENED). Update `docs/CURRENT_STATE.md`. Replace this file with Day 3 tasking (telephony skeleton) per `docs/30_DAY_PLAN.md` only if Day 2 closeout is approved.

## Definition of Done
- 40 UK plumbing/heating businesses researched
- ICP signals and software clues recorded in local `prospects.csv`
- prospects scored and tiered (A/B/C)
- Claude ICP review completed (PASS WITH CORRECTIONS)
- approved corrections applied
- Human Validation Protocol V2 frozen and executed on six-business cohort
- validation gate outcome recorded (PASS A / PASS B / REASSESS / WEDGE WEAKENED)
- evidence supports or refines the initial ICP in `docs/PROJECT.md`
- `docs/CURRENT_STATE.md` updated
- Project Lead final Day 2 closeout completed
- next task points to Day 3 telephony foundation (only after Step 7)
