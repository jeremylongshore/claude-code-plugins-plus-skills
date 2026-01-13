---
name: windsurf-sdk-patterns
description: |
  Apply production-ready windsurf sdk patterns for typescript and python. use when implementing windsurf integrations, refactoring sdk usage, or establishing team coding standards for windsurf. trigger with phrases like "windsurf sdk patterns", "win...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Windsurf Sdk Patterns

This skill provides automated assistance for windsurf sdk patterns tasks.

## Prerequisites
- Completed `windsurf-install-auth` setup
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
- [Windsurf SDK Reference](https://docs.windsurf.com/sdk)
- [Windsurf API Types](https://docs.windsurf.com/types)
- [Zod Documentation](https://zod.dev/)