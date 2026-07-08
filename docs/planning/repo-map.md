# OpenSmartRouting Repository Map

This map records the important paths that exist in the repository today.

The repository is still in planning and research setup mode, so several product-code directories are present but not populated yet.

| Path | What it contains | Current role |
| --- | --- | --- |
| `README.md` | Project definition, roadmap, scope, constraints, and open questions. | This is the main source of truth for the product direction. |
| `NEXT_STEPS.md` | Ordered follow-up work after the runtime baseline. | This lists the current planning and research sequence. |
| `vision.md` | Objective, user, problem, success signals, and non-goals. | This captures the planning baseline completed so far. |
| `AGENTS.md` | Repository-level runtime instructions. | This defines how agents should treat the project at a high level. |
| `.github/copilot-instructions.md` | Copilot-specific repository guidance. | This gives the local operating rules for work in this repo. |
| `.github/instructions/` | Path-scoped instruction files. | This applies extra rules to docs, Python, research, review, and experiments work. |
| `.github/prompts/` | Reusable workflow prompt files. | This stores the ordered planning, research, implementation, and review workflows. |
| `.github/workflows/` | GitHub Actions workflow files. | This currently contains workflow-evaluation automation rather than product CI. |
| `harmonic-custom/AGENTS.md` | Local override rules for the shared runtime. | This keeps the repo Python-first, CLI-first, and free-stack-first. |
| `harmonic-custom/config.yml` | Local Harmonic runtime configuration. | This holds repository-specific runtime configuration. |
| `harmonic-custom/skills/` | Local skill entrypoints and skill docs. | This provides reusable workflows such as planning, research, and review skills. |
| `docs/guide/` | Guidance documents such as security and hotspot review rules. | This stores supporting documentation for repo workflows. |
| `docs/planning/` | Planning artifacts for project definition and decomposition. | This is where repo map, scope, capability, and later planning docs live. |
| `docs/research/` | Research notes and stack comparisons. | This is reserved for free-stack and routing research outputs. |
| `docs/specs/` | Product or prototype specification documents. | This is reserved for later MVP and interface specs. |
| `ai-evals/` | Workflow evaluation assets and reports. | This supports evaluation of the markdown workflow setup. |
| `data/` | Placeholder for datasets and data notes. | This is reserved for sample inputs and later experiment data. |
| `experiments/` | Placeholder for experiment scripts or notebooks. | This is reserved for routing and algorithm experiments. |
| `src/` | Placeholder for application source code. | This is where the future Python CLI codebase will live. |
| `tests/` | Placeholder for automated tests. | This is where future test coverage for the routing core will live. |
| `tools/` | Utility scripts for repository maintenance. | This currently contains workflow evaluation tooling. |

## Notes

- Empty directories such as `src/`, `tests/`, `data/`, `experiments/`, `docs/research/`, and `docs/specs/` are present as scaffolding.
- The repository currently contains planning and runtime setup artifacts, but not product implementation yet.
