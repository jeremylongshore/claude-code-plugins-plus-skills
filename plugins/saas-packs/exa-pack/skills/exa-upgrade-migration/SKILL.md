---
name: exa-upgrade-migration
description: |
  Analyze, plan, and execute Exa SDK upgrades with breaking change detection. Use when upgrading Exa SDK versions, detecting deprecations, or migrating to new API versions. Trigger with phrases like "upgrade exa", "exa migration", "exa breaking chan...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Exa Upgrade Migration

This skill provides automated assistance for exa upgrade migration tasks.

## Prerequisites
- Current Exa SDK installed
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
- [Exa Changelog](https://github.com/exa/sdk/releases)
- [Exa Migration Guide](https://docs.exa.com/migration)