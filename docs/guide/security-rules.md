# OpenSmartRouting Security Rules

> Practical security rules for a free routing and export workflow.

## Main rule

Keep security concrete and relevant to the actual product surfaces.

## Important surfaces

1. address input files
2. export files
3. API keys or credentials if geocoding or routing services are used
4. logs that may contain addresses or user data
5. CI workflows that use secrets or publish artifacts

## Required checks

- do not commit secrets
- validate imported address data
- review export formats for unsafe assumptions
- avoid logging sensitive user data unnecessarily
- review external service trust and rate-limit handling
