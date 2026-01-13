---
name: customerio-ci-integration
description: |
  Configure Customer.io CI/CD integration. Use when setting up automated testing, deployment pipelines, or continuous integration for Customer.io integrations. Trigger with phrases like "customer.io ci", "customer.io github actions", "customer.io pi...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Customerio Ci Integration

This skill provides automated assistance for customerio ci integration tasks.

## Prerequisites
- CI/CD platform (GitHub Actions, GitLab CI, etc.)
- Separate Customer.io workspace for testing
- Secrets management configured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- GitHub Actions workflow for testing
- GitLab CI configuration
- Integration test suite
- Pre-commit hooks
- Environment management

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [GitHub Actions Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [GitLab CI Variables](https://docs.gitlab.com/ee/ci/variables/)