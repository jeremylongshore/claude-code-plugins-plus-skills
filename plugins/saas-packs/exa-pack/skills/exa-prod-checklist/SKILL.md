---
allowed-tools: Read, Bash, Grep
license: MIT
description: Execute exa production deployment checklist and rollback procedures.
  use when deploying exa integrations to production, preparing for launch, or implementing
  go-live procedures. trigger with phrases like "exa production", "deploy exa", "exa
  go-liv...
name: exa-prod-checklist
---
# Exa Prod Checklist

This skill provides automated assistance for exa prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Exa integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Exa Status](https://status.exa.com)
- [Exa Support](https://docs.exa.com/support)