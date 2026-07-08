---
name: Create Tickets
description: Turn phase and epic plans into one-ticket execution units.
---

Break the active phase into small execution tickets.

If Phase 0 (delivery workflow and DevOps setup) has not been delivered yet, it is the active phase — break it down before any product-phase tickets.

## File convention

Give each phase its own tickets file: `docs/planning/tickets-phase-N.md` (e.g. `tickets-phase-0.md`, `tickets-phase-1.md`). Never mix two phases' tickets in one file. Each file states which phase it covers and links to the sibling phase files.

## Required closing tickets

The last two tickets in every phase's file must be, in this order:

1. a **phase review ticket** that re-reads all of that phase's delivered artifacts, checks them against the phase's "Expected outputs," and either confirms the phase is consistent enough to close or flags specific earlier tickets as **Needs Rework** with a reason.
2. a **next-phase readiness ticket** that reconciles the outcome of the review with the next phase's tickets file — creating it if it does not exist yet, or checking/adjusting it if it already does — and records the reconciliation result explicitly (clean handoff, or list of adjustments made).

Do not skip these two tickets, and do not merge them into one.

## Required fields

Each ticket should define:

- objective
- scope
- acceptance
- validation
- dependencies
- **status** — one of: Not Started, Ready, In Progress, Blocked, Done, Needs Rework
- **status history** — a dated log of every status change and the reason for it, so the ticket's full lifecycle stays visible; update it every time the status changes, never just overwrite the current status silently

Prefer one coherent unit of work at a time.
