---
name: juicebox-multi-env-setup
description: |
  Configure Juicebox multi-environment setup. Use when setting up dev/staging/production environments, managing per-environment configurations, or implementing environment isolation. Trigger with phrases like "juicebox environments", "juicebox stagi...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Juicebox Multi Env Setup

This skill provides automated assistance for juicebox multi env setup tasks.

## Prerequisites
- Separate Juicebox accounts or API keys per environment
- Secret management solution (Vault, AWS Secrets Manager, etc.)
- CI/CD pipeline with environment variables
- Environment detection in application


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Environment-specific configurations
- Secret management per environment
- Kubernetes overlays
- Environment guards

## Resources
- [Multi-Environment Guide](https://juicebox.ai/docs/environments)
- [12-Factor App Config](https://12factor.net/config)