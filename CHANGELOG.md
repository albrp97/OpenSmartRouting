# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
uses [Semantic Versioning](https://semver.org/) (`vMAJOR.MINOR.PATCH` git tags).

## [Unreleased]

## [0.0.1] - 2026-07-08

### Added

- Phase 0 DevOps setup: Python package scaffold (`uv`, `hatchling`), `ruff` format/lint, `pytest`
  with coverage reporting, a local `make check` quality gate, CI (`pr-checks.yml`) with branch
  protection on `main`, packaging via `uv build`, and this release process.
- No routing logic yet — this is infrastructure only.

<!--
No `v0.0.1` git tag/release has actually been cut yet (only throwaway test tags used to validate
the release workflow, e.g. in P0-E0-T11 and P0-E0-T21, each deleted after validation). Add the
comparison/release links below once a real `v0.0.1` tag is pushed, so the broken-link checker
(P0-E0-T22) does not flag a 404 for a release that does not exist yet:

[Unreleased]: https://github.com/albrp97/OpenSmartRouting/compare/v0.0.1...HEAD
[0.0.1]: https://github.com/albrp97/OpenSmartRouting/releases/tag/v0.0.1
-->

