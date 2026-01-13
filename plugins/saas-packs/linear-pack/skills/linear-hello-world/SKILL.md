---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Create your first Linear issue and query using the GraphQL API. Use when
  making initial API calls, testing Linear connection, or learning basic Linear operations.
  Trigger with phrases like "linear hello world", "first linear issue", "create linear...
name: linear-hello-world
---
# Linear Hello World

This skill provides automated assistance for linear hello world tasks.

## Prerequisites
- Linear SDK installed (`@linear/sdk`)
- Valid API key configured
- Access to at least one Linear team


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- List of teams you have access to
- Created issue with identifier and URL
- Query results showing recent issues

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Linear SDK Getting Started](https://developers.linear.app/docs/sdk/getting-started)
- [GraphQL API Reference](https://developers.linear.app/docs/graphql/working-with-the-graphql-api)
- [Issue Object Reference](https://developers.linear.app/docs/graphql/schema#issue)