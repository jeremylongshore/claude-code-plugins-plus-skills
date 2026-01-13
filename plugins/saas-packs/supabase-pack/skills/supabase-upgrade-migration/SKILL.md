---
name: supabase-upgrade-migration
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Execute analyze, plan, and execute supabase sdk upgrades with breaking
  change detection. use when upgrading supabase sdk versions, detecting deprecations,
  or migrating to new api versions. trigger with phrases like "upgrade supabase",
  "supabase mi...
---
# Supabase Upgrade Migration

## Prerequisites
- Current Supabase SDK installed
- Git for version control
- Test suite available
- Staging environment


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Updated SDK version
- Fixed breaking changes
- Passing test suite
- Documented rollback procedure

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Supabase Changelog](https://github.com/supabase/sdk/releases)
- [Supabase Migration Guide](https://supabase.com/docs/migration)
