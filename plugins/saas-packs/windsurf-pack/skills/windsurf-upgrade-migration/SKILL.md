---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Analyze, plan, and execute Windsurf SDK upgrades with breaking change
  detection. Use when upgrading Windsurf SDK versions, detecting deprecations, or
  migrating to new API versions. Trigger with phrases like "upgrade windsurf", "windsurf
  migration"...
name: windsurf-upgrade-migration
---
# Windsurf Upgrade Migration

This skill provides automated assistance for windsurf upgrade migration tasks.

## Prerequisites
- Current Windsurf SDK installed
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
- [Windsurf Changelog](https://github.com/windsurf/sdk/releases)
- [Windsurf Migration Guide](https://docs.windsurf.com/migration)