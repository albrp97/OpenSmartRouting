---
name: Review Pull Request Workflow
description: Review changed work against scope, validation, docs, and merge readiness.
---

Review `${PR_OR_CHANGESET}` as delivery work, not only as a diff.

## Outcome

Leave a clear decision on:

- what is correct
- what is missing
- what blocks merge
- whether the work is merge-ready

## Rules

1. Review against the ticket, spec, or phase objective first.
2. Check validation and docs, not only source code.
3. Separate blockers from non-blocking suggestions.
4. If the change affects route quality, data quality, or export behavior, call that out explicitly.

## Workflow

1. identify the objective and scope
2. inspect changed files and stated evidence
3. verify the validation path fits the change
4. verify docs or workflow updates where needed
5. decide whether the change is merge-ready
