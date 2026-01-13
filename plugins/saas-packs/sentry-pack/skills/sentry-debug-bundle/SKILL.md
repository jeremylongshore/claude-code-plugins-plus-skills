---
name: sentry-debug-bundle
license: MIT
allowed-tools: Read, Bash, Grep
description: Execute collect debug information for sentry support tickets. use when
  preparing support requests, debugging complex issues, or gathering diagnostic information.
  trigger with phrases like "sentry debug info", "sentry support ticket", "gather
  sentr...
---
# Sentry Debug Bundle

## Prerequisites

- Debug mode enabled in SDK
- Sentry CLI installed for source map diagnostics
- Access to environment variables
- Application logs available

## Instructions

1. Run npm list to get SDK version for all Sentry packages
2. Create debug config export with DSN redacted for sharing
3. Test network connectivity to sentry.io API endpoint
4. Capture test event and record event ID
5. Check integrations loaded with getIntegrations call
6. Run debug script to collect comprehensive diagnostic info
7. Format output in markdown template for support ticket
8. List uploaded source maps using sentry-cli releases files
9. Use sentry-cli sourcemaps explain for specific event debugging
10. Include relevant logs and reproduction steps in debug bundle

## Output
- Debug information bundle generated
- SDK version and configuration documented
- Network connectivity verified
- Test event capture confirmed

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Support](https://sentry.io/support/)
- [Sentry GitHub Issues](https://github.com/getsentry/sentry-javascript/issues)
