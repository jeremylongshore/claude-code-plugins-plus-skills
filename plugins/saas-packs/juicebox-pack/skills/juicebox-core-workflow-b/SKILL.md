---
name: juicebox-core-workflow-b
description: |
  Implement juicebox candidate enrichment workflow. use when enriching profile data, gathering additional candidate details, or building comprehensive candidate profiles. trigger with phrases like "juicebox enrich profile", "juicebox candidate detai...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Juicebox Core Workflow B

This skill provides automated assistance for juicebox core workflow b tasks.

## Prerequisites
- Juicebox SDK configured
- Search workflow implemented (`juicebox-core-workflow-a`)
- Data storage for enriched profiles


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Enriched profile schema
- Batch enrichment service
- Data persistence layer
- Freshness tracking

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Profile API Reference](https://juicebox.ai/docs/api/profiles)
- [Enrichment Guide](https://juicebox.ai/docs/enrichment)