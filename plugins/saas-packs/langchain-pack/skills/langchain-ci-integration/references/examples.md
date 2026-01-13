# Examples

### Running Tests Locally
```bash
# Run unit tests only (fast)
pytest tests/unit -v

# Run with coverage
pytest tests/unit --cov=src --cov-report=html

# Run integration tests (requires API key)
OPENAI_API_KEY=sk-... pytest tests/integration -v -m integration

# Skip slow tests
pytest tests/ -v -m "not slow"
```

### Integration Test Example
```python
# tests/integration/test_chain.py
import pytest
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

@pytest.mark.integration
def test_real_chain_invocation():
    """Test with real LLM (requires API key)."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt = ChatPromptTemplate.from_template("Say exactly: {word}")
    chain = prompt | llm

    result = chain.invoke({"word": "hello"})
    assert "hello" in result.content.lower()
```