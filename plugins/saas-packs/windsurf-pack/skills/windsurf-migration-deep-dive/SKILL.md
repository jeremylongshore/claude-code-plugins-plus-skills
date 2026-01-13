---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Execute windsurf major re-architecture and migration strategies with
  strangler fig pattern. use when migrating to or from windsurf, performing major
  version upgrades, or re-platforming existing integrations to windsurf. trigger with
  phrases like "...
name: windsurf-migration-deep-dive
---
# Windsurf Migration Deep Dive

This skill provides automated assistance for windsurf migration deep dive tasks.

## Prerequisites
- Current system documentation
- Windsurf SDK installed
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
Gradually route traffic to new Windsurf integration.

## Output
- Migration assessment complete
- Adapter layer implemented
- Data migrated successfully
- Traffic fully shifted to Windsurf

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Strangler Fig Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [Windsurf Migration Guide](https://docs.windsurf.com/migration)