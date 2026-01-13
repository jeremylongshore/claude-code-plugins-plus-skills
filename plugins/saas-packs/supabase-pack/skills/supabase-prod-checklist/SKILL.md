---
name: supabase-prod-checklist
description: |
  Execute supabase production deployment checklist and rollback procedures. use when deploying supabase integrations to production, preparing for launch, or implementing go-live procedures. trigger with phrases like "supabase production", "deploy su...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Supabase Prod Checklist

This skill provides automated assistance for supabase prod checklist tasks.

## Prerequisites
- Staging environment tested and verified
- Production API keys available
- Deployment pipeline configured
- Monitoring and alerting ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Deployed Supabase integration
- Health checks passing
- Monitoring active
- Rollback procedure documented

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Supabase Status](https://status.supabase.com)
- [Supabase Support](https://supabase.com/docs/support)