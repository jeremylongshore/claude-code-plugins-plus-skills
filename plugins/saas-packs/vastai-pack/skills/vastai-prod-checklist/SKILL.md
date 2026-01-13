---
name: vastai-prod-checklist
description: |
  Execute vast.ai production deployment checklist and rollback procedures. use when deploying vast.ai integrations to production, preparing for launch, or implementing go-live procedures. trigger with phrases like "vastai production", "deploy vastai...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Vastai Prod Checklist

This skill provides automated assistance for vastai prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Vast.ai integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Vast.ai Status](https://status.vastai.com)
- [Vast.ai Support](https://docs.vastai.com/support)