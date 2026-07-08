# OpenSmartRouting Scope

This document defines the current scope boundary for OpenSmartRouting before deeper planning or implementation work begins.

## In scope now

The current scope is the first useful Python-first routing workflow for the Spain delivery use case.

- a **Python** implementation as the first product target
- a **CLI** as the first usable interface
- accepting a start point, end point, and multiple delivery addresses
- geocoding those addresses into usable coordinates
- computing an efficient multi-stop delivery order
- using **free or open** map, routing, and optimization tooling
- reflecting real road constraints such as one-way streets and local street layout
- comparing routing and optimization approaches before stack lock-in
- producing practical route output such as an ordered stop list, coordinates, basic distance or duration estimates, and a one-tap Google Maps multi-stop directions link (batched when a route exceeds the Google Maps waypoint limit)
- evaluating usefulness against real delivery needs rather than only abstract optimization metrics

## Out of scope now

These items are explicitly outside the current scope boundary.

- a polished consumer mobile app
- a production Android build
- a custom turn-by-turn navigation engine unless later research proves it is lightweight enough
- broad support beyond the current Spain-focused use case
- fleet dispatch, multi-driver planning, or enterprise operations
- accounts, payments, subscriptions, or multi-tenant SaaS features
- locking a permanent architecture before research and experiments are complete

## Deferred or later

These items may matter later, but they are not part of the current scope boundary.

- the later Android product once the Python routing core is proven
- richer or alternative handoff formats beyond the Google Maps directions link (e.g. GPX/KML export, native app deep links, per-app turn-by-turn integration)
- offline versus online execution decisions
- the exact geocoding provider, routing engine, and optimization library
- stronger desktop workflow features such as CSV, Excel, or saved sessions
- backend services, only if later evidence shows they are necessary

## Scope guardrails

- **Free-first is mandatory:** prefer free or open data and tooling.
- **Python-first is mandatory:** do not treat Android as the current target.
- **CLI-first is mandatory:** the first useful interface is a command-line workflow.
- **Research before lock-in:** stack decisions stay provisional until routing and data experiments produce evidence.
