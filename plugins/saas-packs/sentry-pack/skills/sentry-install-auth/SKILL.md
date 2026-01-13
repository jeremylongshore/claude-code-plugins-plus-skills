---
name: sentry-install-auth
license: MIT
allowed-tools: Read, Write, Edit, Bash, Grep
description: Install and configure sentry sdk authentication. use when setting up
  a new sentry integration, configuring dsn, or initializing sentry in your project.
  trigger with phrases like "install sentry", "setup sentry", "sentry auth", "configure
  sentry dsn".
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
