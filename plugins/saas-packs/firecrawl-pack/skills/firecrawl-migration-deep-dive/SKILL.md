---
name: firecrawl-migration-deep-dive
description: |
  Execute firecrawl major re-architecture and migration strategies with strangler fig pattern. use when migrating to or from firecrawl, performing major version upgrades, or re-platforming existing integrations to firecrawl. trigger with phrases lik...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Firecrawl Migration Deep Dive

This skill provides automated assistance for firecrawl migration deep dive tasks.

## Prerequisites
- Current system documentation
- FireCrawl SDK installed
- Feature flag infrastructure
- Rollback strategy tested

## Instructions

### Step 1: Assess Current State
Document existing implementation and data inventory.

### Step 2: Build Adapter Layer
Create abstraction layer for gradual migration.

### Step 3: Migrate Data
Run batch data migration with error handling.

### Step 4: Shift Traffic
Gradually route traffic to new FireCrawl integration.

## Output
- Migration assessment complete
- Adapter layer implemented
- Data migrated successfully
- Traffic fully shifted to FireCrawl

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Strangler Fig Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [FireCrawl Migration Guide](https://docs.firecrawl.com/migration)