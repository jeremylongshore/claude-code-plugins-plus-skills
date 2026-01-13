# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Connection Closed | Network interruption | Implement auto-reconnect |
| Buffer Overflow | Too much audio data | Reduce sample rate or chunk size |
| No Transcripts | Silent audio | Check audio levels and format |
| High Latency | Network/processing delay | Use interim results |