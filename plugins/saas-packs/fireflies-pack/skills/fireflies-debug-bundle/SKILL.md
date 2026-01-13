---
name: fireflies-debug-bundle
description: |
  Collect fireflies.ai debug evidence for support tickets and troubleshooting. use when encountering persistent issues, preparing support tickets, or collecting diagnostic information for fireflies.ai problems. trigger with phrases like "fireflies d...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Fireflies Debug Bundle

This skill provides automated assistance for fireflies debug bundle tasks.

## Prerequisites
- Fireflies.ai SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `fireflies-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Fireflies.ai Support](https://docs.fireflies.com/support)
- [Fireflies.ai Status](https://status.fireflies.com)