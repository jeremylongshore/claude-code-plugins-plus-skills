---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Configure PostHog local development with hot reload and testing. Use
  when setting up a development environment, configuring test workflows, or establishing
  a fast iteration cycle with PostHog. Trigger with phrases like "posthog dev setup",
  "postho...
name: posthog-local-dev-loop
---
# Posthog Local Dev Loop

This skill provides automated assistance for posthog local dev loop tasks.

## Prerequisites
- Completed `posthog-install-auth` setup
- Node.js 18+ with npm/pnpm
- Code editor with TypeScript support
- Git for version control


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Working development environment with hot reload
- Configured test suite with mocking
- Environment variable management
- Fast iteration cycle for PostHog development

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [PostHog SDK Reference](https://docs.posthog.com/sdk)
- [Vitest Documentation](https://vitest.dev/)
- [tsx Documentation](https://github.com/esbuild-kit/tsx)