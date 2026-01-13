---
name: clerk-hello-world
description: |
  Create your first authenticated request with Clerk. Use when making initial API calls, testing authentication, or verifying Clerk integration works correctly. Trigger with phrases like "clerk hello world", "first clerk request", "test clerk auth",...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Clerk Hello World

This skill provides automated assistance for clerk hello world tasks.

## Prerequisites
- Clerk SDK installed (`clerk-install-auth` completed)
- Environment variables configured
- ClerkProvider wrapping application


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Protected page showing user information
- API route returning authenticated user data
- Successful request/response verification

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Clerk Auth Object](https://clerk.com/docs/references/nextjs/auth)
- [Clerk Hooks](https://clerk.com/docs/references/react/use-user)
- [Protected Routes](https://clerk.com/docs/references/nextjs/auth-middleware)