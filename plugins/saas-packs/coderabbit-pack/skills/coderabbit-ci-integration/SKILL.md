---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Configure CodeRabbit CI/CD integration with GitHub Actions and testing.
  Use when setting up automated testing, configuring CI pipelines, or integrating
  CodeRabbit tests into your build process. Trigger with phrases like "coderabbit
  CI", "coderabbi...
name: coderabbit-ci-integration
---
# Coderabbit Ci Integration

This skill provides automated assistance for coderabbit ci integration tasks.

## Prerequisites
- GitHub repository with Actions enabled
- CodeRabbit test API key
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
- [CodeRabbit CI Guide](https://docs.coderabbit.com/ci)