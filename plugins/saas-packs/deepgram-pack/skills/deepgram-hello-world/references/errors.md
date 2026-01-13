# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Import Error | SDK not installed | Verify with `npm list @deepgram/sdk` |
| Auth Error | Invalid credentials | Check environment variable is set |
| Audio Format Error | Unsupported format | Use WAV, MP3, FLAC, or OGG |
| URL Not Accessible | Cannot fetch audio | Ensure URL is publicly accessible |