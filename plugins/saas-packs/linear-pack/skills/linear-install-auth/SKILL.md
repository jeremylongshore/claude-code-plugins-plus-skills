---
name: linear-install-auth
description: |
  Install and configure linear sdk/cli authentication. use when setting up a new linear integration, configuring api keys, or initializing linear in your project. trigger with phrases like "install linear", "setup linear", "linear auth", "configure ...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Linear Install Auth

This skill provides automated assistance for linear install auth tasks.

## Prerequisites
- Node.js 18+ (Linear SDK is TypeScript/JavaScript only)
- Package manager (npm, pnpm, or yarn)
- Linear account with API access
- Personal API key or OAuth app from Linear settings

## Instructions

1. Go to Linear Settings > API > Personal API keys
2. Click "Create key"
3. Copy the generated key (shown only once)


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Installed `@linear/sdk` package in node_modules
- Environment variable or .env file with API key
- Successful connection verification output

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Linear API Documentation](https://developers.linear.app/docs)
- [Linear SDK Reference](https://developers.linear.app/docs/sdk/getting-started)
- [Linear API Settings](https://linear.app/settings/api)