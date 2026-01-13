---
name: customerio-sdk-patterns
description: |
  Apply production-ready customer.io sdk patterns. use when implementing best practices, refactoring integrations, or optimizing customer.io usage in your application. trigger with phrases like "customer.io best practices", "customer.io patterns", "...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Customerio Sdk Patterns

This skill provides automated assistance for customerio sdk patterns tasks.

## Prerequisites
- Customer.io SDK installed
- TypeScript project (recommended)
- Understanding of async/await patterns


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Type-safe Customer.io client
- Resilient error handling with retries
- Event batching for high-volume scenarios
- Singleton pattern for resource efficiency

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Customer.io SDK GitHub](https://github.com/customerio/customerio-node)
- [API Rate Limits](https://customer.io/docs/api/track/#section/Limits)