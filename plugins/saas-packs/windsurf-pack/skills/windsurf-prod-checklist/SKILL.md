---
name: windsurf-prod-checklist
description: |
  Execute windsurf production deployment checklist and rollback procedures. use when deploying windsurf integrations to production, preparing for launch, or implementing go-live procedures. trigger with phrases like "windsurf production", "deploy wi...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Windsurf Prod Checklist

This skill provides automated assistance for windsurf prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Windsurf integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Windsurf Status](https://status.windsurf.com)
- [Windsurf Support](https://docs.windsurf.com/support)