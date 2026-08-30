# Initial Architecture

## Goal
Implement the smallest reliable production path for missed-lead recovery.

## Conceptual Flow

```text
CUSTOMER
   |
   v
Business phone number
   |
   v
Plumber answers?
  / \
YES  NO
 |    |
END   v
   Missed/no-answer event
         |
         v
   Recovery SMS
         |
         v
   Customer replies
         |
         v
   Qualification engine
         |
         +--> nonsense/unsupported -> fallback
         |
         +--> normal/urgent -> capture details
                              |
                              v
                        qualified lead
                         /          \
                        v            v
                  owner alert    database
                        |
                        v
                     follow-up
```

## Recommended Components

### Application
Python web service.

Suggested framework: FastAPI or Flask. Choose one and record the decision in `DECISIONS.md`.

### Database
PostgreSQL.

### Telephony/SMS
Twilio webhooks and messaging.

### State Management
Prefer a deterministic state machine for V1.

Use an LLM only for bounded tasks such as:

- extracting structured fields from messy text
- classifying intent/urgency where deterministic rules are insufficient
- rewriting a constrained response

Never let the LLM silently invent pricing, availability, policy or technical advice.

## Minimal Data Model

### businesses
- id
- name
- phone number(s)
- timezone
- business hours
- escalation number
- settings JSON

### leads
- id
- business_id
- phone
- name
- postcode
- problem_summary
- urgency
- status
- created_at
- updated_at

### conversations
- id
- business_id
- lead_id
- state
- started_at
- updated_at

### messages
- id
- conversation_id
- provider_message_id
- direction
- body
- status
- timestamp

### events
- id
- business_id
- provider_event_id
- event_type
- payload JSON
- processed_at

## Required Reliability Properties

- webhook idempotency
- duplicate-message protection
- retry-safe processing
- structured logs
- no secrets in source control
- explicit failure path
- explicit human fallback
- opt-out handling
- safe default if classification fails

## Integration Philosophy
Do not replace the plumber's existing job-management software.

V1 may simply notify the owner by SMS/email with a structured lead.

Integrate with ServiceM8/Tradify/Powered Now only when a real client justifies it.
