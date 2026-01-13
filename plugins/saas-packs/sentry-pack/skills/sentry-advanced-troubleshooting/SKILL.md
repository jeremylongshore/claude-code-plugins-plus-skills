---
allowed-tools: Read, Write, Edit, Grep, Bash
license: MIT
description: Execute advanced sentry troubleshooting techniques. use when debugging
  complex sdk issues, missing events, source map problems, or performance anomalies.
  trigger with phrases like "sentry not working", "debug sentry", "sentry events missing",
  "fix...
name: sentry-advanced-troubleshooting
---
# Sentry Advanced Troubleshooting

This skill provides automated assistance for sentry advanced troubleshooting tasks.

## Prerequisites

- Debug mode enabled in SDK
- Access to application logs
- Sentry dashboard access
- Sentry CLI installed for source map debugging

## Instructions

1. Enable debug mode in SDK configuration to see verbose logging
2. Verify SDK initialization by checking if client exists after init
3. Test network connectivity to Sentry ingest endpoint
4. Check sampling configuration to ensure events are not being dropped
5. Temporarily disable beforeSend filtering during debugging
6. Use sentry-cli sourcemaps explain to diagnose source map issues
7. Verify transaction creation and finish calls for performance data
8. Check breadcrumb capture with beforeBreadcrumb debugging
9. Resolve SDK conflicts by ensuring single initialization
10. Run diagnostic script to generate comprehensive health report

## Output
- Root cause identified for SDK issues
- Source map problems resolved
- Event capture verified working
- Performance monitoring validated

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Troubleshooting](https://docs.sentry.io/platforms/javascript/troubleshooting/)
- [Source Maps Troubleshooting](https://docs.sentry.io/platforms/javascript/sourcemaps/troubleshooting/)