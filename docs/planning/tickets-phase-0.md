# OpenSmartRouting Tickets — Phase 0: Delivery workflow and DevOps setup

This document breaks **Phase 0: Delivery workflow and DevOps setup** into the smallest coherent execution units.

Each phase has its own tickets file (`docs/planning/tickets-phase-N.md`). See `docs/planning/tickets-phase-1.md` for the Research phase. Phase 0 delivers the lean, free-stack local, CI, coverage, packaging, and release baseline defined in `docs/planning/phases.md` and executed via `.github/prompts/setup-project-workflow.prompt.md`. Android tooling stays explicitly out of scope for this phase.

## Ticket status legend

- **Not Started** — created but no work has begun
- **Ready** — can be executed next without waiting on unrelated work
- **In Progress** — actively being worked on
- **Blocked** — depends on another ticket being completed first
- **Done** — completed and validated
- **Needs Rework** — was done but a review found it must be revisited

Every ticket also carries a **Status History** log recording each status change with a date and short reason, so the full lifecycle of the ticket stays visible.

## Active phase tickets

### Ticket P0-E0-T1 — Scaffold the Python project

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P0
- **Status:** Done
- **Objective:** Give the repo a real Python package layout instead of placeholder folders.
- **Scope:** Add `pyproject.toml`, a `src/opensmartrouting/` package with an entry point, and a dependency/lock manager (`uv`). Replace the `src/.gitkeep` and `tests/.gitkeep` placeholders as needed.
- **Steps:**
  1. Choose `uv` as the dependency and environment manager and record why in the setup docs.
  2. Add `pyproject.toml` with project metadata, build system, and the CLI entry point.
  3. Create the `src/opensmartrouting/` package with a minimal placeholder module and a `tests/` package that can host pytest tests.
  4. Generate and commit the lock file.
- **Acceptance:** `uv sync` (or equivalent) installs a working environment, and the package imports cleanly.
- **Validation:** Run the install command and a trivial `python -c "import opensmartrouting"` check.
- **Dependencies:** none
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).
  - 2026-07-08 — In Progress (starting scaffolding work: pyproject.toml, src package, uv lock file).
  - 2026-07-08 — Done. Added `pyproject.toml` (hatchling build, `opensmartrouting` CLI entry point), `src/opensmartrouting/` package (`__init__.py`, `cli.py`), `tests/` package with a scaffold test, and `uv.lock`. Validated with `uv sync`, `python -c "import opensmartrouting"`, `uv run pytest` (2 passed), and `uv run opensmartrouting`. Documented `uv` usage and rationale in README.md.

### Ticket P0-E0-T2 — Add local formatting and linting

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P0
- **Status:** Not Started
- **Objective:** Give the project one formatter/linter entrypoint instead of an ad hoc style.
- **Scope:** Add `ruff` as the single formatting and linting tool, with a minimal `ruff` config in `pyproject.toml`.
- **Steps:**
  1. Add `ruff` as a dev dependency.
  2. Add a `[tool.ruff]` config with sane defaults for a small CLI project.
  3. Run `ruff format` and `ruff check` against the current `src/`/`tests/` scaffolding and fix any findings.
- **Acceptance:** `ruff format --check .` and `ruff check .` both pass locally.
- **Validation:** Run both commands and confirm a clean exit code.
- **Dependencies:** P0-E0-T1
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T3 — Add the local test command

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P0
- **Status:** Not Started
- **Objective:** Give the project a working local test command before any real routing logic exists.
- **Scope:** Add `pytest` as a dev dependency and one smoke test that proves the test runner and package import path both work.
- **Steps:**
  1. Add `pytest` as a dev dependency.
  2. Add a minimal smoke test under `tests/` that imports the package and asserts something trivial but real.
  3. Confirm `pytest` discovers and runs it.
- **Acceptance:** `pytest` runs and passes with at least one real test.
- **Validation:** Run `pytest` locally and confirm the smoke test passes.
- **Dependencies:** P0-E0-T1
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T4 — Add a single local "check" command

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Not Started
- **Objective:** Let a developer or AI run the entire local quality gate with one command.
- **Scope:** Add a `Makefile` (or equivalent script) with a `check` target that runs `ruff format --check`, `ruff check`, and `pytest` in sequence.
- **Steps:**
  1. Add a `Makefile` (or `scripts/check.sh`) with a `check` target.
  2. Wire it to call ruff format-check, ruff check, and pytest, failing fast on the first failure.
  3. Document the command in `README.md`.
- **Acceptance:** Running `make check` (or the chosen equivalent) runs all three local gates and fails clearly if any of them fail.
- **Validation:** Run the command against a clean repo and against a deliberately broken one to confirm it fails correctly.
- **Dependencies:** P0-E0-T2, P0-E0-T3
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T5 — Document branch and commit conventions

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Not Started
- **Objective:** Give the project an explicit, lightweight branch and commit convention.
- **Scope:** Document short-lived feature branches off `main`, and a simple imperative commit style, in a `CONTRIBUTING.md` or a setup section of `README.md`.
- **Steps:**
  1. Decide and record the branch naming convention (e.g. `feature/<short-topic>`).
  2. Decide and record the commit message convention.
  3. State explicitly that `main` stays deployable and work happens on short-lived branches.
- **Acceptance:** The convention is written down in a discoverable location and is unambiguous enough to follow without asking.
- **Validation:** Re-read the doc and confirm it answers "what do I name my branch" and "how do I write my commit message" without further questions.
- **Dependencies:** none
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T6 — Add the PR template and document the PR flow

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Not Started
- **Objective:** Make pull requests consistent and scoped to one ticket each.
- **Scope:** Add `.github/PULL_REQUEST_TEMPLATE.md` and document that one PR maps to one ticket and must pass local validation before opening.
- **Steps:**
  1. Add a minimal PR template covering: what changed, which ticket it closes, and how it was validated.
  2. Document the one-PR-per-ticket convention next to the branch/commit conventions.
  3. State that PRs must pass `make check` locally before being opened.
- **Acceptance:** The PR template exists and the PR flow is documented next to the branch/commit conventions.
- **Validation:** Open a test PR locally (draft) and confirm the template renders and covers the required fields.
- **Dependencies:** P0-E0-T5
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T7 — Add the CI workflow for lint and test on every PR

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P0
- **Status:** Not Started
- **Objective:** Make lint and test checks run automatically and block merge on failure.
- **Scope:** Add a GitHub Actions workflow (separate from the existing `workflow-evals.yml`) that installs the project, runs `ruff format --check`, `ruff check`, and `pytest` on every PR to `main`.
- **Steps:**
  1. Add `.github/workflows/pr-checks.yml` triggered on `pull_request` to `main`.
  2. Set up Python and the dependency manager with caching.
  3. Run the same commands as the local `check` target.
- **Acceptance:** The workflow runs on a test PR and fails when a lint or test error is deliberately introduced.
- **Validation:** Open a draft PR with a deliberate lint failure and confirm the workflow fails; fix it and confirm it passes.
- **Dependencies:** P0-E0-T4
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T8 — Add branch protection guidance for `main`

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Not Started
- **Objective:** Ensure `main` cannot be merged into without the CI checks passing.
- **Scope:** Document (and where the current GitHub plan/permissions allow, configure) branch protection on `main` requiring the PR-checks workflow to pass before merge.
- **Steps:**
  1. Document the required branch protection rule for `main` (required status check: PR checks workflow).
  2. Apply the setting via the GitHub repo settings if the acting account has admin rights; otherwise, record it as a manual follow-up with exact steps.
  3. Note the rule in the delivery workflow documentation.
- **Acceptance:** The branch protection rule is documented with exact steps, and applied if permissions allow.
- **Validation:** Attempt to merge a PR with a failing check (in a test branch) and confirm merge is blocked, or confirm the documented steps are accurate if it could not be applied directly.
- **Dependencies:** P0-E0-T7
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T9 — Wire coverage reporting into CI

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Not Started
- **Objective:** Make test coverage visible on every PR without gating on a strict threshold yet.
- **Scope:** Add `pytest-cov`, generate a coverage report in CI, and upload it as a PR artifact or step summary.
- **Steps:**
  1. Add `pytest-cov` as a dev dependency.
  2. Update the local `check` target and the CI workflow to run `pytest --cov=opensmartrouting`.
  3. Publish the coverage report as a workflow artifact or job summary; do not fail the build on a coverage threshold yet.
- **Acceptance:** Coverage output is visible in the CI run and locally, with no gating threshold at this stage.
- **Validation:** Run the workflow and confirm the coverage report is generated and viewable.
- **Dependencies:** P0-E0-T7
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T10 — Define the packaging process for the CLI

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Not Started
- **Objective:** Define how the Python CLI is built into an installable artifact.
- **Scope:** Confirm the build backend already declared in `pyproject.toml` (Ticket P0-E0-T1) produces a valid wheel/sdist, and document the packaging command.
- **Steps:**
  1. Run the build command (e.g. `uv build` or `python -m build`) and confirm it produces a valid wheel and sdist.
  2. Document the packaging command and expected output location.
  3. Note explicitly that publishing to PyPI is out of scope for now (personal/local CLI use case).
- **Acceptance:** The build command produces a valid, installable artifact locally, and the process is documented.
- **Validation:** Build the package and `pip install` the resulting wheel into a scratch environment to confirm it installs and the CLI entry point runs.
- **Dependencies:** P0-E0-T1
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T11 — Define the release process (versioning, tagging, changelog)

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Not Started
- **Objective:** Define a lean, low-ceremony release process for the CLI.
- **Scope:** Adopt manual semver git tags (`vX.Y.Z`) plus a `CHANGELOG.md`, and add a release workflow that builds and attaches artifacts to a GitHub Release when a tag is pushed.
- **Steps:**
  1. Document the semver tagging convention and when a release is warranted.
  2. Add `CHANGELOG.md` with a "Keep a Changelog"-style structure and an initial entry.
  3. Add `.github/workflows/release.yml` triggered on `v*.*.*` tags that builds the package and attaches artifacts to a GitHub Release.
- **Acceptance:** Pushing a test tag triggers the release workflow and produces a GitHub Release with build artifacts attached.
- **Validation:** Push a test pre-release tag (e.g. `v0.0.1-test`) and confirm the workflow runs and the release is created correctly, then clean up the test tag/release.
- **Dependencies:** P0-E0-T10
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T12 — Write the now-vs-later setup boundary note

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Not Started
- **Objective:** Make explicit what is intentionally deferred so later phases do not re-litigate setup decisions.
- **Scope:** Add a short section (in `README.md` or a dedicated setup doc) listing what Phase 0 deliberately does not include yet: type checking, coverage gating, PyPI publishing, Android CI, preview environments, SonarQube.
- **Steps:**
  1. List everything Phase 0 intentionally defers and why.
  2. Cross-check the list against `docs/planning/phases.md` Phase 0 non-goals.
  3. State the trigger condition for revisiting each deferred item (e.g. "add coverage gating once routing logic exists").
- **Acceptance:** The repo has a clear, short now-vs-later note that later phases can point to instead of re-deciding setup scope.
- **Validation:** Confirm the note is consistent with `docs/planning/phases.md` Phase 0 and does not contradict any ticket above.
- **Dependencies:** P0-E0-T7, P0-E0-T9, P0-E0-T11
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T13 — Review Phase 0 work for inconsistencies and required changes

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Blocked
- **Objective:** Review the completed Phase 0 work as a whole and identify inconsistencies, gaps, or changes needed before the phase is considered closed.
- **Scope:** Review all Phase 0 artifacts together (scaffolding, CI workflows, docs, conventions) for contradictions, missing links, or drift between what was planned and what was actually built. Rework or re-open earlier tickets in this file if the review finds real gaps.
- **Steps:**
  1. Re-read the Phase 0 artifacts together: `pyproject.toml`, CI workflow files, `README.md`/`CONTRIBUTING.md` conventions, `CHANGELOG.md`, and `docs/planning/phases.md` Phase 0 section.
  2. Compare what was delivered against the Phase 0 "Expected outputs" in `docs/planning/phases.md`.
  3. Either mark specific earlier tickets **Needs Rework** with a reason, or confirm the phase outputs are internally consistent enough to close.
- **Acceptance:** The repo contains a concise Phase 0 review result that either lists the required fixes (with ticket-level rework flags) or states the phase is consistent enough to close.
- **Validation:** Verify the review explicitly checks every Phase 0 "Expected output" and every ticket in this file.
- **Dependencies:** P0-E0-T4, P0-E0-T6, P0-E0-T8, P0-E0-T9, P0-E0-T11, P0-E0-T12
- **Status History:**
  - 2026-07-08 — Blocked (ticket created; depends on the rest of Phase 0's execution tickets).

### Ticket P0-E0-T14 — Confirm Phase 1 readiness and record any Phase 0 follow-ups

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Blocked
- **Objective:** Confirm the Phase 0 baseline does not change anything assumed by the already-written Phase 1 (Research) tickets, and record any genuine Phase 0 follow-up work as new tickets rather than silently expanding scope.
- **Scope:** Cross-check `docs/planning/tickets-phase-1.md` against the delivered Phase 0 baseline. Since Phase 1 tickets already exist, this is a reconciliation pass, not a from-scratch planning pass.
- **Steps:**
  1. Re-read `docs/planning/tickets-phase-1.md` and confirm none of its tickets assumed a different local/CI setup than what Phase 0 actually delivered.
  2. If Phase 0 review (P0-E0-T13) found deferred or follow-up work that is not just a rework of an existing ticket, add it as a new ticket in this file with status **Not Started**, rather than leaving it implicit.
  3. Record the reconciliation result (clean handoff, or list of adjustments made) at the end of this file.
- **Acceptance:** The repo states explicitly that Phase 1 tickets remain valid after Phase 0 setup, or lists the adjustments made to either phase's ticket set.
- **Validation:** Verify the reconciliation note cross-references specific ticket IDs in both files rather than making a general claim.
- **Dependencies:** P0-E0-T13
- **Status History:**
  - 2026-07-08 — Blocked (ticket created; depends on the Phase 0 review ticket).

## Current execution order

The smallest **ready now** tickets in the active phase are:

1. **P0-E0-T1** — Scaffold the Python project
2. **P0-E0-T5** — Document branch and commit conventions

Once those land, the next layer unlocks:

3. **P0-E0-T2** — Add local formatting and linting
4. **P0-E0-T3** — Add the local test command
5. **P0-E0-T6** — Add the PR template and document the PR flow

Then the CI/quality layer:

6. **P0-E0-T4** — Add a single local "check" command
7. **P0-E0-T7** — Add the CI workflow for lint and test on every PR
8. **P0-E0-T8** — Add branch protection guidance for `main`
9. **P0-E0-T9** — Wire coverage reporting into CI

Then packaging and release:

10. **P0-E0-T10** — Define the packaging process for the CLI
11. **P0-E0-T11** — Define the release process
12. **P0-E0-T12** — Write the now-vs-later setup boundary note

Finally, the phase-closing sequence:

13. **P0-E0-T13** — Review Phase 0 work for inconsistencies and required changes
14. **P0-E0-T14** — Confirm Phase 1 readiness and record any Phase 0 follow-ups

These stay intentionally narrow so the DevOps baseline can be delivered in small, independently verifiable steps.
