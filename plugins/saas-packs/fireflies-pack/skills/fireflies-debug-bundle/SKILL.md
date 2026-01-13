---
allowed-tools: Read, Bash, Grep
license: MIT
description: Collect fireflies.ai debug evidence for support tickets and troubleshooting.
  use when encountering persistent issues, preparing support tickets, or collecting
  diagnostic information for fireflies.ai problems. trigger with phrases like "fireflies
  d...
name: fireflies-debug-bundle
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