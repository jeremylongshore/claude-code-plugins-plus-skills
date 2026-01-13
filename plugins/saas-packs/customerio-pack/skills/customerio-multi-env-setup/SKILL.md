---
name: customerio-multi-env-setup
description: |
  Configure Customer.io multi-environment setup. Use when setting up development, staging, and production environments with proper isolation. Trigger with phrases like "customer.io environments", "customer.io staging", "customer.io dev prod", "custo...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Customerio Multi Env Setup

This skill provides automated assistance for customerio multi env setup tasks.

## Prerequisites
- Customer.io account with multiple workspaces
- Environment variable management system
- CI/CD pipeline configured

## Instructions

1. Go to Customer.io Dashboard > Settings > Workspaces
2. Create workspaces: `[app-name]-dev`, `[app-name]-staging`, `[app-name]-prod`
3. Generate API keys for each workspace
4. Store credentials securely


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Customer.io Workspaces](https://customer.io/docs/workspaces/)
- [API Environments](https://customer.io/docs/api/track/)