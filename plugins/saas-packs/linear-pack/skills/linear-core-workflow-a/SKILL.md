---
allowed-tools: Read, Write, Edit, Grep
license: MIT
description: 'Issue lifecycle management with linear: create, update, and transition
  issues. use when implementing issue crud operations, state transitions, or building
  issue management features. trigger with phrases like "linear issue workflow", "linear
  issue ...'
name: linear-core-workflow-a
---
# Linear Core Workflow A

This skill provides automated assistance for linear core workflow a tasks.

## Prerequisites
- Linear SDK configured
- Access to target team(s)
- Understanding of Linear's issue model


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Issue creation with all metadata
- Bulk update capabilities
- State transition handling
- Parent/child relationships
- Blocking relationships
- Comments and activity

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Issue Object Reference](https://developers.linear.app/docs/graphql/schema#issue)
- [Workflow States](https://developers.linear.app/docs/graphql/schema#workflowstate)
- [Issue Relations](https://developers.linear.app/docs/graphql/schema#issuerelation)