---
name: supabase-prod-checklist
description: |
  Execute Supabase production deployment checklist and rollback procedures.
  Use when deploying Supabase integrations to production, preparing for launch,
  or implementing go-live procedures.
  Trigger with phrases like "supabase production", "deploy supabase",
  "supabase go-live", "supabase launch checklist".
allowed-tools: Read, Bash, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Supabase Prod Checklist

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
