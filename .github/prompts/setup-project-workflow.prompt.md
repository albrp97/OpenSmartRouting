---
name: Set Up Project Delivery Workflow
description: Define the branch, PR, CI/CD, and validation baseline for OpenSmartRouting without overengineering it.
---

Use `README.md` as the current product context.

This workflow's deliverables are Phase 0 in `docs/planning/phases.md`. Choose a lean setup for:

- Python development
- CLI testing
- free-stack research support
- future Android handoff

Cover, at minimum:

- local commands (format, lint, test)
- branch and PR flow
- a CI workflow (lint + test) required on every PR, using free GitHub Actions
- coverage reporting wired into CI
- a packaging process for the Python CLI
- a release process (versioning, tagging, changelog) for the Python CLI

Document:

- local commands
- branch and PR flow
- validation layers
- what setup is enough now versus later
