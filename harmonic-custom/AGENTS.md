# OpenSmartRouting Local Overrides

These rules override the shared runtime assumptions for this repository.

## Local defaults

- keep the first useful version Python-first and CLI-first
- treat Android as a later-stage delivery target
- prefer strong research and experiment evidence before stack lock-in
- keep the free-data and free-tooling requirement visible in setup, research, and implementation work

## Immediate priority

The repo is in setup mode.

That means:

- the runtime should be prepared
- the workflows should exist
- the next work should be listed
- the planning breakdown should not be executed until explicitly requested

## Quality gate baseline

`docs/guide/quality-gates.md` is the canonical menu of delivery-quality checks
(static analysis, dependency/supply-chain scanning, type checking, testing layers,
security scanning, runtime/behavioral checks, reproducibility, docs/data integrity)
considered for this project. Consult it before adding or re-litigating any CI/local
quality check: it records what is active now, what is deferred, and the concrete
trigger condition for revisiting each deferred item.
