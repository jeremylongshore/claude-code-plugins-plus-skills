---
allowed-tools: Read, Write, Edit, Grep
license: MIT
description: Manage best-practice Sentry architecture patterns. Use when designing
  Sentry integration architecture, structuring projects, or planning enterprise rollout.
  Trigger with phrases like "sentry architecture", "sentry best practices", "design
  sentry i...
name: sentry-reference-architecture
---
# Sentry Reference Architecture

This skill provides automated assistance for sentry reference architecture tasks.

## Prerequisites

- Sentry organization created
- Team structure defined
- Service inventory documented
- Alert escalation paths established

## Instructions

1. Define project structure based on application architecture
2. Create centralized SDK configuration module with standard settings
3. Implement global error handler middleware with Sentry integration
4. Create domain-specific error classes with appropriate tags
5. Configure distributed tracing with header propagation between services
6. Set up alert hierarchy (critical, warning, info) with routing rules
7. Configure issue routing based on team ownership and tags
8. Enable release tracking for every deployment
9. Document architecture patterns and configuration standards
10. Review and adjust based on error patterns after initial deployment

## Output
- Project structure following best practices
- Centralized SDK configuration module
- Distributed tracing configured across services
- Alert routing rules defined

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Best Practices](https://docs.sentry.io/product/issues/best-practices/)
- [Distributed Tracing](https://docs.sentry.io/product/performance/distributed-tracing/)