---
name: vercel-reference-architecture
description: |
  Implement vercel reference architecture with best-practice project layout. use when designing new vercel integrations, reviewing project structure, or establishing architecture standards for vercel applications. trigger with phrases like "vercel a...
allowed-tools: Read, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Vercel Reference Architecture

This skill provides automated assistance for vercel reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Vercel SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Vercel operations.

### Step 4: Configure Health Checks
Add health check endpoint for Vercel connectivity.

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
- [Vercel SDK Documentation](https://vercel.com/docs/sdk)
- [Vercel Best Practices](https://vercel.com/docs/best-practices)