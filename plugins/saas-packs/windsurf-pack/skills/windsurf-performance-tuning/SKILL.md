---
allowed-tools: Read, Write, Edit
license: MIT
description: Optimize Windsurf API performance with caching, batching, and connection
  pooling. Use when experiencing slow API responses, implementing caching strategies,
  or optimizing request throughput for Windsurf integrations. Trigger with phrases
  like "win...
name: windsurf-performance-tuning
---
# Windsurf Performance Tuning

This skill provides automated assistance for windsurf performance tuning tasks.

## Prerequisites
- Windsurf SDK installed
- Understanding of async patterns
- Redis or in-memory cache available (optional)
- Performance monitoring in place

## Instructions

### Step 1: Establish Baseline
Measure current latency for critical Windsurf operations.

### Step 2: Implement Caching
Add response caching for frequently accessed data.

### Step 3: Enable Batching
Use DataLoader or similar for automatic request batching.

### Step 4: Optimize Connections
Configure connection pooling with keep-alive.

## Output
- Reduced API latency
- Caching layer implemented
- Request batching enabled
- Connection pooling configured

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Windsurf Performance Guide](https://docs.windsurf.com/performance)
- [DataLoader Documentation](https://github.com/graphql/dataloader)
- [LRU Cache Documentation](https://github.com/isaacs/node-lru-cache)