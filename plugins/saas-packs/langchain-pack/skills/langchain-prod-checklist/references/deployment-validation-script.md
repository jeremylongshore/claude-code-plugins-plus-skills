# Deployment Validation Script

## Deployment Validation Script
```python
#!/usr/bin/env python3
"""Pre-deployment validation script."""

def run_checks():
    checks = []

    # Check 1: API key configured
    try:
        settings = Settings()
        checks.append(("API Key", "PASS"))
    except Exception as e:
        checks.append(("API Key", f"FAIL: {e}"))

    # Check 2: LLM connectivity
    try:
        llm = ChatOpenAI(model="gpt-4o-mini")
        llm.invoke("test")
        checks.append(("LLM Connection", "PASS"))
    except Exception as e:
        checks.append(("LLM Connection", f"FAIL: {e}"))

    # Check 3: Cache connectivity
    try:
        redis_client.ping()
        checks.append(("Cache (Redis)", "PASS"))
    except Exception as e:
        checks.append(("Cache (Redis)", f"FAIL: {e}"))

    for name, status in checks:
        print(f"[{status}] {name}")

    return all("PASS" in status for _, status in checks)

if __name__ == "__main__":
    exit(0 if run_checks() else 1)
```