---
name: sentry-upgrade-migration
description: |
  Execute upgrade sentry sdk and migrate between versions. use when upgrading sentry sdk, handling breaking changes, or migrating from legacy versions. trigger with phrases like "upgrade sentry", "sentry migration", "update sentry sdk", "sentry brea...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Sentry Upgrade Migration

This skill provides automated assistance for sentry upgrade migration tasks.

## Prerequisites

- Current Sentry SDK version identified
- Target version changelog reviewed
- Non-production environment for testing
- Test suite for error capture and performance monitoring

## Instructions

1. Check current SDK version with npm list or pip show
2. Review release notes and changelog for target version
3. Back up current Sentry configuration file
4. Update package to target version in non-production first
5. Run tests to identify breaking changes
6. Update deprecated APIs following migration guide patterns
7. Verify error capture works with test error
8. Verify performance monitoring works with test transaction
9. Deploy to staging and monitor for issues
10. Deploy to production after staging validation

## Output
- SDK upgraded to target version
- Breaking changes resolved
- Code updated for new APIs
- Error capture verified working

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry JavaScript Changelog](https://github.com/getsentry/sentry-javascript/blob/master/CHANGELOG.md)
- [Sentry Python Changelog](https://github.com/getsentry/sentry-python/blob/master/CHANGELOG.md)
- [Migration Guides](https://docs.sentry.io/platforms/javascript/migration/)