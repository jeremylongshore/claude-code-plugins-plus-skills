---
name: gastown
description: |
  Manage multi-agent orchestrator for Claude Code. Use when user mentions gastown, gas town, gt commands, bd commands, convoys, polecats, crew, rigs, slinging work, multi-agent coordination, beads, hooks, molecules, workflows, the witness, the mayor...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep, Glob, WebFetch
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: Apache-2.0
---
# Gastown

This skill provides automated assistance for gastown tasks.

## Overview

Gas Town is a multi-agent orchestration system for Claude Code that enables parallel AI workers to execute tasks simultaneously. It provides work tracking through beads, agent lifecycle management via polecats and crew, and automated code merging through the Refinery.

## Prerequisites

- Go 1.21+ installed for CLI tools (`gt` and `bd`)
- Git configured with SSH or HTTPS access
- Terminal access for running commands
- Sufficient disk space for workspace (~100MB for ~/gt)
- GitHub account for repository integration (optional)

## Instructions

1. Install Gas Town CLI tools (gt and bd) using Go
2. Create your workshop directory at ~/gt
3. Run diagnostics with gt doctor and bd doctor
4. Add a project as a rig using gt rig add
5. Create work items as beads using bd create
6. Sling work to agents using gt sling
7. Monitor progress with gt status and gt peek
8. Let the Refinery merge completed work

The Cognition Engine. Track work with convoys; sling to agents.

## Output

- Executed gt and bd commands with results reported to user
- Engine status reports showing system health and worker states
- Work tracking updates (beads created, assigned, completed)
- Polecat and crew lifecycle events (spawn, completion, termination)
- Diagnostic results from gt doctor and bd doctor
- Merge pipeline status from Refinery operations

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

