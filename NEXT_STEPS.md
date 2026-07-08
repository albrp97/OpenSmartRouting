# OpenSmartRouting Next Steps

> Ordered list of what to do after the runtime baseline is in place.

This file is the immediate follow-up list.

It does **not** mean these steps should all be executed right now. It means the repository is now ready for them.

## Current state

The repo now has:

- root instructions
- Copilot instructions
- path-scoped rules
- local runtime overrides
- reusable workflow prompts
- reusable skill entrypoints
- review, security, hotspot, user-testing, pipeline, and eval workflow scaffolding

The project does **not** yet have:

- an experiment plan
- experiments
- source code
- tests
- CI setup

Planning artifacts completed so far:

- `vision.md` covering the project objective plus problem / users / success
- `docs/planning/repo-map.md` covering the current repository structure
- `docs/planning/scope.md` defining the current product boundary
- `docs/planning/capability-map.md` mapping the approved capabilities, including the foundational delivery workflow/DevOps capability
- `docs/planning/epics.md` grouping the capabilities into outcome-based workstreams, including Epic 0 (delivery workflow and DevOps setup)
- `docs/planning/phases.md` sequencing those epics into the staged delivery path, led by Phase 0 (delivery workflow and DevOps setup)
- `docs/planning/tickets-phase-0.md` and `docs/planning/tickets-phase-1.md` breaking each phase into minimal execution units, one tickets file per phase, each ticket carrying a full status history
- `docs/research/free-routing-stack.md` comparing the free stack candidates and tradeoffs

## What to do next, in order

1. **Run Phase 0: delivery workflow and DevOps setup**
   - Python project scaffolding and local commands (format, lint, test)
   - branch and PR conventions
   - CI workflow (lint + test) on every PR
   - coverage reporting
   - packaging process for the CLI
   - release process for the CLI
   - Android tooling stays deferred

2. **Research the free stack**
   - map data
   - geocoding
   - routing engines
   - optimization libraries
   - Python integration
   - later Android path

3. **Design the experiment harness**
   - sample datasets
   - route-quality metrics
   - comparison against the paid app
   - algorithm comparison method

4. **Decide the Python MVP boundary**
   - CLI input format
   - route output format
   - validation method
   - what is in scope for the first useful version

5. **Start the first implementation ticket**
   - only after Phase 0 is delivered and the planning/MVP boundary is clear

## Recommended first concrete actions

From the current state, the best immediate sequence is:

1. execute `docs/planning/tickets-phase-0.md` ticket by ticket and deliver the DevOps baseline (CI, coverage, packaging, release)
2. finish the remaining ready research tickets
3. then define the experiment plan and Python MVP boundary
4. keep architecture decisions provisional until the experiments produce evidence
5. only then expand into implementation work
