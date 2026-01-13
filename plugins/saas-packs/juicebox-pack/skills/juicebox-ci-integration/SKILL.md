---
name: juicebox-ci-integration
description: |
  Configure Juicebox CI/CD integration with GitHub Actions and testing. Use when setting up automated testing, configuring CI pipelines, or integrating Juicebox tests into your build process. Trigger with phrases like "juicebox CI", "juicebox GitHub...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Juicebox Ci Integration

This skill provides automated assistance for juicebox ci integration tasks.

## Prerequisites
- GitHub repository with Actions enabled
- Juicebox test API key
- npm/pnpm project configured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- GitHub Actions workflow files
- Integration test suite
- Branch protection rules
- Deployment pipeline

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Juicebox CI Guide](https://juicebox.ai/docs/ci)