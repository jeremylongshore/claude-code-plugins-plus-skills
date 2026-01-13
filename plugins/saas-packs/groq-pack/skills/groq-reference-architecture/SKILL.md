---
name: groq-reference-architecture
description: |
  Implement groq reference architecture with best-practice project layout. use when designing new groq integrations, reviewing project structure, or establishing architecture standards for groq applications. trigger with phrases like "groq architect...
allowed-tools: Read, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Groq Reference Architecture

This skill provides automated assistance for groq reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Groq SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Groq operations.

### Step 4: Configure Health Checks
Add health check endpoint for Groq connectivity.

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
- [Groq SDK Documentation](https://docs.groq.com/sdk)
- [Groq Best Practices](https://docs.groq.com/best-practices)