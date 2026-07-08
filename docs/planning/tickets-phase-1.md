# OpenSmartRouting Tickets — Phase 1: Research

This document breaks **Phase 1: Research** into the smallest coherent execution units.

Each phase has its own tickets file (`docs/planning/tickets-phase-N.md`). See `docs/planning/tickets-phase-0.md` for the Delivery workflow and DevOps setup phase. These tickets stay inside the current repo rules: **free-first**, **Python-first**, **CLI-first**, and **research before stack lock-in**.

## Ticket status legend

- **Not Started** — created but no work has begun
- **Ready** — can be executed next without waiting on unrelated work
- **In Progress** — actively being worked on
- **Blocked** — depends on another ticket being completed first
- **Done** — already completed by the current planning and research artifacts
- **Needs Rework** — was done but a review found it must be revisited

Every ticket also carries a **Status History** log recording each status change with a date and short reason, so the full lifecycle of the ticket stays visible.

## Active phase tickets

### Ticket P1-E1-T1 — Record the base road-data source

- **Phase:** Phase 1 — Research
- **Epic:** Epic 1 — Free data and geocoding research
- **Priority:** P0
- **Status:** Done
- **Objective:** Confirm the free road-data base the project will use for research and experiments.
- **Scope:** Document the chosen base source, its license, and why it fits the Spain delivery use case.
- **Steps:**
  1. Review the road-data options already identified for the project.
  2. Select the base source that best fits the free-first Spain research path.
  3. Record the source, license, and rationale in the research artifact.
- **Acceptance:** The repo states that OpenStreetMap is the base road-data source and explains why it is acceptable for the project.
- **Validation:** Check that `docs/research/free-routing-stack.md` documents the source, license, and Spain suitability.
- **Dependencies:** none
- **Status History:**
  - 2026-07-08 — Status History field introduced retroactively. Current status carried over as **Done**; earlier transitions were not tracked before this date.

### Ticket P1-E1-T2 — Record the road-data refresh path

- **Phase:** Phase 1 — Research
- **Epic:** Epic 1 — Free data and geocoding research
- **Priority:** P0
- **Status:** Done
- **Objective:** Confirm how road-data freshness will be handled in the research path.
- **Scope:** Document the practical refresh path for Spain extracts and note why it is enough for the current phase.
- **Steps:**
  1. Identify the practical update path for the selected road-data source.
  2. Record the refresh cadence and update mechanism relevant to Spain extracts.
  3. Note why this refresh path is sufficient for the research phase.
- **Acceptance:** The repo identifies a realistic update path for Spain road data and keeps the freshness question explicit.
- **Validation:** Check that `docs/research/free-routing-stack.md` records the Geofabrik Spain extract and its refresh posture.
- **Dependencies:** P1-E1-T1
- **Status History:**
  - 2026-07-08 — Status History field introduced retroactively. Current status carried over as **Done**; earlier transitions were not tracked before this date.

### Ticket P1-E1-T3 — Compare Spain-first geocoding candidates

- **Phase:** Phase 1 — Research
- **Epic:** Epic 1 — Free data and geocoding research
- **Priority:** P0
- **Status:** Done
- **Objective:** Compare the smallest useful set of geocoding candidates for the Spain delivery use case.
- **Scope:** Cover CartoCiudad and at least the main OSM-based fallback options with their tradeoffs.
- **Steps:**
  1. List the minimum serious Spain-relevant geocoding candidates.
  2. Compare them on Spain suitability, hosting posture, and practical fit.
  3. Record the tradeoffs and current preference without locking the final choice.
- **Acceptance:** The repo documents the Spain suitability, hosting posture, and practical role of each candidate.
- **Validation:** Check that `docs/research/free-routing-stack.md` compares CartoCiudad, Nominatim, Photon, and Pelias.
- **Dependencies:** none
- **Status History:**
  - 2026-07-08 — Status History field introduced retroactively. Current status carried over as **Done**; earlier transitions were not tracked before this date.

### Ticket P1-E1-T4 — Review geocoder operating constraints

- **Phase:** Phase 1 — Research
- **Epic:** Epic 1 — Free data and geocoding research
- **Priority:** P0
- **Status:** Done
- **Objective:** Clarify the operational constraints that could block the chosen geocoding path.
- **Scope:** Review public-service limits, self-hosting implications, caching implications, and any unresolved usage concerns that affect research and later experiments.
- **Steps:**
  1. Re-read the constraints and usage limitations for the preferred geocoding candidates.
  2. Separate confirmed operating limits from unresolved assumptions.
  3. Write a short decision note describing acceptable use now and required cautions or fallbacks.
- **Acceptance:** The repo has a short decision note stating which geocoder constraints are acceptable now and which require explicit caution or fallback handling.
- **Validation:** Verify that the resulting note distinguishes confirmed terms from unresolved assumptions.
- **Dependencies:** P1-E1-T3
- **Status History:**
  - 2026-07-08 — Status History field introduced retroactively. Current status carried over as **Ready**; earlier transitions were not tracked before this date.
  - 2026-07-08 — In Progress (starting the geocoder operating-constraints review).
  - 2026-07-08 — Done. Reviewed the published usage terms for the three geocoders already shortlisted in `docs/research/free-routing-stack.md`: Nominatim's official usage policy (1 req/s hard cap, required User-Agent/Referer, bulk geocoding discouraged, must cache), Photon's terms of use (usable but throttled with no published quota/SLA), and CartoCiudad's service documentation (API surface described, but no explicit rate limit/quota/SLA published on the pages found). Pelias remains self-hosted-only in this project's plan, so its constraint is infra cost, not a third-party limit. Added a new "Geocoder operating constraints (decision note)" section distinguishing confirmed limits from unresolved assumptions (CartoCiudad's exact bulk-use terms; whether research-phase batch traffic counts as "bulk" under Nominatim's policy; undocumented throttling thresholds for Photon/CartoCiudad) and stating what is acceptable to build against now (small-scale, cached, single-threaded queries against CartoCiudad primary with Photon/Nominatim as secondary comparison; no geocoder treated as a guaranteed-availability dependency until confirmed or self-hosted).

### Ticket P1-E2-T1 — Compare routing-engine candidates

- **Phase:** Phase 1 — Research
- **Epic:** Epic 2 — Routing engine evaluation
- **Priority:** P0
- **Status:** Done
- **Objective:** Compare the routing engines that are realistic candidates for the research and experiment phases.
- **Scope:** Cover OSRM, Valhalla, GraphHopper, and pgRouting across licensing, Python fit, local practicality, and matrix support.
- **Steps:**
  1. Identify the minimum routing engines worth comparing for this repo.
  2. Compare them on license, Python posture, hosting practicality, and matrix support.
  3. Record the leading candidates and the reasons weaker candidates are not first choice.
- **Acceptance:** The repo documents a clear tradeoff comparison and narrows the strongest candidates for experiments.
- **Validation:** Check that `docs/research/free-routing-stack.md` includes all four routing families and a recommendation.
- **Dependencies:** P1-E1-T1, P1-E1-T2
- **Status History:**
  - 2026-07-08 — Status History field introduced retroactively. Current status carried over as **Done**; earlier transitions were not tracked before this date.

### Ticket P1-E2-T2 — Define the research exit criteria

- **Phase:** Phase 1 — Research
- **Epic:** Epic 2 — Routing engine evaluation
- **Priority:** P1
- **Status:** Ready
- **Objective:** Define what evidence is enough to move from research into the experiment phase.
- **Scope:** Specify the minimum decision points for geocoding, routing engines, optimization direction, and unresolved risks.
- **Steps:**
  1. Review the expected outputs for Phase 1 in `docs/planning/phases.md`.
  2. Translate those outputs into a short exit checklist.
  3. Record what unresolved items are still acceptable versus phase-blocking.
- **Acceptance:** The repo has a concise research exit checklist that says what must be known before experiments are considered properly defined.
- **Validation:** Verify that the criteria match the outputs listed in `docs/planning/phases.md` for Phase 1.
- **Dependencies:** P1-E1-T4, P1-E2-T1
- **Status History:**
  - 2026-07-08 — Status History field introduced retroactively. Current status carried over as **Ready**; earlier transitions were not tracked before this date.

### Ticket P1-E2-T3 — Define route-quality evaluation criteria

- **Phase:** Phase 1 — Research
- **Epic:** Epic 2 — Routing engine evaluation
- **Priority:** P1
- **Status:** Ready
- **Objective:** Define the route-quality criteria that later experiments will measure.
- **Scope:** Specify the minimum evaluation dimensions such as practicality, route quality versus naive ordering, comparison against the paid app, and tolerance for imperfect addresses.
- **Steps:**
  1. Review the current success signals and practical constraints already documented.
  2. Distill them into a small set of experiment evaluation criteria.
  3. Record the criteria in a form that Phase 2 tickets can directly reuse.
- **Acceptance:** The repo has a concise criteria document or section that states how route usefulness will be judged in the experiment phase.
- **Validation:** Verify that the criteria align with `vision.md`, `README.md`, and `docs/planning/phases.md`.
- **Dependencies:** none
- **Status History:**
  - 2026-07-08 — Status History field introduced retroactively. Current status carried over as **Ready**; earlier transitions were not tracked before this date.

### Ticket P1-E2-T4 — Publish the research-phase decision summary

- **Phase:** Phase 1 — Research
- **Epic:** Epic 2 — Routing engine evaluation
- **Priority:** P1
- **Status:** Done
- **Objective:** Publish the current research recommendation without presenting it as a final architecture lock-in.
- **Scope:** Summarize the strongest current stack candidates, the main tradeoffs, and the still-unproven items.
- **Steps:**
  1. Summarize the strongest road-data, geocoding, routing, and optimization candidates.
  2. Explicitly record the major tradeoffs and unknowns.
  3. Publish the shortlist as a research recommendation rather than a final decision.
- **Acceptance:** The repo clearly states the current preferred research stack and the uncertainties that still require experiments.
- **Validation:** Check that `docs/research/free-routing-stack.md` includes both the shortlist and the unresolved questions.
- **Dependencies:** P1-E1-T1, P1-E1-T2, P1-E1-T3, P1-E2-T1
- **Status History:**
  - 2026-07-08 — Status History field introduced retroactively. Current status carried over as **Done**; earlier transitions were not tracked before this date.

### Ticket P1-E2-T5 — Review Phase 1 work for inconsistencies and required changes

- **Phase:** Phase 1 — Research
- **Epic:** Epic 2 — Routing engine evaluation
- **Priority:** P1
- **Status:** Ready
- **Objective:** Review the completed Phase 1 work as a whole and identify inconsistencies, gaps, or changes needed before the phase is considered closed.
- **Scope:** Review the Phase 1 planning and research artifacts together, check for contradictions, missing links, stale assumptions, or places where the phase outputs no longer match each other.
- **Steps:**
  1. Re-read the Phase 1 artifacts together: `vision.md`, `docs/planning/scope.md`, `docs/planning/capability-map.md`, `docs/planning/epics.md`, `docs/planning/phases.md`, and `docs/research/free-routing-stack.md`.
  2. Compare the documents for inconsistencies, unresolved gaps, and outdated wording.
  3. Record the changes required to close the phase cleanly or confirm that no changes are needed.
- **Acceptance:** The repo contains a concise Phase 1 review result that either lists the required fixes or states that the phase outputs are internally consistent enough to close.
- **Validation:** Verify that the review explicitly checks cross-document consistency and phase-completion readiness.
- **Dependencies:** P1-E1-T4, P1-E2-T2, P1-E2-T3
- **Status History:**
  - 2026-07-08 — Status History field introduced retroactively. Current status carried over as **Blocked**; earlier transitions were not tracked before this date.
  - 2026-07-08 — Ready (user requested all Phase 1 tickets be set to Ready so execution order is not gated on dependency completion; dependencies P1-E1-T4, P1-E2-T2, P1-E2-T3 are not yet Done, so this ticket should still be executed after them in practice even though its status now reads Ready).

### Ticket P1-E3-T1 — Plan the ticket set for Phase 2

- **Phase:** Phase 1 — Research
- **Epic:** Epic 3 — Experiment harness
- **Priority:** P1
- **Status:** Ready
- **Objective:** Create the minimal ticket set that will drive Phase 2 once Phase 1 is closed.
- **Scope:** Define the smallest coherent Phase 2 tickets for experiment inputs, evaluation criteria use, matrix generation comparisons, and optimization comparisons.
- **Steps:**
  1. Use the completed Phase 1 review and exit criteria as the handoff input.
  2. Break Phase 2 into the minimum coherent execution tickets with dependencies and priorities.
  3. Record the next-phase ticket set in a form ready to execute when Phase 2 starts.
- **Acceptance:** The repo contains a Phase 2 ticket plan with minimal units, each tied to the experiment phase and its relevant epic.
- **Validation:** Verify that the planned Phase 2 tickets align with `docs/planning/phases.md`, the Phase 1 review result, and the route-quality criteria.
- **Dependencies:** P1-E2-T5
- **Status History:**
  - 2026-07-08 — Status History field introduced retroactively. Current status carried over as **Blocked**; earlier transitions were not tracked before this date.
  - 2026-07-08 — Ready (user requested all Phase 1 tickets be set to Ready; dependency P1-E2-T5 is not yet Done, so this ticket should still be executed last in practice even though its status now reads Ready).

## Current execution order

The smallest **ready now** tickets still open in the active phase are:

1. **P1-E1-T4** — Review geocoder operating constraints
2. **P1-E2-T3** — Define route-quality evaluation criteria
3. **P1-E2-T2** — Define the research exit criteria

After those are complete, the phase-closing sequence is:

4. **P1-E2-T5** — Review Phase 1 work for inconsistencies and required changes
5. **P1-E3-T1** — Plan the ticket set for Phase 2

These stay intentionally narrow so the research phase can advance in small, testable units.
