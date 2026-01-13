---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Execute exa major re-architecture and migration strategies with strangler
  fig pattern. use when migrating to or from exa, performing major version upgrades,
  or re-platforming existing integrations to exa. trigger with phrases like "migrate
  exa", "...
name: exa-migration-deep-dive
---
# Exa Migration Deep Dive

This skill provides automated assistance for exa migration deep dive tasks.

## Prerequisites
- Current system documentation
- Exa SDK installed
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
Gradually route traffic to new Exa integration.

## Output
- Migration assessment complete
- Adapter layer implemented
- Data migrated successfully
- Traffic fully shifted to Exa

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Strangler Fig Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [Exa Migration Guide](https://docs.exa.com/migration)