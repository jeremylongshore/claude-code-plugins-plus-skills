---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Implement instantly webhook signature validation and event handling.
  use when setting up webhook endpoints, implementing signature verification, or handling
  instantly event notifications securely. trigger with phrases like "instantly webhook",
  "in...
name: instantly-webhooks-events
---
# Instantly Webhooks Events

This skill provides automated assistance for instantly webhooks events tasks.

## Prerequisites
- Instantly webhook secret configured
- HTTPS endpoint accessible from internet
- Understanding of cryptographic signatures
- Redis or database for idempotency (optional)

## Instructions

### Step 1: Register Webhook Endpoint
Configure your webhook URL in the Instantly dashboard.

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
- [Instantly Webhooks Guide](https://docs.instantly.com/webhooks)
- [Webhook Security Best Practices](https://docs.instantly.com/webhooks/security)