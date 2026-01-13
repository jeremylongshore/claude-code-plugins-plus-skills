---
allowed-tools: Read, Grep
license: MIT
description: Implement fireflies.ai reference architecture with best-practice project
  layout. use when designing new fireflies.ai integrations, reviewing project structure,
  or establishing architecture standards for fireflies.ai applications. trigger with
  phra...
name: fireflies-reference-architecture
---
# Fireflies Reference Architecture

This skill provides automated assistance for fireflies reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Fireflies.ai SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Fireflies.ai operations.

### Step 4: Configure Health Checks
Add health check endpoint for Fireflies.ai connectivity.

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
- [Fireflies.ai SDK Documentation](https://docs.fireflies.com/sdk)
- [Fireflies.ai Best Practices](https://docs.fireflies.com/best-practices)