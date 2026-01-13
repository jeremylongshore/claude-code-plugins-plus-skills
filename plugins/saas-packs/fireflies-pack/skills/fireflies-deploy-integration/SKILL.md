---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Deploy Fireflies.ai integrations to Vercel, Fly.io, and Cloud Run platforms.
  Use when deploying Fireflies.ai-powered applications to production, configuring
  platform-specific secrets, or setting up deployment pipelines. Trigger with phrases
  like "...
name: fireflies-deploy-integration
---
# Fireflies Deploy Integration

This skill provides automated assistance for fireflies deploy integration tasks.

## Prerequisites
- Fireflies.ai API keys for production environment
- Platform CLI installed (vercel, fly, or gcloud)
- Application code ready for deployment
- Environment variables documented

## Instructions

### Step 1: Choose Deployment Platform
Select the platform that best fits your infrastructure needs and follow the platform-specific guide below.

### Step 2: Configure Secrets
Store Fireflies.ai API keys securely using the platform's secrets management.

### Step 3: Deploy Application
Use the platform CLI to deploy your application with Fireflies.ai integration.

### Step 4: Verify Health
Test the health check endpoint to confirm Fireflies.ai connectivity.

## Output
- Application deployed to production
- Fireflies.ai secrets securely configured
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
- [Fireflies.ai Deploy Guide](https://docs.fireflies.com/deploy)