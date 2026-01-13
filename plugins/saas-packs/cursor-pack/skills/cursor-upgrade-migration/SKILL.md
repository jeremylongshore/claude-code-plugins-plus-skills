---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Execute upgrade cursor versions and migrate settings. triggers on "upgrade
  cursor", "update cursor", "cursor migration", "cursor new version", "cursor changelog".
  use when working with cursor upgrade migration functionality. trigger with phrases
  l...
name: cursor-upgrade-migration
---
# Cursor Upgrade Migration

This skill provides automated assistance for cursor upgrade migration tasks.

## Overview

This skill provides comprehensive guidance for upgrading Cursor IDE versions and migrating settings between installations. It covers version checking, upgrade methods, settings backup, and troubleshooting common migration issues.

## Prerequisites

- Current Cursor installation to upgrade
- Backup of current settings (recommended)
- Admin rights for installation (if required)
- Network access for download

## Instructions

1. Check current version (Help > About)
2. Backup settings and extensions list
3. Check release notes for breaking changes
4. Apply update (auto-update or manual download)
5. Verify settings preserved
6. Test AI features working
7. Reinstall extensions if needed

## Output

- Updated Cursor installation
- Preserved settings and configurations
- Verified working AI features
- Documented changes and fixes

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Cursor Changelog](https://cursor.com/changelog)
- [Cursor Downloads](https://cursor.com/download)
- [Settings Sync Documentation](https://cursor.com/docs/sync)
- [Cursor GitHub Releases](https://github.com/getcursor/cursor/releases)