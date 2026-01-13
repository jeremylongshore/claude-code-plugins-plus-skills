# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Development/Production mismatch | Using prod keys in dev | Use pk_test_/sk_test_ keys locally |
| SSL Required | Clerk needs HTTPS | Use `next dev --experimental-https` |
| Cookies Not Set | Wrong domain config | Check Clerk dashboard domain settings |
| Session Not Persisting | LocalStorage issues | Clear browser storage, check domain |