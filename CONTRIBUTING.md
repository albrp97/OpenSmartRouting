# Contributing to OpenSmartRouting

This document defines the branch and commit conventions for this repository. It exists so a
contributor (human or AI) can start work without having to ask "what do I name my branch" or
"how do I write my commit message."

## `main` stays deployable

`main` is always expected to be in a working state. Nobody commits directly to `main`; all work
happens on a short-lived branch and lands via a pull request (see the PR flow once
`P0-E0-T6`/`P0-E0-T7` are done for the required checks).

## Branch naming

Branches are named:

```
phase-<phase-number>/p<phase>-e<epic>-t<ticket>-<short-topic>
```

- `<phase-number>` — the phase number the ticket belongs to (e.g. `0`, `1`).
- `p<phase>-e<epic>-t<ticket>` — the ticket ID from the phase's tickets file (e.g. `p0-e0-t5`),
  lowercased.
- `<short-topic>` — a few kebab-case words summarizing the ticket.

Example: `phase-0/p0-e0-t5-branch-commit-conventions`.

If work is not tied to a specific ticket (rare — most work should be), use
`phase-<phase-number>/<short-topic>` instead.

Branches are short-lived: created for one ticket, merged (squash) into `main`, then deleted
(`gh pr merge --delete-branch`, followed by `git fetch --prune` locally).

## Commit messages

Commit messages use an imperative summary line, optionally prefixed with the ticket ID, followed
by a blank line and a short bullet list of what changed:

```
<Ticket ID>: <imperative summary>

- <what changed, bullet 1>
- <what changed, bullet 2>
- Mark <ticket ID> Done with validation notes (if this commit closes a ticket)
```

Example:

```
P0-E0-T4: Add a single local check command

- Add Makefile with check (default), format, lint, test targets
- check depends on format -> lint -> test in sequence, failing fast
- Document make check in README.md
- Mark P0-E0-T4 Done with validation notes
```

Rules:

- Use the imperative mood ("Add", "Fix", "Document"), not past tense ("Added") or gerunds
  ("Adding").
- Keep the summary line short (roughly 50-72 characters); put detail in the bullet list, not the
  summary.
- One commit per ticket is the default; split further only if the ticket's steps are genuinely
  independent and reviewable separately.
- If AI assistance was used to author the commit, include a `Co-authored-by:` trailer for the
  assisting agent, in addition to the human author's own commit identity.

## Ticket status updates are part of the commit

Every ticket in `docs/planning/tickets-phase-N.md` has a `Status` and an append-only
`Status History`. Updating these is not a separate, optional step — it happens in the same
commit (or PR) as the work: mark `In Progress` when starting, and `Done`
(or `Needs Rework` with a reason) when finishing, with a dated history entry each time.

## Pull request flow

- **One PR per ticket.** A PR's scope is exactly one ticket from a `docs/planning/tickets-phase-N.md`
  file. If a ticket turns out to need splitting, split the ticket first, not the PR.
- **Pass `make check` locally before opening the PR.** `make check` runs the full local quality
  gate (format check, lint, tests). A PR should never be opened to "see if CI catches it" —
  validate locally first.
- Every PR uses `.github/PULL_REQUEST_TEMPLATE.md`, which asks for: what changed, which ticket it
  closes, and how it was validated.
- Once CI exists (see the CI ticket in `docs/planning/tickets-phase-0.md`), CI must also pass
  before merging.
- Merge with squash and delete the branch afterward (`gh pr merge --squash --delete-branch`,
  then `git fetch --prune` locally) to keep history linear and branches short-lived.

## Branch protection on `main`

`main` is protected: it requires the `lint-and-test` status check (from
`.github/workflows/pr-checks.yml`) to pass before a PR can be merged, and this is enforced even
for repo admins. Force pushes and branch deletion are also disabled on `main`.

This was applied via the GitHub API:

```bash
gh api --method PUT repos/albrp97/OpenSmartRouting/branches/main/protection \
  --input - <<'EOF'
{
  "required_status_checks": { "strict": true, "contexts": ["lint-and-test"] },
  "enforce_admins": true,
  "required_pull_request_reviews": null,
  "restrictions": null,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF
```

Equivalent manual steps (GitHub UI): **Settings → Branches → Branch protection rules → Add rule**
for `main`, enable "Require status checks to pass before merging" and select `lint-and-test`,
enable "Do not allow bypassing the above settings" (enforces admins too), and disable force pushes
and branch deletion.

If this rule ever needs to change (e.g. adding required reviews once the project has more than
one contributor), update it with the same API call or through the UI, and update this section.

## Secret scanning and push protection

GitHub's native secret scanning and push protection are enabled for this public repository
(free for public repos). Secret scanning flags known credential patterns already committed to the
repo; push protection blocks a push containing a detectable secret before it ever lands in
history. Dependabot security updates are also enabled, so Dependabot can open PRs for known
vulnerable dependencies once any are added.

Confirm the current state at any time with:

```bash
gh api repos/albrp97/OpenSmartRouting --jq '.security_and_analysis'
```

This should show `secret_scanning`, `secret_scanning_push_protection`, and
`dependabot_security_updates` all as `"enabled"`. If a setting is ever `"disabled"`, re-enable it
via the GitHub UI (**Settings → Code security**) or:

```bash
gh api --method PUT repos/albrp97/OpenSmartRouting/vulnerability-alerts
gh api --method PUT repos/albrp97/OpenSmartRouting/automated-security-fixes
```

`.github/workflows/pr-checks.yml` also runs `gitleaks` on every PR as a CI-visible backup to
GitHub's background scanning (see the "Secret scanning" step in that workflow).

## Keeping `uv.lock` in sync

CI runs `uv lock --check` before installing dependencies, so any PR that changes `pyproject.toml`
dependencies without regenerating `uv.lock` will fail fast with a clear error. If you change a
dependency, run `uv lock` locally and commit the updated `uv.lock` alongside your `pyproject.toml`
change.

## Release process

Releases are lean and manual — no automatic version bumping.

- **Versioning:** [Semantic Versioning](https://semver.org/) via git tags of the form `vX.Y.Z`
  (e.g. `v0.1.0`), matching the `version` field in `pyproject.toml`.
- **When to release:** whenever a set of merged changes is worth marking as a usable milestone
  (e.g. end of a phase, or a meaningful CLI capability). Not every merged PR needs a release.
- **Changelog:** every release gets an entry in `CHANGELOG.md` (["Keep a Changelog"](https://keepachangelog.com/en/1.1.0/)
  format) before tagging, describing what changed since the previous release.
- **Cutting a release:**
  1. Update the `version` field in `pyproject.toml` and move the `[Unreleased]` entry in
     `CHANGELOG.md` into a new dated version section.
  2. Commit that on `main` (via a normal PR).
  3. Tag the resulting commit: `git tag vX.Y.Z && git push origin vX.Y.Z`.
  4. Pushing the tag triggers `.github/workflows/release.yml`, which re-runs the full check suite,
     builds the wheel/sdist with `uv build`, and attaches them to a new GitHub Release (tags
     containing a `-`, e.g. `v0.1.0-rc1`, are marked as a pre-release automatically).
- **No PyPI publishing** at this stage — see the "Packaging" section of `README.md`.



