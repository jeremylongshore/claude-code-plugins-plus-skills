---
name: linear-upgrade-migration
description: |
  Upgrade linear sdk versions and migrate breaking changes. use when updating to a new sdk version, handling deprecations, or migrating between major linear api versions. trigger with phrases like "upgrade linear sdk", "linear sdk migration", "updat...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Linear Upgrade Migration

This skill provides automated assistance for linear upgrade migration tasks.

## Prerequisites
- Existing Linear integration
- Version control (Git) configured
- Test suite for Linear operations


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Resources
- [Linear SDK Changelog](https://github.com/linear/linear/blob/master/packages/sdk/CHANGELOG.md)
- [Linear API Changelog](https://developers.linear.app/docs/changelog)
- [TypeScript Migration](https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html)