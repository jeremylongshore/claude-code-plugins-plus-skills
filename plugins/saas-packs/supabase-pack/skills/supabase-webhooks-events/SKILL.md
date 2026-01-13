---
name: supabase-webhooks-events
description: |
  Implement supabase webhook signature validation and event handling. use when setting up webhook endpoints, implementing signature verification, or handling supabase event notifications securely. trigger with phrases like "supabase webhook", "supab...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Supabase Webhooks Events

This skill provides automated assistance for supabase webhooks events tasks.

## Prerequisites
- Supabase webhook secret configured
- HTTPS endpoint accessible from internet
- Understanding of cryptographic signatures
- Redis or database for idempotency (optional)

## Instructions

### Step 1: Register Webhook Endpoint
Configure your webhook URL in the Supabase dashboard.

### Step 2: Implement Signature Verification
Use the signature verification code to validate incoming webhooks.

### Step 3: Handle Events
Implement handlers for each event type your application needs.

### Step 4: Add Idempotency
Prevent duplicate processing with event ID tracking.

## Output
- Secure webhook endpoint
- Signature validation enabled
- Event handlers implemented
- Replay attack protection active

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Supabase Webhooks Guide](https://supabase.com/docs/webhooks)
- [Webhook Security Best Practices](https://supabase.com/docs/webhooks/security)