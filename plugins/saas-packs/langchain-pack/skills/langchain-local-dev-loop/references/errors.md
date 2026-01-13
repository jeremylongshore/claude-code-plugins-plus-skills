# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Import Error | Missing package | Install with `pip install -e ".[dev]"` |
| Fixture Not Found | conftest.py issue | Ensure conftest.py is in tests/ directory |
| Async Test Error | Missing marker | Add `@pytest.mark.asyncio` decorator |
| Env Var Missing | .env not loaded | Use `python-dotenv` and load_dotenv() |