---
name: gamma-ci-integration
description: |
  Configure Gamma CI/CD integration with GitHub Actions and testing. Use when setting up automated testing, configuring CI pipelines, or integrating Gamma tests into your build process. Trigger with phrases like "gamma CI", "gamma GitHub Actions", "...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Gamma Ci Integration

This skill provides automated assistance for gamma ci integration tasks.

## Prerequisites
- GitHub repository with Actions enabled
- Gamma test API key
- npm/pnpm project configured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Automated test pipeline running on push/PR
- Mock mode for PR checks (no API calls)
- Live integration tests on main branch
- Coverage reports uploaded

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Vitest Documentation](https://vitest.dev/)
- [Gamma Testing Guide](https://gamma.app/docs/testing)