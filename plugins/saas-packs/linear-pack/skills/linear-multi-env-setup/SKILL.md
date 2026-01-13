---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Configure Linear across development, staging, and production environments.
  Use when setting up multi-environment deployments, managing per-environment API
  keys, or implementing environment-specific Linear configurations. Trigger with phrases
  like ...
name: linear-multi-env-setup
---
# Linear Multi Env Setup

This skill provides automated assistance for linear multi env setup tasks.

## Prerequisites
- Separate Linear workspaces or API keys per environment
- Secret management solution (Vault, AWS Secrets Manager, GCP Secret Manager)
- CI/CD pipeline with environment variables
- Environment detection in application


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Linear API Authentication](https://developers.linear.app/docs/graphql/authentication)
- [12-Factor App Config](https://12factor.net/config)
- [HashiCorp Vault](https://www.vaultproject.io/docs)