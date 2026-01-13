---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Implement monitoring, logging, and observability for clerk authentication.
  use when setting up monitoring, debugging auth issues in production, or implementing
  audit logging. trigger with phrases like "clerk monitoring", "clerk logging", "clerk
  ob...
name: clerk-observability
---
# Clerk Observability

This skill provides automated assistance for clerk observability tasks.

## Prerequisites
- Clerk integration working
- Monitoring platform (DataDog, New Relic, Sentry, etc.)
- Logging infrastructure


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Authentication event logging
- Performance monitoring
- Error tracking integration
- Health check endpoints

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Clerk Dashboard Analytics](https://dashboard.clerk.com)
- [Sentry Integration](https://docs.sentry.io)
- [DataDog APM](https://docs.datadoghq.com/tracing)