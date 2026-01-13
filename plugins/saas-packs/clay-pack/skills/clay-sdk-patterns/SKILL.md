---
allowed-tools: Read, Write, Edit
license: MIT
description: Apply production-ready clay sdk patterns for typescript and python. use
  when implementing clay integrations, refactoring sdk usage, or establishing team
  coding standards for clay. trigger with phrases like "clay sdk patterns", "clay
  best practices...
name: clay-sdk-patterns
---
# Clay Sdk Patterns

This skill provides automated assistance for clay sdk patterns tasks.

## Prerequisites
- Completed `clay-install-auth` setup
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
- [Clay SDK Reference](https://docs.clay.com/sdk)
- [Clay API Types](https://docs.clay.com/types)
- [Zod Documentation](https://zod.dev/)