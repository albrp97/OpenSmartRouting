# OpenSmartRouting

> Free route optimization for delivery work in small towns and mixed urban areas in Spain.

## What this project is about

OpenSmartRouting is intended to replace a paid delivery routing app with a free solution focused on a real use case:

- a delivery worker has a list of addresses
- the system should start near the driver's current location
- visit all required stops in an efficient order
- finish near the driver's desired ending location
- account for real road constraints such as one-way streets and local street layout

The initial motivation comes from a practical family use case: a delivery driver working across smaller towns and dispersed areas in Spain needs better routing without paying for a commercial service.

## Repository setup status

This repository now has a Harmonic Coding-style runtime baseline so it is ready to be used later for planning, research, setup, and implementation.

Added setup layer:

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.github/instructions/`
- `.github/prompts/`
- `harmonic-custom/`
- `NEXT_STEPS.md`
- workflow eval scaffolding

What has **not** been done yet:

- the experiment plan has not been written yet
- no experiments have been run yet
- no MVP routing logic has been implemented yet (only the Phase 0 Python package scaffold exists)

Planning work completed so far:

- `vision.md` now defines the current objective, primary user, core problem, success signals, and non-goals
- `docs/planning/repo-map.md` now maps the repository structure and current scaffolding
- `docs/planning/scope.md` now defines the current product boundary
- `docs/planning/capability-map.md` now defines the current capability set without turning it into tasks
- `docs/planning/epics.md` now groups the capabilities into outcome-based workstreams
- `docs/planning/phases.md` now sequences the epics into the staged delivery path
- `docs/planning/tickets-phase-0.md` and `docs/planning/tickets-phase-1.md` now break each phase into minimal execution units with priorities, dependencies, and full status history (one tickets file per phase)
- `docs/research/free-routing-stack.md` now compares the free road, geocoding, routing, and optimization options

Use `NEXT_STEPS.md` for the ordered follow-up work.

## Local development setup

The project uses [`uv`](https://docs.astral.sh/uv/) as the single dependency, environment, and packaging manager. It was chosen because it is free, fast, single-binary, and replaces the pip/venv/pip-tools combination with one tool — a good fit for a lean Python CLI project.

```bash
# install uv (one-time, per machine)
curl -LsSf https://astral.sh/uv/install.sh | sh

# install the project and its dependencies into a local .venv
uv sync

# run the placeholder CLI
uv run opensmartrouting

# run tests
uv run pytest

# run tests with a coverage report (no gating threshold yet)
uv run pytest --cov=opensmartrouting --cov-report=term-missing

# format and lint (ruff is the single tool for both)
uv run ruff format .
uv run ruff check .

# run the full local quality gate (format check + lint + tests) in one command
make check
```

`pyproject.toml` defines the package (`src/opensmartrouting/`) and the `opensmartrouting` CLI entry point. `uv.lock` pins exact dependency versions for reproducible installs. This is Phase 0 scaffolding only — no routing logic yet.

See `CONTRIBUTING.md` for the branch naming and commit message conventions, and
`docs/guide/ci-pipeline.md` for a diagram of the full CI/CD pipeline (PR checks through release).

## Packaging

The CLI is packaged as a standard Python wheel/sdist using the `hatchling` build backend already
declared in `pyproject.toml`.

```bash
# build a wheel and sdist into dist/
uv build

# install the built wheel into any Python environment
pip install dist/opensmartrouting-<version>-py3-none-any.whl

# the CLI entry point is then available directly
opensmartrouting
```

This is for local/personal installation only — **publishing to PyPI is explicitly out of scope**
for now, since the current use case is a personal/local CLI tool, not a published package.
`dist/` is gitignored; it is a local build output, not something committed.

## Core problem

The problem is not just "show a route on a map."

The real problem is:

1. take a set of delivery addresses
2. turn them into usable map locations
3. build an efficient route through all stops
4. use road data that is as current as possible while staying free
5. return something practical enough to use during real delivery work

For this use case, correctness is strongly affected by:

- one-way streets
- local access patterns
- address quality and geocoding quality
- small-town road networks
- whether the route is easy to follow in practice, not only mathematically short

## Project goal

Build a free routing system that can generate a useful delivery order for addresses in Spain, using free and up-to-date-enough road data, and make it practical for real-world daily delivery work.

## Current product direction

### Phase 1 — Python-first prototype

The first version should be built in Python and should focus on proving the routing logic before building a mobile product.

Current assumption for the first usable version:

- the main interface is a **CLI tool**
- it outputs the ordered route or ordered stop list
- it generates a one-tap Google Maps directions link for the route (no API key needed), batched into multiple links if the route exceeds Google Maps' waypoint limit
- the plain address list is always available too, as a manual fallback into Google Maps or Waze

### Phase 2 — Android product

Once the routing logic and data approach are validated, the system can later be exported or rebuilt as an Android app.

## What success looks like

The project is successful if it can do the following reliably:

1. accept a delivery start point
2. accept a delivery end point
3. accept a list of delivery addresses
4. convert those addresses into usable coordinates with acceptable quality
5. produce a stop order that is meaningfully better than naive manual ordering
6. account for road direction and routing constraints from free map data
7. output the route in a way the driver can actually use

## First-release scope

The first release should stay narrow.

### In scope

- Python implementation
- CLI interface
- address input
- route optimization for multiple stops
- use of free mapping / routing / road-network data
- testing different routing or optimization approaches
- practical route output for real delivery work

### Likely acceptable outputs

- ordered list of stops
- ordered list with coordinates
- ordered list with estimated distance or duration
- a one-tap Google Maps directions link built from the ordered route (free, no API key)

### Out of scope for the first release

- full production mobile app
- polished consumer UX
- custom turn-by-turn navigation engine unless it proves lightweight enough
- broad international support beyond the Spanish use case
- large fleet dispatch features
- payments, accounts, or multi-tenant SaaS features

## Key constraints

### 1. Free is non-negotiable

The system should rely on free or open data and tools as much as possible.

That makes these choices especially important:

- map data source
- geocoding source
- route engine
- optimization library
- hosting or local execution model

### 2. Data freshness matters

The route quality depends heavily on whether road restrictions and street directions are reasonably current.

This project should prefer data sources and tooling that:

- are free to use
- are updateable
- have strong OpenStreetMap compatibility or similar open-road-network support

### 3. Real-world usability matters more than theoretical elegance

The best route is not only the shortest route in abstract graph terms.

It must also be:

- understandable
- stable
- practical to follow in the field
- tolerant of imperfect addresses

## Main technical workstreams

This project has four major workstreams.

### 1. Address ingestion and geocoding

Questions to answer:

- how will addresses be entered
- how messy can the input be
- what free geocoding source is good enough for the Spain-specific use case
- how will low-confidence matches be detected

### 2. Routing data and road-network accuracy

Questions to answer:

- which free road data source is best
- how often can it be refreshed
- how well does it handle one-way streets and local restrictions
- whether it works locally, remotely, or both

### 3. Stop-order optimization

Questions to answer:

- which optimization strategy gives the best practical result
- how much the system should optimize for time versus distance
- whether the route should return to origin by default or only when requested
- how to compare alternative algorithms objectively

### 4. Output and driver workflow

Questions to answer:

- is an ordered list enough
- should the output include share/export links
- should there be a GPX, CSV, or other exchange format
- how the driver will actually consume the result during delivery

## Research areas that matter before implementation grows

The project needs focused research before locking the stack.

### Free map and road data

Investigate options centered on open road data, especially:

- OpenStreetMap-based approaches
- update frequency
- Spain coverage quality
- one-way and local-access accuracy

### Free routing engines

Investigate candidate routing engines and their tradeoffs for:

- local execution versus hosted use
- Python integration
- support for road restrictions
- performance for multiple-stop routing

Candidate families worth evaluating:

- OSRM
- GraphHopper
- Valhalla
- pgRouting-based approaches

These are **research directions**, not final decisions.

### Optimization algorithms

The system will likely need to compare different ways to solve the stop-order problem.

Research should compare:

- exact approaches when stop counts are small enough
- heuristic or metaheuristic approaches when practical speed matters
- routing-plus-optimization approaches that use real road travel cost instead of simple straight-line distance

Potential algorithm families to evaluate:

- TSP variants
- vehicle-routing style heuristics for a single driver
- nearest-neighbor baselines
- 2-opt / 3-opt style improvements
- OR-Tools-based experimentation

Again, these are candidate directions, not yet chosen architecture.

### Android path later

The Android phase should only happen after the Python routing core is proven.

Research for the Android phase should focus on:

- how to reuse the routing core
- whether the Python logic should become a service or be reimplemented
- whether offline use is required
- what free mapping SDK or display layer best fits the constraints

## Recommended stages

The project should move in stages, not all at once.

### Stage 1 — Problem definition and research

Goal: understand the real delivery problem well enough to avoid building the wrong tool.

Main work:

- document the user workflow clearly
- define scope and non-goals
- define what "good enough" route quality means
- research free map data, geocoding, routing engines, and optimization libraries
- define how results will be compared against the paid app

Expected output:

- project definition
- research notes
- candidate stack shortlist
- initial evaluation criteria

### Stage 2 — Data science and routing experiments

Goal: test route-quality ideas before committing to a full product architecture.

Main work:

- gather realistic sample address sets
- test geocoding quality on Spanish addresses
- test route computation using real road-network data
- compare multiple optimization approaches
- compare results by time, distance, practicality, and route stability

This stage should act like an experimentation lab.

It does not need a polished app yet. It needs:

- repeatable inputs
- measurable outputs
- side-by-side algorithm comparison

Expected output:

- experiment scripts or notebooks
- benchmark datasets
- route-quality comparison results
- first decision on which routing approach is worth building into the MVP

### Stage 3 — Build the Python MVP

Goal: create the first usable version for real delivery work.

Main work:

- build the Python CLI
- accept real address input
- geocode addresses
- compute the ordered route
- return a practical stop order
- optionally include useful export formats if they remain low-scope

The MVP should optimize for usefulness, not polish.

Expected output:

- a working Python CLI
- test coverage for the core logic
- documented input and output format
- first real-world usable route workflow

### Stage 4 — Real-world field testing

Goal: validate whether the MVP is actually useful during delivery work.

Main work:

- test with actual delivery address sets
- compare output against the paid app
- compare route quality and usability
- identify bad geocoding cases, routing failures, and workflow friction
- capture where the mathematically best route is not the most practical route

Expected output:

- field-test notes
- real-world comparison results
- prioritized bug list
- decision on whether the MVP is already useful enough or still too weak

### Stage 5 — Expand and harden the Python version

Goal: improve reliability before building the Android layer.

Main work:

- improve address parsing and input formats
- improve geocoding confidence handling
- improve route quality and output formatting
- add useful exports if they help the real workflow
- improve error handling and repeatability

Possible additions in this stage:

- CSV input
- Excel input
- saved route sessions
- basic route report output

Expected output:

- a stronger desktop or laptop workflow
- fewer failure cases
- a more stable routing core worth carrying forward

### Stage 6 — Define the Android architecture

Goal: decide how the proven routing core becomes a mobile product.

Main work:

- decide whether routing runs locally or through a backend
- decide whether Python logic is wrapped, exposed as a service, or reimplemented
- decide what free map display and Android stack fit the constraints
- define the minimum mobile scope

Expected output:

- Android architecture decision
- technical stack decision for mobile
- clear mobile MVP scope

### Stage 7 — Build the Android MVP

Goal: create the first narrow Android version around the proven routing workflow.

Main work:

- build a minimal Android interface
- support entering or loading stops
- display the route result or ordered stops
- connect the mobile layer to the validated routing logic

The Android MVP does not need to solve every product problem at once.

Expected output:

- first installable Android build
- basic end-to-end mobile flow

### Stage 8 — Test in Android desktop environment

Goal: validate the Android build before regular phone use.

Main work:

- run the app in an emulator or desktop Android environment
- test address input, route generation, and result display
- identify mobile-specific bugs, performance issues, and UX problems

Expected output:

- emulator test results
- mobile bug list
- fixes needed before phone testing

### Stage 9 — Install and test on a real phone

Goal: prove the product works in the actual physical environment where it will be used.

Main work:

- install the Android app on a real phone
- test in realistic conditions
- check usability while preparing or performing delivery work
- identify issues with mobile performance, connectivity, battery, and workflow convenience

Expected output:

- real-device feedback
- decision on whether the Android version is already useful
- final list of improvements before wider use

### Stage 10 — Decide what to productize next

Goal: choose the next major direction based on evidence.

Possible directions:

- improve the Python workflow further
- improve the Android app
- add export or navigation handoff features
- add offline capability
- add backend services only if they are truly necessary

The point of the earlier stages is to make this decision from real evidence, not from guesswork.

## What should be documented next

After this README, the most useful next documents would be:

1. experiment-planning documentation for route-quality evaluation
2. `docs/specs/python-prototype.md` — exact scope for the first prototype
3. delivery-workflow documentation for branches, validation, and CI boundaries

## Open questions

These are the most important unanswered questions right now:

1. How many stops does a typical route contain on a normal working day?
2. Should the first version assume online connectivity, offline capability, or both?
3. How should addresses be entered in the first version: CLI args, CSV, Excel, pasted text, or another format?
4. Is the route always supposed to end where it started, or should start and end be separate configurable points by default?
5. Is the first useful output only an ordered stop list, or do you also want an export format in the first prototype?
6. How should route quality be judged in testing: time, distance, practicality, or comparison against the paid app?
7. For the later Android phase, do you expect the phone app to compute routes locally or call a backend?

## Summary

OpenSmartRouting is a Python-first, free-routing project aimed at optimizing multi-stop delivery routes in Spain using free map and routing data, with special attention to one-way streets, small-town geography, and practical real-world use. The first goal is not a full mobile app. The first goal is to prove that a free Python-based routing workflow can generate a stop order good enough to replace or meaningfully compete with the paid tool currently being used.
