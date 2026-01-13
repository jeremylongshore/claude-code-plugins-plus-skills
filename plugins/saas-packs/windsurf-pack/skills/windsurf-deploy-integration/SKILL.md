---
name: windsurf-deploy-integration
description: |
  Deploy Windsurf integrations to Vercel, Fly.io, and Cloud Run platforms. Use when deploying Windsurf-powered applications to production, configuring platform-specific secrets, or setting up deployment pipelines. Trigger with phrases like "deploy w...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Windsurf Deploy Integration

This skill provides automated assistance for windsurf deploy integration tasks.

## Prerequisites
- Windsurf API keys for production environment
- Platform CLI installed (vercel, fly, or gcloud)
- Application code ready for deployment
- Environment variables documented

## Instructions

### Step 1: Choose Deployment Platform
Select the platform that best fits your infrastructure needs and follow the platform-specific guide below.

### Step 2: Configure Secrets
Store Windsurf API keys securely using the platform's secrets management.

### Step 3: Deploy Application
Use the platform CLI to deploy your application with Windsurf integration.

### Step 4: Verify Health
Test the health check endpoint to confirm Windsurf connectivity.

## Output
- Application deployed to production
- Windsurf secrets securely configured
- Health check endpoint functional
- Environment-specific configuration in place

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Vercel Documentation](https://vercel.com/docs)
- [Fly.io Documentation](https://fly.io/docs)
- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Windsurf Deploy Guide](https://docs.windsurf.com/deploy)