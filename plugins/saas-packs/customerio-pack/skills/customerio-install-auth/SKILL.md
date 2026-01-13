---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Install and configure customer.io sdk/cli authentication. use when setting
  up a new customer.io integration, configuring api keys, or initializing customer.io
  in your project. trigger with phrases like "install customer.io", "setup customer.io",
  "...
name: customerio-install-auth
---
# Customerio Install Auth

This skill provides automated assistance for customerio install auth tasks.

## Prerequisites
- Node.js 18+ or Python 3.10+
- Package manager (npm, pnpm, or pip)
- Customer.io account with API access
- Site ID and API Key from Customer.io dashboard


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Installed SDK package in node_modules or site-packages
- Environment variables or .env file with Site ID and API Key
- Successful connection verification output

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Customer.io Documentation](https://customer.io/docs/)
- [Track API Reference](https://customer.io/docs/api/track/)
- [Customer.io Status](https://status.customer.io/)