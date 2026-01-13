---
name: posthog-ci-integration
description: |
  Configure PostHog CI/CD integration with GitHub Actions and testing. Use when setting up automated testing, configuring CI pipelines, or integrating PostHog tests into your build process. Trigger with phrases like "posthog CI", "posthog GitHub Act...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Posthog Ci Integration

This skill provides automated assistance for posthog ci integration tasks.

## Prerequisites
- GitHub repository with Actions enabled
- PostHog test API key
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
- [PostHog CI Guide](https://docs.posthog.com/ci)