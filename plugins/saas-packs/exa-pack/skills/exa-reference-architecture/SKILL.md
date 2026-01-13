---
name: exa-reference-architecture
description: |
  Implement exa reference architecture with best-practice project layout. use when designing new exa integrations, reviewing project structure, or establishing architecture standards for exa applications. trigger with phrases like "exa architecture"...
allowed-tools: Read, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Exa Reference Architecture

This skill provides automated assistance for exa reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Exa SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Exa operations.

### Step 4: Configure Health Checks
Add health check endpoint for Exa connectivity.

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
- [Exa SDK Documentation](https://docs.exa.com/sdk)
- [Exa Best Practices](https://docs.exa.com/best-practices)