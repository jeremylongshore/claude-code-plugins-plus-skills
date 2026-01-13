---
name: openrouter-routing-rules
description: |
  Implement intelligent model routing based on request characteristics. Use when optimizing for cost, speed, or quality per request. Trigger with phrases like 'openrouter routing', 'model selection', 'smart routing', 'dynamic model'.
allowed-tools: Read, Write, Edit, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---
# OpenRouter Routing Rules

## Overview

This skill covers implementing request-based routing logic to select optimal models based on content, urgency, or cost constraints.

## Prerequisites

- OpenRouter integration
- Understanding of model capabilities and pricing

## Instructions

Follow these steps to implement this skill:

1. **Verify Prerequisites**: Ensure all prerequisites listed above are met
2. **Review the Implementation**: Study the code examples and patterns below
3. **Adapt to Your Environment**: Modify configuration values for your setup
4. **Test the Integration**: Run the verification steps to confirm functionality
5. **Monitor in Production**: Set up appropriate logging and monitoring

This skill provides automated assistance for openrouter routing rules tasks.

## Overview

This skill covers implementing request-based routing logic to select optimal models based on content, urgency, or cost constraints.

## Prerequisites

- OpenRouter integration
- Understanding of model capabilities and pricing

## Instructions

Follow these steps to implement this skill:

1. **Verify Prerequisites**: Ensure all prerequisites listed above are met
2. **Review the Implementation**: Study the code examples and patterns below
3. **Adapt to Your Environment**: Modify configuration values for your setup
4. **Test the Integration**: Run the verification steps to confirm functionality
5. **Monitor in Production**: Set up appropriate logging and monitoring

## Overview

This skill covers implementing request-based routing logic to select optimal models based on content, urgency, or cost constraints.

## Prerequisites

- OpenRouter integration
- Understanding of model capabilities and pricing

## Basic Routing Strategies

### Content-Based Routing
```python
def route_by_content(prompt: str) -> str:
    """Route to appropriate model based on content analysis."""
    prompt_lower = prompt.lower()

    # Code-related
    if any(word in prompt_lower for word in ["code", "function", "debug", "python", "javascript"]):
        return "anthropic/claude-3.5-sonnet"

## Detailed Reference

See `{baseDir}/references/implementation.md` for complete implementation guide.

## Output

Successful execution produces:
- Working OpenRouter integration
- Verified API connectivity
- Example responses demonstrating functionality

## Error Handling

Common errors and solutions:
1. **401 Unauthorized**: Check API key format (must start with `sk-or-`)
2. **429 Rate Limited**: Implement exponential backoff
3. **500 Server Error**: Retry with backoff, check OpenRouter status page
4. **Model Not Found**: Verify model ID includes provider prefix

## Examples

See code examples in sections above for complete, runnable implementations.

## Resources

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenRouter Models](https://openrouter.ai/models)
- [OpenRouter API Reference](https://openrouter.ai/docs/api-reference)
- [OpenRouter Status](https://status.openrouter.ai)
