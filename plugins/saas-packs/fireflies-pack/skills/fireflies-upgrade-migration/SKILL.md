---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Analyze, plan, and execute Fireflies.ai SDK upgrades with breaking change
  detection. Use when upgrading Fireflies.ai SDK versions, detecting deprecations,
  or migrating to new API versions. Trigger with phrases like "upgrade fireflies",
  "fireflies ...
name: fireflies-upgrade-migration
---
# Fireflies Upgrade Migration

This skill provides automated assistance for fireflies upgrade migration tasks.

## Prerequisites
- Current Fireflies.ai SDK installed
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
- [Fireflies.ai Changelog](https://github.com/fireflies/sdk/releases)
- [Fireflies.ai Migration Guide](https://docs.fireflies.com/migration)