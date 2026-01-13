---
name: instantly-ci-integration
description: |
  Configure Instantly CI/CD integration with GitHub Actions and testing. Use when setting up automated testing, configuring CI pipelines, or integrating Instantly tests into your build process. Trigger with phrases like "instantly CI", "instantly Gi...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Instantly Ci Integration

This skill provides automated assistance for instantly ci integration tasks.

## Prerequisites
- GitHub repository with Actions enabled
- Instantly test API key
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
- [Instantly CI Guide](https://docs.instantly.com/ci)