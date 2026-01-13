---
allowed-tools: Read, Grep
license: MIT
description: Execute identify and avoid supabase anti-patterns and common integration
  mistakes. use when reviewing supabase code for issues, onboarding new developers,
  or auditing existing supabase integrations for best practices violations. trigger
  with phras...
name: supabase-known-pitfalls
---
# Supabase Known Pitfalls

This skill provides automated assistance for supabase known pitfalls tasks.

## Prerequisites
- Access to Supabase codebase for review
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
- [Supabase Security Guide](https://supabase.com/docs/security)
- [Supabase Best Practices](https://supabase.com/docs/best-practices)