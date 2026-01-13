---
name: retellai-prod-checklist
description: |
  Execute retell ai production deployment checklist and rollback procedures. use when deploying retell ai integrations to production, preparing for launch, or implementing go-live procedures. trigger with phrases like "retellai production", "deploy ...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Retellai Prod Checklist

This skill provides automated assistance for retellai prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Retell AI integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Retell AI Status](https://status.retellai.com)
- [Retell AI Support](https://docs.retellai.com/support)