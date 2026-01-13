---
name: clerk-multi-env-setup
description: |
  Configure Clerk for multiple environments (dev, staging, production). Use when setting up environment-specific configurations, managing multiple Clerk instances, or implementing environment promotion. Trigger with phrases like "clerk environments"...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Clerk Multi Env Setup

This skill provides automated assistance for clerk multi env setup tasks.

## Prerequisites
- Clerk account with multiple instances
- Understanding of environment management
- CI/CD pipeline configured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Separate Clerk instances per environment
- Environment-aware configuration
- Webhook handling per environment
- CI/CD pipeline configured

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Clerk Instances](https://clerk.com/docs/deployments/overview)
- [Environment Variables](https://clerk.com/docs/deployments/set-up-preview-environment)
- [Next.js Environments](https://nextjs.org/docs/app/building-your-application/configuring/environment-variables)