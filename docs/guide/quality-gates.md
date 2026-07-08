# OpenSmartRouting Quality Gate Menu

> The full menu of delivery-quality checks considered for this project, split into what
> Phase 0 activates now and what is deliberately deferred. This is the canonical
> reference for "why isn't X in CI yet" questions in later phases — check here before
> re-litigating setup scope.

## How items were chosen

A check is activated in Phase 0 when it is free, low-effort to run on a small Python
CLI scaffold, and gives useful signal even before routing logic exists. A check is
deferred when it needs product surface that does not exist yet (APIs, containers,
long-running processes, real geodata schemas) or when its setup cost is not justified
until there is more code to protect.

## Active now (Phase 0)

| Area | Check | Where | Ticket |
|---|---|---|---|
| Static analysis | Lint/format (ruff) | local `make check`, CI | P0-E0-T2, T7 |
| Type & correctness | Type checking (mypy) | local `make check`, CI | P0-E0-T12 |
| Type & correctness | Dead code detection beyond unused imports (vulture) | local `make check`, CI | P0-E0-T18 |
| Dependency & supply chain | Vulnerability scanning (pip-audit) | CI | P0-E0-T13 |
| Dependency & supply chain | Automated dependency + Actions updates (Dependabot) | GitHub-native | P0-E0-T14 |
| Dependency & supply chain | Lockfile drift check (`uv lock --check`) | CI | P0-E0-T20 |
| Security | Secret scanning + push protection (GitHub-native) | repo settings | P0-E0-T15 |
| Security | Secret scanning CI backup (gitleaks) | CI | P0-E0-T16 |
| Security | SAST (CodeQL) | CI (scheduled + PR) | P0-E0-T17 |
| Testing | Unit tests + coverage reporting | local `make check`, CI | P0-E0-T9 |
| Testing | Coverage threshold gate | CI | P0-E0-T19 |
| Runtime/behavioral | Post-build smoke test (install wheel, run CLI) | release workflow | P0-E0-T21 |
| Docs & data integrity | Broken link checker | CI (docs changes) | P0-E0-T22 |
| Docs & data integrity | Config/schema lint (`harmonic-custom/config.yml`) | CI | P0-E0-T23 |
| Reproducibility | Pre-commit hooks mirroring CI checks | local, opt-in | P0-E0-T26 |

## Deferred, with trigger condition

| Area | Check | Why deferred | Revisit when |
|---|---|---|---|
| Dependency & supply chain | License compliance checks | No dependencies yet with ambiguous licenses; no external distribution | Before publishing to PyPI, or when a new dependency's license is unclear |
| Dependency & supply chain | SBOM generation | No external consumers of build artifacts yet | Before publishing to PyPI or distributing built artifacts outside the team |
| Dependency & supply chain | Dependency CVE **gating** (fail build on critical/high) beyond pip-audit reporting | Zero runtime dependencies today, so there is nothing to gate on yet; pip-audit already reports | Once `dependencies` in `pyproject.toml` is non-empty |
| Testing | Integration tests | No integration surface exists (no geocoding/routing calls yet) | Phase 2 (Experiments) once real external services are wired in |
| Testing | Mutation testing (mutmut) | Needs meaningful unit tests around real logic first; expensive to run per-PR | Phase 3 (Python MVP) once routing/optimization logic exists |
| Testing | Property-based/fuzz testing | No routing algorithm exists yet to fuzz | Phase 2/3 once routing and optimization code exists |
| Testing | Contract tests | No APIs exposed by this project | If/when OpenSmartRouting exposes an API (not currently planned) |
| Runtime/behavioral | Performance/regression benchmarks | No routing algorithm to benchmark yet | Phase 2 (Experiments) once route-cost comparisons exist |
| Runtime/behavioral | Memory/resource leak checks | CLI is short-lived, not a long-running process | If a long-running process (e.g. a service) is ever introduced |
| Reproducibility & build health | Docker image scanning | Project is not containerized | If/when a Dockerfile is added |
| Docs & data integrity | Data schema validation (routing input/output geodata) | No routing input/output schema exists yet | Phase 3 (Python MVP) once the CLI defines real input/output formats |

## Notes

- All active checks use free tooling only (GitHub Actions free tier, GitHub-native
  secret scanning/Dependabot on a public repo, open-source CLI tools), consistent with
  the project's free-first constraint.
- Static analysis, dependency scanning, and secret scanning run on every PR. CodeQL
  also runs on a schedule since it is slower. Pre-commit hooks are opt-in locally (not
  enforced in CI) to keep local setup friction low while still catching most issues
  before push.
