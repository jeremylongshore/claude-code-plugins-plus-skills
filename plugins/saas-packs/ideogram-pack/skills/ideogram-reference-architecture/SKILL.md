---
allowed-tools: Read, Grep
license: MIT
description: Implement ideogram reference architecture with best-practice project
  layout. use when designing new ideogram integrations, reviewing project structure,
  or establishing architecture standards for ideogram applications. trigger with phrases
  like "id...
name: ideogram-reference-architecture
---
# Ideogram Reference Architecture

This skill provides automated assistance for ideogram reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Ideogram SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Ideogram operations.

### Step 4: Configure Health Checks
Add health check endpoint for Ideogram connectivity.

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
- [Ideogram SDK Documentation](https://docs.ideogram.com/sdk)
- [Ideogram Best Practices](https://docs.ideogram.com/best-practices)