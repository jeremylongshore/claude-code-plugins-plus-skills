# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| form_identifier_not_found | Email not registered | Show sign-up prompt |
| form_password_incorrect | Wrong password | Show error, offer reset |
| session_exists | Already signed in | Redirect to dashboard |
| verification_failed | Wrong code | Allow retry, resend code |