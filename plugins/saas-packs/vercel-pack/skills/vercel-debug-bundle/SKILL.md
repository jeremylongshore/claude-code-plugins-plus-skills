---
allowed-tools: Read, Bash, Grep
license: MIT
description: Execute collect vercel debug evidence for support tickets and troubleshooting.
  use when encountering persistent issues, preparing support tickets, or collecting
  diagnostic information for vercel problems. trigger with phrases like "vercel debug",
  ...
name: vercel-debug-bundle
---
# Vercel Debug Bundle

This skill provides automated assistance for vercel debug bundle tasks.

## Prerequisites
- Vercel SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `vercel-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Vercel Support](https://vercel.com/docs/support)
- [Vercel Status](https://www.vercel-status.com)