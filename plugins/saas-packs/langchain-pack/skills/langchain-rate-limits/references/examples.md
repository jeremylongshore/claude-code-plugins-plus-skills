# Examples

### Handling Rate Limits in Production
```python
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableConfig

llm = ChatOpenAI(
    model="gpt-4o-mini",
    max_retries=5,
)

# Use batch with max_concurrency
inputs = [{"input": f"Query {i}"} for i in range(100)]

results = chain.batch(
    inputs,
    config=RunnableConfig(max_concurrency=10)  # Limit concurrent calls
)
```

### Fallback on Rate Limit
```python
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

primary = ChatOpenAI(model="gpt-4o-mini", max_retries=2)
fallback = ChatAnthropic(model="claude-3-5-sonnet-20241022")

# Automatically switch to fallback on rate limit
robust_llm = primary.with_fallbacks([fallback])
```