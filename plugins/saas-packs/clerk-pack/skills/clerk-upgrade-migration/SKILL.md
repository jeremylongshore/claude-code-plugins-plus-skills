---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Upgrade clerk sdk versions and handle breaking changes. use when upgrading
  clerk packages, migrating to new sdk versions, or handling deprecation warnings.
  trigger with phrases like "upgrade clerk", "clerk migration", "update clerk sdk",
  "clerk br...
name: clerk-upgrade-migration
---
# Clerk Upgrade Migration

This skill provides automated assistance for clerk upgrade migration tasks.

## Prerequisites
- Current Clerk integration working
- Git repository with clean working state
- Test environment available


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Updated Clerk SDK
- Migrated breaking changes
- All tests passing
- Production deployment ready

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Clerk Changelog](https://clerk.com/changelog)
- [Migration Guides](https://clerk.com/docs/upgrade-guides)
- [GitHub Releases](https://github.com/clerk/javascript/releases)