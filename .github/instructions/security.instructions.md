---
applyTo: "{.github/prompts/review-security-workflow.prompt.md,docs/guide/security-rules.md,harmonic-custom/skills/review-security/SKILL.md}"
---

# Security Rules

- Keep the free-stack requirement compatible with safe defaults; free must not mean unsafe.
- Review auth, secrets, input validation, export behavior, logging, and workflow permissions explicitly when they are touched.
- Treat route exports, file imports, and external API calls as security-relevant surfaces.
- Prefer high-signal findings over generic checklist dumping.
