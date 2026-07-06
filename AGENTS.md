# OpenSmartRouting Agent Instructions

This repository uses a Harmonic Coding-style runtime baseline.

## Read order

Before major work, read these in order:

1. `README.md`
2. `NEXT_STEPS.md`
3. `.github/copilot-instructions.md`
4. `harmonic-custom/AGENTS.md`
5. the relevant file in `.github/prompts/`

## Current source of truth

Until the planning workflows are run, the main project context lives in `README.md`.

Use it as the source of truth for:

- project purpose
- first-release scope
- free-stack constraint
- Python-first direction
- later Android direction

## Project constraints

- the first useful version is Python-first
- the first usable interface is a CLI
- free or open data and tooling are a hard requirement
- routing quality must reflect real road constraints such as one-way streets
- practical usability matters more than theoretical elegance

## What not to do yet

- do not start the planning breakdown automatically
- do not create epics, phases, or tickets unless explicitly asked
- do not lock the stack before the research and experiment steps are done
- do not assume a mobile architecture before the Python routing core is proven

## What this setup is for

The runtime layer is being added now so the repo is ready to use later for:

- planning
- research
- setup
- implementation
- review

The next actions are listed in `NEXT_STEPS.md`.

## Runtime layout

- `.github/copilot-instructions.md` — Copilot-specific baseline context
- `.github/instructions/` — path-scoped rules
- `.github/prompts/` — reusable workflow prompts
- `harmonic-custom/` — local overrides and skill entrypoints

## Override layer

After reading this file, read `harmonic-custom/AGENTS.md` for local overrides.
