---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Migrate from other authentication providers to clerk. use when migrating
  from auth0, firebase, supabase auth, nextauth, or custom authentication solutions.
  trigger with phrases like "migrate to clerk", "clerk migration", "switch to clerk",
  "auth0 ...
name: clerk-migration-deep-dive
---
# Clerk Migration Deep Dive

This skill provides automated assistance for clerk migration deep dive tasks.

## Prerequisites
- Current auth provider access
- User data export capability
- Clerk account and API keys
- Migration timeline planned

## Output
- User migration scripts
- Parallel running configuration
- Phased migration plan
- Rollback procedures

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Clerk Migration Guide](https://clerk.com/docs/deployments/migrate-overview)
- [User Import API](https://clerk.com/docs/users/creating-users)
- [Auth0 Migration](https://clerk.com/docs/deployments/migrate-from-auth0)