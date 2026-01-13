---
name: klingai-ci-integration
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Execute integrate kling ai video generation into ci/cd pipelines. use
  when automating video content generation in build pipelines. trigger with phrases
  like 'klingai ci', 'kling ai github actions', 'klingai automation', 'automated video
  generation'.
---
# Klingai Ci Integration

## Overview

This skill shows how to integrate Kling AI video generation into CI/CD pipelines using GitHub Actions, GitLab CI, and other automation platforms.

## Prerequisites

- Kling AI API key stored as CI secret
- CI/CD platform (GitHub Actions, GitLab CI, etc.)
- Python 3.8+ available in CI environment

## Instructions

Follow these steps for CI/CD integration:

1. **Store Secrets**: Add API key to CI secrets
2. **Create Workflow**: Define pipeline configuration
3. **Build Script**: Create video generation script
4. **Handle Output**: Store or deploy generated videos
5. **Add Notifications**: Alert on success/failure

## Output

Successful execution produces:
- Automated video generation in CI pipeline
- Generated videos stored in cloud storage
- Notifications on completion/failure
- Artifacts for downstream processing

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [GitHub Actions](https://docs.github.com/en/actions)
- [GitLab CI](https://docs.gitlab.com/ee/ci/)
- [Kling AI API](https://docs.klingai.com/api)
