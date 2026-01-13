---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Debug AI suggestions and code generation in Cursor. Triggers on "debug
  cursor ai", "cursor suggestions wrong", "bad cursor completion", "cursor ai debug".
  Use when debugging issues or troubleshooting. Trigger with phrases like "cursor
  debug bundle...
name: cursor-debug-bundle
---
# Cursor Debug Bundle

This skill provides automated assistance for cursor debug bundle tasks.

## Overview

This skill helps debug AI suggestions and code generation issues in Cursor. It covers understanding why AI gives wrong suggestions, debugging completions, chat context issues, and diagnostic tools for troubleshooting AI behavior.

## Prerequisites

- Cursor IDE with AI features active
- Understanding of AI behavior factors
- Access to settings and developer tools
- Ability to view and export logs

## Instructions

1. Identify the type of AI issue (completion, chat, composer)
2. Check common causes (context, rules, model)
3. Use debugging tools (dev tools, verbose logging)
4. Test with different models and settings
5. Apply fix and verify improvement
6. Document solution for future reference

## Output

- Identified root cause of AI issues
- Improved AI suggestion quality
- Updated configuration if needed
- Documented debugging process

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Cursor Debug Guide](https://cursor.com/docs/debugging)
- [AI Troubleshooting](https://cursor.com/docs/troubleshooting)
- [Cursor GitHub Issues](https://github.com/getcursor/cursor/issues)