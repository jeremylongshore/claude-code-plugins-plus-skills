---
name: clerk-core-workflow-a
description: |
  Implement user sign-up and sign-in flows with clerk. use when building authentication ui, customizing sign-in experience, or implementing oauth social login. trigger with phrases like "clerk sign-in", "clerk sign-up", "clerk login flow", "clerk oa...
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Clerk Core Workflow A

This skill provides automated assistance for clerk core workflow a tasks.

## Prerequisites
- Clerk SDK installed and configured
- OAuth providers configured in Clerk dashboard (if using social login)
- Sign-in/sign-up URLs configured in environment


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Working sign-in/sign-up pages
- OAuth social login configured
- Email verification flow
- Custom authentication UI

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Sign-In Component](https://clerk.com/docs/components/authentication/sign-in)
- [Custom Flows](https://clerk.com/docs/custom-flows/overview)
- [OAuth Configuration](https://clerk.com/docs/authentication/social-connections/overview)