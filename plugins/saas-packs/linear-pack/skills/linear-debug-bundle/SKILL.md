---
name: linear-debug-bundle
description: |
  Comprehensive debugging toolkit for linear integrations. use when setting up logging, tracing api calls, or building debug utilities for linear. trigger with phrases like "debug linear integration", "linear logging", "trace linear api", "linear de...
allowed-tools: Read, Write, Edit, Grep, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Linear Debug Bundle

This skill provides automated assistance for linear debug bundle tasks.

## Prerequisites
- Linear SDK configured
- Node.js environment
- Optional: logging library (pino, winston)


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Debug client with request/response logging
- Request tracer with performance metrics
- Health check endpoint
- Interactive debug console
- Environment validator

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Linear SDK Source](https://github.com/linear/linear)
- [Node.js Debugging](https://nodejs.org/en/docs/guides/debugging-getting-started)
- [Performance Tracing](https://nodejs.org/api/perf_hooks.html)