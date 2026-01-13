---
allowed-tools: Read, Bash, Grep
license: MIT
description: Collect vast.ai debug evidence for support tickets and troubleshooting.
  use when encountering persistent issues, preparing support tickets, or collecting
  diagnostic information for vast.ai problems. trigger with phrases like "vastai debug",
  "vasta...
name: vastai-debug-bundle
---
# Vastai Debug Bundle

This skill provides automated assistance for vastai debug bundle tasks.

## Prerequisites
- Vast.ai SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `vastai-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Vast.ai Support](https://docs.vastai.com/support)
- [Vast.ai Status](https://status.vastai.com)