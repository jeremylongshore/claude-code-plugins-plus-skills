---
name: lindy-multi-env-setup
description: |
  Configure Lindy AI across development, staging, and production environments. Use when setting up multi-environment deployments, configuring per-environment secrets, or implementing environment-specific Lindy configurations. Trigger with phrases li...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Lindy Multi Env Setup

This skill provides automated assistance for lindy multi env setup tasks.

## Prerequisites
- Separate Lindy API keys per environment
- Secret management solution (Vault, AWS Secrets Manager, etc.)
- CI/CD pipeline with environment variables
- Environment detection in application


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Multi-environment configuration
- Environment detection logic
- Secure secret management
- Environment-specific agents
- Production safeguards

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Lindy Environments Guide](https://docs.lindy.ai/environments)
- [12-Factor App Config](https://12factor.net/config)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)