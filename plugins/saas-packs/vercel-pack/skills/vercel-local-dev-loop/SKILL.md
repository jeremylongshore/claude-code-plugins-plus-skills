---
name: vercel-local-dev-loop
license: MIT
allowed-tools: Read, Write, Edit, Bash, Grep
description: Configure Vercel local development with hot reload and testing. Use when
  setting up a development environment, configuring test workflows, or establishing
  a fast iteration cycle with Vercel. Trigger with phrases like "vercel dev setup",
  "vercel lo...
---
# Vercel Local Dev Loop

## Prerequisites
- Completed `vercel-install-auth` setup
- Node.js 18+ with npm/pnpm
- Code editor with TypeScript support
- Git for version control


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Working development environment with hot reload
- Configured test suite with mocking
- Environment variable management
- Fast iteration cycle for Vercel development

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Vercel SDK Reference](https://vercel.com/docs/sdk)
- [Vitest Documentation](https://vitest.dev/)
- [tsx Documentation](https://github.com/esbuild-kit/tsx)
