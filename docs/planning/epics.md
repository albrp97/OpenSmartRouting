# OpenSmartRouting Epics

This document groups the current capabilities into outcome-based workstreams.

The epics below are planning artifacts, not implementation tickets. They follow the current repo constraints: **free-first**, **Python-first**, **CLI-first**, and **research before stack lock-in**.

## Epic 0: Delivery workflow and DevOps setup

**Outcome**

Give the project a lean, free-stack local development, branch/PR, CI, coverage, packaging, and release baseline so that later phases can validate and ship work without re-deciding setup basics each time.

**Capabilities grouped here**

- delivery workflow and validation baseline

**Why this epic exists**

The repo direction requires free tooling, a Python-first CLI, and evidence-driven decisions. None of that is safe to build on top of without an agreed way to run code, check quality, and ship changes. This epic exists to set that baseline once, lean, and early — before it would otherwise be improvised ticket by ticket. It excludes Android tooling, which stays deferred to Epic 7.

## Epic 1: Free data and geocoding research

**Outcome**

Identify a free or open path for road data and geocoding that is suitable for the Spain delivery use case and realistic for a Python CLI workflow.

**Capabilities grouped here**

- geocode addresses into map coordinates
- road-network access (supporting)
- experiment and comparison workflow (supporting)

**Why this epic exists**

Route quality depends heavily on address quality, one-way streets, and map freshness. The project needs a credible free data path before implementation decisions become stable.

## Epic 2: Routing engine evaluation

**Outcome**

Compare candidate routing engines and decide which ones are strong enough for experiments and later MVP work.

**Capabilities grouped here**

- road-network access (supporting)
- compute an efficient multi-stop route
- experiment and comparison workflow (supporting)

**Why this epic exists**

The repo already treats OSRM, Valhalla, GraphHopper, and pgRouting as research candidates rather than fixed choices. This epic turns that research into an evidence-based shortlist.

## Epic 3: Experiment harness

**Outcome**

Create a repeatable way to compare geocoding quality, travel-cost matrices, route quality, and optimization strategies on realistic delivery inputs.

**Capabilities grouped here**

- load and check addresses
- geocode addresses into map coordinates
- compute an efficient multi-stop route
- get a usable route result
- hand the route off to external navigation
- experiment and comparison workflow (supporting)

**Why this epic exists**

The project should prove usefulness through measurable experiments before locking the stack or starting serious product implementation.

## Epic 4: Python CLI MVP

**Outcome**

Deliver the first useful Python-first, CLI-first routing workflow for the real Spain delivery use case.

**Capabilities grouped here**

- define a delivery run
- load and check addresses
- geocode addresses into map coordinates
- compute an efficient multi-stop route
- get a usable route result
- hand the route off to external navigation

**Why this epic exists**

The first usable product is not an Android app. It is a Python CLI that can accept real delivery inputs and return a practical stop order.

## Epic 5: Output and export workflow

**Outcome**

Make the route result usable in real delivery work: a clear route output plus a one-tap Google Maps directions link a driver can open to start navigating immediately.

**Capabilities grouped here**

- get a usable route result
- hand the route off to external navigation (Google Maps one-tap export link, batched for longer routes)
- alternative navigation handoff formats (later)

**Why this epic exists**

Even a technically good route will fail if the driver cannot consume it easily during delivery work.

## Epic 6: MVP hardening and field readiness

**Outcome**

Improve the proven Python workflow so it is more repeatable, tolerant of real-world input, and ready for ongoing field use.

**Capabilities grouped here**

- handle real-world input more gracefully (later)
- save and reuse delivery runs (later)
- get a usable route result
- experiment and comparison workflow (supporting)

**Why this epic exists**

After the first useful CLI exists, the next need is stability, better inputs, better error handling, and better repeatability under real use.

## Epic 7: Android transition

**Outcome**

Define how the validated routing core could later become an Android experience without treating Android as the current target.

**Capabilities grouped here**

- Android app equivalent (later)

**Why this epic exists**

Android is part of the long-term direction, but only after the Python routing core is proven through research, experiments, and field evidence.

## Epic ordering guidance

The current epic order should be treated as:

0. delivery workflow and DevOps setup
1. free data and geocoding research
2. routing engine evaluation
3. experiment harness
4. Python CLI MVP
5. output and export workflow
6. MVP hardening and field readiness
7. Android transition

This is an ordered planning view, not a commitment that all later epics should start now.
