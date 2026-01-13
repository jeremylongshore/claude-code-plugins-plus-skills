# Error Handling Reference

### Retry Logic
```javascript
async function processWithRetry(data, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      await processEvent(data);
      return { success: true };
    } catch (error) {
      console.error(`Attempt ${attempt} failed:`, error);

      if (attempt === maxRetries) {
        await notifyError(data, error);
        return { success: false, error };
      }

      // Exponential backoff
      await sleep(Math.pow(2, attempt) * 1000);
    }
  }
}
```

### Dead Letter Queue
```yaml
On Error:
  1. Log error details
  2. Store failed event in queue
  3. Alert ops team
  4. Retry after 1 hour
  5. If still failing, archive for manual review
```