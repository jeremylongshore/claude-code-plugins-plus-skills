---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Install and configure clerk sdk/cli authentication. use when setting
  up a new clerk integration, configuring api keys, or initializing clerk in your
  project. trigger with phrases like "install clerk", "setup clerk", "clerk auth",
  "configure clerk ...
name: clerk-install-auth
---
# Clerk Install Auth

This skill provides automated assistance for clerk install auth tasks.

## Prerequisites
- Node.js 18+ (Next.js, React, Express, etc.)
- Package manager (npm, pnpm, or yarn)
- Clerk account with API access
- Publishable and Secret keys from Clerk dashboard


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Installed SDK package in node_modules
- Environment variables configured in .env.local
- ClerkProvider wrapping application
- Middleware protecting routes

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Clerk Documentation](https://clerk.com/docs)
- [Clerk Dashboard](https://dashboard.clerk.com)
- [Clerk Status](https://status.clerk.com)