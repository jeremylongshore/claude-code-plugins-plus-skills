---
name: langchain-ci-integration
description: |
  Configure LangChain CI/CD integration with GitHub Actions and testing.
  Use when setting up automated testing, configuring CI pipelines,
  or integrating LangChain tests into your build process.
  Trigger with phrases like "langchain CI", "langchain GitHub Actions",
  "langchain automated tests", "CI langchain", "langchain pipeline".
allowed-tools: Read, Write, Edit, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# LangChain CI Integration

## Overview
Configure comprehensive CI/CD pipelines for LangChain applications with testing, linting, and deployment automation.

## Prerequisites
- GitHub repository with Actions enabled
- LangChain application with test suite
- API keys for testing (stored as GitHub Secrets)

## Instructions

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

## Output
- GitHub Actions workflow with lint, test, deploy stages
- pytest configuration with markers
- Mock fixtures for unit testing
- Pre-commit hooks for code quality

## Examples

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

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| Secret Not Found | Missing GitHub secret | Add OPENAI_API_KEY to repository secrets |
| Rate Limit in CI | Too many API calls | Use mocks for unit tests, limit integration tests |
| Timeout | Slow tests | Add timeout markers, parallelize tests |
| Import Error | Missing dev dependencies | Ensure `.[dev]` extras installed |

## Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [pytest Documentation](https://docs.pytest.org/)
- [Pre-commit](https://pre-commit.com/)

## Next Steps
Proceed to `langchain-deploy-integration` for deployment configuration.
