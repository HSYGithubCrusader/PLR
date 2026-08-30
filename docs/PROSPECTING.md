# Prospecting System

## Ideal Prospect

- UK plumbing/heating Ltd company
- approximately 2–8 engineers
- domestic service
- owner visibly involved
- emergency/boiler/heating work
- no obvious full-time receptionist
- phone-led enquiries
- good Google reviews
- no obvious strong missed-call recovery workflow

## Prospect Fields

```text
business_name
location
company_type
website
phone
owner_or_contact
employee_estimate
emergency_service
boiler_heating_service
google_review_count
checkatrade_or_other_directory
online_booking
receptionist_signal
job_management_software_signal
missed_call_followup_observed
score
tier
status
last_contacted
next_action
owner_answers_calls
notes
```

### Field definitions (operational)

**`online_booking`**

- `yes` — self-service appointment or callout scheduling (customer can book without human confirmation).
- `no` — quote form, callback request, contact form, or appointment request that requires human confirmation.

**`receptionist_signal` / receptionist penalty**

Apply the `-5 obvious receptionist/call centre` scoring penalty only when there is clear evidence of a dedicated receptionist, answering bureau, customer control centre, or call centre. “Available/open 24/7” alone does not qualify.

**`owner_answers_calls`**

Evidence-only field (`yes` / `no` / `unknown`). Records whether the owner/operator is evidenced as answering inbound calls. No scoring weight.

## Initial Scoring Model

```text
+3 emergency plumber
+2 2–8 engineers
+2 Ltd
+2 30+ reviews
+2 Checkatrade/major trade directory presence
+2 owner still visible/involved
+1 no online booking
+2 no observed missed-call follow-up
-5 obvious receptionist/call centre
-5 national firm
-3 obvious AI answering/recovery already present
```

Adjust only after real evidence.

## Tiers

- A: strong fit; prioritise
- B: plausible; contact after A
- C: weak fit; deprioritise

## Outreach Principle
Personalised and evidence-led.

Do not open with “I run an AI automation agency.”

A better structure:

1. identify the missed-call problem
2. explain the specific recovery system
3. offer a short demo
4. keep language tied to jobs/revenue rather than AI novelty

## Example Outreach

> Hi — I was looking at how plumbing firms handle calls while engineers are out on jobs. I build a simple missed-call recovery system that immediately texts an unanswered caller, captures the problem and postcode, and sends the plumber a qualified lead before the customer rings another company. I've got a working demo and can show you what it would look like for your business in a few minutes.

## Compliance Reminder
For UK B2B outreach, maintain an internal do-not-contact list and follow applicable PECR/UK GDPR requirements. Before conducting scaled campaigns, verify current ICO guidance for live calls, emails and sole traders.
