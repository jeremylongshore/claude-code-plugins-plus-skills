---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Configure Lindy AI CI/CD integration with GitHub Actions and testing.
  Use when setting up automated testing, configuring CI pipelines, or integrating
  Lindy tests into your build process. Trigger with phrases like "lindy CI", "lindy
  GitHub Actions"...
name: lindy-ci-integration
---
# Lindy Ci Integration

This skill provides automated assistance for lindy ci integration tasks.

## Prerequisites
- GitHub repository with Actions enabled
- Lindy test API key
- npm/pnpm project configured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Automated test pipeline
- PR checks configured
- Coverage reports uploaded
- Integration test suite

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Lindy CI Guide](https://docs.lindy.ai/ci)
- [Jest Configuration](https://jestjs.io/docs/configuration)