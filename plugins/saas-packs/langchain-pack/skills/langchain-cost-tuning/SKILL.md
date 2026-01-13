---
name: langchain-cost-tuning
license: MIT
allowed-tools: Read, Write, Edit
description: Optimize LangChain API costs and token usage. Use when reducing LLM API
  expenses, implementing cost controls, or optimizing token consumption in production.
  Trigger with phrases like "langchain cost", "langchain tokens", "reduce langchain
  cost", "...
---
# LangChain Cost Tuning

## Overview
Strategies for reducing LLM API costs while maintaining quality in LangChain applications.

## Prerequisites
- LangChain application in production
- Access to API usage dashboard
- Understanding of token pricing

## Instructions

### Step 1: Understand Token Pricing
```python
# Current approximate pricing (check provider for current rates)
PRICING = {
    "openai": {
        "gpt-4o": {"input": 0.005, "output": 0.015},      # per 1K tokens
        "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
        "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
    },
    "anthropic": {
        "claude-3-5-sonnet": {"input": 0.003, "output": 0.015},
        "claude-3-haiku": {"input": 0.00025, "output": 0.00125},
    },
    "google": {
        "gemini-1.5-pro": {"input": 0.00125, "output": 0.005},
        "gemini-1.5-flash": {"input": 0.000075, "output": 0.0003},
    }
}

def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    model: str = "gpt-4o-mini"
) -> float:
    """Estimate API cost for a request."""
    provider, model_name = model.split("/") if "/" in model else ("openai", model)
    rates = PRICING.get(provider, {}).get(model_name, {"input": 0.001, "output": 0.002})
    return (input_tokens / 1000 * rates["input"]) + (output_tokens / 1000 * rates["output"])
```

### Step 2: Implement Token Counting
```python
import tiktoken
from langchain_core.callbacks import BaseCallbackHandler

class CostTrackingCallback(BaseCallbackHandler):
    """Track token usage and costs."""

    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model
        self.total_input_tokens = 0
        self.total_output_tokens = 0
        self.requests = 0

    def on_llm_end(self, response, **kwargs) -> None:
        """Track tokens from LLM response."""
        if response.llm_output and "token_usage" in response.llm_output:
            usage = response.llm_output["token_usage"]
            self.total_input_tokens += usage.get("prompt_tokens", 0)
            self.total_output_tokens += usage.get("completion_tokens", 0)
            self.requests += 1

    @property
    def total_cost(self) -> float:
        return estimate_cost(
            self.total_input_tokens,
            self.total_output_tokens,
            self.model
        )

    def report(self) -> dict:
        return {
            "requests": self.requests,
            "input_tokens": self.total_input_tokens,
            "output_tokens": self.total_output_tokens,
            "total_tokens": self.total_input_tokens + self.total_output_tokens,
            "estimated_cost": f"${self.total_cost:.4f}"
        }

# Usage
tracker = CostTrackingCallback()
llm = ChatOpenAI(model="gpt-4o-mini", callbacks=[tracker])

# After operations
print(tracker.report())
```

### Step 3: Optimize Prompt Length
```python
import tiktoken

def optimize_prompt(
    text: str,
    max_tokens: int = 2000,
    model: str = "gpt-4o-mini"
) -> str:
    """Truncate text to fit within token budget."""
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)

    if len(tokens) <= max_tokens:
        return text

    # Truncate and add indicator
    truncated = encoding.decode(tokens[:max_tokens - 10])
    return truncated + "... [truncated]"

def summarize_context(long_text: str, llm) -> str:
    """Summarize long context to reduce tokens."""
    if count_tokens(long_text) < 2000:
        return long_text

    summary_prompt = ChatPromptTemplate.from_template(
        "Summarize this text in 500 words or less, preserving key facts:\n\n{text}"
    )
    chain = summary_prompt | llm | StrOutputParser()
    return chain.invoke({"text": long_text})
```

### Step 4: Model Tiering Strategy
```python
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableBranch

# Define model tiers
llm_cheap = ChatOpenAI(model="gpt-4o-mini", temperature=0)    # $0.15/1M tokens
llm_medium = ChatOpenAI(model="gpt-4o", temperature=0)         # $5/1M tokens
llm_powerful = ChatOpenAI(model="o1", temperature=0)           # $15/1M tokens

def select_model(input_data: dict) -> str:
    """Route to appropriate model based on task."""
    task_type = input_data.get("task_type", "simple")

    if task_type in ["chat", "faq", "simple"]:
        return "cheap"
    elif task_type in ["analysis", "summary", "medium"]:
        return "medium"
    else:
        return "powerful"

router = RunnableBranch(
    (lambda x: select_model(x) == "cheap", prompt | llm_cheap),
    (lambda x: select_model(x) == "medium", prompt | llm_medium),
    prompt | llm_powerful
)

# Simple chat: ~$0.0001 per request
# Complex analysis: ~$0.01 per request
# Cost reduction: 100x for simple tasks
```

### Step 5: Implement Caching
```python
from langchain_core.globals import set_llm_cache
from langchain_community.cache import RedisSemanticCache
from langchain_openai import OpenAIEmbeddings

# Semantic caching - finds similar queries
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
set_llm_cache(RedisSemanticCache(
    redis_url="redis://localhost:6379",
    embedding=embeddings,
    score_threshold=0.95  # High similarity required
))

# Example savings:
# - "What is Python?" and "What's Python?" -> Same cached response
# - 100 similar queries -> 1 API call + 99 cache hits
# - Potential 99% cost reduction for repetitive queries
```

### Step 6: Set Budget Limits
```python
class BudgetLimitCallback(BaseCallbackHandler):
    """Enforce budget limits."""

    def __init__(self, daily_budget: float = 10.0, model: str = "gpt-4o-mini"):
        self.daily_budget = daily_budget
        self.model = model
        self.daily_spend = 0.0
        self.last_reset = datetime.now().date()

    def on_llm_start(self, serialized, prompts, **kwargs) -> None:
        """Check budget before request."""
        today = datetime.now().date()
        if today != self.last_reset:
            self.daily_spend = 0.0
            self.last_reset = today

        if self.daily_spend >= self.daily_budget:
            raise RuntimeError(f"Daily budget of ${self.daily_budget} exceeded")

    def on_llm_end(self, response, **kwargs) -> None:
        """Update spend after request."""
        if response.llm_output and "token_usage" in response.llm_output:
            usage = response.llm_output["token_usage"]
            cost = estimate_cost(
                usage.get("prompt_tokens", 0),
                usage.get("completion_tokens", 0),
                self.model
            )
            self.daily_spend += cost

# Usage
budget_callback = BudgetLimitCallback(daily_budget=50.0)
llm = ChatOpenAI(model="gpt-4o-mini", callbacks=[budget_callback])
```

## Cost Optimization Summary
| Strategy | Potential Savings | Implementation Effort |
|----------|-------------------|----------------------|
| Model tiering | 50-100x | Medium |
| Response caching | 50-99% | Low |
| Prompt optimization | 10-50% | Low |
| Semantic caching | 30-70% | Medium |
| Budget limits | Risk mitigation | Low |

## Output
- Token counting and cost tracking
- Prompt optimization utilities
- Model routing for cost efficiency
- Budget enforcement callbacks

## Resources
- [OpenAI Pricing](https://openai.com/pricing)
- [Anthropic Pricing](https://www.anthropic.com/pricing)
- [tiktoken](https://github.com/openai/tiktoken)

## Next Steps
Use `langchain-reference-architecture` for scalable production patterns.
