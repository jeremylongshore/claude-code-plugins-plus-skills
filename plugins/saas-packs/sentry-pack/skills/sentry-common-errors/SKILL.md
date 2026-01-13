---
allowed-tools: Read, Grep, Bash
license: MIT
description: Execute troubleshoot common sentry integration issues and fixes. use
  when encountering sentry errors, missing events, or configuration problems. trigger
  with phrases like "sentry not working", "sentry errors missing", "fix sentry", "sentry
  trouble...
name: sentry-common-errors
---
# Sentry Common Errors

This skill provides automated assistance for sentry common errors tasks.

## Prerequisites

- Sentry SDK installed
- Debug mode enabled for troubleshooting
- Access to Sentry dashboard
- Application logs available

## Instructions

1. Enable debug mode in SDK configuration for verbose output
2. Verify DSN is set correctly in environment variables
3. Check beforeSend function returns event (not undefined)
4. Review sampling rates to ensure events are not being dropped
5. Verify source maps are uploaded with correct release version
6. Set user context after authentication for user tracking
7. Add ignoreErrors patterns for noisy errors to reduce volume
8. Enable Breadcrumbs integration with appropriate options
9. Set tracesSampleRate greater than 0 for performance monitoring
10. Run diagnostic commands to verify connectivity and capture

## Output
- Issue root cause identified
- Configuration fix applied
- Error capture verified working
- Documentation of resolution

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Troubleshooting](https://docs.sentry.io/platforms/javascript/troubleshooting/)
- [Sentry Status](https://status.sentry.io)