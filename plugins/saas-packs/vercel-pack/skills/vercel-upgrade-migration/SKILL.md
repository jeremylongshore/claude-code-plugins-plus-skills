---
name: vercel-upgrade-migration
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Execute analyze, plan, and execute vercel sdk upgrades with breaking
  change detection. use when upgrading vercel sdk versions, detecting deprecations,
  or migrating to new api versions. trigger with phrases like "upgrade vercel", "vercel
  migration"...
---
# Vercel Upgrade Migration

## Prerequisites
- Current Vercel SDK installed
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
- [Vercel Changelog](https://github.com/vercel/vercel/releases)
- [Vercel Migration Guide](https://vercel.com/docs/migration)
