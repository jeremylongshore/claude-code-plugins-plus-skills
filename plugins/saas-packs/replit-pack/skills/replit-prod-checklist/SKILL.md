---
name: replit-prod-checklist
description: |
  Execute replit production deployment checklist and rollback procedures. use when deploying replit integrations to production, preparing for launch, or implementing go-live procedures. trigger with phrases like "replit production", "deploy replit",...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Replit Prod Checklist

This skill provides automated assistance for replit prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Replit integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Replit Status](https://status.replit.com)
- [Replit Support](https://docs.replit.com/support)