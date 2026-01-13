# Error Handling Reference

| Issue | Resolution |
|-------|------------|
| Invalid signature | Check webhook secret |
| Unknown event | Log and acknowledge (200) |
| Processing error | Log error, return 500 |
| Duplicate events | Implement idempotency |