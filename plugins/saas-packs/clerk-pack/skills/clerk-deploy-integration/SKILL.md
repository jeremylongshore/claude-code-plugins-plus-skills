---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Configure Clerk for deployment on various platforms. Use when deploying
  to Vercel, Netlify, Railway, or other platforms, or when setting up production environment.
  Trigger with phrases like "deploy clerk", "clerk Vercel", "clerk Netlify", "clerk
  p...
name: clerk-deploy-integration
---
# Clerk Deploy Integration

This skill provides automated assistance for clerk deploy integration tasks.

## Prerequisites
- Clerk production instance configured
- Production API keys ready
- Hosting platform account

## Instructions

1. Add Vercel domain to allowed origins
2. Set production URLs in Clerk Dashboard
3. Configure webhook endpoint


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Platform-specific deployment configuration
- Environment variables configured
- Webhook endpoints ready
- Production domain configured

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Vercel Deployment](https://clerk.com/docs/deployments/deploy-to-vercel)
- [Netlify Deployment](https://clerk.com/docs/deployments/deploy-to-netlify)
- [Railway Guide](https://railway.app/docs)