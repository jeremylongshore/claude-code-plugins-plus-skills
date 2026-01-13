---
name: instantly-sdk-patterns
description: |
  Apply production-ready instantly sdk patterns for typescript and python. use when implementing instantly integrations, refactoring sdk usage, or establishing team coding standards for instantly. trigger with phrases like "instantly sdk patterns", ...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Instantly Sdk Patterns

This skill provides automated assistance for instantly sdk patterns tasks.

## Prerequisites
- Completed `instantly-install-auth` setup
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
- [Instantly SDK Reference](https://docs.instantly.com/sdk)
- [Instantly API Types](https://docs.instantly.com/types)
- [Zod Documentation](https://zod.dev/)