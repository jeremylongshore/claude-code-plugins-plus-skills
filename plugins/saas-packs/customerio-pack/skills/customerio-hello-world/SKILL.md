---
name: customerio-hello-world
description: |
  Create a minimal working Customer.io example. Use when learning Customer.io basics, testing SDK setup, or creating your first messaging integration. Trigger with phrases like "customer.io hello world", "first customer.io message", "test customer.i...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Customerio Hello World

This skill provides automated assistance for customerio hello world tasks.

## Prerequisites
- Completed `customerio-install-auth` skill
- Customer.io SDK installed
- Valid Site ID and API Key configured

## Instructions

1. Go to Customer.io dashboard
2. Navigate to People section
3. Search for "user-123" or "hello@example.com"
4. Verify user profile shows attributes
5. Check Activity tab for "hello_world" event


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- User created/updated in Customer.io
- Event recorded in user's activity log
- Console output confirming success

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Identify API](https://customer.io/docs/api/track/#operation/identify)
- [Track API](https://customer.io/docs/api/track/#operation/track)