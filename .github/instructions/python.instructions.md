---
applyTo: "src/**/*.py"
---

# Python Rules

- Keep routing, geocoding, optimization, input parsing, and output formatting separated by responsibility.
- Prefer typed Python with clear function boundaries.
- Keep the routing core testable without mobile or UI dependencies.
- Do not introduce paid APIs or proprietary dependencies without explicit approval.
- Optimize for reproducible experiments before optimizing for framework sophistication.
