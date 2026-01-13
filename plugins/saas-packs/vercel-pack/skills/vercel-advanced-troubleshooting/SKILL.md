---
name: vercel-advanced-troubleshooting
description: |
  Execute apply vercel advanced debugging techniques for hard-to-diagnose issues. use when standard troubleshooting fails, investigating complex race conditions, or preparing evidence bundles for vercel support escalation. trigger with phrases like ...
allowed-tools: Read, Grep, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Vercel Advanced Troubleshooting

This skill provides automated assistance for vercel advanced troubleshooting tasks.

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
- [Vercel Support Portal](https://support.vercel.com)
- [Vercel Status Page](https://www.vercel-status.com)