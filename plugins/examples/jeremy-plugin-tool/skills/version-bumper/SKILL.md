---
name: version-bumper
description: |
  Execute automatically handles semantic version updates across plugin.json and marketplace catalog when user mentions version bump, update version, or release. ensures version consistency in AI assistant-code-plugins repository. Use when appropriate context detected. Trigger with relevant phrases based on skill purpose.
allowed-tools: Read, Write, Edit, Grep, Bash
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---

# Version Bumper

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

- Appropriate file access permissions
- Required dependencies installed

## Instructions

1. Invoke this skill when the trigger conditions are met
2. Provide necessary context and parameters
3. Review the generated output
4. Apply modifications as needed

## Output

The output is a concrete, repo-ready version bump plan and execution summary, including the computed `old_version → new_version`, the exact files updated (plugin `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.extended.json`, regenerated `.claude-plugin/marketplace.json` when applicable), and the next validation commands to run.

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- Project documentation
- Related skills and commands
