# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Import Error | SDK not installed | Run `pip install langchain langchain-openai` |
| Auth Error | Invalid credentials | Check environment variable is set |
| Timeout | Network issues | Increase timeout or check connectivity |
| Rate Limit | Too many requests | Wait and retry with exponential backoff |
| Model Not Found | Invalid model name | Check available models in provider docs |