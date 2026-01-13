---
allowed-tools: Read, Bash, Grep
license: MIT
description: Execute groq production deployment checklist and rollback procedures.
  use when deploying groq integrations to production, preparing for launch, or implementing
  go-live procedures. trigger with phrases like "groq production", "deploy groq",
  "groq g...
name: groq-prod-checklist
---
# Groq Prod Checklist

This skill provides automated assistance for groq prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Groq integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Groq Status](https://status.groq.com)
- [Groq Support](https://docs.groq.com/support)