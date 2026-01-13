---
allowed-tools: Read, Bash, Grep
license: MIT
description: Collect retell ai debug evidence for support tickets and troubleshooting.
  use when encountering persistent issues, preparing support tickets, or collecting
  diagnostic information for retell ai problems. trigger with phrases like "retellai
  debug", ...
name: retellai-debug-bundle
---
# Retellai Debug Bundle

This skill provides automated assistance for retellai debug bundle tasks.

## Prerequisites
- Retell AI SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `retellai-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Retell AI Support](https://docs.retellai.com/support)
- [Retell AI Status](https://status.retellai.com)