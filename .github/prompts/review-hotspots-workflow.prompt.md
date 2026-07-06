---
name: Review Hotspots Workflow
description: Identify risky files using size, churn, complexity, and instability signals before or during review.
---

Assess `${CHANGESET_OR_REPO_AREA}` for hotspot risk.

## Signals

- file size
- recent churn
- mixed responsibility
- complexity
- unstable or frequently touched routing-critical surfaces

## Output

Provide:

1. ranked hotspot files
2. dominant risk signal for each
3. why it matters to the current change
4. recommended review action
