# Contributing to OpenSmartRouting

This document defines the branch and commit conventions for this repository. It exists so a
contributor (human or AI) can start work without having to ask "what do I name my branch" or
"how do I write my commit message."

## `main` stays deployable

`main` is always expected to be in a working state. Nobody commits directly to `main`; all work
happens on a short-lived branch and lands via a pull request (see the PR flow once
`P0-E0-T6`/`P0-E0-T7` are done for the required checks).

## Branch naming

Branches are named:

```
phase-<phase-number>/p<phase>-e<epic>-t<ticket>-<short-topic>
```

- `<phase-number>` — the phase number the ticket belongs to (e.g. `0`, `1`).
- `p<phase>-e<epic>-t<ticket>` — the ticket ID from the phase's tickets file (e.g. `p0-e0-t5`),
  lowercased.
- `<short-topic>` — a few kebab-case words summarizing the ticket.

Example: `phase-0/p0-e0-t5-branch-commit-conventions`.

If work is not tied to a specific ticket (rare — most work should be), use
`phase-<phase-number>/<short-topic>` instead.

Branches are short-lived: created for one ticket, merged (squash) into `main`, then deleted
(`gh pr merge --delete-branch`, followed by `git fetch --prune` locally).

## Commit messages

Commit messages use an imperative summary line, optionally prefixed with the ticket ID, followed
by a blank line and a short bullet list of what changed:

```
<Ticket ID>: <imperative summary>

- <what changed, bullet 1>
- <what changed, bullet 2>
- Mark <ticket ID> Done with validation notes (if this commit closes a ticket)
```

Example:

```
P0-E0-T4: Add a single local check command

- Add Makefile with check (default), format, lint, test targets
- check depends on format -> lint -> test in sequence, failing fast
- Document make check in README.md
- Mark P0-E0-T4 Done with validation notes
```

Rules:

- Use the imperative mood ("Add", "Fix", "Document"), not past tense ("Added") or gerunds
  ("Adding").
- Keep the summary line short (roughly 50-72 characters); put detail in the bullet list, not the
  summary.
- One commit per ticket is the default; split further only if the ticket's steps are genuinely
  independent and reviewable separately.
- If AI assistance was used to author the commit, include a `Co-authored-by:` trailer for the
  assisting agent, in addition to the human author's own commit identity.

## Ticket status updates are part of the commit

Every ticket in `docs/planning/tickets-phase-N.md` has a `Status` and an append-only
`Status History`. Updating these is not a separate, optional step — it happens in the same
commit (or PR) as the work: mark `In Progress` when starting, and `Done`
(or `Needs Rework` with a reason) when finishing, with a dated history entry each time.
