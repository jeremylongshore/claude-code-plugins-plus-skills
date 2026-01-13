---
allowed-tools: Read, Write, Edit
license: MIT
description: Build LangChain agents with tools for autonomous task execution. Use
  when creating AI agents, implementing tool calling, or building autonomous workflows
  with decision-making. Trigger with phrases like "langchain agents", "langchain tools",
  "tool ...
name: langchain-core-workflow-b
---
# Langchain Core Workflow B

This skill provides automated assistance for langchain core workflow b tasks.

## Prerequisites
- Completed `langchain-core-workflow-a` (chains)
- Understanding of function/tool calling concepts
- Familiarity with async programming


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Typed tool definitions with Pydantic schemas
- Configured agent executor with error handling
- Working agent that can reason and use tools
- Streaming output for real-time feedback

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Agents Conceptual Guide](https://python.langchain.com/docs/concepts/agents/)
- [Tool Calling](https://python.langchain.com/docs/concepts/tool_calling/)
- [Agent Types](https://python.langchain.com/docs/how_to/agent_executor/)