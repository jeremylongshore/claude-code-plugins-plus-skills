---
allowed-tools: Read, Grep
license: MIT
description: Implement perplexity reference architecture with best-practice project
  layout. use when designing new perplexity integrations, reviewing project structure,
  or establishing architecture standards for perplexity applications. trigger with
  phrases li...
name: perplexity-reference-architecture
---
# Perplexity Reference Architecture

This skill provides automated assistance for perplexity reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- Perplexity SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for Perplexity operations.

### Step 4: Configure Health Checks
Add health check endpoint for Perplexity connectivity.

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
- [Perplexity SDK Documentation](https://docs.perplexity.com/sdk)
- [Perplexity Best Practices](https://docs.perplexity.com/best-practices)