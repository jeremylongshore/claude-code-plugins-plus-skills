---
name: vercel-known-pitfalls
description: |
  Execute identify and avoid vercel anti-patterns and common integration mistakes. use when reviewing vercel code for issues, onboarding new developers, or auditing existing vercel integrations for best practices violations. trigger with phrases lik...
allowed-tools: Read, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Vercel Known Pitfalls

This skill provides automated assistance for vercel known pitfalls tasks.

## Prerequisites
- Access to Vercel codebase for review
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
- [Vercel Security Guide](https://vercel.com/docs/security)
- [Vercel Best Practices](https://vercel.com/docs/best-practices)