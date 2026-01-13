# Error Handling Reference

| Layer | Strategy |
|-------|----------|
| Client | Retry with backoff |
| Service | Graceful degradation |
| Jobs | Dead letter queue |
| API | Structured error responses |