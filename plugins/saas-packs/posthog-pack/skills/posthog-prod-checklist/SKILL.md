---
name: posthog-prod-checklist
description: |
  Execute posthog production deployment checklist and rollback procedures. use when deploying posthog integrations to production, preparing for launch, or implementing go-live procedures. trigger with phrases like "posthog production", "deploy posth...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Posthog Prod Checklist

This skill provides automated assistance for posthog prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed PostHog integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [PostHog Status](https://status.posthog.com)
- [PostHog Support](https://docs.posthog.com/support)