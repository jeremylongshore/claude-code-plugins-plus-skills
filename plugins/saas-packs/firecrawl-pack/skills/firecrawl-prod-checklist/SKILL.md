---
name: firecrawl-prod-checklist
description: |
  Execute firecrawl production deployment checklist and rollback procedures. use when deploying firecrawl integrations to production, preparing for launch, or implementing go-live procedures. trigger with phrases like "firecrawl production", "deploy...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Firecrawl Prod Checklist

This skill provides automated assistance for firecrawl prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed FireCrawl integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [FireCrawl Status](https://status.firecrawl.com)
- [FireCrawl Support](https://docs.firecrawl.com/support)