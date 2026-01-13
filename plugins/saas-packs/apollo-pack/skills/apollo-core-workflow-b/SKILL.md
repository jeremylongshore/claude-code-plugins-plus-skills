---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Implement apollo.io email sequences and outreach workflow. use when building
  automated email campaigns, creating sequences, or managing outreach through apollo.
  trigger with phrases like "apollo email sequence", "apollo outreach", "apollo campaign...
name: apollo-core-workflow-b
---
# Apollo Core Workflow B

This skill provides automated assistance for apollo core workflow b tasks.

## Prerequisites
- Completed `apollo-core-workflow-a` (lead search)
- Apollo account with Sequences feature enabled
- Connected email account in Apollo

## Output
- List of available sequences with stats
- New sequence creation with steps
- Contacts added to sequences
- Campaign analytics and metrics

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Apollo Sequences API](https://apolloio.github.io/apollo-api-docs/#emailer-campaigns)
- [Apollo Email Templates](https://knowledge.apollo.io/hc/en-us/articles/4415154183053)
- [Sequence Best Practices](https://knowledge.apollo.io/hc/en-us/articles/4405955284621)