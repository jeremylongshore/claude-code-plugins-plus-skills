---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Set up local linear development environment and testing workflow. use
  when configuring local development, testing integrations, or setting up a development
  workflow with linear. trigger with phrases like "linear local development", "linear
  dev set...
name: linear-local-dev-loop
---
# Linear Local Dev Loop

This skill provides automated assistance for linear local dev loop tasks.

## Prerequisites
- Node.js 18+ with TypeScript
- Linear SDK installed
- Separate Linear workspace for development (recommended)
- ngrok or similar for webhook testing


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Local development environment ready
- Environment variables configured
- Test utilities for creating/cleaning test data
- Watch mode for rapid iteration

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Linear SDK TypeScript](https://developers.linear.app/docs/sdk/getting-started)
- [Webhook Development](https://developers.linear.app/docs/graphql/webhooks)
- [ngrok Documentation](https://ngrok.com/docs)