---
name: clerk-local-dev-loop
description: |
  Set up local development workflow with clerk. use when configuring development environment, testing auth locally, or setting up hot reload with clerk. trigger with phrases like "clerk local dev", "clerk development", "test clerk locally", "clerk d...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Clerk Local Dev Loop

This skill provides automated assistance for clerk local dev loop tasks.

## Prerequisites
- Clerk SDK installed
- Development and production instances in Clerk dashboard
- Node.js development environment


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Development environment configured
- Test users available
- Hot reload working with auth
- Mocked auth for testing

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Clerk Development Mode](https://clerk.com/docs/deployments/overview)
- [Test Mode](https://clerk.com/docs/testing/overview)
- [CLI Tools](https://clerk.com/docs/references/cli)