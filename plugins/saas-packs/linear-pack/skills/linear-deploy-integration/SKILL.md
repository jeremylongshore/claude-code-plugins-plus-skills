---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Deploy Linear-integrated applications and track deployments. Use when
  deploying to production, setting up deployment tracking, or integrating Linear with
  deployment platforms. Trigger with phrases like "deploy linear integration", "linear
  deployme...
name: linear-deploy-integration
---
# Linear Deploy Integration

This skill provides automated assistance for linear deploy integration tasks.

## Prerequisites
- Working Linear integration
- Deployment platform account (Vercel, Railway, Cloud Run, etc.)
- CI/CD pipeline configured


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Vercel Environment Variables](https://vercel.com/docs/environment-variables)
- [Cloud Run Secrets](https://cloud.google.com/run/docs/configuring/secrets)
- [Linear Deployment Tracking](https://linear.app/docs/git-integrations)