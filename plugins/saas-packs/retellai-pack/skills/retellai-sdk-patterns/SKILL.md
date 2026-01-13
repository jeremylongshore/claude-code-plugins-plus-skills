---
allowed-tools: Read, Write, Edit
license: MIT
description: Apply production-ready retell ai sdk patterns for typescript and python.
  use when implementing retell ai integrations, refactoring sdk usage, or establishing
  team coding standards for retell ai. trigger with phrases like "retellai sdk patterns",
  "...
name: retellai-sdk-patterns
---
# Retellai Sdk Patterns

This skill provides automated assistance for retellai sdk patterns tasks.

## Prerequisites
- Completed `retellai-install-auth` setup
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
- [Retell AI SDK Reference](https://docs.retellai.com/sdk)
- [Retell AI API Types](https://docs.retellai.com/types)
- [Zod Documentation](https://zod.dev/)