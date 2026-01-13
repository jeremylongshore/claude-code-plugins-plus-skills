---
allowed-tools: Read, Bash, Grep
license: MIT
description: Collect exa debug evidence for support tickets and troubleshooting. use
  when encountering persistent issues, preparing support tickets, or collecting diagnostic
  information for exa problems. trigger with phrases like "exa debug", "exa support
  bund...
name: exa-debug-bundle
---
# Exa Debug Bundle

This skill provides automated assistance for exa debug bundle tasks.

## Prerequisites
- Exa SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `exa-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Exa Support](https://docs.exa.com/support)
- [Exa Status](https://status.exa.com)