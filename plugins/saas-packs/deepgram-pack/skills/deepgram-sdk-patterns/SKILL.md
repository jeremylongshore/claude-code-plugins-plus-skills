---
allowed-tools: Read, Write, Edit
license: MIT
description: Apply production-ready deepgram sdk patterns for typescript and python.
  use when implementing deepgram integrations, refactoring sdk usage, or establishing
  team coding standards for deepgram. trigger with phrases like "deepgram sdk patterns",
  "dee...
name: deepgram-sdk-patterns
---
# Deepgram Sdk Patterns

This skill provides automated assistance for deepgram sdk patterns tasks.

## Prerequisites
- Completed `deepgram-install-auth` setup
- Familiarity with async/await patterns
- Understanding of error handling best practices

## Instructions

### Step 1: Create Type-Safe Client Singleton
Implement a singleton pattern for the Deepgram client.

### Step 2: Add Robust Error Handling
Wrap all API calls with proper error handling and logging.

### Step 3: Implement Response Validation
Validate API responses before processing.

### Step 4: Add Retry Logic
Implement exponential backoff for transient failures.

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
- [Deepgram SDK Reference](https://developers.deepgram.com/docs/sdk)
- [Deepgram TypeScript Types](https://github.com/deepgram/deepgram-js-sdk)
- [Error Handling Best Practices](https://developers.deepgram.com/docs/error-handling)