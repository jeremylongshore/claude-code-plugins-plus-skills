---
allowed-tools: Read, Grep, Bash
license: MIT
description: Collect juicebox debug evidence for support. use when creating support
  tickets, gathering diagnostic info, or preparing error reports for juicebox support
  team. trigger with phrases like "juicebox debug info", "juicebox support bundle",
  "collect j...
name: juicebox-debug-bundle
---
# Juicebox Debug Bundle

This skill provides automated assistance for juicebox debug bundle tasks.

## Prerequisites
- Access to application logs
- Juicebox API key configured
- Terminal access


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `debug-bundle.txt` - Text summary
- `debug-bundle-*.json` - Structured data
- Filtered error logs
- API connectivity results

## Resources
- [Support Portal](https://juicebox.ai/support)
- [Community Forum](https://community.juicebox.ai)