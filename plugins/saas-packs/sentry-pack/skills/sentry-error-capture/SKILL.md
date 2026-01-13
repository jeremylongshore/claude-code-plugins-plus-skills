---
name: sentry-error-capture
description: |
  Execute advanced error capture and context enrichment with sentry. use when implementing detailed error tracking, adding context, or customizing error capture behavior. trigger with phrases like "sentry error capture", "sentry context", "enrich se...
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Sentry Error Capture

This skill provides automated assistance for sentry error capture tasks.

## Prerequisites
- Sentry SDK installed and configured
- Understanding of error handling
- Application logging infrastructure


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Errors with full context in Sentry dashboard
- Filterable tags for issue management
- User attribution for error tracking

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Enriching Events](https://docs.sentry.io/platforms/javascript/enriching-events/)
- [Sentry Scopes](https://docs.sentry.io/platforms/javascript/enriching-events/scopes/)