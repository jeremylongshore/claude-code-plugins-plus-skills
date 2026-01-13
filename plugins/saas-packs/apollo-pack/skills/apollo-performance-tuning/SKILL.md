---
name: apollo-performance-tuning
description: |
  Optimize Apollo.io API performance. Use when improving API response times, reducing latency, or optimizing bulk operations. Trigger with phrases like "apollo performance", "optimize apollo", "apollo slow", "apollo latency", "speed up apollo".
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Apollo Performance Tuning

This skill provides automated assistance for apollo performance tuning tasks.

## Output
- Connection pooling configuration
- LRU cache with TTL per endpoint
- Parallel request patterns
- Query optimization techniques
- Performance monitoring setup

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Node.js HTTP Agent](https://nodejs.org/api/http.html#class-httpagent)
- [LRU Cache](https://github.com/isaacs/node-lru-cache)
- [Prometheus Metrics](https://prometheus.io/docs/concepts/metric_types/)