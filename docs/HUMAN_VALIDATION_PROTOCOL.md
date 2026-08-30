# Human Missed-Call Validation Protocol — V1

**STATUS: DRAFT — AWAITING CLAUDE ADVERSARIAL REVIEW AND PROJECT LEAD ADJUDICATION**

*(Supplied status: DRAFT — MUST BE REVIEWED BEFORE USE)*

## Purpose

Determine whether target UK plumbing/heating businesses have an observable missed-call recovery gap and learn how incoming/missed calls are currently handled.

This is research and genuine business-development contact.

The tester must **NOT**:

- pretend to be a plumbing customer;
- invent a plumbing problem;
- fake an emergency;
- leave a deceptive customer voicemail;
- repeatedly call to force a missed-call event.

---

## 1. Pre-call eligibility

For each business record:

```text
Business:
Number:
Legal type:
TPS checked: PASS / FAIL
CTPS checked: PASS / FAIL
Existing DNC objection: NO / YES
Call permitted: YES / NO
```

Do not call businesses that fail the applicable compliance checks.

Use a genuine phone number with caller ID enabled.

---

## 2. Call conditions

Call during ordinary working/business hours.

One attempt per business during the initial validation round.

Do not deliberately call at unreasonable times or attempt to manufacture an unanswered call.

---

## 3. If the business answers

Do not hang up.

Say:

> "Hi, my name's Francisco. I'm doing some research into how independent plumbing and heating businesses handle missed enquiries. Could I ask you a really quick question?"

If they agree:

> "When you're out on jobs and can't answer the phone, what normally happens to that enquiry? Do you call them back manually, does someone else handle it, or have you got some kind of automated system?"

Where useful, ask:

> "And are you usually the person answering the calls yourself?"

Record their answers factually.

Do not pitch PLR unless the conversation naturally develops and they explicitly show interest in what is being worked on.

If they decline:

> "No worries, thanks anyway."

End the call.

---

## 4. If the business does not answer

Do not leave a fake plumbing voicemail.

Do not send them a message.

Do not immediately call again.

At **T+0** record:

**Initial outcome:**

- rang out
- voicemail
- answering service
- automated IVR
- other

Observe whether the business attempts recovery.

At **T+5 minutes** record:

- Automated SMS: yes/no
- Human SMS: yes/no
- Callback: yes/no
- WhatsApp: yes/no
- Other recovery: yes/no

Repeat observations at:

- T+30 minutes
- T+2 hours
- End of business day

Timestamp any recovery contact actually received.

---

## 5. If the business calls back

Do not pretend the original call concerned plumbing work.

Say:

> "Hi, thanks for calling me back. I'm Francisco. I'm actually researching how independent plumbing and heating businesses handle missed calls — that's why I called. Do you mind if I ask you one quick question about what normally happens when you miss a customer enquiry?"

If they agree, ask the standard missed-call question.

If they decline or object:

> "No problem at all. I won't contact you again."

Record any do-not-contact request immediately.

---

## 6. Evidence record

For every business capture:

```text
BUSINESS:
DATE:
CALL TIME:

PRE-CALL
TPS:
CTPS:
DNC:
Legal type:

INITIAL OUTCOME
Owner answered: yes/no
Employee answered: yes/no
Receptionist answered: yes/no
Answering service: yes/no
IVR: yes/no
Voicemail: yes/no
Rang out: yes/no
Unknown: yes/no

RECOVERY

Automated SMS:
Time:

Human SMS:
Time:

Callback:
Time:

WhatsApp:
Time:

Other:
Time:

IF HUMAN CONTACT OCCURRED

Owner handles calls:
yes / no / unknown

Reported missed-call process:
[verbatim/factual summary]

Dedicated receptionist:
yes / no / unknown

External answering service:
yes / no / unknown

Automated recovery:
yes / no / unknown

NOTES:
[factual observations only]
```

---

## 7. Unknown vs no

Unknown must not be converted into "no".

**Example:**

If the business answers the initial call, no missed-call event occurred.

Therefore:

`missed_call_followup_observed` = **unknown**

**NOT:**

`missed_call_followup_observed` = **no**

Likewise, absence of public evidence for a receptionist, automation, team size, or answering service is not evidence that one does not exist.

---

## 8. Predefined interpretation

| Observation | Interpretation |
|-------------|----------------|
| Observed missed call + no recovery | Strong evidence of PLR wedge opportunity. |
| Observed missed call + late manual callback | Strong/moderate opportunity. |
| Observed missed call + fast manual callback | Moderate opportunity. Pain exists, but current manual process may work reasonably well. |
| Basic automatic "we missed your call" SMS | Potential opportunity. Assess sophistication before rejecting prospect. |
| Automated SMS + qualification | Weak PLR V1 prospect. |
| Answering service / dedicated receptionist | Weak PLR V1 prospect. |
| Owner personally answers | Positive owner-operated ICP signal, but missed-call recovery remains unknown unless an actual missed-call event is observed or process evidence is obtained. |
| Full automated qualification/booking | Reject/very weak PLR V1 prospect. |

---

## 9. Provisional Day 2 validation gate

Among eligible successfully tested businesses, seek either:

**A)** At least 2 businesses with an observed missed call and no immediate automated recovery;

**OR**

**B)** Qualitative owner/business evidence that missed calls are handled manually/inconsistently and represent a genuine operational burden.

This gate is provisional and must be challenged by the Adversarial Reviewer before any calls occur.

The purpose is not statistical proof about the entire UK plumbing industry.

The purpose is determining whether sufficient real-world evidence exists to justify continuing PLR's current missed-lead-recovery wedge.

---

## 10. Current test cohort

1. PJS Plumbing & Heating Services
2. T.H.Williams Plumbing and Heating Ltd
3. Heat365
4. John The Plumber
5. RM Plumbing & Electrical Ltd
6. Matt Plumbing & Heating

The cohort may change before execution if compliance screening or reviewer findings make a business unsuitable.

---

## 11. Evidence discipline

Record observations, not assumptions.

Do not infer:

- no automation merely because none was publicly visible;
- no receptionist merely because one was not advertised;
- a missed-call problem when the call was answered;
- company size without evidence;
- that a callback was automated unless evidence establishes that;
- customer pain that the business did not express.

Do not fabricate validation evidence.

Local prospect/customer research containing sensitive or operational information remains outside the committed repository where existing project rules require this.

---

## 12. Stop conditions

Stop interaction with a business if:

- they request no further contact;
- the applicable compliance screening prohibits the call;
- the business is discovered to be unsuitable for the experiment;
- continuing would require deception;
- continuing would create unreasonable nuisance.

Any material uncertainty should return to the Project Lead before proceeding.
