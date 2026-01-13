---
name: groq-upgrade-migration
description: |
  Analyze, plan, and execute Groq SDK upgrades with breaking change detection. Use when upgrading Groq SDK versions, detecting deprecations, or migrating to new API versions. Trigger with phrases like "upgrade groq", "groq migration", "groq breaking...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Groq Upgrade Migration

This skill provides automated assistance for groq upgrade migration tasks.

## Prerequisites
- Current Groq SDK installed
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
- [Groq Changelog](https://github.com/groq/sdk/releases)
- [Groq Migration Guide](https://docs.groq.com/migration)