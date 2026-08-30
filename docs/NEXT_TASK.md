# Next Task

## CURRENT DAY
2

## PROJECT DAY STATUS
IN PROGRESS

## START WITH
Claude (Human Validation Protocol V1 adversarial review)

## TODAY'S OBJECTIVE
Model the customer — build an evidence-backed ICP from real UK plumbing/heating businesses.

## COMPLETED
- research completed: **40** UK plumbing/heating businesses (not 20)
- ICP signals and software clues recorded in local `prospects.csv`
- prospects scored and tiered (A/B/C)
- Claude review completed: **PASS WITH CORRECTIONS**
- approved corrections applied to local tracker and prospecting documentation
- Human Validation Protocol V1 drafted (`docs/HUMAN_VALIDATION_PROTOCOL.md`)

## NEXT GATE
Protocol review and approval, then human validation of the six-business cohort (missed-call tests). After validation, return to **ChatGPT** for final Day 2 closeout.

**Immediate sequence:**

1. Claude — protocol adversarial review — **NEXT**
2. Project Lead — adjudicate protocol findings — **PENDING**
3. Project Lead — freeze approved protocol — **PENDING**
4. Human Owner — execute validation on cohort — **PENDING**
5. ChatGPT — final Day 2 closeout — **AFTER human validation**

## HUMAN-VALIDATION COHORT (order)
1. PJS Plumbing & Heating Services
2. T.H.Williams Plumbing and Heating Ltd
3. Heat365
4. John The Plumber
5. RM Plumbing & Electrical Ltd
6. Matt Plumbing & Heating

## AGENT SEQUENCE
1. ChatGPT — lead session / research plan — **DONE**
2. ChatGPT + Human — customer research and prospect logging — **DONE**
3. Claude — ICP evidence red-team — **DONE (PASS WITH CORRECTIONS)**
4. Cursor — approved corrections — **DONE**
5. ChatGPT — technical verification of research/review — **DONE**
5b. Cursor — draft Human Validation Protocol V1 — **DONE**
5c. Claude — protocol adversarial review — **NEXT**
5d. Project Lead — adjudicate protocol + freeze — **PENDING**
6. Human Owner — execute missed-call validation on cohort — **PENDING**
7. ChatGPT — final Day 2 closeout — **AFTER human validation**

## DO NOT
- Begin Day 3 (telephony skeleton)
- Build product features
- Expand scope
- Commit local `prospects.csv` (local-only data; must never be committed)
- Replace this file with Day 3 tasking until ChatGPT completes final Day 2 closeout

---

## Claude Handoff (Step 5c)
Adversarial review of `docs/HUMAN_VALIDATION_PROTOCOL.md` against `docs/PROJECT.md`, `docs/SCOPE.md`, `docs/PROSPECTING.md`, and `docs/COMPLIANCE.md`. Red-team methodology, evidence discipline, compliance framing, and the provisional validation gate. Rank findings by severity. Do not rewrite the protocol wholesale.

## Project Lead Handoff (Step 5d)
Adjudicate Claude protocol findings. Freeze approved protocol for execution or return corrections to Cursor for documentation-only updates.

## Human Owner Handoff (Step 6)
Execute missed-call validation per the **frozen** protocol on the six-business cohort above. Record outcomes in local `prospects.csv` only (`missed_call_followup_observed`, `owner_answers_calls`, and related notes as evidence permits). Do not commit `prospects.csv`. Do not execute until protocol is frozen.

## ChatGPT Handoff (Step 7)
After human validation, verify Day 2 definition of done. Confirm the ICP is evidence-backed from real businesses and human tests. Update `docs/CURRENT_STATE.md`. Replace this file with Day 3 tasking (telephony skeleton) per `docs/30_DAY_PLAN.md`.

## Definition of Done
- 40 UK plumbing/heating businesses researched
- ICP signals and software clues recorded in local `prospects.csv`
- prospects scored and tiered (A/B/C)
- Claude review completed (PASS WITH CORRECTIONS)
- approved corrections applied
- Human Validation Protocol V1 drafted (awaiting Claude review and Project Lead approval)
- evidence supports or refines the initial ICP in `docs/PROJECT.md`
- protocol adversarial review completed and protocol frozen for execution
- human missed-call validation completed on the six-business cohort
- `docs/CURRENT_STATE.md` updated
- ChatGPT final Day 2 closeout completed
- next task points to Day 3 telephony foundation (only after Step 7)
