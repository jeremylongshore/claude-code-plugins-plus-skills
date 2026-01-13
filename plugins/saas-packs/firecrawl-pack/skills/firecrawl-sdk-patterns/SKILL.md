---
name: firecrawl-sdk-patterns
description: |
  Apply production-ready firecrawl sdk patterns for typescript and python. use when implementing firecrawl integrations, refactoring sdk usage, or establishing team coding standards for firecrawl. trigger with phrases like "firecrawl sdk patterns", ...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Firecrawl Sdk Patterns

This skill provides automated assistance for firecrawl sdk patterns tasks.

## Prerequisites
- Completed `firecrawl-install-auth` setup
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
- [FireCrawl SDK Reference](https://docs.firecrawl.com/sdk)
- [FireCrawl API Types](https://docs.firecrawl.com/types)
- [Zod Documentation](https://zod.dev/)