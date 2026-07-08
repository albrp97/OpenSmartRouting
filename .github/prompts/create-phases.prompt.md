---
name: Create Phases
description: Sequence epics into a practical delivery path.
---

Create phases that respect the current staged direction:

0. delivery workflow and DevOps setup
1. research
2. experiments
3. Python MVP
4. field testing
5. hardening
6. Android transition

Phase 0 always comes first and executes the `setup-project-workflow.prompt.md` deliverables (local commands, branch/PR flow, CI, coverage, packaging, release) end to end, except Android tooling, which stays deferred to Phase 6. It is infrastructure sequencing, not product research, so it does not violate the research-before-lock-in rule.
