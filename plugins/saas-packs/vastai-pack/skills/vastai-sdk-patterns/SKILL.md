---
name: vastai-sdk-patterns
description: |
  Apply production-ready vast.ai sdk patterns for typescript and python. use when implementing vast.ai integrations, refactoring sdk usage, or establishing team coding standards for vast.ai. trigger with phrases like "vastai sdk patterns", "vastai b...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Vastai Sdk Patterns

This skill provides automated assistance for vastai sdk patterns tasks.

## Prerequisites
- Completed `vastai-install-auth` setup
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
- [Vast.ai SDK Reference](https://docs.vastai.com/sdk)
- [Vast.ai API Types](https://docs.vastai.com/types)
- [Zod Documentation](https://zod.dev/)