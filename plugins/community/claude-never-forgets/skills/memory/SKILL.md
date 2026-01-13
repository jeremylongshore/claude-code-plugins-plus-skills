---
allowed-tools: Read, Write
license: MIT
description: Execute extract and use project memories from previous sessions for context-aware
  assistance. use when recalling past decisions, checking project conventions, or
  understanding user preferences. trigger with phrases like "remember when", "like
  befo...
name: memory
---
# Memory

This skill provides automated assistance for memory tasks.

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure you have:
- Project memory file at `{baseDir}/.memories/project_memory.json`
- Read permissions for the memory storage location
- Understanding that memories persist across sessions
- Knowledge of slash commands for manual memory management

## Instructions

1. Locate memory file using Read tool
2. Parse JSON structure containing memory entries
3. Identify relevant memories based on current context
4. Extract applicable decisions, conventions, or preferences


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- Memories applied automatically without announcement
- Decisions informed by historical context
- Consistent behavior aligned with past choices
- Natural incorporation of established patterns
- List of all stored memories with timestamps
- Confirmation of newly added memories

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- `/remember [text]` - Add new memory to manual_memories array
- `/forget [text]` - Remove matching memory from storage
- `/memories` - Display all currently stored memories
- Apply memories silently without announcing to user
- Current explicit requests always override stored memories