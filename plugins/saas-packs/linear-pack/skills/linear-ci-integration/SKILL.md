---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Configure Linear CI/CD integration with GitHub Actions and testing. Use
  when setting up automated testing, configuring CI pipelines, or integrating Linear
  sync into your build process. Trigger with phrases like "linear CI", "linear GitHub
  Actions"...
name: linear-ci-integration
---
# Linear Ci Integration

This skill provides automated assistance for linear ci integration tasks.

## Prerequisites
- GitHub repository with Actions enabled
- Linear API key for CI
- npm/pnpm project configured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Automated test pipeline
- PR-to-issue linking
- Automatic state transitions
- Failure issue creation
- Test result artifacts

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Linear GitHub Integration](https://linear.app/docs/github)
- [Linear API Authentication](https://developers.linear.app/docs/graphql/authentication)