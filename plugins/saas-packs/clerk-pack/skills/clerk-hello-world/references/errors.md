# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| userId is null | User not authenticated | Redirect to sign-in or check middleware |
| currentUser returns null | Session expired | Refresh page or re-authenticate |
| 401 Unauthorized | Token missing or invalid | Check Authorization header |
| Hydration Error | Server/client mismatch | Use 'use client' for client hooks |