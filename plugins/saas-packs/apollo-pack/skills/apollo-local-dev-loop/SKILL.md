---
name: apollo-local-dev-loop
description: |
  Configure Apollo.io local development workflow. Use when setting up development environment, testing API calls locally, or establishing team development practices. Trigger with phrases like "apollo local dev", "apollo development setup", "apollo d...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Apollo Local Dev Loop

This skill provides automated assistance for apollo local dev loop tasks.

## Prerequisites
- Completed `apollo-install-auth` setup
- Node.js 18+ or Python 3.10+
- Git repository initialized


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Environment file structure (.env, .env.example)
- Development client with logging interceptors
- Mock server for testing without API calls
- npm scripts for development workflow
- Quota monitoring utility

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [MSW (Mock Service Worker)](https://mswjs.io/)
- [Vitest Testing Framework](https://vitest.dev/)
- [dotenv Documentation](https://github.com/motdotla/dotenv)