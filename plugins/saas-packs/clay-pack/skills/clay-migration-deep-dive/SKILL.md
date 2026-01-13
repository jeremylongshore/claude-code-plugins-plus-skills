---
name: clay-migration-deep-dive
description: |
  Execute clay major re-architecture and migration strategies with strangler fig pattern. use when migrating to or from clay, performing major version upgrades, or re-platforming existing integrations to clay. trigger with phrases like "migrate clay...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Clay Migration Deep Dive

This skill provides automated assistance for clay migration deep dive tasks.

## Prerequisites
- Current system documentation
- Clay SDK installed
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
Gradually route traffic to new Clay integration.

## Output
- Migration assessment complete
- Adapter layer implemented
- Data migrated successfully
- Traffic fully shifted to Clay

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Strangler Fig Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [Clay Migration Guide](https://docs.clay.com/migration)