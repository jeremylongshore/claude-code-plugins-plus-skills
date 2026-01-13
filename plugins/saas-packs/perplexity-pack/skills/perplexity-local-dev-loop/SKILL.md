---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Configure Perplexity local development with hot reload and testing. Use
  when setting up a development environment, configuring test workflows, or establishing
  a fast iteration cycle with Perplexity. Trigger with phrases like "perplexity dev
  setup"...
name: perplexity-local-dev-loop
---
# Perplexity Local Dev Loop

This skill provides automated assistance for perplexity local dev loop tasks.

## Prerequisites
- Completed `perplexity-install-auth` setup
- Node.js 18+ with npm/pnpm
- Code editor with TypeScript support
- Git for version control


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Working development environment with hot reload
- Configured test suite with mocking
- Environment variable management
- Fast iteration cycle for Perplexity development

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Perplexity SDK Reference](https://docs.perplexity.com/sdk)
- [Vitest Documentation](https://vitest.dev/)
- [tsx Documentation](https://github.com/esbuild-kit/tsx)