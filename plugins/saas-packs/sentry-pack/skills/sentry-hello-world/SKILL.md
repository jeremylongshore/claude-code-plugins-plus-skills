---
name: sentry-hello-world
license: MIT
allowed-tools: Read, Write, Edit, Bash, Grep
description: Execute capture your first error with sentry and verify it appears in
  the dashboard. use when testing sentry integration or verifying error capture works.
  trigger with phrases like "test sentry", "sentry hello world", "verify sentry",
  "first sentr...
---
# Sentry Hello World

## Prerequisites
- Sentry SDK installed and initialized
- Valid DSN configured
- Network access to Sentry servers

## Instructions

1. Open https://sentry.io
2. Navigate to your project
3. Check Issues tab for the test error
4. Verify event details are correct


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Test error visible in Sentry dashboard
- Event contains stack trace and metadata
- User context and tags attached to event

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Error Capture](https://docs.sentry.io/platforms/javascript/usage/)
- [Sentry Context](https://docs.sentry.io/platforms/javascript/enriching-events/context/)
