---
allowed-tools: Read, Write, Edit
license: MIT
description: Apply production-ready apollo.io sdk patterns. use when implementing
  apollo integrations, refactoring api usage, or establishing team coding standards.
  trigger with phrases like "apollo sdk patterns", "apollo best practices", "apollo
  code patterns...
name: apollo-sdk-patterns
---
# Apollo Sdk Patterns

This skill provides automated assistance for apollo sdk patterns tasks.

## Prerequisites
- Completed `apollo-install-auth` setup
- Familiarity with async/await patterns
- Understanding of TypeScript generics

## Output
- Type-safe client singleton with Zod validation
- Robust error handling with custom error classes
- Automatic retry with exponential backoff
- Async pagination iterator
- Request batching for bulk operations

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Zod Documentation](https://zod.dev/)
- [Axios Interceptors](https://axios-http.com/docs/interceptors)
- [TypeScript Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)