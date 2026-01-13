---
allowed-tools: Read, Bash, Grep
license: MIT
description: Collect coderabbit debug evidence for support tickets and troubleshooting.
  use when encountering persistent issues, preparing support tickets, or collecting
  diagnostic information for coderabbit problems. trigger with phrases like "coderabbit
  debu...
name: coderabbit-debug-bundle
---
# Coderabbit Debug Bundle

This skill provides automated assistance for coderabbit debug bundle tasks.

## Prerequisites
- CodeRabbit SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `coderabbit-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [CodeRabbit Support](https://docs.coderabbit.com/support)
- [CodeRabbit Status](https://status.coderabbit.com)