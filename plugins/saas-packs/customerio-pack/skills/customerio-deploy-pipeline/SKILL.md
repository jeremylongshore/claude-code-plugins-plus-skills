---
name: customerio-deploy-pipeline
description: |
  Deploy Customer.io integrations to production. Use when deploying to cloud platforms, setting up production infrastructure, or automating deployments. Trigger with phrases like "deploy customer.io", "customer.io production", "customer.io cloud run...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Customerio Deploy Pipeline

This skill provides automated assistance for customerio deploy pipeline tasks.

## Prerequisites
- CI/CD pipeline configured
- Cloud platform access (GCP, AWS, Vercel, etc.)
- Production credentials ready


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Cloud Run deployment workflow
- Vercel serverless deployment
- AWS Lambda configuration
- Kubernetes deployment manifests
- Health check endpoint
- Blue-green deployment script

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Vercel Serverless Functions](https://vercel.com/docs/functions)
- [AWS Lambda Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)