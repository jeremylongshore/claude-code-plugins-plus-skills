---
name: coderabbit-local-dev-loop
description: |
  Configure CodeRabbit local development with hot reload and testing. Use when setting up a development environment, configuring test workflows, or establishing a fast iteration cycle with CodeRabbit. Trigger with phrases like "coderabbit dev setup"...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Coderabbit Local Dev Loop

This skill provides automated assistance for coderabbit local dev loop tasks.

## Prerequisites
- Completed `coderabbit-install-auth` setup
- Node.js 18+ with npm/pnpm
- Code editor with TypeScript support
- Git for version control


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Working development environment with hot reload
- Configured test suite with mocking
- Environment variable management
- Fast iteration cycle for CodeRabbit development

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [CodeRabbit SDK Reference](https://docs.coderabbit.com/sdk)
- [Vitest Documentation](https://vitest.dev/)
- [tsx Documentation](https://github.com/esbuild-kit/tsx)