# Scope

## P0 — Must Exist Before Selling

- Missed-call detection
- Recovery SMS
- Inbound SMS handling
- Lead state tracking
- Basic qualification flow
- Basic urgency classification
- Owner notification
- Conversation logging
- STOP/unsubscribe handling
- Failure handling
- Idempotency for inbound webhooks/events

## P1 — Build Only If Needed After P0

- Booking link
- Follow-up automation
- Simple analytics
- Business-specific FAQ handling
- Service-area filtering

## P2 — Explicitly Deferred Until After First Client Unless a Live Sale Requires It

- ServiceM8 integration
- Tradify integration
- Powered Now integration
- Quote chasing
- Old lead reactivation
- WhatsApp
- AI voice receptionist
- Review automation
- Custom mobile app
- Multi-industry support
- Full CRM
- Automatic quoting
- Complex dashboards
- General lead generation platform
- Marketing website beyond a minimal demo/landing page

## V1 Qualification Fields

- customer name
- phone number
- problem summary
- postcode
- active leak: yes/no/unknown
- no heating or hot water: yes/no/unknown
- residential/commercial if relevant
- urgency / desired timing

## V1 Output to Plumber

```text
NEW QUALIFIED LEAD

Name: Sarah
Phone: 07...
Postcode: BR2
Problem: Boiler not firing
Urgency: No heating/hot water
Property: Residential
Preferred time: ASAP

NEXT ACTION: Call Sarah
```

## Scope Gate
After Day 7, a proposed dev task must name one of:

1. a current prospect that requires it,
2. a production failure,
3. a repeated sales objection or blocker,
4. a legal/compliance requirement,
5. a P0 defect.

Otherwise defer it.
