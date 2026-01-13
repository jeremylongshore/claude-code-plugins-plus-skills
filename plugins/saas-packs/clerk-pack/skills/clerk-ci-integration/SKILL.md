---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Configure Clerk CI/CD integration with GitHub Actions and testing. Use
  when setting up automated testing, configuring CI pipelines, or integrating Clerk
  tests into your build process. Trigger with phrases like "clerk CI", "clerk GitHub
  Actions", "...
name: clerk-ci-integration
---
# Clerk Ci Integration

This skill provides automated assistance for clerk ci integration tasks.

## Prerequisites
- GitHub repository with Actions enabled
- Clerk test API keys
- npm/pnpm project configured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- GitHub Actions workflows configured
- E2E tests with Playwright
- Test user management
- CI/CD pipeline ready

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Playwright Testing](https://playwright.dev)
- [Clerk Testing Guide](https://clerk.com/docs/testing/overview)