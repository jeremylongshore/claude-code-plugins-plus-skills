---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Configure Apollo.io CI/CD integration. Use when setting up automated
  testing, continuous integration, or deployment pipelines for Apollo integrations.
  Trigger with phrases like "apollo ci", "apollo github actions", "apollo pipeline",
  "apollo ci/cd...
name: apollo-ci-integration
---
# Apollo Ci Integration

This skill provides automated assistance for apollo ci integration tasks.

## Output
- GitHub Actions workflows for CI
- Secrets management configuration
- Test setup with MSW mocks
- Integration test suite
- Validation scripts

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [GitHub Actions Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [MSW (Mock Service Worker)](https://mswjs.io/)
- [Vitest Documentation](https://vitest.dev/)