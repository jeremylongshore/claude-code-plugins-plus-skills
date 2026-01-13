---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Analyze, plan, and execute Instantly SDK upgrades with breaking change
  detection. Use when upgrading Instantly SDK versions, detecting deprecations, or
  migrating to new API versions. Trigger with phrases like "upgrade instantly", "instantly
  migrat...
name: instantly-upgrade-migration
---
# Instantly Upgrade Migration

This skill provides automated assistance for instantly upgrade migration tasks.

## Prerequisites
- Current Instantly SDK installed
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
- [Instantly Changelog](https://github.com/instantly/sdk/releases)
- [Instantly Migration Guide](https://docs.instantly.com/migration)