---
name: vastai-migration-deep-dive
description: |
  Execute vast.ai major re-architecture and migration strategies with strangler fig pattern. use when migrating to or from vast.ai, performing major version upgrades, or re-platforming existing integrations to vast.ai. trigger with phrases like "mig...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Vastai Migration Deep Dive

This skill provides automated assistance for vastai migration deep dive tasks.

## Prerequisites
- Current system documentation
- Vast.ai SDK installed
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
Gradually route traffic to new Vast.ai integration.

## Output
- Migration assessment complete
- Adapter layer implemented
- Data migrated successfully
- Traffic fully shifted to Vast.ai

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Strangler Fig Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [Vast.ai Migration Guide](https://docs.vastai.com/migration)