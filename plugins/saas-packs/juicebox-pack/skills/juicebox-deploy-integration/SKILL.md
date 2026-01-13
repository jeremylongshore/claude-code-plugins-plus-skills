---
name: juicebox-deploy-integration
description: |
  Deploy Juicebox integrations to production. Use when deploying to cloud platforms, configuring production environments, or setting up infrastructure for Juicebox. Trigger with phrases like "deploy juicebox", "juicebox production deploy", "juicebox...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Juicebox Deploy Integration

This skill provides automated assistance for juicebox deploy integration tasks.

## Prerequisites
- CI pipeline configured
- Cloud provider account (AWS, GCP, or Azure)
- Production API key secured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Secret management configuration
- Docker/Kubernetes manifests
- Health check endpoints
- Deployment scripts

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [AWS Deployment Guide](https://juicebox.ai/docs/deploy/aws)
- [GCP Deployment Guide](https://juicebox.ai/docs/deploy/gcp)