---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Profile and optimize code with ai-assisted analysis. activate when users
  mention "performance profiling", "optimize performance", "bottleneck analysis",
  "profiling", or "performance tuning". handles performance analysis and optimization.
  use when ...
name: windsurf-performance-profiling
---
# Windsurf Performance Profiling

This skill provides automated assistance for windsurf performance profiling tasks.

## Overview

This skill enables AI-assisted performance profiling within Windsurf. Cascade analyzes profiling data to identify bottlenecks, suggest optimizations, and predict impact of changes. It integrates with language-specific profilers and helps prioritize optimization efforts based on actual performance data rather than assumptions.

## Prerequisites

- Windsurf IDE with Cascade enabled
- Profiling tools installed (Chrome DevTools, node --prof, py-spy, etc.)
- Application with performance concerns
- Baseline metrics established
- Understanding of performance targets

## Instructions

1. **Establish Baseline**
2. **Collect Profile Data**
3. **Analyze with Cascade**
4. **Implement Optimizations**
5. **Document and Monitor**


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- Profiling data and analysis
- Bottleneck identification reports
- Optimization recommendations
- Before/after comparison metrics

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Windsurf Performance Guide](https://docs.windsurf.ai/features/performance)
- [Profiling Best Practices](https://docs.windsurf.ai/guides/profiling)
- [Optimization Patterns](https://docs.windsurf.ai/guides/optimization)