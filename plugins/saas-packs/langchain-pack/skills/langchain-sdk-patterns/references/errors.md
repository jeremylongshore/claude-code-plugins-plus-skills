# Error Handling Reference

### Standard Error Pattern
```python
from langchain_core.exceptions import OutputParserException
from openai import RateLimitError, APIError

def safe_invoke(chain, input_data, max_retries=3):
    """Invoke chain with error handling."""
    for attempt in range(max_retries):
        try:
            return chain.invoke(input_data)
        except RateLimitError:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise
        except OutputParserException as e:
            # Handle parsing failures
            return {"error": str(e), "raw": e.llm_output}
        except APIError as e:
            raise RuntimeError(f"API error: {e}")
```