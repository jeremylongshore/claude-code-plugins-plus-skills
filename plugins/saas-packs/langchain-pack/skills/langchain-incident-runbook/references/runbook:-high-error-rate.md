# Runbook: High Error Rate

## Runbook: High Error Rate

### Detection
```bash
# Check recent errors in logs
grep -i "error" /var/log/langchain/app.log | tail -50

# Check LangSmith for failed traces
# Navigate to: https://smith.langchain.com/o/YOUR_ORG/projects/YOUR_PROJECT/runs?filter=error%3Atrue
```

### Diagnosis
```python
# Analyze error distribution
from collections import Counter
import json

def analyze_errors(log_file: str) -> dict:
    """Analyze error patterns from logs."""
    errors = []

    with open(log_file) as f:
        for line in f:
            if "error" in line.lower():
                try:
                    log = json.loads(line)
                    errors.append(log.get("error_type", "unknown"))
                except:
                    pass

    return dict(Counter(errors).most_common(10))

# Common error types and causes
ERROR_CAUSES = {
    "RateLimitError": "Exceeded API quota - reduce load or increase limits",
    "AuthenticationError": "Invalid API key - check secrets",
    "Timeout": "Network issues or overloaded provider",
    "OutputParserException": "LLM output format changed - check prompts",
    "ValidationError": "Schema mismatch - update Pydantic models",
}
```

### Mitigation
```python
# 1. Reduce load
# Scale down instances or enable circuit breaker

# 2. Emergency rate limiting
from functools import wraps
import time

def emergency_rate_limit(calls_per_minute: int = 10):
    """Emergency rate limiter decorator."""
    interval = 60.0 / calls_per_minute
    last_call = [0]

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            elapsed = time.time() - last_call[0]
            if elapsed < interval:
                await asyncio.sleep(interval - elapsed)
            last_call[0] = time.time()
            return await func(*args, **kwargs)
        return wrapper
    return decorator

# 3. Enable caching for repeated queries
from langchain_core.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
set_llm_cache(InMemoryCache())
```

---