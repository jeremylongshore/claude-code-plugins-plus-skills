---
allowed-tools: Read, Grep, Bash
license: MIT
description: Execute production deployment checklist for sentry integration. use when
  preparing for production deployment, reviewing sentry configuration, or verifying
  production readiness. trigger with phrases like "sentry production", "deploy sentry",
  "sentr...
name: sentry-prod-checklist
---
# Sentry Prod Checklist

This skill provides automated assistance for sentry prod checklist tasks.

## Prerequisites

- Sentry account with project created
- Production DSN separate from development/staging
- Build pipeline with source map generation
- sentry-cli installed and configured with auth token

## Instructions

1. Configure production DSN via environment variables (never hardcode)
2. Set environment to "production" and configure release version
3. Generate source maps during build process
4. Upload source maps using sentry-cli releases commands
5. Verify security settings (sendDefaultPii: false, debug: false)
6. Configure appropriate sample rates for production volume
7. Set up alert rules with team notification channels
8. Connect source control and issue tracker integrations
9. Run verification test to confirm error capture and source maps
10. Document rollback procedure for emergency disable

## Output

- Production-ready Sentry configuration
- Verified source map uploads
- Configured alert rules and notifications
- Documented release workflow
- Validated error capture with test events

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Production Checklist](https://docs.sentry.io/product/releases/setup/)
- [Sentry Release Health](https://docs.sentry.io/product/releases/health/)