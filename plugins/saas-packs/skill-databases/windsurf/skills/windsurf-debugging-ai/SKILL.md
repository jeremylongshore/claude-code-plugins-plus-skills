---
name: windsurf-debugging-ai
description: |
  Execute use cascade for intelligent debugging and error analysis. activate when users mention "debug with ai", "error analysis", "cascade debug", "find bug", or "troubleshoot code". handles ai-assisted debugging workflows. use when debugging issue...
allowed-tools: Read, Grep, Glob, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Windsurf Debugging Ai

This skill provides automated assistance for windsurf debugging ai tasks.

## Overview

This skill enables AI-assisted debugging within Windsurf. Cascade analyzes error messages, stack traces, and code context to identify root causes and suggest fixes. It learns from your codebase patterns to provide contextually relevant debugging assistance, reducing time spent on common errors and helping identify subtle bugs that might otherwise be missed.

## Prerequisites

- Windsurf IDE with Cascade enabled
- Application with reproducible issues
- Debug configuration set up
- Error logs accessible
- Understanding of application architecture

## Instructions

1. **Capture Error Context**
2. **Analyze with Cascade**
3. **Investigate Root Cause**
4. **Apply Fix**
5. **Document for Prevention**


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- Root cause analysis
- Fix recommendations
- Debug session logs
- Prevention strategies

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Windsurf Debugging Guide](https://docs.windsurf.ai/features/debugging)
- [AI-Assisted Debugging](https://docs.windsurf.ai/cascade/debugging)
- [Debug Configuration Reference](https://docs.windsurf.ai/reference/debug-config)