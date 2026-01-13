---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Analyze, plan, and execute Vast.ai SDK upgrades with breaking change
  detection. Use when upgrading Vast.ai SDK versions, detecting deprecations, or migrating
  to new API versions. Trigger with phrases like "upgrade vastai", "vastai migration",
  "vas...
name: vastai-upgrade-migration
---
# Vastai Upgrade Migration

This skill provides automated assistance for vastai upgrade migration tasks.

## Prerequisites
- Current Vast.ai SDK installed
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
- [Vast.ai Changelog](https://github.com/vastai/sdk/releases)
- [Vast.ai Migration Guide](https://docs.vastai.com/migration)