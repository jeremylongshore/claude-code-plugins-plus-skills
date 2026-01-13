# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Webhook Timeout | Slow endpoint | Increase timeout, use async |
| WebSocket Disconnect | Client closed | Handle disconnect gracefully |
| Event Queue Full | Too many events | Add queue size limit |
| SSE Timeout | Long response | Add keep-alive pings |