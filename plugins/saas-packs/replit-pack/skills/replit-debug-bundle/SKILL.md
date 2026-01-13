---
allowed-tools: Read, Bash, Grep
license: MIT
description: Collect replit debug evidence for support tickets and troubleshooting.
  use when encountering persistent issues, preparing support tickets, or collecting
  diagnostic information for replit problems. trigger with phrases like "replit debug",
  "replit ...
name: replit-debug-bundle
---
# Replit Debug Bundle

This skill provides automated assistance for replit debug bundle tasks.

## Prerequisites
- Replit SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `replit-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Replit Support](https://docs.replit.com/support)
- [Replit Status](https://status.replit.com)