---
name: vercel-prod-checklist
description: |
  Execute Vercel production deployment checklist and rollback procedures.
  Use when deploying Vercel integrations to production, preparing for launch,
  or implementing go-live procedures.
  Trigger with phrases like "vercel production", "deploy vercel",
  "vercel go-live", "vercel launch checklist".
allowed-tools: Read, Bash, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Vercel Prod Checklist

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Vercel integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Vercel Status](https://www.vercel-status.com)
- [Vercel Support](https://vercel.com/docs/support)
