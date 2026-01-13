---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Configure Ideogram local development with hot reload and testing. Use
  when setting up a development environment, configuring test workflows, or establishing
  a fast iteration cycle with Ideogram. Trigger with phrases like "ideogram dev setup",
  "ide...
name: ideogram-local-dev-loop
---
# Ideogram Local Dev Loop

This skill provides automated assistance for ideogram local dev loop tasks.

## Prerequisites
- Completed `ideogram-install-auth` setup
- Node.js 18+ with npm/pnpm
- Code editor with TypeScript support
- Git for version control


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Working development environment with hot reload
- Configured test suite with mocking
- Environment variable management
- Fast iteration cycle for Ideogram development

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Ideogram SDK Reference](https://docs.ideogram.com/sdk)
- [Vitest Documentation](https://vitest.dev/)
- [tsx Documentation](https://github.com/esbuild-kit/tsx)