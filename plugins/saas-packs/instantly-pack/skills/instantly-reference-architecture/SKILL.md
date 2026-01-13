---
name: instantly-reference-architecture
description: |
  Implement instantly reference architecture with best-practice project layout. use when designing new instantly integrations, reviewing project structure, or establishing architecture standards for instantly applications. trigger with phrases like ...
allowed-tools: Read, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Instantly Reference Architecture

This skill provides automated assistance for instantly reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Instantly SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Instantly operations.

### Step 4: Configure Health Checks
Add health check endpoint for Instantly connectivity.

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
- [Instantly SDK Documentation](https://docs.instantly.com/sdk)
- [Instantly Best Practices](https://docs.instantly.com/best-practices)