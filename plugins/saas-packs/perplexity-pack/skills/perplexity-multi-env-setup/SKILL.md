---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Configure Perplexity across development, staging, and production environments.
  Use when setting up multi-environment deployments, configuring per-environment secrets,
  or implementing environment-specific Perplexity configurations. Trigger with phr...
name: perplexity-multi-env-setup
---
# Perplexity Multi Env Setup

This skill provides automated assistance for perplexity multi env setup tasks.

## Prerequisites
- Separate Perplexity accounts or API keys per environment
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
- [Perplexity Environments Guide](https://docs.perplexity.com/environments)
- [12-Factor App Config](https://12factor.net/config)