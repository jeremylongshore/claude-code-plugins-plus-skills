---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Configure Gamma across development, staging, and production environments.
  Use when setting up multi-environment deployments, configuring per-environment secrets,
  or implementing environment-specific Gamma configurations. Trigger with phrases
  like ...
name: gamma-multi-env-setup
---
# Gamma Multi Env Setup

This skill provides automated assistance for gamma multi env setup tasks.

## Prerequisites
- Separate Gamma API keys per environment
- Secret management solution (Vault, AWS Secrets Manager, etc.)
- CI/CD pipeline with environment variables
- Environment detection in application


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Resources
- [Gamma Environments Guide](https://gamma.app/docs/environments)
- [12-Factor App Config](https://12factor.net/config)