---
name: sentry-local-dev-loop
license: MIT
allowed-tools: Read, Write, Edit, Bash, Grep
description: Execute set up local development workflow with sentry. use when configuring
  sentry for development environments, setting up debug mode, or testing error capture
  locally. trigger with phrases like "sentry local dev", "sentry development", "debug
  se...
---
# Sentry Local Dev Loop

## Prerequisites
- Sentry SDK installed
- Development environment set up
- Separate Sentry project for development (recommended)


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Environment-aware Sentry configuration
- Debug logging enabled for development
- Separate project/DSN for development events

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sentry Environment Config](https://docs.sentry.io/platforms/javascript/configuration/environments/)
- [Sentry Debug Mode](https://docs.sentry.io/platforms/javascript/configuration/options/#debug)
