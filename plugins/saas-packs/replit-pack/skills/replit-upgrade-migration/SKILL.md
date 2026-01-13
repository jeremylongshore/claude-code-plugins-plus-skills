---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Analyze, plan, and execute Replit SDK upgrades with breaking change detection.
  Use when upgrading Replit SDK versions, detecting deprecations, or migrating to
  new API versions. Trigger with phrases like "upgrade replit", "replit migration",
  "repli...
name: replit-upgrade-migration
---
# Replit Upgrade Migration

This skill provides automated assistance for replit upgrade migration tasks.

## Prerequisites
- Current Replit SDK installed
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
- [Replit Changelog](https://github.com/replit/sdk/releases)
- [Replit Migration Guide](https://docs.replit.com/migration)