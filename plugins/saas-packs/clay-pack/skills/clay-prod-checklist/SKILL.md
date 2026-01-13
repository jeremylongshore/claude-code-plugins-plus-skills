---
name: clay-prod-checklist
description: |
  Execute clay production deployment checklist and rollback procedures. use when deploying clay integrations to production, preparing for launch, or implementing go-live procedures. trigger with phrases like "clay production", "deploy clay", "clay g...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Clay Prod Checklist

This skill provides automated assistance for clay prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Clay integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Clay Status](https://status.clay.com)
- [Clay Support](https://docs.clay.com/support)