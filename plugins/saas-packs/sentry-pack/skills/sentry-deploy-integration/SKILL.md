---
name: sentry-deploy-integration
description: |
  Track deployments and releases in sentry. use when configuring deployment tracking, release health, or connecting deployments to error data. trigger with phrases like "sentry deploy tracking", "sentry release health", "track deployments sentry", "...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Sentry Deploy Integration

This skill provides automated assistance for sentry deploy integration tasks.

## Prerequisites

- Sentry CLI installed
- `SENTRY_AUTH_TOKEN` configured
- Build pipeline access
- Source maps generated during build

## Instructions

1. Create release using git SHA or semantic version with sentry-cli
2. Upload source maps from build output directory
3. Associate commits using sentry-cli releases set-commits --auto
4. Finalize the release to mark it complete
5. Deploy application to target environment
6. Notify Sentry of deployment with environment and timestamps
7. Enable session tracking for release health metrics
8. Configure environment-specific sample rates
9. Set up rollback tracking to record version changes
10. Use Sentry dashboard to compare releases and monitor health

## Output
- Releases created for each deployment
- Source maps uploaded and linked
- Deployment notifications sent
- Release health metrics tracked

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Releases](https://docs.sentry.io/product/releases/)
- [Release Health](https://docs.sentry.io/product/releases/health/)