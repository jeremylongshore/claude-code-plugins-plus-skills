---
name: exa-multi-env-setup
description: |
  Configure Exa across development, staging, and production environments. Use when setting up multi-environment deployments, configuring per-environment secrets, or implementing environment-specific Exa configurations. Trigger with phrases like "exa...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Exa Multi Env Setup

This skill provides automated assistance for exa multi env setup tasks.

## Prerequisites
- Separate Exa accounts or API keys per environment
- Secret management solution (Vault, AWS Secrets Manager, etc.)
- CI/CD pipeline with environment variables
- Environment detection in application

## Instructions

### Step 1: Create Config Structure
Set up the base and per-environment configuration files.

### Step 2: Implement Environment Detection
Add logic to detect and load environment-specific config.

### Step 3: Configure Secrets
Store API keys securely using your secret management solution.

### Step 4: Add Environment Guards
Implement safeguards for production-only operations.

## Output
- Multi-environment config structure
- Environment detection logic
- Secure secret management
- Production safeguards enabled

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Exa Environments Guide](https://docs.exa.com/environments)
- [12-Factor App Config](https://12factor.net/config)