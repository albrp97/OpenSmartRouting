# OpenSmartRouting Vision

## Project objective

OpenSmartRouting exists to replace a paid delivery-routing workflow with a free alternative that is practical for real delivery work in Spain.

The immediate target is a driver who needs to turn a list of delivery addresses into a stop order that starts near the current location, visits all required stops efficiently, and finishes near the desired ending point while respecting real road constraints.

Success in the current stage means proving that a Python-first, CLI-first workflow can produce route results that are useful enough to compete with manual ordering or the paid app for the real use case that motivated the project.

## Why this project exists

- a real delivery workflow currently depends on a paid routing app
- the route quality needs to reflect one-way streets and local road layout
- the solution must stay free or open as much as possible
- practical usability during daily delivery work matters more than theoretical elegance

## Primary user

The primary user is a delivery worker operating across smaller towns and mixed urban areas in Spain who needs a better daily route without paying for a commercial routing tool.

## Real problem to solve

The problem is not only drawing a line on a map.

The actual job is to:

1. accept a start point, an end point, and a list of delivery addresses
2. turn those addresses into usable map locations with acceptable quality
3. compute an efficient stop order using free road and routing data
4. account for road direction and local street constraints
5. return an output that is easy to use in real delivery work

## Practical outcome that matters

The useful outcome is a route result that saves time and decision effort for the driver and is practical enough to follow in the field.

At this stage, the expected form is an ordered route or ordered stop list produced by a Python CLI, plus a one-tap Google Maps directions link built from that route so the driver can start navigating immediately without retyping addresses.

## Success signals

The route is useful enough when it can reliably do the following:

1. accept start, end, and delivery-stop input
2. geocode Spanish delivery addresses with acceptable quality
3. produce a stop order that is meaningfully better than naive manual ordering
4. reflect one-way streets and other road-direction constraints from free data
5. return output the driver can actually use during delivery work

Additional evidence of success should come from later experiments and field testing, especially:

- comparison against the current paid app
- route practicality, not only raw distance or duration
- tolerance for imperfect real-world addresses
- stable results on repeated runs of similar inputs

## What is not the goal yet

The current goal is not to build:

- a polished consumer mobile app
- a custom turn-by-turn navigation engine unless later research proves it is lightweight enough
- large fleet or dispatch features
- account, payment, or SaaS functionality
- a fixed long-term architecture before the research and routing experiments are done

## Current assumptions and constraints

- **Decided now:** the first useful version is Python-first and CLI-first
- **Decided now:** free or open data and tooling are a hard requirement
- **Decided now:** Android is a later-stage target, not the current build target
- **Still under research:** which geocoding source, routing engine, optimization library, and execution model are best for the MVP
