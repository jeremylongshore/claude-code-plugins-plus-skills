---
name: deepgram-ci-integration
description: |
  Configure Deepgram CI/CD integration for automated testing and deployment. Use when setting up continuous integration pipelines, automated testing, or deployment workflows for Deepgram integrations. Trigger with phrases like "deepgram CI", "deepgr...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Deepgram Ci Integration

This skill provides automated assistance for deepgram ci integration tasks.

## Prerequisites
- CI/CD platform access (GitHub Actions, GitLab CI, etc.)
- Deepgram API key for testing
- Secret management configured
- Test fixtures prepared

## Instructions

### Step 1: Configure Secrets
Store API keys securely in CI/CD environment.

### Step 2: Create Test Workflow
Set up automated testing on push/PR.

### Step 3: Add Integration Tests
Implement Deepgram-specific integration tests.

### Step 4: Configure Deployment
Set up automated deployment pipeline.

## Output
- CI workflow configuration
- Automated test suite
- Deployment pipeline
- Secret management

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitLab CI Documentation](https://docs.gitlab.com/ee/ci/)
- [Deepgram SDK Testing](https://developers.deepgram.com/docs/testing)