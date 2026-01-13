---
name: posthog-upgrade-migration
description: |
  Analyze, plan, and execute PostHog SDK upgrades with breaking change detection. Use when upgrading PostHog SDK versions, detecting deprecations, or migrating to new API versions. Trigger with phrases like "upgrade posthog", "posthog migration", "p...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Posthog Upgrade Migration

This skill provides automated assistance for posthog upgrade migration tasks.

## Prerequisites
- Current PostHog SDK installed
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
- [PostHog Changelog](https://github.com/posthog/sdk/releases)
- [PostHog Migration Guide](https://docs.posthog.com/migration)