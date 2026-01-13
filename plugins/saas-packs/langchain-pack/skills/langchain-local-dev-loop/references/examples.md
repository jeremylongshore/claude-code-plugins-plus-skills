# Examples

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test
pytest tests/test_chains.py::test_chain_invoke -v

# Watch mode (requires pytest-watch)
ptw
```

### Integration Test Example
```python
# tests/test_integration.py
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.integration
def test_real_llm_call():
    """Integration test with real LLM (requires API key)."""
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    response = llm.invoke("Say 'test passed'")
    assert "test" in response.content.lower()
```