---
name: orchestrating-multi-agent-systems
description: |
  Execute orchestrate multi-agent systems with handoffs, routing, and workflows across AI providers.
  Use when building complex AI systems requiring agent collaboration, task delegation, or workflow coordination.
  Trigger with phrases like "create multi-agent system", "orchestrate agents", or "coordinate agent workflows".
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Orchestrating Multi Agent Systems

This skill provides automated assistance for orchestrating multi agent systems tasks.

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure you have:
- Node.js 18+ installed for TypeScript agent development
- AI SDK v5 package installed (`npm install ai`)
- API keys for AI providers (OpenAI, Anthropic, Google, etc.)
- Understanding of agent-based architecture patterns
- TypeScript knowledge for agent implementation
- Project directory structure for multi-agent systems

## Instructions

1. Create project directory with necessary subdirectories
2. Initialize npm project with TypeScript configuration
3. Install AI SDK v5 and provider-specific packages
4. Set up configuration files for agent orchestration
1. Write agent initialization code with AI SDK
2. Configure system prompts for agent behavior
3. Define tool functions for agent capabilities
4. Implement handoff rules for inter-agent delegation


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- TypeScript files with AI SDK v5 integration
- System prompts tailored to each agent role
- Tool definitions and implementations
- Handoff rules and coordination logic
- Workflow definitions for task sequences
- Routing rules for intelligent task distribution

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- AI SDK v5 official documentation for agent creation
- Provider-specific integration guides (OpenAI, Anthropic, Google)
- Tool definition and implementation examples
- Handoff and routing pattern references
- Coordinator-worker pattern for task distribution