---
allowed-tools: Read, Grep
license: MIT
description: Optimize PostHog costs through tier selection, sampling, and usage monitoring.
  Use when analyzing PostHog billing, reducing API costs, or implementing usage monitoring
  and budget alerts. Trigger with phrases like "posthog cost", "posthog billing",...
name: posthog-cost-tuning
---
# Posthog Cost Tuning

This skill provides automated assistance for posthog cost tuning tasks.

## Prerequisites
- Access to PostHog billing dashboard
- Understanding of current usage patterns
- Database for usage tracking (optional)
- Alerting system configured (optional)

## Instructions

### Step 1: Analyze Current Usage
Review PostHog dashboard for usage patterns and costs.

### Step 2: Select Optimal Tier
Use the cost estimation function to find the right tier.

### Step 3: Implement Monitoring
Add usage tracking to catch budget overruns early.

### Step 4: Apply Optimizations
Enable batching, caching, and sampling where appropriate.

## Output
- Optimized tier selection
- Usage monitoring implemented
- Budget alerts configured
- Cost reduction strategies applied

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [PostHog Pricing](https://posthog.com/pricing)
- [PostHog Billing Dashboard](https://dashboard.posthog.com/billing)