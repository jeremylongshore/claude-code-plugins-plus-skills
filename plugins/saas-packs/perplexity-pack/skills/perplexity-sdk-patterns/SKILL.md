---
name: perplexity-sdk-patterns
description: |
  Apply production-ready perplexity sdk patterns for typescript and python. use when implementing perplexity integrations, refactoring sdk usage, or establishing team coding standards for perplexity. trigger with phrases like "perplexity sdk pattern...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Perplexity Sdk Patterns

This skill provides automated assistance for perplexity sdk patterns tasks.

## Prerequisites
- Completed `perplexity-install-auth` setup
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
- [Perplexity SDK Reference](https://docs.perplexity.com/sdk)
- [Perplexity API Types](https://docs.perplexity.com/types)
- [Zod Documentation](https://zod.dev/)