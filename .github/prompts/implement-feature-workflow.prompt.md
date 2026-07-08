---
name: Implement Feature From Ticket
description: Deliver one OpenSmartRouting ticket through code, tests, docs, and PR repair loop.
---

Solve `${TICKET_OR_FEATURE}` end to end.

Rules:

1. stay inside the ticket scope
2. prefer a failing-test-first loop when practical
3. validate before and after the change
4. update docs when the change affects behavior, commands, setup, or workflow
5. do not stop at "PR opened"
6. update the ticket's Status and append a dated Status History entry when work starts (In Progress) and again when it finishes (Done, or Needs Rework with a reason)
