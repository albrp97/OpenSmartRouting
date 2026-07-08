---
name: Create Capability Map
description: Turn approved scope into a user-facing feature list.
---

The capability map is a **feature list**, not a workstream grouping. It must describe what the tool lets a user do, how they interact with it, what goes in, and what comes out — not restate the epics at a different label. If it reads like a clone of the epics (same groupings, same abstraction level), it is wrong; rewrite it at the feature level.

For each entry, capture:
- what it lets you do
- how you use it (CLI flags, input file, prompts, automatic behavior)
- input
- output
- status (now / later), and how firm the interaction shape is

Cover features such as:

- define a delivery run (start, end, addresses)
- load and check addresses
- geocode addresses into map coordinates
- compute an efficient multi-stop route
- get a usable route result
- hand the route off to external navigation
- later Android app equivalent

Separate any internal, non-user-facing capability (e.g. road-network access, experiment/comparison workflow) into its own "supporting technical capabilities" section so it doesn't get mixed with the feature list.

Always include one foundational, non-product capability first: **delivery workflow and validation baseline** (local commands, branch/PR flow, CI, coverage, packaging, release). It is infrastructure, not a product feature, so it does not compete with research-before-lock-in and can be built ahead of the product features.

Do not turn the map into implementation tasks yet.
