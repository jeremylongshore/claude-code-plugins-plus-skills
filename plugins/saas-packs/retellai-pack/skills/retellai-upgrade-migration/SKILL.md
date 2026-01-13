---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Analyze, plan, and execute Retell AI SDK upgrades with breaking change
  detection. Use when upgrading Retell AI SDK versions, detecting deprecations, or
  migrating to new API versions. Trigger with phrases like "upgrade retellai", "retellai
  migratio...
name: retellai-upgrade-migration
---
# Retellai Upgrade Migration

This skill provides automated assistance for retellai upgrade migration tasks.

## Prerequisites
- Current Retell AI SDK installed
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
- [Retell AI Changelog](https://github.com/retellai/sdk/releases)
- [Retell AI Migration Guide](https://docs.retellai.com/migration)