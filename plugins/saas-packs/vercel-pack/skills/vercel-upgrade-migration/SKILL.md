---
name: vercel-upgrade-migration
description: |
  Execute analyze, plan, and execute Vercel SDK upgrades with breaking change detection.
  Use when upgrading Vercel SDK versions, detecting deprecations,
  or migrating to new API versions.
  Trigger with phrases like "upgrade vercel", "vercel migration",
  "vercel breaking changes", "update vercel SDK", "analyze vercel version".
allowed-tools: Read, Write, Edit, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Vercel Upgrade Migration

## Prerequisites
- Current Vercel SDK installed
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
- [Vercel Changelog](https://github.com/vercel/vercel/releases)
- [Vercel Migration Guide](https://vercel.com/docs/migration)
