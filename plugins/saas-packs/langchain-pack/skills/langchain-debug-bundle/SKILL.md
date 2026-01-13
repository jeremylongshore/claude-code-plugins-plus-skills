---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Collect langchain debug evidence for troubleshooting and support. use
  when preparing bug reports, collecting traces, or gathering diagnostic information
  for complex issues. trigger with phrases like "langchain debug bundle", "langchain
  diagnostics...
name: langchain-debug-bundle
---
# Langchain Debug Bundle

This skill provides automated assistance for langchain debug bundle tasks.

## Prerequisites
- LangChain installed
- Reproducible error condition
- Access to logs and environment


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- `debug_bundle.json` with full diagnostic information
- `minimal_repro.py` for issue reproduction
- Environment and version information
- Trace logs with timestamps

## Resources
- [LangChain GitHub Issues](https://github.com/langchain-ai/langchain/issues)
- [LangSmith Tracing](https://docs.smith.langchain.com/)
- [LangChain Discord](https://discord.gg/langchain)