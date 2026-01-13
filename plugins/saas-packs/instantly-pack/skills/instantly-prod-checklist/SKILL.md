---
name: instantly-prod-checklist
description: |
  Execute instantly production deployment checklist and rollback procedures. use when deploying instantly integrations to production, preparing for launch, or implementing go-live procedures. trigger with phrases like "instantly production", "deploy...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Instantly Prod Checklist

This skill provides automated assistance for instantly prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Instantly integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Instantly Status](https://status.instantly.com)
- [Instantly Support](https://docs.instantly.com/support)