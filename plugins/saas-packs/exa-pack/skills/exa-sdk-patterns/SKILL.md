---
allowed-tools: Read, Write, Edit
license: MIT
description: Apply production-ready exa sdk patterns for typescript and python. use
  when implementing exa integrations, refactoring sdk usage, or establishing team
  coding standards for exa. trigger with phrases like "exa sdk patterns", "exa best
  practices", "e...
name: exa-sdk-patterns
---
# Exa Sdk Patterns

This skill provides automated assistance for exa sdk patterns tasks.

## Prerequisites
- Completed `exa-install-auth` setup
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
- [Exa SDK Reference](https://docs.exa.com/sdk)
- [Exa API Types](https://docs.exa.com/types)
- [Zod Documentation](https://zod.dev/)