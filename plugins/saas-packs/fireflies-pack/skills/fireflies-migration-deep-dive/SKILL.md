---
name: fireflies-migration-deep-dive
description: |
  Execute fireflies.ai major re-architecture and migration strategies with strangler fig pattern. use when migrating to or from fireflies.ai, performing major version upgrades, or re-platforming existing integrations to fireflies.ai. trigger with ph...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Fireflies Migration Deep Dive

This skill provides automated assistance for fireflies migration deep dive tasks.

## Prerequisites
- Current system documentation
- Fireflies.ai SDK installed
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
Gradually route traffic to new Fireflies.ai integration.

## Output
- Migration assessment complete
- Adapter layer implemented
- Data migrated successfully
- Traffic fully shifted to Fireflies.ai

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Strangler Fig Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [Fireflies.ai Migration Guide](https://docs.fireflies.com/migration)