---
allowed-tools: Read, Bash, Grep
license: MIT
description: Execute coderabbit production deployment checklist and rollback procedures.
  use when deploying coderabbit integrations to production, preparing for launch,
  or implementing go-live procedures. trigger with phrases like "coderabbit production",
  "dep...
name: coderabbit-prod-checklist
---
# Coderabbit Prod Checklist

This skill provides automated assistance for coderabbit prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed CodeRabbit integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [CodeRabbit Status](https://status.coderabbit.com)
- [CodeRabbit Support](https://docs.coderabbit.com/support)