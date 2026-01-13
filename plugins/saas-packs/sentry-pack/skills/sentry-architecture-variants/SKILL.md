---
name: sentry-architecture-variants
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Execute sentry architecture patterns for different application types.
  use when setting up sentry for monoliths, microservices, serverless, or hybrid architectures.
  trigger with phrases like "sentry monolith setup", "sentry microservices", "sentry
  ...
---
# Sentry Architecture Variants

## Prerequisites

- Application architecture documented
- Service inventory available
- Team ownership defined
- Deployment model understood

## Instructions

1. Identify application type (monolith, microservices, serverless, hybrid)
2. For monoliths, create single project and use tags for module filtering
3. For microservices, create one project per service with shared config
4. Configure distributed tracing with sentry-trace and baggage headers
5. For serverless, use framework-specific SDK wrappers
6. Set up cross-system tracing for hybrid architectures
7. Configure message queue integration with trace context propagation
8. Add tenant isolation tags for multi-tenant applications
9. Set up edge function monitoring with platform-specific SDKs
10. Document architecture decisions and implement team-based access controls

## Output
- Architecture-appropriate Sentry configuration
- Project structure matching application topology
- Distributed tracing configured
- Team-based access controls

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Architecture Guide](https://docs.sentry.io/product/sentry-basics/integrate-backend/)
- [Distributed Tracing](https://docs.sentry.io/product/performance/distributed-tracing/)
