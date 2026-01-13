# Implementation Guide

### Step 1: Understand Provider Limits
```python
# Common rate limits by provider:
RATE_LIMITS = {
    "openai": {
        "gpt-4o": {"rpm": 10000, "tpm": 800000},
        "gpt-4o-mini": {"rpm": 10000, "tpm": 4000000},
    },
    "anthropic": {
        "claude-3-5-sonnet": {"rpm": 4000, "tpm": 400000},
    },
    "google": {
        "gemini-1.5-pro": {"rpm": 360, "tpm": 4000000},
    }
}
# rpm = requests per minute, tpm = tokens per minute
```

### Step 2: Built-in Retry Configuration
```python
from langchain_openai import ChatOpenAI

# LangChain has built-in retry with exponential backoff
llm = ChatOpenAI(
    model="gpt-4o-mini",
    max_retries=3,  # Number of retries
    request_timeout=30,  # Timeout per request
)
```

### Step 3: Advanced Retry with Tenacity
```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)
from openai import RateLimitError, APIError

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=4, max=60),
    retry=retry_if_exception_type((RateLimitError, APIError))
)
def call_with_retry(chain, input_data):
    """Call chain with exponential backoff."""
    return chain.invoke(input_data)

# Usage
result = call_with_retry(chain, {"input": "Hello"})
```

### Step 4: Rate Limiter Wrapper
```python
import asyncio
import time
from collections import deque
from threading import Lock

class RateLimiter:
    """Token bucket rate limiter for API calls."""

    def __init__(self, requests_per_minute: int = 60):
        self.rpm = requests_per_minute
        self.interval = 60.0 / requests_per_minute
        self.timestamps = deque()
        self.lock = Lock()

    def acquire(self):
        """Block until request can be made."""
        with self.lock:
            now = time.time()
            # Remove timestamps older than 1 minute
            while self.timestamps and now - self.timestamps[0] > 60:
                self.timestamps.popleft()

            if len(self.timestamps) >= self.rpm:
                sleep_time = 60 - (now - self.timestamps[0])
                if sleep_time > 0:
                    time.sleep(sleep_time)

            self.timestamps.append(time.time())

# Usage with LangChain
rate_limiter = RateLimiter(requests_per_minute=100)

def rate_limited_call(chain, input_data):
    rate_limiter.acquire()
    return chain.invoke(input_data)
```

### Step 5: Async Rate Limiting
```python
import asyncio
from asyncio import Semaphore

class AsyncRateLimiter:
    """Async rate limiter with semaphore."""

    def __init__(self, max_concurrent: int = 10):
        self.semaphore = Semaphore(max_concurrent)

    async def call(self, chain, input_data):
        async with self.semaphore:
            return await chain.ainvoke(input_data)

# Batch processing with rate limiting
async def process_batch(chain, inputs: list, max_concurrent: int = 5):
    limiter = AsyncRateLimiter(max_concurrent)
    tasks = [limiter.call(chain, inp) for inp in inputs]
    return await asyncio.gather(*tasks, return_exceptions=True)
```