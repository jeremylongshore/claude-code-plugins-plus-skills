---
name: supabase-advanced-troubleshooting
license: MIT
allowed-tools: Read, Grep, Bash
description: Execute apply supabase advanced debugging techniques for hard-to-diagnose
  issues. use when standard troubleshooting fails, investigating complex race conditions,
  or preparing evidence bundles for supabase support escalation. trigger with phrases
  l...
---
# Supabase Advanced Troubleshooting

## Prerequisites
- Access to production logs and metrics
- kubectl access to clusters
- Network capture tools available
- Understanding of distributed tracing

## Instructions

### Step 1: Collect Evidence Bundle
Run the comprehensive debug script to gather all relevant data.

### Step 2: Systematic Isolation
Test each layer independently to identify the failure point.

### Step 3: Create Minimal Reproduction
Strip down to the simplest failing case.

### Step 4: Escalate with Evidence
Use the support template with all collected evidence.

## Output
- Comprehensive debug bundle collected
- Failure layer identified
- Minimal reproduction created
- Support escalation submitted

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Supabase Support Portal](https://support.supabase.com)
- [Supabase Status Page](https://status.supabase.com)
