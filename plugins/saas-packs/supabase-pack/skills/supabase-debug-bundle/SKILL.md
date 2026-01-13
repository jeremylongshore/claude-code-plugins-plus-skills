---
name: supabase-debug-bundle
license: MIT
allowed-tools: Read, Bash, Grep
description: Execute collect supabase debug evidence for support tickets and troubleshooting.
  use when encountering persistent issues, preparing support tickets, or collecting
  diagnostic information for supabase problems. trigger with phrases like "supabase
  de...
---
# Supabase Debug Bundle

## Prerequisites
- Supabase SDK installed
- Access to application logs
- Permission to collect environment info


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `supabase-debug-YYYYMMDD-HHMMSS.tar.gz` archive containing:
  - `summary.txt` - Environment and SDK info
  - `logs.txt` - Recent redacted logs
  - `config-redacted.txt` - Configuration (secrets removed)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Supabase Support](https://supabase.com/docs/support)
- [Supabase Status](https://status.supabase.com)
