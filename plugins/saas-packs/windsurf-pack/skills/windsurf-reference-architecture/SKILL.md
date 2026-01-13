---
allowed-tools: Read, Grep
license: MIT
description: Implement windsurf reference architecture with best-practice project
  layout. use when designing new windsurf integrations, reviewing project structure,
  or establishing architecture standards for windsurf applications. trigger with phrases
  like "wi...
name: windsurf-reference-architecture
---
# Windsurf Reference Architecture

This skill provides automated assistance for windsurf reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Windsurf SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Windsurf operations.

### Step 4: Configure Health Checks
Add health check endpoint for Windsurf connectivity.

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
- [Windsurf SDK Documentation](https://docs.windsurf.com/sdk)
- [Windsurf Best Practices](https://docs.windsurf.com/best-practices)