# OpenSmartRouting Phases

This document sequences the approved epics into a practical staged delivery path.

The phases follow the repo direction already stated in the README: research first, experiments second, Python MVP before Android, and evidence before architectural lock-in.

## Phase 0: Delivery workflow and DevOps setup

**Goal**

Establish the lean local development, branch/PR, CI, coverage, packaging, and release baseline the project needs before real implementation work starts, without overengineering ahead of actual code.

**Primary epics**

- Epic 0: Delivery workflow and DevOps setup

**Main focus**

- Python project scaffolding (`pyproject.toml`, dependency and lock management)
- local quality commands (formatting, linting, tests) runnable with one command
- branch and PR conventions for all later phases
- CI workflow that runs linting and tests on every PR using free GitHub Actions
- coverage reporting wired into CI
- packaging process for the Python CLI
- release process (versioning, tagging, changelog) for the Python CLI
- the quality gate menu in `docs/guide/quality-gates.md`: the free, low-effort checks that make sense before real routing code exists (type checking, dependency vulnerability scanning, secret scanning, CodeQL, dead code detection, coverage threshold, lockfile drift, release smoke test, docs link check, config schema lint, pre-commit hooks)
- explicit non-goals for this phase: no Android CI/build pipeline, no paid infrastructure, no cloud hosting, and the checks listed as "deferred" in `docs/guide/quality-gates.md` (integration/mutation/property/contract testing, performance benchmarks, memory leak checks, SBOM, license compliance, container scanning, data schema validation)

**Expected outputs**

- documented local commands for formatting, linting, and testing
- documented branch and PR flow
- working CI workflow (lint + test) required on every PR
- coverage reporting visible in CI, with a minimum threshold gate
- a defined packaging process for the CLI
- a defined release process for the CLI, with a post-build smoke test
- type checking, dead code detection, dependency vulnerability scanning, secret scanning, and CodeQL wired into CI
- a written now-vs-later boundary so later phases do not re-litigate setup decisions

## Phase 1: Research

**Goal**

Reduce the biggest early uncertainties around free data, geocoding, and routing choices before product implementation becomes the main activity.

**Primary epics**

- Epic 1: Free data and geocoding research
- Epic 2: Routing engine evaluation

**Main focus**

- confirm the free road-data path
- compare Spain-suitable geocoding options
- compare routing-engine candidates
- define what route quality and practical usefulness mean for this project

**Expected outputs**

- research notes
- candidate stack shortlist
- evaluation criteria for experiments

## Phase 2: Experiments

**Goal**

Test routing quality and stack choices on realistic delivery inputs before building the full MVP flow.

**Primary epics**

- Epic 3: Experiment harness
- supporting work from Epic 2: Routing engine evaluation

**Main focus**

- gather realistic address samples
- compare geocoding quality
- generate and compare route-cost matrices
- compare optimization strategies
- measure route usefulness against practical delivery needs

**Expected outputs**

- repeatable experiment workflow
- benchmark datasets
- route-quality comparison results
- first evidence-based stack preference for the MVP

## Phase 3: Python MVP

**Goal**

Build the first useful Python-first, CLI-first routing workflow for real delivery work.

**Primary epics**

- Epic 4: Python CLI MVP
- Epic 5: Output and export workflow

**Main focus**

- accept route input
- geocode addresses
- compute an ordered route
- return practical route output, including a one-tap Google Maps directions link
- keep the scope narrow and usable

**Expected outputs**

- working Python CLI
- documented input and output behavior
- first usable delivery-routing workflow, including a Google Maps export link (batched for routes exceeding Google Maps' waypoint limit)

## Phase 4: Field testing

**Goal**

Validate the MVP in realistic usage and identify where technical output and practical usability differ.

**Primary epics**

- Epic 5: Output and export workflow
- Epic 6: MVP hardening and field readiness

**Main focus**

- compare the workflow against the paid app
- test with real delivery address sets
- identify geocoding failures, routing failures, and workflow friction
- capture where the route is mathematically good but practically weak

**Expected outputs**

- field-test notes
- prioritized issues
- decision on whether the MVP is useful enough already or still needs major fixes

## Phase 5: Hardening

**Goal**

Strengthen the proven Python workflow so it is more repeatable and resilient for continued real-world use.

**Primary epics**

- Epic 6: MVP hardening and field readiness
- continuing work from Epic 5: Output and export workflow

**Main focus**

- improve input handling
- improve error handling and route-output clarity
- improve repeatability and robustness
- add only the lowest-scope additions that materially help the workflow

**Expected outputs**

- stronger Python workflow
- fewer common failure cases
- more stable base for any later platform transition

## Phase 6: Android transition

**Goal**

Decide how the validated routing core can later move into an Android product path without making Android the current delivery target.

**Primary epics**

- Epic 7: Android transition

**Main focus**

- decide whether the routing logic stays local, becomes a service, or is reimplemented
- decide the mobile scope boundary
- decide what free mobile mapping and display path fits the constraints

**Expected outputs**

- Android transition decision
- mobile architecture direction
- mobile MVP boundary for later work

## Phase ordering summary

0. Delivery workflow and DevOps setup
1. Research
2. Experiments
3. Python MVP
4. Field testing
5. Hardening
6. Android transition

This phase plan is a sequencing artifact. It does not mean later phases should begin before the current phase has produced enough evidence. Phase 0 is infrastructure, not product research, so it can run ahead of Phase 1 without violating the research-before-lock-in rule — it sets up how work is validated and shipped, not what the routing stack should be.
