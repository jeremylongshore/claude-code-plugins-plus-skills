---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Configure Exa local development with hot reload and testing. Use when
  setting up a development environment, configuring test workflows, or establishing
  a fast iteration cycle with Exa. Trigger with phrases like "exa dev setup", "exa
  local developm...
name: exa-local-dev-loop
---
# Exa Local Dev Loop

This skill provides automated assistance for exa local dev loop tasks.

## Prerequisites
- Completed `exa-install-auth` setup
- Node.js 18+ with npm/pnpm
- Code editor with TypeScript support
- Git for version control


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Working development environment with hot reload
- Configured test suite with mocking
- Environment variable management
- Fast iteration cycle for Exa development

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Exa SDK Reference](https://docs.exa.com/sdk)
- [Vitest Documentation](https://vitest.dev/)
- [tsx Documentation](https://github.com/esbuild-kit/tsx)