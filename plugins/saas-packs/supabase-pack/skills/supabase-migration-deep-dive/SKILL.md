---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Execute supabase major re-architecture and migration strategies with
  strangler fig pattern. use when migrating to or from supabase, performing major
  version upgrades, or re-platforming existing integrations to supabase. trigger with
  phrases like "...
name: supabase-migration-deep-dive
---
# Supabase Migration Deep Dive

This skill provides automated assistance for supabase migration deep dive tasks.

## Prerequisites
- Current system documentation
- Supabase SDK installed
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
Gradually route traffic to new Supabase integration.

## Output
- Migration assessment complete
- Adapter layer implemented
- Data migrated successfully
- Traffic fully shifted to Supabase

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Strangler Fig Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html)
- [Supabase Migration Guide](https://supabase.com/docs/migration)