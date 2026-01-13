---
allowed-tools: Read, Bash, Grep
license: MIT
description: Execute vercel production deployment checklist and rollback procedures.
  use when deploying vercel integrations to production, preparing for launch, or implementing
  go-live procedures. trigger with phrases like "vercel production", "deploy vercel",...
name: vercel-prod-checklist
---
# Vercel Prod Checklist

This skill provides automated assistance for vercel prod checklist tasks.

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