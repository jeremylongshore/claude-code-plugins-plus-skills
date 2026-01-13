---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Integrate granola meeting notes into your local development workflow.
  use when setting up development workflows, accessing notes programmatically, or
  syncing meeting outcomes with project tools. trigger with phrases like "granola
  dev workflow", "g...
name: granola-local-dev-loop
---
# Granola Local Dev Loop

This skill provides automated assistance for granola local dev loop tasks.

## Prerequisites
- Granola installed and configured
- Zapier account (for automation)
- Project management tool (Jira, Linear, GitHub Issues)
- Local development environment

## Instructions

1. Open Granola Settings
2. Go to Integrations > Zapier
3. Connect your Zapier account
4. Create a Zap: "New Granola Note" trigger


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Local meeting notes directory structure
- Sync script for project integration
- Action item extraction workflow
- Git-integrated note tracking

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Granola Zapier Integration](https://granola.ai/integrations/zapier)
- [Granola Export Formats](https://granola.ai/help/export)