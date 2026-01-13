---
name: langchain-common-errors
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Diagnose and fix common langchain errors and exceptions. use when encountering
  langchain errors, debugging failures, or troubleshooting integration issues. trigger
  with phrases like "langchain error", "langchain exception", "debug langchain", "lan...
---
# LangChain Common Errors

## Overview
Quick reference for diagnosing and resolving the most common LangChain errors.

## Prerequisites
- LangChain installed and configured
- Access to application logs
- Understanding of your LangChain implementation

## Error Reference

### Authentication Errors

#### `openai.AuthenticationError: Incorrect API key provided`
```python
# Cause: Invalid or missing API key
# Solution:
import os
os.environ["OPENAI_API_KEY"] = "sk-..."  # Set correct key

# Verify key is loaded
from langchain_openai import ChatOpenAI
llm = ChatOpenAI()  # Will raise error if key invalid
```

#### `anthropic.AuthenticationError: Invalid x-api-key`
```python
# Cause: Anthropic API key not set or invalid
# Solution:
os.environ["ANTHROPIC_API_KEY"] = "sk-ant-..."

# Or pass directly
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(api_key="sk-ant-...")
```

### Import Errors

#### `ModuleNotFoundError: No module named 'langchain_openai'`
```bash
# Cause: Provider package not installed
# Solution:
pip install langchain-openai

# For other providers:
pip install langchain-anthropic
pip install langchain-google-genai
pip install langchain-community
```

#### `ImportError: cannot import name 'ChatOpenAI' from 'langchain'`
```python
# Cause: Using old import path (pre-0.2.0)
# Old (deprecated):
from langchain.chat_models import ChatOpenAI

# New (correct):
from langchain_openai import ChatOpenAI
```

### Rate Limiting

#### `openai.RateLimitError: Rate limit reached`
```python
# Cause: Too many API requests
# Solution: Implement retry with backoff
from langchain_openai import ChatOpenAI
from tenacity import retry, wait_exponential, stop_after_attempt

@retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(5))
def call_with_retry(llm, prompt):
    return llm.invoke(prompt)

# Or use LangChain's built-in retry
llm = ChatOpenAI(max_retries=3)
```

### Output Parsing Errors

#### `OutputParserException: Failed to parse output`
```python
# Cause: LLM output doesn't match expected format
# Solution 1: Use with_retry
from langchain.output_parsers import RetryOutputParser

parser = RetryOutputParser.from_llm(parser=your_parser, llm=llm)

# Solution 2: Use structured output (more reliable)
from pydantic import BaseModel

class Output(BaseModel):
    answer: str

llm_with_structure = llm.with_structured_output(Output)
```

#### `ValidationError: field required`
```python
# Cause: Pydantic model validation failed
# Solution: Make fields optional or provide defaults
from pydantic import BaseModel, Field
from typing import Optional

class Output(BaseModel):
    answer: str
    confidence: Optional[float] = Field(default=None)
```

### Chain Errors

#### `ValueError: Missing required input keys`
```python
# Cause: Input dict missing required variables
# Debug:
prompt = ChatPromptTemplate.from_template("Hello {name}, you are {age}")
print(prompt.input_variables)  # ['name', 'age']

# Solution: Provide all required keys
chain.invoke({"name": "Alice", "age": 30})
```

#### `TypeError: Expected mapping type as input`
```python
# Cause: Passing wrong input type
# Wrong:
chain.invoke("hello")

# Correct:
chain.invoke({"input": "hello"})
```

### Agent Errors

#### `AgentExecutor: max iterations reached`
```python
# Cause: Agent stuck in loop
# Solution: Increase iterations or improve prompts
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    max_iterations=20,  # Increase from default 15
    early_stopping_method="force"  # Force stop after max
)
```

#### `ToolException: Tool execution failed`
```python
# Cause: Tool raised an exception
# Solution: Add error handling in tool
@tool
def my_tool(input: str) -> str:
    """Tool description."""
    try:
        # Tool logic
        return result
    except Exception as e:
        return f"Tool error: {str(e)}"
```

### Memory Errors

#### `KeyError: 'chat_history'`
```python
# Cause: Memory key mismatch
# Solution: Ensure consistent key names
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),  # Match this
    ("human", "{input}")
])

# When invoking:
chain.invoke({
    "input": "hello",
    "chat_history": []  # Must match placeholder name
})
```

## Debugging Tips

### Enable Verbose Mode
```python
import langchain
langchain.debug = True  # Shows all chain steps

# Or per-component
agent_executor = AgentExecutor(verbose=True)
```

### Trace with LangSmith
```python
# Set environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-key"
os.environ["LANGCHAIN_PROJECT"] = "my-project"

# All chains automatically traced
```

### Check Version Compatibility
```bash
pip show langchain langchain-core langchain-openai

# Ensure versions are compatible:
# langchain >= 0.3.0
# langchain-core >= 0.3.0
# langchain-openai >= 0.2.0
```

## Resources
- [LangChain Troubleshooting](https://python.langchain.com/docs/troubleshooting/)
- [LangSmith Debugging](https://docs.smith.langchain.com/)
- [GitHub Issues](https://github.com/langchain-ai/langchain/issues)

## Next Steps
For complex debugging, use `langchain-debug-bundle` to collect evidence.
