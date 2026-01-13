---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Analyze, plan, and execute Ideogram SDK upgrades with breaking change
  detection. Use when upgrading Ideogram SDK versions, detecting deprecations, or
  migrating to new API versions. Trigger with phrases like "upgrade ideogram", "ideogram
  migration"...
name: ideogram-upgrade-migration
---
# Ideogram Upgrade Migration

This skill provides automated assistance for ideogram upgrade migration tasks.

## Prerequisites
- Current Ideogram SDK installed
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
- [Ideogram Changelog](https://github.com/ideogram/sdk/releases)
- [Ideogram Migration Guide](https://docs.ideogram.com/migration)