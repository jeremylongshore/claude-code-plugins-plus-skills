---
name: sentry-install-auth
description: |
  Install and configure Sentry SDK authentication.
  Use when setting up a new Sentry integration, configuring DSN,
  or initializing Sentry in your project.
  Trigger with phrases like "install sentry", "setup sentry",
  "sentry auth", "configure sentry DSN".
allowed-tools: Read, Write, Edit, Bash, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Sentry Install Auth

## Prerequisites
- Node.js 18+ or Python 3.10+
- Package manager (npm, pnpm, or pip)
- Sentry account with project DSN
- DSN from Sentry project settings


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Installed SDK package in node_modules or site-packages
- Environment variable or .env file with DSN
- Sentry initialized and ready to capture errors

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Documentation](https://docs.sentry.io)
- [Sentry Dashboard](https://sentry.io)
- [Sentry Status](https://status.sentry.io)
