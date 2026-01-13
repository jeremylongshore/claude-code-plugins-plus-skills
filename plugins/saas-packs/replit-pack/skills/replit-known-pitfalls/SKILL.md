---
allowed-tools: Read, Grep
license: MIT
description: Identify and avoid replit anti-patterns and common integration mistakes.
  use when reviewing replit code for issues, onboarding new developers, or auditing
  existing replit integrations for best practices violations. trigger with phrases
  like "repli...
name: replit-known-pitfalls
---
# Replit Known Pitfalls

This skill provides automated assistance for replit known pitfalls tasks.

## Prerequisites
- Access to Replit codebase for review
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
- [Replit Security Guide](https://docs.replit.com/security)
- [Replit Best Practices](https://docs.replit.com/best-practices)