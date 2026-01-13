# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Audio Too Long | Exceeds limits | Split into chunks or use async |
| Unsupported Format | Invalid audio type | Convert to WAV/MP3/FLAC |
| Empty Response | No speech detected | Check audio quality |
| Timeout | Large file processing | Use callback URL pattern |