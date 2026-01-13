---
allowed-tools: Read, Grep, Bash
license: MIT
description: Apply retell ai advanced debugging techniques for hard-to-diagnose issues.
  use when standard troubleshooting fails, investigating complex race conditions,
  or preparing evidence bundles for retell ai support escalation. trigger with phrases
  like "r...
name: retellai-advanced-troubleshooting
---
# Retellai Advanced Troubleshooting

This skill provides automated assistance for retellai advanced troubleshooting tasks.

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
- [Retell AI Support Portal](https://support.retellai.com)
- [Retell AI Status Page](https://status.retellai.com)