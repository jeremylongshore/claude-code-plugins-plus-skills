---
name: lindy-local-dev-loop
description: |
  Set up local development workflow for lindy ai agents. use when configuring local testing, hot reload, or development environment. trigger with phrases like "lindy local dev", "lindy development", "lindy hot reload", "test lindy locally".
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Lindy Local Dev Loop

This skill provides automated assistance for lindy local dev loop tasks.

## Prerequisites
- Completed `lindy-install-auth` setup
- Node.js 18+ with npm/pnpm
- Code editor with TypeScript support


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Configured development environment
- Hot reload enabled for agent code
- Test harness for rapid iteration
- TypeScript support with type checking

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Lindy SDK Reference](https://docs.lindy.ai/sdk)
- [TypeScript Best Practices](https://docs.lindy.ai/typescript)