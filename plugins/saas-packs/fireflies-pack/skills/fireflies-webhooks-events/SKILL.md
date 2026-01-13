---
name: fireflies-webhooks-events
description: |
  Implement fireflies.ai webhook signature validation and event handling. use when setting up webhook endpoints, implementing signature verification, or handling fireflies.ai event notifications securely. trigger with phrases like "fireflies webhook...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Fireflies Webhooks Events

This skill provides automated assistance for fireflies webhooks events tasks.

## Prerequisites
- Fireflies.ai webhook secret configured
- HTTPS endpoint accessible from internet
- Understanding of cryptographic signatures
- Redis or database for idempotency (optional)

## Instructions

### Step 1: Register Webhook Endpoint
Configure your webhook URL in the Fireflies.ai dashboard.

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
- [Fireflies.ai Webhooks Guide](https://docs.fireflies.com/webhooks)
- [Webhook Security Best Practices](https://docs.fireflies.com/webhooks/security)