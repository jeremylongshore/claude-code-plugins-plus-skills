---
name: perplexity-prod-checklist
description: |
  Execute perplexity production deployment checklist and rollback procedures. use when deploying perplexity integrations to production, preparing for launch, or implementing go-live procedures. trigger with phrases like "perplexity production", "dep...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Perplexity Prod Checklist

This skill provides automated assistance for perplexity prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Perplexity integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Perplexity Status](https://status.perplexity.com)
- [Perplexity Support](https://docs.perplexity.com/support)