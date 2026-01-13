---
name: sentry-migration-deep-dive
license: MIT
allowed-tools: Read, Write, Edit, Bash, Grep
description: Execute migrate to sentry from other error tracking tools. use when migrating
  from rollbar, bugsnag, raygun, or other error tracking solutions. trigger with phrases
  like "migrate to sentry", "sentry migration", "switch from rollbar to sentry", "re...
---
# Sentry Migration Deep Dive

## Prerequisites

- Current error tracking tool access
- Sentry project created
- API access to old tool (for data export)
- Parallel run timeline established

## Instructions

1. Complete assessment phase documenting current tool usage
2. Set up Sentry projects matching existing structure
3. Install Sentry SDK alongside existing tool for parallel running
4. Map feature equivalents between old tool and Sentry APIs
5. Run both tools in parallel for 2-4 weeks
6. Compare error capture rates and verify parity
7. Recreate alert rules in Sentry matching old tool
8. Export historical data from old tool API if needed
9. Remove old SDK dependencies and configuration
10. Train team on Sentry dashboard and cancel old subscription

## Output
- SDK migration complete
- Historical data exported (if needed)
- Alert rules recreated
- Team transitioned to Sentry

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Migration Guide](https://docs.sentry.io/product/accounts/migration/)
- [SDK Documentation](https://docs.sentry.io/platforms/)
