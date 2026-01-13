---
name: customerio-webhooks-events
description: |
  Implement customer.io webhook handling. use when processing delivery events, handling callbacks, or integrating customer.io event streams. trigger with phrases like "customer.io webhook", "customer.io events", "customer.io callback", "customer.io ...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Customerio Webhooks Events

This skill provides automated assistance for customerio webhooks events tasks.

## Prerequisites
- Public endpoint for webhooks
- Webhook signing secret from Customer.io
- Event processing infrastructure


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Webhook event type definitions
- Signature verification handler
- Express router setup
- Event queue for reliability
- Reporting API integration
- Data warehouse streaming

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Webhooks Documentation](https://customer.io/docs/webhooks/)
- [Reporting API](https://customer.io/docs/api/app/)