---
allowed-tools: Read, Write, Edit
license: MIT
description: Execute apply production-ready supabase sdk patterns for typescript and
  python. use when implementing supabase integrations, refactoring sdk usage, or establishing
  team coding standards for supabase. trigger with phrases like "supabase sdk pattern...
name: supabase-sdk-patterns
---
# Supabase Sdk Patterns

This skill provides automated assistance for supabase sdk patterns tasks.

## Prerequisites
- Completed `supabase-install-auth` setup
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
- [Supabase SDK Reference](https://supabase.com/docs/sdk)
- [Supabase API Types](https://supabase.com/docs/types)
- [Zod Documentation](https://zod.dev/)