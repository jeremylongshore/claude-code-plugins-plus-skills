---
name: cursor-codebase-indexing
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Execute set up and optimize cursor codebase indexing. triggers on "cursor
  index setup", "codebase indexing", "index codebase", "cursor semantic search". use
  when working with cursor codebase indexing functionality. trigger with phrases like
  "curso...
---
# Cursor Codebase Indexing

## Overview

### What is Codebase Indexing?
```
Codebase indexing creates a searchable representation of your code:
- Enables @codebase queries
- Powers semantic code search
- Improves AI context awareness
- Helps AI understand project structure
```

## Prerequisites

- Cursor IDE installed and authenticated
- Project workspace with source files
- Sufficient disk space for index storage
- Stable network connection for initial setup

## Instructions

1. Open your project in Cursor
2. Navigate to Settings > Cursor > Codebase Indexing
3. Enable "Index this workspace"
4. Create `.cursorignore` file at project root
5. Add exclusion patterns for large/irrelevant directories
6. Wait for indexing to complete (check status bar)
7. Test with `@codebase` queries in chat

## Output

- Indexed codebase enabling `@codebase` queries
- Semantic code search functionality
- Improved AI context awareness
- Searchable symbol table and definitions

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Cursor Indexing Documentation](https://cursor.com/docs/indexing)
- [gitignore Pattern Syntax](https://git-scm.com/docs/gitignore)
- [Cursor Performance Guide](https://cursor.com/docs/performance)
