---
allowed-tools: Read, Grep
license: MIT
description: Implement vast.ai reference architecture with best-practice project layout.
  use when designing new vast.ai integrations, reviewing project structure, or establishing
  architecture standards for vast.ai applications. trigger with phrases like "vasta...
name: vastai-reference-architecture
---
# Vastai Reference Architecture

This skill provides automated assistance for vastai reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Vast.ai SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Vast.ai operations.

### Step 4: Configure Health Checks
Add health check endpoint for Vast.ai connectivity.

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
- [Vast.ai SDK Documentation](https://docs.vastai.com/sdk)
- [Vast.ai Best Practices](https://docs.vastai.com/best-practices)