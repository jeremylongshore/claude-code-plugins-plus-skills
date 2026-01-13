---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Configure deployment pipelines for Lindy AI integrations. Use when deploying
  to production, setting up staging environments, or automating agent deployments.
  Trigger with phrases like "deploy lindy", "lindy deployment", "lindy production
  deploy", ...
name: lindy-deploy-integration
---
# Lindy Deploy Integration

This skill provides automated assistance for lindy deploy integration tasks.

## Prerequisites
- CI pipeline configured (see `lindy-ci-integration`)
- Production Lindy API key
- Deployment target (Vercel, AWS, GCP, etc.)


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Automated deployment pipeline
- Agent sync mechanism
- Environment-specific deployments
- Rollback capability

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Lindy Deployment Guide](https://docs.lindy.ai/deployment)
- [Vercel Documentation](https://vercel.com/docs)
- [GitHub Environments](https://docs.github.com/en/actions/deployment)