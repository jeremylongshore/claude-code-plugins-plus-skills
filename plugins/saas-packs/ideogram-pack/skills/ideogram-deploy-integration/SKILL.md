---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Deploy Ideogram integrations to Vercel, Fly.io, and Cloud Run platforms.
  Use when deploying Ideogram-powered applications to production, configuring platform-specific
  secrets, or setting up deployment pipelines. Trigger with phrases like "deploy i...
name: ideogram-deploy-integration
---
# Ideogram Deploy Integration

This skill provides automated assistance for ideogram deploy integration tasks.

## Prerequisites
- Ideogram API keys for production environment
- Platform CLI installed (vercel, fly, or gcloud)
- Application code ready for deployment
- Environment variables documented

## Instructions

### Step 1: Choose Deployment Platform
Select the platform that best fits your infrastructure needs and follow the platform-specific guide below.

### Step 2: Configure Secrets
Store Ideogram API keys securely using the platform's secrets management.

### Step 3: Deploy Application
Use the platform CLI to deploy your application with Ideogram integration.

### Step 4: Verify Health
Test the health check endpoint to confirm Ideogram connectivity.

## Output
- Application deployed to production
- Ideogram secrets securely configured
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
- [Ideogram Deploy Guide](https://docs.ideogram.com/deploy)