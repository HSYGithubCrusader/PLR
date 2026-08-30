# Compliance Guardrails

This is an operating checklist, not legal advice.

## Prospecting
Before scaled UK outreach, verify current ICO guidance for:

- live B2B marketing calls
- TPS / CTPS screening
- electronic mail marketing rules
- treatment of sole traders and some partnerships
- suppression / do-not-contact lists
- identification and opt-out requirements

For the first campaign, prefer identifiable limited companies where practical and maintain a local suppression list from day one.

## Customer Messaging
The recovery system should:

- identify the business clearly
- provide an opt-out path where required
- honour STOP/unsubscribe immediately
- retain only data needed for the service
- avoid using customer conversation data for unrelated purposes

## Data Handling
Minimum principles:

- secrets in environment variables only
- minimise stored personal data
- limit access
- log operational events without unnecessarily exposing full message bodies in insecure logs
- document retention policy before real-client production launch
- provide deletion/export capability if required by the client's process

## Safety / Business Claims
The automated system must not invent:

- technical plumbing diagnoses
- guaranteed arrival times
- prices
- appointment availability
- legal/regulatory claims
- emergency instructions not explicitly approved by the client

Ambiguity should escalate to a human.

## Pre-Production Compliance Gate
Before the first real client's customers are processed:

- [ ] current UK outreach rules checked
- [ ] client/customer privacy responsibilities agreed
- [ ] opt-out handling tested
- [ ] business identity in messages confirmed
- [ ] data retention decision recorded
- [ ] secrets/access reviewed
- [ ] human fallback tested
- [ ] prohibited claims tested
