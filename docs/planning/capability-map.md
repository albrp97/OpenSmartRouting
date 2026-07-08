# OpenSmartRouting Capability Map

This map is a **feature list**, not a workstream grouping. It describes what the tool actually lets a delivery driver do, how they interact with it, what goes in, and what comes back out. It intentionally does not restate the epics — epics group this work into delivery workstreams; this map describes the product itself.

Each entry below states:
- **What it lets you do** — the concrete thing a user can accomplish
- **How you use it** — the interaction shape (CLI input, flags, files, prompts)
- **Input** — what you provide
- **Output** — what you get back
- **Status** — Now (current-stage), Later (deferred), or a note on how firm the interaction shape is

## Foundational capability

### 0. Delivery workflow and validation baseline

Not a user-facing feature. It is the lean, free-stack way the project itself is developed, validated, packaged, and released before any feature below is built. See `docs/planning/phases.md` Phase 0 for details.

## Product features (current stage)

### 1. Define a delivery run

**What it lets you do:** Tell the tool where you start, where you want to end, and which addresses you need to visit in between.

**How you use it:** Run the CLI with a start point, an end point, and a list of addresses — either as command-line arguments for a quick run, or as a single input file (format still assumed, not locked — likely a plain text or CSV list) for a full day's route.

**Input:** a start address/point, an end address/point, a list of delivery addresses.

**Output:** none directly — this feeds the rest of the run.

**Status:** Now. Exact CLI flags and file format are still assumed, pending the Python MVP boundary decision.

### 2. Load and check addresses

**What it lets you do:** Give the tool your real, messy address list — not a perfectly cleaned one — and have it accepted in a usable form.

**How you use it:** Paste/type addresses directly, or point the CLI at a file with one address per line. The tool should not silently drop malformed addresses; it should surface which ones look wrong before continuing.

**Input:** raw address strings, one per delivery stop.

**Output:** a validated address list, with any addresses that look incomplete or ambiguous flagged for the user to fix.

**Status:** Now.

### 3. Geocode addresses into map coordinates

**What it lets you do:** Turn the address list into coordinates the router can actually use, using a free/open geocoder suitable for Spain.

**How you use it:** Happens automatically as part of running the CLI — the user does not call geocoding directly, but sees its results.

**Input:** the validated address list.

**Output:** a coordinate for each address, plus a confidence or "weak match" flag so the user knows which stops might be off and worth double-checking manually.

**Status:** Now.

### 4. Compute an efficient multi-stop route

**What it lets you do:** Get a visiting order for all your stops, between your start and end point, that is meaningfully better than just visiting addresses in the order you typed them — and that respects real road behavior such as one-way streets.

**How you use it:** Automatic once the run is defined and addresses are geocoded; no separate command needed.

**Input:** the start/end points and geocoded stop coordinates.

**Output:** an ordered list of stops with the travel path between them, computed from real road-network data.

**Status:** Now. Which routing engine and optimization method power this is still under research (`docs/research/free-routing-stack.md`); the user-facing behavior described here is what should stay stable regardless of which engine wins.

### 5. Get a usable route result

**What it lets you do:** See or save the final route in a form you can actually use while driving, without needing to interpret raw coordinates or debug output.

**How you use it:** The CLI prints the ordered stop list to the terminal by default, and can optionally write it to a file (e.g. for printing or forwarding).

**Input:** the computed route.

**Output:** an ordered, numbered stop list with the original addresses (not just coordinates), and basic distance/duration information where available.

**Status:** Now.

### 6. Hand the route off to external navigation

**What it lets you do:** Get the entire multi-stop route open and ready to drive in Google Maps with a single tap, in the correct visiting order, without retyping any address.

**How you use it:** The CLI generates a Google Maps Directions URL (`https://www.google.com/maps/dir/?api=1&origin=...&destination=...&waypoints=...`) built from the ordered route — no API key or paid service required. Opening the link (tap, click, or scanned QR code) launches the Google Maps app or web with the full route loaded. Google Maps' own consumer URL limits how many stops one link can carry (up to 9 waypoints on desktop, 3 on mobile browsers), so a route with more stops than that is split into multiple sequential links (e.g. "Leg 1 of 2"), each opened after finishing the previous one. The plain ordered address list (capability 5) is always available too, as a manual fallback if a link cannot be used.

**Input:** the route output from capability 5.

**Output:** one or more Google Maps directions links (batched if needed), plus the manual fallback address list.

**Status:** Now. Free, no API key needed; the batching threshold and exact link format are confirmed, the CLI-side generation is not built yet.

## Supporting technical capabilities (not directly user-facing)

These are necessary for the features above to work, but the user does not interact with them directly.

### Road-network access

Access to routing data reflecting real road constraints (one-way streets, local access patterns) that capability 4 depends on. Sourced from free/open data (OpenStreetMap-based, per current research).

### Experiment and comparison workflow

An internal way for the project to compare routing approaches, geocoding quality, and route usefulness before locking the stack. This supports development decisions; it is not something a delivery driver ever sees or runs.

## Later-stage features

### 7. Handle real-world input more gracefully

Stronger input formats (CSV/Excel), clearer error messages, and more stable repeat-use behavior once the core is proven. Example: re-running yesterday's route with one address changed, without retyping everything.

### 8. Save and reuse delivery runs

Keep a previous run's input (start, end, addresses) so a driver can tweak and re-run it instead of starting from scratch each day.

### 9. Alternative navigation handoff formats

If the Google Maps link (capability 6) proves insufficient — e.g. a driver prefers Waze, or a native app deep link is worth the added complexity — evaluate GPX/KML export or per-app deep links. Deferred because the Google Maps link already covers the common case for free.

### 10. Android app equivalent

Once the Python routing core is proven, the same feature set (define a run, load addresses, geocode, compute route, get a usable result, hand off to navigation) delivered as an Android experience instead of a CLI.

## Capability constraints

- Every current-stage feature must preserve the **free-first** constraint.
- Every current-stage feature must be reachable through the **Python CLI** — no feature should require a GUI to use in the current stage.
- Later features should only advance after research and experiments justify them.
- The exact CLI syntax, input file format, and output format named above are the current best assumption, not a locked interface — they should be confirmed when the Python MVP boundary is decided.
