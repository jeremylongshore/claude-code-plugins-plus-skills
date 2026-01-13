---
allowed-tools: Read, Bash, Grep
license: MIT
description: Collect perplexity debug evidence for support tickets and troubleshooting.
  use when encountering persistent issues, preparing support tickets, or collecting
  diagnostic information for perplexity problems. trigger with phrases like "perplexity
  debu...
name: perplexity-debug-bundle
---
# Perplexity Debug Bundle

This skill provides automated assistance for perplexity debug bundle tasks.

## Prerequisites
- Perplexity SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `perplexity-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Perplexity Support](https://docs.perplexity.com/support)
- [Perplexity Status](https://status.perplexity.com)