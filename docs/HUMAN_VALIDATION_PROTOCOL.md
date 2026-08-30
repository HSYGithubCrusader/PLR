# Day 2 Commercial Discovery + Missed-Call Validation Protocol — V2

**STATUS: FROZEN V2 — PROJECT LEAD APPROVED FOR HUMAN EXECUTION**

*Supersedes Human Missed-Call Validation Protocol V1.*

## Purpose and positioning

Determine whether target UK plumbing/heating businesses have an observable missed-call recovery gap, validate ICP fit, and learn how incoming/missed calls are currently handled.

The calls have three legitimate purposes:

1. validate ICP;
2. observe/understand missed-call behaviour;
3. permit creation of a warm commercial lead if genuine interest develops.

They are **not** fake customer enquiries and must never involve fabricated plumbing needs or emergencies.

The tester must **NOT**:

- pretend to be a plumbing customer;
- invent a plumbing problem;
- fake an emergency;
- leave a deceptive customer voicemail;
- repeatedly call to force a missed-call event.

---

## 1. Compliance screening

Before **every** call, screen the **specific number** against:

- TPS;
- CTPS;
- PLR's local suppression/DNC list (`suppression.csv` — local-only; copy from `suppression.csv.example`).

If the number appears on TPS or CTPS, do not make an unsolicited commercial/discovery call unless an appropriate exception/permission has been established.

If meaningful compliance uncertainty remains, stop and escalate to the Human Owner / Project Lead.

Record:

```text
TPS: clear / registered / uncertain
CTPS: clear / registered / uncertain
PLR suppression: clear / blocked
Eligible to call: yes / no
Notes:
```

Do not require legal-entity classification solely to decide which register to screen; **both** TPS and CTPS are screened.

Use a genuine phone number with caller ID enabled.

---

## 2. Local suppression list

If someone requests no further contact:

1. stop the interaction;
2. immediately add the number/business to local `suppression.csv`;
3. exclude it from future PLR validation and sales outreach;
4. preserve only the minimum information required to honour suppression.

Template: `suppression.csv.example` (committed). Real list: `suppression.csv` (local-only, gitignored). Do not commit real business/contact data.

---

## 3. Call conditions

Call during ordinary working/business hours.

**One initial attempt** per business during the initial validation round.

Do not deliberately call at unreasonable times or attempt to manufacture an unanswered call.

---

## 4. If the business answers — commercial discovery

Do not hang up.

Opening (required transparency):

> "Hi, I'm Francisco. I'm researching a system I'm building for small plumbing businesses around missed customer enquiries. Could I ask you one quick question about how you currently handle them?"

If they decline:

> "No worries, thanks anyway."

End interaction.

If they engage, ask the open discovery question (Section 5).

If they organically show interest in the system, the caller **MAY** continue the commercial conversation. Do not force a pitch merely because they answered.

If useful after genuine interest:

> "That's why I'm looking at this. The system I'm building texts missed callers immediately, gets the basic job details and sends the lead back to the plumber."

Then allow the conversation to develop naturally.

---

## 5. Discovery question (non-leading)

Ask:

> "When you're out on a job and can't answer the phone, what normally happens to that call?"

Wait for an unprompted answer. Do not immediately offer answer categories.

Only if clarification is necessary may the caller probe neutrally.

Useful follow-up:

> "And does that process work well for you, or is there anything about it that's a pain?"

Do not imply that a problem must exist.

Where useful:

> "And are you usually the person answering the calls yourself?"

Record answers factually.

---

## 6. If the business does not answer

Do not leave a fake plumbing voicemail.

Do not send them a message merely to provoke a response.

Do not immediately call again.

Record the **actual** initial outcome at **T+0**:

- rang out
- voicemail
- answering service
- automated IVR
- other/unclear (+ notes)

### Voicemail distinction

- **Voicemail + no proactive callback/recovery** → basic call-capture infrastructure exists, but no observed proactive recovery.
- **Voicemail + callback** → evidence of active manual/proactive recovery; record recovery speed.

Do not treat voicemail itself as equivalent to automated lead recovery.

### Callback availability (tester)

Do **not** require the tester to avoid all other calls until the observation period ends.

Require:

- phone remains powered/reachable;
- caller ID / call history remains available;
- incoming callback attempts are recorded even if not answered;
- any period where callback observation was technically unreliable is explicitly recorded.

Measure **attempted** recovery as well as successful conversation.

### Observation windows

Record recovery observations at:

- **T+5 minutes**
- **T+30 minutes**
- **T+2 hours**
- **T+6 hours**

Any recovery after six hours should still be recorded as **late/post-window recovery** with actual timestamp.

The principal PLR commercial question is speed of recovery, particularly immediate/near-immediate recovery.

### Recovery-message classification

For every SMS / WhatsApp / message received, record:

```text
Channel:
Time:
Message text:

Classification:
- clearly automated
- likely automated
- likely human
- clearly human
- unknown

Reason for classification:
```

Never infer automation merely because a message is generic. When evidence is insufficient: **classification = unknown**.

Preserve **unknown ≠ no**.

---

## 7. If the business calls back

Never imply the original call concerned plumbing work.

Say:

> "Hi, thanks for calling me back. I'm Francisco. I'm researching a system I'm building for small plumbing businesses around missed customer enquiries — that was the reason for my call. Could I ask you one quick question about how you currently handle missed calls?"

If they agree, ask the standard discovery question (Section 5).

If they decline or object:

> "No problem at all. I won't contact you again."

Record any do-not-contact request immediately and add to local suppression (Section 2).

---

## 8. Evidence record

For every business capture:

```text
BUSINESS:
DATE:
CALL TIME:

PRE-CALL
TPS:
CTPS:
PLR suppression:
Eligible:

INITIAL OUTCOME
owner answered:
employee answered:
receptionist:
answering service:
IVR:
voicemail:
rang out:
other/unclear + notes:

DISCOVERY
owner handles calls: yes/no/unknown
missed-call process:
process works well: yes/no/unknown
reported pain/effort/delay/lost opportunity:
dedicated receptionist: yes/no/unknown
external answering service: yes/no/unknown
existing automated recovery: yes/no/unknown

RECOVERY
T+5m:
T+30m:
T+2h:
T+6h:
late/post-window:

For each contact:
  channel
  timestamp
  message text if applicable
  automation/manual classification
  classification reason

CALLBACK ATTEMPT OBSERVED:
yes/no
time:

DNC REQUESTED:
yes/no
suppression entry recorded:
yes/no

NOTES:
[factual observations only]
```

Validation evidence containing prospect/contact information remains **local-only**. Do not commit real prospect evidence or the real suppression list. Store only information needed for validation/outreach decisions.

If a business requests no further contact, retain only the minimum suppression information necessary to prevent future contact and remove unnecessary research notes when appropriate when safe to do so.

---

## 9. Unknown vs no

Unknown must not be converted into "no".

**Example:** If the business answers the initial call, no missed-call event occurred.

Therefore: `missed_call_followup_observed` = **unknown** — **NOT** `no`.

Likewise, absence of public evidence for a receptionist, automation, team size, or answering service is not evidence that one does not exist.

---

## 10. Predefined interpretation

| Observation | Interpretation |
|-------------|----------------|
| Observed missed call + no recovery within 30 minutes | Strong evidence of PLR wedge opportunity. |
| Observed missed call + late manual callback | Strong/moderate opportunity. Record timing. |
| Observed missed call + fast manual callback | Moderate opportunity. Pain may exist; manual process may work reasonably well. |
| Basic automatic "we missed your call" SMS | Potential opportunity. Assess sophistication before rejecting prospect. |
| Automated SMS + qualification | Weak PLR V1 prospect. |
| Answering service / dedicated receptionist | Weak PLR V1 prospect. |
| Owner personally answers | Positive owner-operated ICP signal; missed-call recovery remains unknown unless missed-call event observed or process evidence obtained. |
| Full automated qualification/booking | Reject/very weak PLR V1 prospect. |

---

## 11. Frozen Day 2 validation gate

### PASS A — observed behaviour

At least **2** genuine unanswered calls where the business shows **no automated recovery within 30 minutes**.

A later manual callback does not invalidate this evidence; record its timing because PLR's wedge is immediate recovery.

**OR**

### PASS B — first-person discovery evidence

At least **3** eligible businesses independently describe missed enquiries as:

- being lost;
- being inconsistently recovered; or
- requiring manual recovery;

**AND** at least one describes meaningful effort, delay, lost opportunity or dissatisfaction associated with that process.

### REASSESS / INSUFFICIENT

Fewer than 3 businesses produce usable observational or first-person evidence.

### WEDGE WEAKENED

Several businesses reveal competent immediate automated missed-call recovery/qualification, or reached businesses overwhelmingly report that their existing process works well and the missed-call problem has little salience.

Do not automatically abandon PLR from six observations. A weakened result triggers Project Lead reassessment of ICP/wedge before Day 3.

---

## 12. Current test cohort

1. PJS Plumbing & Heating Services
2. T.H.Williams Plumbing and Heating Ltd
3. Heat365
4. John The Plumber
5. RM Plumbing & Electrical Ltd
6. Matt Plumbing & Heating

The cohort may change before or during execution if compliance screening makes a business ineligible.

---

## 13. Evidence discipline

Record observations, not assumptions.

Do not infer:

- no automation merely because none was publicly visible;
- no receptionist merely because one was not advertised;
- a missed-call problem when the call was answered;
- company size without evidence;
- that a callback was automated unless evidence establishes that;
- customer pain that the business did not express.

Do not fabricate validation evidence.

---

## 14. Stop conditions

Stop interaction with a business if:

- they request no further contact (add to suppression immediately);
- compliance screening prohibits the call;
- the business is discovered to be unsuitable;
- continuing would require deception;
- continuing would create unreasonable nuisance.

Any material uncertainty should return to the Project Lead before proceeding.

---

## 15. Explicitly rejected / deferred (adjudication record)

The following reviewer recommendations are **not** implemented in V2:

- mandatory legal-entity classification solely to choose TPS vs CTPS;
- requirement to remain off all other calls until 23:59;
- 23:59 as the primary recovery deadline;
- call-duration field;
- separate validation cohort at this stage;
- full GDPR retention-management system;
- additional calls per business merely for statistical strength.
