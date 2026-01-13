---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Generate and maintain GitHub Actions with Cascade assistance. Activate
  when users mention "github actions", "ci/cd pipeline", "workflow automation", "continuous
  integration", or "deployment pipeline". Handles CI/CD configuration with AI assistance...
name: windsurf-cicd-github-actions
---
# Windsurf Cicd Github Actions

This skill provides automated assistance for windsurf cicd github actions tasks.

## Overview

This skill enables AI-assisted CI/CD workflow creation within Windsurf. Cascade can generate GitHub Actions workflows from project requirements, optimize existing pipelines, debug workflow failures, and implement security best practices. It understands common CI/CD patterns and can create workflows for testing, building, and deploying applications.

## Prerequisites

- Windsurf IDE with Cascade enabled
- GitHub repository with write access
- Understanding of CI/CD concepts
- GitHub Actions enabled on repository
- Deployment targets configured (if applicable)

## Instructions

1. **Analyze Requirements**
2. **Generate Workflows**
3. **Configure Secrets**
4. **Test Workflows**
5. **Deploy and Monitor**


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- GitHub Actions workflow files
- Reusable action definitions
- Secrets documentation
- CODEOWNERS configuration

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Windsurf CI/CD Guide](https://docs.windsurf.ai/features/cicd)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)