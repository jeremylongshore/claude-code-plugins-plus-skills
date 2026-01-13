---
allowed-tools: Read, Write, Edit
license: MIT
description: Optimize FireCrawl API performance with caching, batching, and connection
  pooling. Use when experiencing slow API responses, implementing caching strategies,
  or optimizing request throughput for FireCrawl integrations. Trigger with phrases
  like "f...
name: firecrawl-performance-tuning
---
# Firecrawl Performance Tuning

This skill provides automated assistance for firecrawl performance tuning tasks.

## Prerequisites
- FireCrawl SDK installed
- Understanding of async patterns
- Redis or in-memory cache available (optional)
- Performance monitoring in place

## Instructions

### Step 1: Establish Baseline
Measure current latency for critical FireCrawl operations.

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
- [FireCrawl Performance Guide](https://docs.firecrawl.com/performance)
- [DataLoader Documentation](https://github.com/graphql/dataloader)
- [LRU Cache Documentation](https://github.com/isaacs/node-lru-cache)