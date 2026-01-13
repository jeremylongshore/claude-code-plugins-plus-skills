---
name: deepgram-local-dev-loop
description: |
  Configure Deepgram local development workflow with testing and iteration. Use when setting up development environment, configuring test fixtures, or establishing rapid iteration patterns for Deepgram integration. Trigger with phrases like "deepgra...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Deepgram Local Dev Loop

This skill provides automated assistance for deepgram local dev loop tasks.

## Prerequisites
- Completed `deepgram-install-auth` setup
- Node.js 18+ with npm/pnpm or Python 3.10+
- Sample audio files for testing
- Environment variables configured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Project structure with src, tests, fixtures directories
- Environment files for development and testing
- Watch mode scripts for rapid iteration
- Sample audio fixtures for testing

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Deepgram SDK Reference](https://developers.deepgram.com/docs/sdk)
- [Vitest Documentation](https://vitest.dev/)
- [dotenv Configuration](https://github.com/motdotla/dotenv)