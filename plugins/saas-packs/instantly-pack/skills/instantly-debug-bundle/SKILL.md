---
name: instantly-debug-bundle
description: |
  Collect instantly debug evidence for support tickets and troubleshooting. use when encountering persistent issues, preparing support tickets, or collecting diagnostic information for instantly problems. trigger with phrases like "instantly debug",...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Instantly Debug Bundle

This skill provides automated assistance for instantly debug bundle tasks.

## Prerequisites
- Instantly SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `instantly-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Instantly Support](https://docs.instantly.com/support)
- [Instantly Status](https://status.instantly.com)