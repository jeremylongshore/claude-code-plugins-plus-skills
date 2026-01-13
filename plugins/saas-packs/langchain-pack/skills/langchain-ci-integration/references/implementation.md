# Implementation Guide

### Step 1: Create GitHub Actions Workflow
```yaml
# .github/workflows/langchain-ci.yml
name: LangChain CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  PYTHON_VERSION: "3.11"

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: |
          pip install ruff mypy

      - name: Lint with Ruff
        run: ruff check .

      - name: Type check with mypy
        run: mypy src/

  test-unit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: |
          pip install -e ".[dev]"

      - name: Run unit tests
        run: |
          pytest tests/unit -v --cov=src --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          files: coverage.xml

  test-integration:
    runs-on: ubuntu-latest
    needs: [lint, test-unit]
    # Only run on main branch or manual trigger
    if: github.ref == 'refs/heads/main' || github.event_name == 'workflow_dispatch'
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: |
          pip install -e ".[dev]"

      - name: Run integration tests
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          pytest tests/integration -v -m integration
```

### Step 2: Configure Test Markers
```python
# pyproject.toml
[tool.pytest.ini_options]
markers = [
    "unit: Unit tests (no external API calls)",
    "integration: Integration tests (requires API keys)",
    "slow: Slow tests (skip in fast mode)",
]
asyncio_mode = "auto"
testpaths = ["tests"]
```

### Step 3: Create Mock Fixtures
```python
# tests/conftest.py
import pytest
from unittest.mock import MagicMock, AsyncMock
from langchain_core.messages import AIMessage

@pytest.fixture
def mock_llm():
    """Mock LLM for unit tests."""
    mock = MagicMock()
    mock.invoke.return_value = AIMessage(content="Mock response")
    mock.ainvoke = AsyncMock(return_value=AIMessage(content="Mock response"))
    return mock

@pytest.fixture
def mock_chain(mock_llm):
    """Mock chain for testing."""
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser

    prompt = ChatPromptTemplate.from_template("{input}")
    return prompt | mock_llm | StrOutputParser()
```

### Step 4: Add Pre-commit Hooks
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.6
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
        additional_dependencies:
          - langchain-core
          - pydantic
```

### Step 5: Add Deployment Stage
```yaml
# Add to .github/workflows/langchain-ci.yml
  deploy:
    runs-on: ubuntu-latest
    needs: [test-integration]
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to Cloud Run
        uses: google-github-actions/deploy-cloudrun@v2
        with:
          service: langchain-api
          source: .
          env_vars: |
            LANGCHAIN_PROJECT=production
```