---
allowed-tools: Read, Bash, Grep
license: MIT
description: Collect ideogram debug evidence for support tickets and troubleshooting.
  use when encountering persistent issues, preparing support tickets, or collecting
  diagnostic information for ideogram problems. trigger with phrases like "ideogram
  debug", "i...
name: ideogram-debug-bundle
---
# Ideogram Debug Bundle

This skill provides automated assistance for ideogram debug bundle tasks.

## Prerequisites
- Ideogram SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `ideogram-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Ideogram Support](https://docs.ideogram.com/support)
- [Ideogram Status](https://status.ideogram.com)