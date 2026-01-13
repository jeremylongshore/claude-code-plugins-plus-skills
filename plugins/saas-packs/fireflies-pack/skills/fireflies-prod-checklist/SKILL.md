---
name: fireflies-prod-checklist
description: |
  Execute fireflies.ai production deployment checklist and rollback procedures. use when deploying fireflies.ai integrations to production, preparing for launch, or implementing go-live procedures. trigger with phrases like "fireflies production", "...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
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