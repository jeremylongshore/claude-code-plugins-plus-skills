---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Analyze, plan, and execute Clay SDK upgrades with breaking change detection.
  Use when upgrading Clay SDK versions, detecting deprecations, or migrating to new
  API versions. Trigger with phrases like "upgrade clay", "clay migration", "clay
  breaking...
name: clay-upgrade-migration
---
# Clay Upgrade Migration

This skill provides automated assistance for clay upgrade migration tasks.

## Prerequisites
- Current Clay SDK installed
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
- [Clay Changelog](https://github.com/clay/sdk/releases)
- [Clay Migration Guide](https://docs.clay.com/migration)