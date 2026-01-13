---
name: windsurf-git-integration
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Configure Git integration with Cascade AI assistance. Activate when users
  mention "git setup", "version control", "commit messages", "branch management",
  or "source control". Handles Git configuration and AI-assisted workflows. Use when
  working wi...
---
# Windsurf Git Integration

## Overview

This skill enables AI-assisted Git workflows within Windsurf. Cascade can generate commit messages from staged changes, suggest branch names, assist with merge conflict resolution, and automate common Git operations. It integrates with hooks for validation and provides intelligent suggestions that follow your team's conventions.

## Prerequisites

- Git installed and configured
- Windsurf IDE with Cascade enabled
- Git repository initialized
- SSH keys or HTTPS credentials configured
- Understanding of team Git workflow (GitFlow, trunk-based, etc.)

## Instructions

1. **Configure Git Credentials**
2. **Set Up AI Assistance**
3. **Install Git Hooks**
4. **Configure Team Standards**
5. **Train on Workflow**


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- Configured Git hooks
- AI-assisted commit messages
- Branch naming suggestions
- PR descriptions with context

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Windsurf Git Integration](https://docs.windsurf.ai/features/git)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Hooks Documentation](https://git-scm.com/docs/githooks)
