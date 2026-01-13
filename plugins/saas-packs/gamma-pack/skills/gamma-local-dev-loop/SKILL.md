---
name: gamma-local-dev-loop
description: |
  Set up efficient local development workflow for gamma. use when configuring hot reload, mock responses, or optimizing your gamma development experience. trigger with phrases like "gamma local dev", "gamma development setup", "gamma hot reload", "g...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Gamma Local Dev Loop

This skill provides automated assistance for gamma local dev loop tasks.

## Prerequisites
- Completed `gamma-hello-world` setup
- Node.js 18+ with nodemon or tsx
- TypeScript project (recommended)


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Hot reload development server
- Mock client for offline development
- Environment-based configuration
- Fast iteration cycle

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [tsx Documentation](https://github.com/esbuild-kit/tsx)
- [Gamma SDK Mock Guide](https://gamma.app/docs/testing)