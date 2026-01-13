---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Plan and execute langchain sdk upgrades and migrations. use when upgrading
  langchain versions, migrating from legacy patterns, or updating to new apis after
  breaking changes. trigger with phrases like "upgrade langchain", "langchain migration",
  "l...
name: langchain-upgrade-migration
---
# Langchain Upgrade Migration

This skill provides automated assistance for langchain upgrade migration tasks.

## Prerequisites
- Existing LangChain application
- Version control with current code committed
- Test suite covering core functionality
- Staging environment for validation


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [LangChain Migration Guide](https://python.langchain.com/docs/versions/migrating_chains/)
- [LCEL Documentation](https://python.langchain.com/docs/concepts/lcel/)
- [Release Notes](https://github.com/langchain-ai/langchain/releases)
- [Deprecation Timeline](https://python.langchain.com/docs/versions/v0_3/)