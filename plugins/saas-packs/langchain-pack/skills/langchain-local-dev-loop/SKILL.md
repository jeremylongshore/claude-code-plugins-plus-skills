---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Configure LangChain local development workflow with hot reload and testing.
  Use when setting up development environment, configuring test fixtures, or establishing
  a rapid iteration workflow for LangChain apps. Trigger with phrases like "langchain...
name: langchain-local-dev-loop
---
# Langchain Local Dev Loop

This skill provides automated assistance for langchain local dev loop tasks.

## Prerequisites
- Completed `langchain-install-auth` setup
- Python 3.9+ with virtual environment
- pytest and related testing tools
- IDE with Python support (VS Code recommended)


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Organized project structure with separation of concerns
- pytest configuration with fixtures for mocking LLMs
- Development dependencies configured
- Ready for rapid iteration

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [pytest Documentation](https://docs.pytest.org/)
- [LangChain Testing Guide](https://python.langchain.com/docs/contributing/testing)
- [python-dotenv](https://pypi.org/project/python-dotenv/)