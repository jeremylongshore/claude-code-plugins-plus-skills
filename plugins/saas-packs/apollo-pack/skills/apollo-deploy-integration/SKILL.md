---
name: apollo-deploy-integration
description: |
  Deploy Apollo.io integrations to production. Use when deploying Apollo integrations, configuring production environments, or setting up deployment pipelines. Trigger with phrases like "deploy apollo", "apollo production deploy", "apollo deployment...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Apollo Deploy Integration

This skill provides automated assistance for apollo deploy integration tasks.

## Output
- Platform-specific deployment configs (Vercel, GCP, AWS, K8s)
- Health check endpoints
- Blue-green deployment workflow
- Pre-deployment validation
- Environment configuration

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Vercel Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)
- [Google Cloud Secret Manager](https://cloud.google.com/secret-manager)
- [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/)
- [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)