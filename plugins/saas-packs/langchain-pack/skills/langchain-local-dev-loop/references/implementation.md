# Implementation Guide

### Step 1: Set Up Project Structure
```
my-langchain-app/
├── src/
│   ├── __init__.py
│   ├── chains/
│   │   └── __init__.py
│   ├── agents/
│   │   └── __init__.py
│   └── prompts/
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_chains.py
├── .env
├── .env.example
├── pyproject.toml
└── README.md
```

### Step 2: Configure Testing
```python
# tests/conftest.py
import pytest
from unittest.mock import MagicMock
from langchain_core.messages import AIMessage

@pytest.fixture
def mock_llm():
    """Mock LLM for unit tests without API calls."""
    mock = MagicMock()
    mock.invoke.return_value = AIMessage(content="Mocked response")
    return mock

@pytest.fixture
def sample_prompt():
    """Sample prompt for testing."""
    from langchain_core.prompts import ChatPromptTemplate
    return ChatPromptTemplate.from_template("Test: {input}")
```

### Step 3: Create Test File
```python
# tests/test_chains.py
def test_chain_construction(mock_llm, sample_prompt):
    """Test that chain can be constructed."""
    from langchain_core.output_parsers import StrOutputParser

    chain = sample_prompt | mock_llm | StrOutputParser()
    assert chain is not None

def test_chain_invoke(mock_llm, sample_prompt):
    """Test chain invocation with mock."""
    from langchain_core.output_parsers import StrOutputParser

    chain = sample_prompt | mock_llm | StrOutputParser()
    result = chain.invoke({"input": "test"})
    assert result == "Mocked response"
```

### Step 4: Set Up Development Tools
```toml
# pyproject.toml
[project]
name = "my-langchain-app"
version = "0.1.0"
requires-python = ">=3.9"
dependencies = [
    "langchain>=0.3.0",
    "langchain-openai>=0.2.0",
    "python-dotenv>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
    "pytest-cov>=4.0.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0",
]

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]

[tool.ruff]
line-length = 100
```