---
allowed-tools: Read, Bash, Grep
license: MIT
description: Execute fireflies.ai production deployment checklist and rollback procedures.
  use when deploying fireflies.ai integrations to production, preparing for launch,
  or implementing go-live procedures. trigger with phrases like "fireflies production",
  "...
name: fireflies-prod-checklist
---
# Fireflies Prod Checklist

This skill provides automated assistance for fireflies prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Fireflies.ai integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Fireflies.ai Status](https://status.fireflies.com)
- [Fireflies.ai Support](https://docs.fireflies.com/support)