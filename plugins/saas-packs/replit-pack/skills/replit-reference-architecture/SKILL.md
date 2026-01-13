---
allowed-tools: Read, Grep
license: MIT
description: Implement replit reference architecture with best-practice project layout.
  use when designing new replit integrations, reviewing project structure, or establishing
  architecture standards for replit applications. trigger with phrases like "replit
  a...
name: replit-reference-architecture
---
# Replit Reference Architecture

This skill provides automated assistance for replit reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Replit SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Replit operations.

### Step 4: Configure Health Checks
Add health check endpoint for Replit connectivity.

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
- [Replit SDK Documentation](https://docs.replit.com/sdk)
- [Replit Best Practices](https://docs.replit.com/best-practices)