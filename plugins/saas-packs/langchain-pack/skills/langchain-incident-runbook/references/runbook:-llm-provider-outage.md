# Runbook: Llm Provider Outage

## Runbook: LLM Provider Outage

### Detection
```bash
# Check if LLM provider is responding
curl -s https://status.openai.com/api/v2/status.json | jq '.status.indicator'
curl -s https://status.anthropic.com/api/v2/status.json | jq '.status.indicator'

# Check your error rate
# Prometheus query:
# sum(rate(langchain_llm_requests_total{status="error"}[5m])) / sum(rate(langchain_llm_requests_total[5m]))
```

### Diagnosis
```python
# Quick diagnostic script
import asyncio
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

async def diagnose_providers():
    """Check all configured providers."""
    results = {}

    # Test OpenAI
    try:
        llm = ChatOpenAI(model="gpt-4o-mini", request_timeout=10)
        await llm.ainvoke("test")
        results["openai"] = "OK"
    except Exception as e:
        results["openai"] = f"FAIL: {e}"

    # Test Anthropic
    try:
        llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", timeout=10)
        await llm.ainvoke("test")
        results["anthropic"] = "OK"
    except Exception as e:
        results["anthropic"] = f"FAIL: {e}"

    return results

# Run
print(asyncio.run(diagnose_providers()))
```

### Mitigation: Enable Fallback
```python
# Emergency fallback configuration
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

# Original
llm = ChatOpenAI(model="gpt-4o-mini")

# With fallback
primary = ChatOpenAI(model="gpt-4o-mini", max_retries=1, request_timeout=5)
fallback = ChatAnthropic(model="claude-3-haiku-20240307")

llm = primary.with_fallbacks([fallback])
```

### Recovery
1. Monitor provider status page
2. Gradually remove fallback when primary recovers
3. Document incident in post-mortem

---