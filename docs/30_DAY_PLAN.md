# 30-Day Execution Plan

Assumption: approximately 2 hours on normal workdays and two full days off per week. Starred days should be moved onto days off where possible.

## Day 1 — Freeze Project
- Finalise ICP, offer, P0, price and success definition.
- Create repo structure and docs.
- Red-team scope.
- Outcome: V1 frozen.

## Day 2 — Model the Customer
- Research 20 UK plumbing/heating businesses.
- Record ICP signals and software clues.
- Outcome: evidence-backed ICP.

## Day 3 ★ — Telephony Skeleton
- Set up Twilio test environment/number.
- Create Python service.
- Connect PostgreSQL.
- Implement/test basic call/SMS webhooks.
- Outcome: real events reach app and database.

## Day 4 — Missed-Call Workflow
- Detect no-answer/missed call.
- Trigger recovery SMS.
- Add idempotency.
- Outcome: missed call reliably triggers one recovery message.

## Day 5 — Qualification
- Implement minimum plumbing qualification state machine.
- Create adversarial customer examples.
- Outcome: messy but common replies are handled safely.

## Day 6 ★ — Finish V1
- Complete qualification, owner alert, timeout, STOP, fallback, logs.
- Red-team and fix serious defects.
- Run full real-phone test.
- Outcome: sellable V1.

## Day 7 — Demo Asset
- Record/create a 60-second demo.
- Create one simple page or document explaining the offer.
- No new features.
- Outcome: something showable.

## Day 8 — Prospect Machine
- Finalise scoring system.
- Research 30 prospects.
- Outcome: ranked list.

## Day 9 ★ — Prospecting Marathon
- Research 70–100 businesses.
- Tier A/B/C.
- Finish with at least 50 A/B prospects.

## Day 10 — Begin Selling
- Contact 10–15 prospects.
- Focus on discovery and demo booking.
- Building phase is over.

## Day 11 — 15 Prospects
- 90 minutes outreach.
- 30 minutes objection logging.

## Day 12 — Demo Objective
- Contact 15 more.
- Seek first demo.
- Cursor only for demo-blocking bugs.

## Day 13 ★ — Sales Day
- Contact 30–40 quality prospects.
- Run demos where possible.
- Prioritise actual conversations.

## Day 14 — Funnel Review 1
Measure:
- contacted
- replies
- conversations
- demos
- objections

Diagnose:
- no conversations = targeting/outreach issue
- conversations/no demos = offer issue
- demos/no interest = value/product issue

## Day 15 — Fix One Bottleneck
- Improve one thing only.
- Contact 10 more prospects.

## Day 16 ★ — 40-Prospect Day
- Heavy outreach.
- Target 5+ real conversations.
- Record prospect language.

## Day 17 — Follow-Up Day
- Follow up every warm/uncertain lead.
- Add 5 new prospects.

## Day 18 — Demo Optimisation
- Make demo <5 minutes.
- Red-team it as a sceptical plumber.

## Day 19 — 15 New Prospects
- Contact 15.
- Run demos.
- Offer business-specific pilot configuration.

## Day 20 ★ — Closing Day
- Demos, calls, follow-ups and proposals.
- Explicitly ask warm prospects for the paid pilot.

## Day 21 — Funnel Review 2
Target by now:
- 150–200 researched
- 100+ contacted
- 10+ live conversations
- 3+ demos ideally
- 1+ pilot discussion

If well below, stop touching code and spend remaining period on sales.

## Day 22 — Objection Campaign
- Pick top objection.
- Improve pitch/demo specifically around it.

## Day 23 ★ — Highest-Volume Outreach
- 40–50 prospects.
- Calls + personalised email/follow-up.

## Day 24 — Warm Leads
- Prioritise anyone who engaged.
- Every lead gets a concrete status and next action.

## Day 25 — Pilot Close
- Ask for payment.
- Use transparent founding-client positioning.

## Day 26 ★ — Emergency Sales Sprint
If no client:
- no product work unless broken
- revisit strongest uncontacted prospects
- revisit “busy/later” prospects
- demo repeatedly

## Day 27 — Onboard or Sell
If client:
- collect business rules, services, areas, hours, escalation, FAQs and tone.
If no client:
- 15 more contacts.

## Day 28 — Configure or Sell
If client:
- configure V1 to their actual business.
- test.
- avoid unnecessary integrations.
If no client:
- outreach.

## Day 29 ★ — Go Live / Final Close
If client:
- soft launch
- monitor conversations
- fix production defects
If no client:
- focus only on previously engaged leads and direct close attempts.

## Day 30 — Revenue Gate
Success:

```text
PAYING_CLIENTS >= 1
```

If successful, next project is making client #1 produce a case study and acquiring client #2.

If unsuccessful, analyse exactly where the funnel died before changing product or niche.
