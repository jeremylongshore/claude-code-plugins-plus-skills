# Production Checklist

## Production Checklist

### 1. Configuration & Secrets
- [ ] All API keys in secrets manager (not env vars in code)
- [ ] Environment-specific configurations separated
- [ ] Fallback values for non-critical settings
- [ ] Configuration validation on startup

```python
from pydantic_settings import BaseSettings
from pydantic import Field, SecretStr

class Settings(BaseSettings):
    """Validated configuration."""
    openai_api_key: SecretStr = Field(..., env="OPENAI_API_KEY")
    model_name: str = "gpt-4o-mini"
    max_retries: int = Field(default=3, ge=1, le=10)
    timeout_seconds: int = Field(default=30, ge=5, le=120)

    class Config:
        env_file = ".env"

settings = Settings()  # Validates on import
```

### 2. Error Handling & Resilience
- [ ] Retry logic with exponential backoff
- [ ] Fallback models configured
- [ ] Circuit breaker for cascading failures
- [ ] Graceful degradation strategy

```python
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

primary = ChatOpenAI(model="gpt-4o-mini", max_retries=3)
fallback = ChatAnthropic(model="claude-3-5-sonnet-20241022")

robust_llm = primary.with_fallbacks([fallback])
```

### 3. Observability
- [ ] Structured logging configured
- [ ] Metrics collection enabled
- [ ] Distributed tracing (LangSmith or OpenTelemetry)
- [ ] Alerting rules defined

```python
import os

# LangSmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = settings.langsmith_api_key
os.environ["LANGCHAIN_PROJECT"] = "production"

# Prometheus metrics
from prometheus_client import Counter, Histogram

llm_requests = Counter("langchain_llm_requests_total", "Total LLM requests")
llm_latency = Histogram("langchain_llm_latency_seconds", "LLM latency")
```

### 4. Performance
- [ ] Caching configured for repeated queries
- [ ] Connection pooling enabled
- [ ] Timeout limits set
- [ ] Batch processing for bulk operations

```python
from langchain_core.globals import set_llm_cache
from langchain_community.cache import RedisCache
import redis

# Production caching with Redis
redis_client = redis.Redis.from_url(os.environ["REDIS_URL"])
set_llm_cache(RedisCache(redis_client))
```

### 5. Security
- [ ] Input validation implemented
- [ ] Output sanitization enabled
- [ ] Rate limiting per user/IP
- [ ] Audit logging for all LLM calls

```python
from langchain_core.runnables import RunnableLambda

def validate_input(input_data: dict) -> dict:
    """Validate and sanitize input."""
    user_input = input_data.get("input", "")
    if len(user_input) > 10000:
        raise ValueError("Input too long")
    return input_data

secure_chain = RunnableLambda(validate_input) | prompt | llm
```

### 6. Testing
- [ ] Unit tests for all chains
- [ ] Integration tests with mock LLMs
- [ ] Load tests completed
- [ ] Chaos engineering (failure injection)

```python
# pytest.ini
[pytest]
markers =
    unit: Unit tests
    integration: Integration tests
    load: Load tests
```

### 7. Deployment
- [ ] Health check endpoint
- [ ] Graceful shutdown handling
- [ ] Rolling deployment strategy
- [ ] Rollback procedure documented

```python
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Warming up LLM connections...")
    yield
    # Shutdown
    print("Cleaning up...")

app = FastAPI(lifespan=lifespan)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model": settings.model_name}
```

### 8. Cost Management
- [ ] Token counting implemented
- [ ] Usage alerts configured
- [ ] Cost allocation by tenant/feature
- [ ] Budget limits enforced

```python
import tiktoken

def estimate_cost(text: str, model: str = "gpt-4o-mini") -> float:
    """Estimate API cost for text."""
    encoding = tiktoken.encoding_for_model(model)
    tokens = len(encoding.encode(text))
    # Approximate pricing (check current rates)
    cost_per_1k = {"gpt-4o-mini": 0.00015, "gpt-4o": 0.005}
    return (tokens / 1000) * cost_per_1k.get(model, 0.001)
```