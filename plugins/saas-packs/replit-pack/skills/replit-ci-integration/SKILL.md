---
name: replit-ci-integration
description: |
  Configure Replit CI/CD integration with GitHub Actions and testing. Use when setting up automated testing, configuring CI pipelines, or integrating Replit tests into your build process. Trigger with phrases like "replit CI", "replit GitHub Actions...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Replit Ci Integration

This skill provides automated assistance for replit ci integration tasks.

## Prerequisites
- GitHub repository with Actions enabled
- Replit test API key
- npm/pnpm project configured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Automated test pipeline
- PR checks configured
- Coverage reports uploaded
- Release workflow ready

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Replit CI Guide](https://docs.replit.com/ci)