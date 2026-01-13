---
allowed-tools: Read, Grep
license: MIT
description: Implement supabase reference architecture with best-practice project
  layout. use when designing new supabase integrations, reviewing project structure,
  or establishing architecture standards for supabase applications. trigger with phrases
  like "su...
name: supabase-reference-architecture
---
# Supabase Reference Architecture

This skill provides automated assistance for supabase reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Supabase SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Supabase operations.

### Step 4: Configure Health Checks
Add health check endpoint for Supabase connectivity.

## Output
- Structured project layout
- Client wrapper with caching
- Error boundary implemented
- Health checks configured

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Supabase SDK Documentation](https://supabase.com/docs/sdk)
- [Supabase Best Practices](https://supabase.com/docs/best-practices)