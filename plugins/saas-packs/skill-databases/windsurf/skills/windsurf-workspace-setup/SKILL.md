---
name: windsurf-workspace-setup
description: |
  Initialize windsurf workspace with project-specific ai rules. activate when users mention "create windsurfrules", "setup workspace", "configure project ai", "initialize windsurf workspace", or "migrate to windsurf". handles workspace configuration...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Windsurf Workspace Setup

This skill provides automated assistance for windsurf workspace setup tasks.

## Overview

This skill enables rapid workspace setup for Windsurf projects. It covers creating .windsurfrules for AI behavior, configuring editor settings, establishing team conventions, and setting up multi-root workspaces. Proper workspace setup ensures consistent AI assistance across all team members and projects.

## Prerequisites

- Windsurf IDE installed
- Project repository cloned
- Understanding of project architecture
- Team conventions documented
- Admin access for team-wide settings (optional)

## Instructions

1. **Create .windsurfrules**
2. **Configure Editor Settings**
3. **Set Up Extensions**
4. **Configure Cross-Editor Consistency**
5. **Establish Team Standards**


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- Configured .windsurfrules file
- Editor settings.json
- Extension recommendations
- Cross-editor configuration files
- Workspace configuration for monorepos

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Windsurf Workspace Guide](https://docs.windsurf.ai/features/workspace)
- [.windsurfrules Reference](https://docs.windsurf.ai/reference/windsurfrules)
- [Multi-Root Workspaces](https://docs.windsurf.ai/features/multi-root)