---
name: sentry-load-scale
description: |
  Manage scale Sentry for high-traffic applications. Use when optimizing for high event volumes, managing costs at scale, or tuning for performance. Trigger with phrases like "sentry high traffic", "scale sentry", "sentry high volume", "sentry milli...
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Sentry Load Scale

This skill provides automated assistance for sentry load scale tasks.

## Prerequisites

- High-traffic application metrics available
- Sentry quota and billing understood
- Performance baseline established
- Event volume estimates calculated

## Instructions

1. Implement adaptive sampling based on error frequency per type
2. Configure tiered transaction sampling with endpoint-specific rates
3. Set up client-side buffering with increased buffer size
4. Reduce SDK overhead with minimal integrations and breadcrumbs
5. Use async event processing to avoid blocking requests
6. Configure background flushing on graceful shutdown
7. Set up multi-region DSN routing if applicable
8. Implement quota budget allocation across environments
9. Add dynamic rate adjustment based on quota usage
10. Monitor SDK event throughput and adjust configuration

## Output
- Optimized sampling configuration
- Quota management strategy
- Cost-efficient event capture
- Scalable Sentry integration

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Quotas](https://docs.sentry.io/product/accounts/quotas/)
- [Performance Best Practices](https://docs.sentry.io/product/performance/)