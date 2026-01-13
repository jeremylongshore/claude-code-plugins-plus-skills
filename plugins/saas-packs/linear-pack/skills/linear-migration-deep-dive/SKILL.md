---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Migrate from jira, asana, github issues, or other tools to linear. use
  when planning a migration to linear, executing data transfer, or mapping workflows
  between tools. trigger with phrases like "migrate to linear", "jira to linear",
  "asana to lin...
name: linear-migration-deep-dive
---
# Linear Migration Deep Dive

This skill provides automated assistance for linear migration deep dive tasks.

## Prerequisites
- Admin access to source system
- Linear workspace with admin access
- API access to both systems
- Migration timeline and rollback plan


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Linear Import Documentation](https://linear.app/docs/import-issues)
- [Jira API Reference](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Asana API Reference](https://developers.asana.com/reference)