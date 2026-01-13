---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Configure Clerk webhooks and handle authentication events. Use when setting
  up user sync, handling auth events, or integrating Clerk with external systems.
  Trigger with phrases like "clerk webhooks", "clerk events", "clerk user sync", "clerk
  notif...
name: clerk-webhooks-events
---
# Clerk Webhooks Events

This skill provides automated assistance for clerk webhooks events tasks.

## Prerequisites
- Clerk account with webhook access
- HTTPS endpoint for webhooks
- svix package for verification

## Instructions

1. Go to Clerk Dashboard > Webhooks
2. Add endpoint URL: `https://yourdomain.com/api/webhooks/clerk`
3. Select events:
4. Copy webhook secret to environment


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Webhook endpoint configured
- Event handlers implemented
- Idempotency protection
- User data sync working

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Clerk Webhooks](https://clerk.com/docs/integrations/webhooks/overview)
- [Svix Verification](https://docs.svix.com/receiving/verifying-payloads)
- [Event Types](https://clerk.com/docs/integrations/webhooks/sync-data)