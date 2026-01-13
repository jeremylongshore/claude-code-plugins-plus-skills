---
name: exa-known-pitfalls
description: |
  Identify and avoid exa anti-patterns and common integration mistakes. use when reviewing exa code for issues, onboarding new developers, or auditing existing exa integrations for best practices violations. trigger with phrases like "exa mistakes",...
allowed-tools: Read, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Exa Known Pitfalls

This skill provides automated assistance for exa known pitfalls tasks.

## Prerequisites
- Access to Exa codebase for review
- Understanding of async/await patterns
- Knowledge of security best practices
- Familiarity with rate limiting concepts

## Instructions

### Step 1: Review for Anti-Patterns
Scan codebase for each pitfall pattern.

### Step 2: Prioritize Fixes
Address security issues first, then performance.

### Step 3: Implement Better Approach
Replace anti-patterns with recommended patterns.

### Step 4: Add Prevention
Set up linting and CI checks to prevent recurrence.

## Output
- Anti-patterns identified
- Fixes prioritized and implemented
- Prevention measures in place
- Code quality improved

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Exa Security Guide](https://docs.exa.com/security)
- [Exa Best Practices](https://docs.exa.com/best-practices)