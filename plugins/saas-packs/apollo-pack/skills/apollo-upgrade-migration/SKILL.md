---
name: apollo-upgrade-migration
description: |
  Plan and execute apollo.io sdk upgrades. use when upgrading apollo api versions, migrating to new endpoints, or updating deprecated api usage. trigger with phrases like "apollo upgrade", "apollo migration", "update apollo api", "apollo breaking ch...
allowed-tools: Read, Grep, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Apollo Upgrade Migration

This skill provides automated assistance for apollo upgrade migration tasks.

## Output
- Pre-upgrade audit results
- Compatibility layer for gradual migration
- Feature flag controlled rollout
- Parallel testing verification
- Cleanup procedures

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Apollo API Changelog](https://apolloio.github.io/apollo-api-docs/#changelog)
- [Apollo Migration Guides](https://knowledge.apollo.io/)
- [Feature Flag Best Practices](https://martinfowler.com/articles/feature-toggles.html)