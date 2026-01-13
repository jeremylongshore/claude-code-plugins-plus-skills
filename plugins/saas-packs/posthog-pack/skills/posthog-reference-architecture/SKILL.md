---
name: posthog-reference-architecture
description: |
  Implement posthog reference architecture with best-practice project layout. use when designing new posthog integrations, reviewing project structure, or establishing architecture standards for posthog applications. trigger with phrases like "posth...
allowed-tools: Read, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Posthog Reference Architecture

This skill provides automated assistance for posthog reference architecture tasks.

## Prerequisites
- Understanding of layered architecture
- PostHog SDK knowledge
- TypeScript project setup
- Testing framework configured

## Instructions

### Step 1: Create Directory Structure
Set up the project layout following the reference structure above.

### Step 2: Implement Client Wrapper
Create the singleton client with caching and monitoring.

### Step 3: Add Error Handling
Implement custom error classes for PostHog operations.

### Step 4: Configure Health Checks
Add health check endpoint for PostHog connectivity.

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
- [PostHog SDK Documentation](https://docs.posthog.com/sdk)
- [PostHog Best Practices](https://docs.posthog.com/best-practices)