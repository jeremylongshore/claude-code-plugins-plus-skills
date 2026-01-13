---
name: coderabbit-migration-deep-dive
description: |
  Execute coderabbit major re-architecture and migration strategies with strangler fig pattern. use when migrating to or from coderabbit, performing major version upgrades, or re-platforming existing integrations to coderabbit. trigger with phrases ...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Coderabbit Migration Deep Dive

This skill provides automated assistance for coderabbit migration deep dive tasks.

## Prerequisites
- Current system documentation
- CodeRabbit SDK installed
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
Gradually route traffic to new CodeRabbit integration.

## Output
- Migration assessment complete
- Adapter layer implemented
- Data migrated successfully
- Traffic fully shifted to CodeRabbit

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Strangler Fig Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [CodeRabbit Migration Guide](https://docs.coderabbit.com/migration)