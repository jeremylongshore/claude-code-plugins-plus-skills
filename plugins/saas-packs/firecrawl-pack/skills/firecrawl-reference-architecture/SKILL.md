---
allowed-tools: Read, Grep
license: MIT
description: Implement firecrawl reference architecture with best-practice project
  layout. use when designing new firecrawl integrations, reviewing project structure,
  or establishing architecture standards for firecrawl applications. trigger with
  phrases like ...
name: firecrawl-reference-architecture
---
# Firecrawl Reference Architecture

This skill provides automated assistance for firecrawl reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- FireCrawl SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for FireCrawl operations.

### Step 4: Configure Health Checks
Add health check endpoint for FireCrawl connectivity.

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
- [FireCrawl SDK Documentation](https://docs.firecrawl.com/sdk)
- [FireCrawl Best Practices](https://docs.firecrawl.com/best-practices)