---
name: windsurf-known-pitfalls
description: |
  Identify and avoid windsurf anti-patterns and common integration mistakes. use when reviewing windsurf code for issues, onboarding new developers, or auditing existing windsurf integrations for best practices violations. trigger with phrases like ...
allowed-tools: Read, Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Windsurf Known Pitfalls

This skill provides automated assistance for windsurf known pitfalls tasks.

## Prerequisites
- Access to Windsurf codebase for review
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
- [Windsurf Security Guide](https://docs.windsurf.com/security)
- [Windsurf Best Practices](https://docs.windsurf.com/best-practices)