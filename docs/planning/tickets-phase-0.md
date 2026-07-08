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
- **Status:** Done
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
  - 2026-07-08 — In Progress (`ruff` already a dev dependency from T1; adding `[tool.ruff]` config and running format/check).
  - 2026-07-08 — Done. Added `[tool.ruff]`/`[tool.ruff.lint]`/`[tool.ruff.format]` config to `pyproject.toml` (line-length 100, py311 target, E/F/I/UP/B/SIM rule set, double-quote format). `ruff format .` reformatted `tools/eval_workflows.py` only (pure whitespace, no behavior change). `ruff format --check .` and `ruff check .` both pass clean; `pytest` still 2 passed.

### Ticket P0-E0-T3 — Add the local test command

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P0
- **Status:** Done
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
  - 2026-07-08 — In Progress (`pytest` dependency and a scaffold smoke test already exist from T1; confirming discovery/verbosity and formalizing this as the official local test command).
  - 2026-07-08 — Done. Confirmed via `uv run pytest -v` that `pytest` (configured through `[tool.pytest.ini_options]` in `pyproject.toml`, `testpaths = ["tests"]`) discovers and runs both scaffold tests (`test_package_has_version`, `test_cli_main_runs`), 2 passed. `uv run pytest` is already documented in `README.md` as the local test command (added in T1). `.pytest_cache/` already gitignored. No code changes needed beyond what T1 provided; this ticket formally validates and closes the acceptance criteria.

### Ticket P0-E0-T4 — Add a single local "check" command

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Done
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
  - 2026-07-08 — In Progress (adding a Makefile with a `check` target wired to ruff format-check, ruff check, and pytest).
  - 2026-07-08 — Done. Added `Makefile` with `check` (default), `format`, `lint`, `test` targets; `check` depends on all three in sequence so make's own dependency resolution fails fast at the first broken step. Validated against a clean repo (`make check` → exit 0, all three gates pass) and three deliberately broken cases (bad formatting, unused-import lint error, failing assertion) — each stopped `make check` at the correct step with a clear error and non-zero exit code. Documented `make check` in `README.md`.

### Ticket P0-E0-T5 — Document branch and commit conventions

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Done
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
  - 2026-07-08 — In Progress (writing `CONTRIBUTING.md`, formalizing the branch/commit convention already used in P0-E0-T1 through T4).
  - 2026-07-08 — Done. Added `CONTRIBUTING.md` documenting: `main` stays deployable, branch naming (`phase-<n>/p<phase>-e<epic>-t<ticket>-<short-topic>`), commit message format (ticket-ID-prefixed imperative summary + bullet list + `Co-authored-by` when AI-assisted), and that ticket Status/Status History updates are part of the same commit. Linked from `README.md`'s local development setup section. Re-read against the acceptance criteria: answers both "what do I name my branch" and "how do I write my commit message" unambiguously, matching the convention already used in T1-T4.

### Ticket P0-E0-T6 — Add the PR template and document the PR flow

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Done
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
  - 2026-07-08 — In Progress (adding `.github/PULL_REQUEST_TEMPLATE.md` and a PR-flow section in `CONTRIBUTING.md`).
  - 2026-07-08 — Done. Added `.github/PULL_REQUEST_TEMPLATE.md` (Ticket/What changed/Validation/Scope fields) and a "Pull request flow" section in `CONTRIBUTING.md` (one PR per ticket, `make check` must pass before opening, squash-merge + delete branch + prune). Validated by opening this ticket's own PR as a draft with `gh pr create --draft` and confirming the template auto-populated the body with all required fields before filling it in and marking it ready.

### Ticket P0-E0-T7 — Add the CI workflow for lint and test on every PR

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P0
- **Status:** Done
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
  - 2026-07-08 — In Progress (adding `.github/workflows/pr-checks.yml` using `astral-sh/setup-uv` with caching, mirroring the local `make check` steps).
  - 2026-07-08 — Done. Added `.github/workflows/pr-checks.yml` (checkout, `astral-sh/setup-uv@v7` with cache, `uv sync`, `ruff format --check`, `ruff check`, `pytest`). Validated live on PR #7: passed on the clean scaffold, then a deliberate `import os` lint break pushed to the same PR made `lint-and-test` fail (11s), then reverting it made it pass again. CI now blocks on lint/test failures on every PR to `main`.

### Ticket P0-E0-T8 — Add branch protection guidance for `main`

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Done
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
  - 2026-07-08 — In Progress (applying branch protection via the GitHub API, then documenting it in `CONTRIBUTING.md`).
  - 2026-07-08 — Done. Confirmed the acting account (albrp97) has repo admin rights, then applied branch protection on `main` via the GitHub API: required status check `lint-and-test`, `enforce_admins: true`, force pushes and branch deletion disabled. Live-validated: pushed a deliberate lint break on a throwaway PR (#8), confirmed CI failed, then confirmed `gh pr merge` was rejected with "the base branch policy prohibits the merge" (no `--admin` override used) — closed and deleted that test PR/branch afterward. Documented the exact `gh api` command and the equivalent manual GitHub UI steps in `CONTRIBUTING.md`.

### Ticket P0-E0-T9 — Wire coverage reporting into CI

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Done
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
  - 2026-07-08 — In Progress (adding `pytest-cov`, wiring `--cov` into `make test`/CI, and publishing a coverage summary in the CI job).
  - 2026-07-08 — Done. Added `pytest-cov` dev dependency, `[tool.coverage.run]`/`[tool.coverage.report]` config, updated `make test` and `pr-checks.yml` to run `pytest --cov=opensmartrouting --cov-report=term-missing --cov-report=html`, publish the term-missing table to `$GITHUB_STEP_SUMMARY`, and upload the HTML report as a workflow artifact. No coverage threshold gating. Live-validated on PR #10: CI log shows the coverage table (83% total, per-file breakdown), and `coverage-html-report` artifact confirmed present via the GitHub API. Locally, `make check`/`uv run pytest --cov=...` shows the same table.

### Ticket P0-E0-T10 — Define the packaging process for the CLI

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Done
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
  - 2026-07-08 — In Progress (running `uv build`, then validating the wheel installs cleanly in a scratch venv).
  - 2026-07-08 — Done. `uv build` produces both `opensmartrouting-0.0.1-py3-none-any.whl` and the sdist `opensmartrouting-0.0.1.tar.gz` in `dist/` using the existing `hatchling` backend. Validated by installing the wheel into a fresh scratch venv (`uv venv` + `uv pip install`) and confirming both `opensmartrouting` (CLI entry point) and `python -c "import opensmartrouting"` work from the installed package, not just the dev checkout. Documented the build/install commands in `README.md`'s new "Packaging" section, and explicitly noted PyPI publishing is out of scope (personal/local CLI use case). `dist/` is already gitignored.

### Ticket P0-E0-T11 — Define the release process (versioning, tagging, changelog)

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Done
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
  - 2026-07-08 — In Progress (adding `CHANGELOG.md`, documenting the tagging convention, and adding `.github/workflows/release.yml`).
  - 2026-07-08 — Done. Live-validated by pushing a real `v0.0.1-test` tag (PR #12 merged first): the `Release` workflow ran, built the package, and created a GitHub Release marked `prerelease: true` (tag contains a hyphen). First run surfaced a real bug — `uv build`'s own generated `dist/.gitignore` was picked up by `files: dist/*` and attached as an unwanted `default.gitignore` asset alongside the wheel/sdist. Fixed in a follow-up PR (#13, merged) by restricting `files` to `dist/*.whl` and `dist/*.tar.gz` explicitly. Re-ran the same live tag validation against the fixed workflow: confirmed via `gh release view` that only `opensmartrouting-0.0.1-py3-none-any.whl` and `opensmartrouting-0.0.1.tar.gz` were attached, `prerelease: true`, and auto-generated release notes listed PRs #1-#13. Cleaned up: deleted the test GitHub Release (`gh release delete`) and the test tag both locally and on the remote.

### Ticket P0-E0-T12 — Add type checking with mypy

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Not Started
- **Objective:** Catch type errors before real routing/geocoding code makes them expensive to find.
- **Scope:** Add `mypy` as a dev dependency, a minimal `[tool.mypy]` config, a `make lint-types` (or fold into `make lint`) target, and a CI step.
- **Steps:**
  1. Add `mypy` to the dev dependency group and a `[tool.mypy]` config scoped to `src/`.
  2. Add a `Makefile` target and wire it into `make check`.
  3. Add a `mypy` step to `.github/workflows/pr-checks.yml`.
- **Acceptance:** `make check` and the PR CI both run `mypy` and fail on a deliberate type error.
- **Validation:** Introduce a deliberate type error locally and in a live PR, confirm both `make check` and CI fail, then fix and confirm both pass.
- **Dependencies:** P0-E0-T4, P0-E0-T7
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).
  - 2026-07-08 — In Progress (adding `mypy` dev dependency, `[tool.mypy]` config, `Makefile` target, and CI step).
  - 2026-07-08 — Done. Locally validated: introduced a deliberate type error in `cli.py` (well-formatted, lint-clean) — `make check` stopped at `types` with a clear mypy error; reverted and confirmed `make check` passes with 83% coverage. Live-validated on PR #16: CI passed clean first, then a deliberate type-error commit made the `Type check` step fail (`lint-and-test` job failed), then a revert commit restored a passing CI run.

### Ticket P0-E0-T13 — Add dependency vulnerability scanning with pip-audit

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Not Started
- **Objective:** Detect known-vulnerable dependencies automatically.
- **Scope:** Add `pip-audit` as a dev dependency and a CI step that runs it against the resolved environment.
- **Steps:**
  1. Add `pip-audit` to the dev dependency group.
  2. Add a CI step running `uv run pip-audit`.
  3. Document the check in `docs/guide/quality-gates.md`.
- **Acceptance:** CI runs `pip-audit` on every PR and the run is visible in the CI logs.
- **Validation:** Confirm a live PR's CI run shows the `pip-audit` step executing and passing against the current (empty) dependency set.
- **Dependencies:** P0-E0-T7
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).
  - 2026-07-08 — In Progress (adding `pip-audit` dev dependency and CI step).
  - 2026-07-08 — Done. Validated locally (`uv run pip-audit` exits 0, "No known vulnerabilities found" against the current empty runtime-dependency set) and live on PR #17 where the `Dependency vulnerability scan` CI step ran and passed.

### Ticket P0-E0-T14 — Add Dependabot configuration

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Not Started
- **Objective:** Get automated pull requests for outdated or vulnerable dependencies and GitHub Actions versions.
- **Scope:** Add `.github/dependabot.yml` covering the `pip` (via `uv`-managed `pyproject.toml`) and `github-actions` ecosystems.
- **Steps:**
  1. Add `.github/dependabot.yml` with weekly update schedules for both ecosystems.
  2. Confirm via the GitHub UI/API that Dependabot recognizes the config (no errors on the repo's Dependabot page).
- **Acceptance:** GitHub's Dependabot config validation shows no errors for the repo.
- **Validation:** Check `gh api repos/albrp97/OpenSmartRouting/dependabot/... ` or the repo's Insights > Dependency graph > Dependabot page for a valid, error-free config.
- **Dependencies:** none
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T15 — Enable GitHub secret scanning and push protection

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Not Started
- **Objective:** Prevent secrets from ever landing in the repo's history.
- **Scope:** Enable GitHub's native secret scanning and push protection for the repository (free for public repos) and document the setting.
- **Steps:**
  1. Enable secret scanning and push protection via `gh api` or the repo Settings > Code security page.
  2. Confirm the settings are active via `gh api repos/albrp97/OpenSmartRouting`.
  3. Document the setting in `CONTRIBUTING.md`.
- **Acceptance:** The repo shows secret scanning and push protection both enabled.
- **Validation:** Query the repo's security-and-analysis settings via the API and confirm both features report `enabled`.
- **Dependencies:** none
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T16 — Add gitleaks as a CI secret-scanning backup

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Not Started
- **Objective:** Add a second, explicit secret-scanning layer that runs in CI and fails the PR, rather than relying solely on GitHub's background scanning.
- **Scope:** Add a `gitleaks` CI job that scans the PR diff and fails on any finding.
- **Steps:**
  1. Add a `gitleaks` step/job to `.github/workflows/pr-checks.yml` (or a dedicated workflow) using the free `gitleaks-action`.
  2. Confirm it runs on every PR.
- **Acceptance:** A live PR containing a deliberately fake secret fails the gitleaks check; a clean PR passes.
- **Validation:** Push a fake, clearly-non-functional secret-shaped string to a throwaway PR branch, confirm gitleaks fails the check, then remove it and confirm the check passes.
- **Dependencies:** P0-E0-T7
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T17 — Add CodeQL static analysis

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Not Started
- **Objective:** Add free SAST coverage for common vulnerability classes beyond linting.
- **Scope:** Add `.github/workflows/codeql.yml` using `github/codeql-action` for Python, triggered on PRs to `main` and a weekly schedule.
- **Steps:**
  1. Add the CodeQL workflow for the `python` language.
  2. Confirm the workflow runs and reports to the repo's Security > Code scanning tab.
- **Acceptance:** CodeQL runs successfully and its results are visible under the repo's code scanning alerts.
- **Validation:** Confirm via `gh api repos/albrp97/OpenSmartRouting/code-scanning/alerts` (or the Security tab) that CodeQL has run and reported a status (even if zero alerts).
- **Dependencies:** none
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T18 — Add dead code detection with vulture

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P3
- **Status:** Not Started
- **Objective:** Catch unused functions, classes, and variables that ruff's unused-import checks do not cover.
- **Scope:** Add `vulture` as a dev dependency, a `make` target, and a CI step, with a whitelist file if needed for false positives.
- **Steps:**
  1. Add `vulture` to the dev dependency group.
  2. Add a `Makefile` target and wire it into `make check`.
  3. Add a CI step; add a `vulture_whitelist.py` only if genuine false positives appear.
- **Acceptance:** `make check` and CI both run `vulture` and fail on a deliberately introduced unused function.
- **Validation:** Introduce a deliberately unused function locally, confirm `make check` fails, remove it, confirm it passes; confirm the same in a live PR's CI.
- **Dependencies:** P0-E0-T4, P0-E0-T7
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T19 — Gate CI on a minimum coverage threshold

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Not Started
- **Objective:** Fail the build if test coverage drops below an agreed floor, instead of only reporting it.
- **Scope:** Add `--cov-fail-under` to the pytest coverage invocation (local `make test` and CI), set at a floor consistent with the current coverage level.
- **Steps:**
  1. Check current coverage percentage from the existing coverage report.
  2. Set `--cov-fail-under` (via `[tool.coverage.report]` `fail_under` or the CLI flag) at or slightly below current coverage.
  3. Update `Makefile` and `.github/workflows/pr-checks.yml` accordingly.
- **Acceptance:** A live PR that drops coverage below the threshold fails CI; a PR at or above the threshold passes.
- **Validation:** Add a deliberately untested branch of code in a throwaway PR to drop coverage below the threshold, confirm CI fails, then remove it and confirm CI passes.
- **Dependencies:** P0-E0-T9
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T20 — Add a lockfile drift check to CI

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P3
- **Status:** Not Started
- **Objective:** Catch cases where `pyproject.toml` changed but `uv.lock` was not regenerated.
- **Scope:** Add a CI step that runs `uv lock --check` (or `uv sync --locked`) and fails if the lockfile is out of date.
- **Steps:**
  1. Add a `uv lock --check` (or equivalent) step to `.github/workflows/pr-checks.yml`, placed before `uv sync`.
  2. Document the check in `CONTRIBUTING.md`.
- **Acceptance:** A live PR with a `pyproject.toml` dependency change but a stale `uv.lock` fails CI at this step.
- **Validation:** Deliberately edit `pyproject.toml` without updating `uv.lock` in a throwaway PR, confirm the drift check fails, then regenerate the lock and confirm it passes.
- **Dependencies:** P0-E0-T7
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T21 — Add a post-build smoke test to the release workflow

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Not Started
- **Objective:** Catch a broken package before it reaches a GitHub Release, beyond "it built without error."
- **Scope:** After `uv build` in `.github/workflows/release.yml`, install the built wheel into a fresh virtual environment and run the CLI entry point.
- **Steps:**
  1. Add steps to `release.yml`: create a scratch venv, `pip install dist/*.whl`, run `opensmartrouting` and confirm it exits 0.
  2. Confirm the step runs on the next live tag validation.
- **Acceptance:** The release workflow fails if the built wheel's CLI entry point cannot run in a clean environment.
- **Validation:** Push a test tag and confirm the smoke-test step runs and passes against the real built wheel (reuse the test-tag/cleanup pattern from P0-E0-T11).
- **Dependencies:** P0-E0-T11
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T22 — Add a broken-link checker for docs

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P3
- **Status:** Not Started
- **Objective:** Keep the heavily cross-referenced planning docs and README free of broken internal/external links.
- **Scope:** Add a CI job (e.g. `lycheeverse/lychee-action`) that checks links in `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, and `docs/**/*.md`, running only when those files change.
- **Steps:**
  1. Add a `docs-links` job triggered on PRs touching Markdown files.
  2. Configure a lychee config to ignore known-flaky or intentionally-unresolvable links (e.g. localhost examples).
- **Acceptance:** A live PR containing a deliberately broken internal link fails the check; removing it passes.
- **Validation:** Introduce a broken relative link in a throwaway PR, confirm the check fails, fix it, confirm it passes.
- **Dependencies:** none
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T23 — Add schema linting for harmonic-custom/config.yml

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P3
- **Status:** Not Started
- **Objective:** Catch malformed YAML/config drift in `harmonic-custom/config.yml` before it silently breaks the runtime.
- **Scope:** Add a lightweight YAML syntax/schema check (e.g. `yamllint`, or a minimal JSON-schema check via `python -c`) covering `harmonic-custom/config.yml` and other repo-controlled YAML (`.github/workflows/*.yml`, `.github/dependabot.yml`).
- **Steps:**
  1. Add `yamllint` (or equivalent) as a dev dependency with a minimal, low-noise config.
  2. Add a `Makefile` target and a CI step.
- **Acceptance:** A live PR with deliberately invalid YAML in `harmonic-custom/config.yml` fails the check; valid YAML passes.
- **Validation:** Introduce a YAML syntax error in a throwaway PR, confirm the check fails, fix it, confirm it passes.
- **Dependencies:** P0-E0-T7
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T24 — Write the now-vs-later setup boundary note

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P2
- **Status:** Not Started
- **Objective:** Make explicit what is intentionally deferred so later phases do not re-litigate setup decisions.
- **Scope:** Confirm `docs/guide/quality-gates.md` (added alongside this batch of tickets) fully covers the now-vs-later boundary; add any missing deferred items and trigger conditions found during execution of T12–T23.
- **Steps:**
  1. Re-read `docs/guide/quality-gates.md`'s "Deferred, with trigger condition" table against what was actually decided while executing T12–T23.
  2. Add any deferred item discovered during execution that is not already listed (e.g. a check that turned out to be too costly to add now).
  3. Cross-check the list against `docs/planning/phases.md` Phase 0 non-goals.
- **Acceptance:** `docs/guide/quality-gates.md` is a clear, short now-vs-later note that later phases can point to instead of re-deciding setup scope.
- **Validation:** Confirm the note is consistent with `docs/planning/phases.md` Phase 0 and does not contradict any ticket in this file.
- **Dependencies:** P0-E0-T7, P0-E0-T9, P0-E0-T11, P0-E0-T12, P0-E0-T13, P0-E0-T14, P0-E0-T15, P0-E0-T16, P0-E0-T17, P0-E0-T18, P0-E0-T19, P0-E0-T20, P0-E0-T21, P0-E0-T22, P0-E0-T23
- **Status History:**
  - 2026-07-08 — Not Started (ticket created).

### Ticket P0-E0-T25 — Review Phase 0 work for inconsistencies and required changes

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Blocked
- **Objective:** Review the completed Phase 0 work as a whole and identify inconsistencies, gaps, or changes needed before the phase is considered closed.
- **Scope:** Review all Phase 0 artifacts together (scaffolding, CI workflows, docs, conventions) for contradictions, missing links, or drift between what was planned and what was actually built. Rework or re-open earlier tickets in this file if the review finds real gaps.
- **Steps:**
  1. Re-read the Phase 0 artifacts together: `pyproject.toml`, CI workflow files, `README.md`/`CONTRIBUTING.md` conventions, `CHANGELOG.md`, `docs/guide/quality-gates.md`, and `docs/planning/phases.md` Phase 0 section.
  2. Compare what was delivered against the Phase 0 "Expected outputs" in `docs/planning/phases.md`.
  3. Either mark specific earlier tickets **Needs Rework** with a reason, or confirm the phase outputs are internally consistent enough to close.
- **Acceptance:** The repo contains a concise Phase 0 review result that either lists the required fixes (with ticket-level rework flags) or states the phase is consistent enough to close.
- **Validation:** Verify the review explicitly checks every Phase 0 "Expected output" and every ticket in this file.
- **Dependencies:** P0-E0-T4, P0-E0-T6, P0-E0-T8, P0-E0-T9, P0-E0-T11, P0-E0-T12, P0-E0-T13, P0-E0-T14, P0-E0-T15, P0-E0-T16, P0-E0-T17, P0-E0-T18, P0-E0-T19, P0-E0-T20, P0-E0-T21, P0-E0-T22, P0-E0-T23, P0-E0-T24
- **Status History:**
  - 2026-07-08 — Blocked (ticket created; depends on the rest of Phase 0's execution tickets).

### Ticket P0-E0-T26 — Confirm Phase 1 readiness and record any Phase 0 follow-ups

- **Phase:** Phase 0 — Delivery workflow and DevOps setup
- **Epic:** Epic 0 — Delivery workflow and DevOps setup
- **Priority:** P1
- **Status:** Blocked
- **Objective:** Confirm the Phase 0 baseline does not change anything assumed by the already-written Phase 1 (Research) tickets, and record any genuine Phase 0 follow-up work as new tickets rather than silently expanding scope.
- **Scope:** Cross-check `docs/planning/tickets-phase-1.md` against the delivered Phase 0 baseline. Since Phase 1 tickets already exist, this is a reconciliation pass, not a from-scratch planning pass.
- **Steps:**
  1. Re-read `docs/planning/tickets-phase-1.md` and confirm none of its tickets assumed a different local/CI setup than what Phase 0 actually delivered.
  2. If Phase 0 review (P0-E0-T25) found deferred or follow-up work that is not just a rework of an existing ticket, add it as a new ticket in this file with status **Not Started**, rather than leaving it implicit.
  3. Record the reconciliation result (clean handoff, or list of adjustments made) at the end of this file.
- **Acceptance:** The repo states explicitly that Phase 1 tickets remain valid after Phase 0 setup, or lists the adjustments made to either phase's ticket set.
- **Validation:** Verify the reconciliation note cross-references specific ticket IDs in both files rather than making a general claim.
- **Dependencies:** P0-E0-T25
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

Then the expanded quality-gate layer (see `docs/guide/quality-gates.md`), each independent and can run in any order:

12. **P0-E0-T12** — Add type checking with mypy
13. **P0-E0-T13** — Add dependency vulnerability scanning with pip-audit
14. **P0-E0-T14** — Add Dependabot configuration
15. **P0-E0-T15** — Enable GitHub secret scanning and push protection
16. **P0-E0-T16** — Add gitleaks as a CI secret-scanning backup
17. **P0-E0-T17** — Add CodeQL static analysis
18. **P0-E0-T18** — Add dead code detection with vulture
19. **P0-E0-T19** — Gate CI on a minimum coverage threshold
20. **P0-E0-T20** — Add a lockfile drift check to CI
21. **P0-E0-T21** — Add a post-build smoke test to the release workflow
22. **P0-E0-T22** — Add a broken-link checker for docs
23. **P0-E0-T23** — Add schema linting for harmonic-custom/config.yml

Finally, the phase-closing sequence:

24. **P0-E0-T24** — Write the now-vs-later setup boundary note
25. **P0-E0-T25** — Review Phase 0 work for inconsistencies and required changes
26. **P0-E0-T26** — Confirm Phase 1 readiness and record any Phase 0 follow-ups

These stay intentionally narrow so the DevOps baseline can be delivered in small, independently verifiable steps.
