# OpenSmartRouting Free Routing Stack Research

This document compares free or open options for the OpenSmartRouting stack.

The current project direction is still **Python-first**, **CLI-first**, and **free-first**. No final stack decision is locked in yet.

## Research goal

The goal is to identify practical free options for:

- road data
- geocoding
- routing engines
- optimization libraries
- Python integration
- local versus hosted execution

The project is focused on delivery routing in Spain, so Spain suitability and data freshness matter as much as raw feature lists.

## Evidence summary

### Road data

- OpenStreetMap data is available under the **ODbL** license and the ecosystem supports both full data snapshots and frequent updates.  
  Sources: [OSM copyright](https://www.openstreetmap.org/copyright), [Planet.osm](https://wiki.openstreetmap.org/wiki/Planet.osm)
- Geofabrik publishes a **Spain extract** and marks it as updated **daily**, with regional update files also available.  
  Source: [Geofabrik Spain extract](https://download.geofabrik.de/europe/spain.html)

### Geocoding

- CartoCiudad provides official Spain-focused geocoding over addresses, roads, house numbers, postal codes, POIs, and related national geographic data.  
  Sources: [CartoCiudad geoprocessing services](https://www.cartociudad.es/web/portal/directorio-de-servicios/geoprocesamiento), [CartoCiudad downloads](https://www.cartociudad.es/web/portal/directorio-de-servicios/descarga)
- Nominatim public usage is rate-limited and not suitable as an unchecked bulk-production dependency without self-hosting or strict request controls.  
  Sources: [Nominatim API overview](https://nominatim.org/release-docs/latest/api/Overview/), [Nominatim usage policy](https://operations.osmfoundation.org/policies/nominatim/)
- Photon is an open-source OSM geocoder with continuous-update support and a lighter self-hosting path than full Nominatim.  
  Sources: [Photon README](https://github.com/komoot/photon/blob/master/README.md), [Photon public service terms](https://photon.komoot.io/)
- Pelias supports structured geocoding, confidence-like result metadata, and multiple source imports, but it is a heavier stack.  
  Sources: [Pelias documentation](https://github.com/pelias/documentation/blob/master/README.md), [Pelias result quality docs](https://github.com/pelias/documentation/blob/master/result_quality.md)

### Routing engines

- OSRM is open source, practical to self-host, and exposes matrix-oriented APIs such as **Table** for travel-time and distance matrices.  
  Sources: [OSRM README](https://github.com/Project-OSRM/osrm-backend/blob/master/README.md), [OSRM license](https://github.com/Project-OSRM/osrm-backend/blob/master/LICENSE.TXT)
- OSRM's default car profile explicitly documents handling for one-way streets and turn restrictions.  
  Source: [OSRM car.lua](https://github.com/Project-OSRM/osrm-backend/blob/master/profiles/car.lua)
- Valhalla is open source, has Python bindings, supports matrix and optimized-route APIs, and documents historical and live traffic support.  
  Sources: [Valhalla README](https://github.com/valhalla/valhalla/blob/master/README.md), [Valhalla Python Actor](https://github.com/valhalla/valhalla/blob/master/docs/docs/python/actor.md), [Valhalla matrix API](https://github.com/valhalla/valhalla/blob/master/docs/docs/api/matrix/api-reference.md)
- GraphHopper is open source and strong on routing customization, but its public matrix and route-optimization positioning is more tied to its Directions API offering than to a Python-first local CLI workflow.  
  Sources: [GraphHopper README](https://github.com/graphhopper/graphhopper/blob/master/README.md), [GraphHopper profiles docs](https://raw.githubusercontent.com/graphhopper/graphhopper/master/docs/core/profiles.md)
- pgRouting is open source and powerful inside PostgreSQL/PostGIS, but it implies a heavier database-centric operating model for a first CLI prototype.  
  Sources: [pgRouting README](https://github.com/pgRouting/pgrouting/blob/main/README.md), [pgRouting TSP docs](https://docs.pgrouting.org/latest/en/pgr_TSP.html)

### Optimization

- OR-Tools is open source, supports Python, and is a practical candidate for TSP or VRP-style route optimization over real travel-cost matrices.  
  Sources: [OR-Tools README](https://github.com/google/or-tools/blob/stable/README.md), [OR-Tools routing docs](https://developers.google.com/optimization/routing)
- NetworkX includes approximation and heuristic algorithms that are useful as simple baselines before adopting a heavier solver.  
  Source: [NetworkX approximation algorithms](https://networkx.org/documentation/stable/reference/algorithms/approximation.html)
- PyVRP is an additional Python option for richer vehicle-routing needs, though that is likely beyond the first narrow CLI scope.  
  Sources: [PyVRP README](https://github.com/PyVRP/PyVRP/blob/main/README.md), [PyVRP license](https://github.com/PyVRP/PyVRP/blob/main/LICENSE.md)

## Compared options

### 1. Road data sources

| Option | Free/open status | Freshness | Spain suitability | Local use | Notes |
| --- | --- | --- | --- | --- | --- |
| OpenStreetMap core data | Open data under ODbL | Supports regular planet snapshots and frequent updates | Strong default choice because all shortlisted routing engines use OSM data well | Yes | Best base road graph for this project |
| Geofabrik Spain extract | Built from OSM data | Daily Spain extract updates | Very strong for a Spain-first MVP | Yes | Practical default for imports and refreshes |

**Current recommendation:** use **OpenStreetMap via the Geofabrik Spain extract** as the default road-data source for experiments.

### 2. Geocoding options

| Option | Free/open status | Spain suitability | Python/use integration posture | Hosted vs local | Notes |
| --- | --- | --- | --- | --- | --- |
| CartoCiudad | Spain public-sector service and open-source components | Strongest Spain-first fit in this research set | API integration should be straightforward from Python | Hosted first | Best candidate for Spanish address quality |
| Nominatim | Open source | General OSM coverage, but not Spain-specialized | Easy HTTP use, heavier to self-host | Hosted public service is limited; local is heavy | Good fallback or benchmark, not ideal as sole public dependency |
| Photon | Open source | OSM-based and practical | Straightforward HTTP use | Hosted fair use or self-hosted | Good lighter fallback for OSM geocoding |
| Pelias | Open source | Potentially strong with multi-source tuning | More stack complexity | Mostly self-hosted | Better if later search quality controls matter a lot |

**Current recommendation:** test **CartoCiudad first** for Spain-specific address quality, with **Photon or Nominatim** as fallback or benchmark options.

### 3. Routing engines

| Engine | License | Python posture | Local practicality | Matrix support | Notable tradeoffs |
| --- | --- | --- | --- | --- | --- |
| OSRM | BSD-style open source | Strong for this repo because of Python bindings and simple HTTP use | Strong | Yes | Best first candidate for speed and simplicity |
| Valhalla | MIT | Strong because of Python Actor support | Strong | Yes | More feature-rich, likely more setup complexity |
| GraphHopper | Apache-2.0 | Weaker Python-first fit than OSRM or Valhalla | Strong | Available, but less aligned with this repo's first workflow | Good engine, but not the best first experiment target here |
| pgRouting | GPL-2.0-or-later | Usable through Python DB clients | Heavier because it needs PostgreSQL/PostGIS | Yes | Better for a DB-centric stack than a narrow first CLI |

**Current recommendation:** test **OSRM first** and **Valhalla second** for routing and matrix generation.

### 4. Optimization libraries

| Option | License | Python fit | Role in this project | Notes |
| --- | --- | --- | --- | --- |
| OR-Tools | Apache-2.0 | Strong | Main optimizer candidate | Best first serious solver to test on real road matrices |
| NetworkX heuristics | Open source | Strong | Baseline comparison | Useful for greedy, approximation, or heuristic baselines |
| PyVRP | MIT | Strong | Later comparison option | More relevant if the scope grows toward richer VRP features |

**Current recommendation:** compare **simple heuristics** against **OR-Tools** before committing to solver complexity.

## Practical shortlist

### Shortlist A: simplest first experiment stack

- **Road data:** OpenStreetMap via Geofabrik Spain
- **Geocoding:** CartoCiudad first, Photon or Nominatim fallback
- **Routing engine:** OSRM
- **Optimization:** OR-Tools
- **Baseline:** NetworkX heuristic or greedy baseline

Why this is attractive now:

- stays free or open
- supports local execution
- matches Python-first CLI work well
- gives real road-time matrices instead of straight-line approximations

### Shortlist B: second experiment stack

- **Road data:** OpenStreetMap via Geofabrik Spain
- **Geocoding:** CartoCiudad plus an OSM-based fallback
- **Routing engine:** Valhalla
- **Optimization:** OR-Tools

Why this is worth testing:

- stronger documented support for richer routing features
- good Python posture
- useful if later experiments show the project needs more flexible costing behavior

## Measured facts vs still-unproven items

### Measured or documented facts

- OSM and Geofabrik provide the free road-data path required by the project.
- CartoCiudad is a serious Spain-specific geocoding candidate.
- OSRM and Valhalla both support matrix-oriented routing needed for stop-order optimization.
- OR-Tools is a viable Python optimizer for matrix-based route ordering.

### Still unproven for this repo

- actual geocoding accuracy on the project's real Spanish address sets
- whether OSM freshness is good enough in the specific towns and delivery areas that matter
- OSRM versus Valhalla runtime, memory, and setup cost on the hardware that will run experiments
- whether OR-Tools materially improves route usefulness over simpler heuristics for the typical stop counts
- whether CartoCiudad usage terms fully fit the intended workflow, caching, and operational model

## Research-based recommendation

The best first stack to test is:

1. **OpenStreetMap road data through the Geofabrik Spain extract**
2. **CartoCiudad geocoding**, with **Photon or Nominatim** as fallback or comparison
3. **OSRM** as the first routing engine for matrix generation
4. **Valhalla** as the second routing engine for comparison
5. **OR-Tools** as the main optimizer, with **simple heuristic baselines** for control

This is a research recommendation, not a final architecture decision.

## What should be tested next

1. Build a realistic Spain delivery address test set.
2. Compare geocoding hit quality across CartoCiudad and an OSM-based fallback.
3. Generate travel-time matrices with OSRM and Valhalla.
4. Compare OR-Tools against simpler stop-order heuristics.
5. Score results by route usefulness, not only by abstract distance or duration.
