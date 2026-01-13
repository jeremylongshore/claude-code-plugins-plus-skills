---
name: vastai-debug-bundle
description: |
  Collect vast.ai debug evidence for support tickets and troubleshooting. use when encountering persistent issues, preparing support tickets, or collecting diagnostic information for vast.ai problems. trigger with phrases like "vastai debug", "vasta...
allowed-tools: Read, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
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