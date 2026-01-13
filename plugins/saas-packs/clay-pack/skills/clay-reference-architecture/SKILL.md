---
allowed-tools: Read, Grep
license: MIT
description: Implement clay reference architecture with best-practice project layout.
  use when designing new clay integrations, reviewing project structure, or establishing
  architecture standards for clay applications. trigger with phrases like "clay architect...
name: clay-reference-architecture
---
# Clay Reference Architecture

This skill provides automated assistance for clay reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Clay SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Clay operations.

### Step 4: Configure Health Checks
Add health check endpoint for Clay connectivity.

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
- [Clay SDK Documentation](https://docs.clay.com/sdk)
- [Clay Best Practices](https://docs.clay.com/best-practices)