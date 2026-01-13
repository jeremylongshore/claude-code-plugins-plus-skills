---
allowed-tools: Read, Write, Edit
license: MIT
description: Apply production-ready fireflies.ai sdk patterns for typescript and python.
  use when implementing fireflies.ai integrations, refactoring sdk usage, or establishing
  team coding standards for fireflies.ai. trigger with phrases like "fireflies sdk
  pa...
name: fireflies-sdk-patterns
---
# Fireflies Sdk Patterns

This skill provides automated assistance for fireflies sdk patterns tasks.

## Prerequisites
- Completed `fireflies-install-auth` setup
- Familiarity with async/await patterns
- Understanding of error handling best practices


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Type-safe client singleton
- Robust error handling with structured logging
- Automatic retry with exponential backoff
- Runtime validation for API responses

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Fireflies.ai SDK Reference](https://docs.fireflies.com/sdk)
- [Fireflies.ai API Types](https://docs.fireflies.com/types)
- [Zod Documentation](https://zod.dev/)