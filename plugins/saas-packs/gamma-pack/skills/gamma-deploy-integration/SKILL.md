---
name: gamma-deploy-integration
description: |
  Deploy Gamma-integrated applications to production environments. Use when deploying to Vercel, AWS, GCP, or other cloud platforms with proper secret management and configuration. Trigger with phrases like "gamma deploy", "gamma production", "gamma...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Gamma Deploy Integration

This skill provides automated assistance for gamma deploy integration tasks.

## Prerequisites
- Completed CI integration
- Cloud platform account (Vercel, AWS, or GCP)
- Production Gamma API key


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Production deployment on chosen platform
- Secrets securely stored
- Environment variables configured
- Automated deployment pipeline

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Vercel Documentation](https://vercel.com/docs)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Google Cloud Run](https://cloud.google.com/run/docs)