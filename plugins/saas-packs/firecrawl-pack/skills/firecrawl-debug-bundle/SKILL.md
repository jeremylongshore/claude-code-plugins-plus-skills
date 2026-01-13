---
allowed-tools: Read, Bash, Grep
license: MIT
description: Collect firecrawl debug evidence for support tickets and troubleshooting.
  use when encountering persistent issues, preparing support tickets, or collecting
  diagnostic information for firecrawl problems. trigger with phrases like "firecrawl
  debug",...
name: firecrawl-debug-bundle
---
# Firecrawl Debug Bundle

This skill provides automated assistance for firecrawl debug bundle tasks.

## Prerequisites
- FireCrawl SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `firecrawl-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [FireCrawl Support](https://docs.firecrawl.com/support)
- [FireCrawl Status](https://status.firecrawl.com)