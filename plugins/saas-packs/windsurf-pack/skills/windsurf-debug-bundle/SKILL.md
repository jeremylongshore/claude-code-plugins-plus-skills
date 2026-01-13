---
allowed-tools: Read, Bash, Grep
license: MIT
description: Collect windsurf debug evidence for support tickets and troubleshooting.
  use when encountering persistent issues, preparing support tickets, or collecting
  diagnostic information for windsurf problems. trigger with phrases like "windsurf
  debug", "w...
name: windsurf-debug-bundle
---
# Windsurf Debug Bundle

This skill provides automated assistance for windsurf debug bundle tasks.

## Prerequisites
- Windsurf SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `windsurf-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Windsurf Support](https://docs.windsurf.com/support)
- [Windsurf Status](https://status.windsurf.com)