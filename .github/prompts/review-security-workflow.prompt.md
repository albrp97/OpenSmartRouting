---
name: Review Security Workflow
description: Perform a focused security review of code, setup, workflow, or export changes.
---

Review `${CHANGE_OR_PR}` for real security risk.

## Focus

- secrets and credentials
- input parsing and validation
- export safety
- logging exposure
- workflow and CI permissions
- external API and data-source trust boundaries

## Output

Report:

1. whether there is meaningful security impact
2. findings by severity
3. affected files or surfaces
4. required fixes before merge
