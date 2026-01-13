---
name: retellai-reference-architecture
description: |
  Implement retell ai reference architecture with best-practice project layout. use when designing new retell ai integrations, reviewing project structure, or establishing architecture standards for retell ai applications. trigger with phrases like ...
allowed-tools: Read, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Retellai Reference Architecture

This skill provides automated assistance for retellai reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Retell AI SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Retell AI operations.

### Step 4: Configure Health Checks
Add health check endpoint for Retell AI connectivity.

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
- [Retell AI SDK Documentation](https://docs.retellai.com/sdk)
- [Retell AI Best Practices](https://docs.retellai.com/best-practices)