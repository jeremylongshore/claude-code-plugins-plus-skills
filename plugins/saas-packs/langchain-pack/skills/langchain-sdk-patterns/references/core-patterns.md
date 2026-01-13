# Core Patterns

## Core Patterns

### Pattern 1: Type-Safe Chain with Pydantic
```python
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class SentimentResult(BaseModel):
    """Structured output for sentiment analysis."""
    sentiment: str = Field(description="positive, negative, or neutral")
    confidence: float = Field(description="Confidence score 0-1")
    reasoning: str = Field(description="Brief explanation")

llm = ChatOpenAI(model="gpt-4o-mini")
structured_llm = llm.with_structured_output(SentimentResult)

prompt = ChatPromptTemplate.from_template(
    "Analyze the sentiment of: {text}"
)

chain = prompt | structured_llm

# Returns typed SentimentResult
result: SentimentResult = chain.invoke({"text": "I love LangChain!"})
print(f"Sentiment: {result.sentiment} ({result.confidence})")
```

### Pattern 2: Retry with Fallback
```python
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnableWithFallbacks

primary = ChatOpenAI(model="gpt-4o")
fallback = ChatAnthropic(model="claude-3-5-sonnet-20241022")

# Automatically falls back on failure
robust_llm = primary.with_fallbacks([fallback])

response = robust_llm.invoke("Hello!")
```

### Pattern 3: Async Batch Processing
```python
import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_template("Summarize: {text}")
chain = prompt | llm

async def process_batch(texts: list[str]) -> list:
    """Process multiple texts concurrently."""
    inputs = [{"text": t} for t in texts]
    results = await chain.abatch(inputs, config={"max_concurrency": 5})
    return results

# Usage
results = asyncio.run(process_batch(["text1", "text2", "text3"]))
```

### Pattern 4: Streaming with Callbacks
```python
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import StreamingStdOutCallbackHandler

llm = ChatOpenAI(
    model="gpt-4o-mini",
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

# Streams tokens to stdout as they arrive
for chunk in llm.stream("Tell me a story"):
    # Each chunk contains partial content
    pass
```

### Pattern 5: Caching for Cost Reduction
```python
from langchain_openai import ChatOpenAI
from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache

# Enable SQLite caching
set_llm_cache(SQLiteCache(database_path=".langchain_cache.db"))

llm = ChatOpenAI(model="gpt-4o-mini")

# First call hits API
response1 = llm.invoke("What is 2+2?")

# Second identical call uses cache (no API cost)
response2 = llm.invoke("What is 2+2?")
```