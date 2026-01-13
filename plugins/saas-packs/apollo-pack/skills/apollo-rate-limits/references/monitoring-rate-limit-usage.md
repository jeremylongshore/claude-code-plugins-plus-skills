# Monitoring Rate Limit Usage

## Monitoring Rate Limit Usage

```typescript
// src/lib/apollo/rate-monitor.ts
class RateLimitMonitor {
  private requests: Array<{ timestamp: number; remaining: number }> = [];

  recordRequest(remaining: number) {
    this.requests.push({
      timestamp: Date.now(),
      remaining,
    });

    // Keep only last 5 minutes
    const cutoff = Date.now() - 5 * 60 * 1000;
    this.requests = this.requests.filter((r) => r.timestamp > cutoff);
  }

  getStats() {
    const lastMinute = this.requests.filter(
      (r) => r.timestamp > Date.now() - 60000
    );

    return {
      requestsLastMinute: lastMinute.length,
      currentRemaining: lastMinute[lastMinute.length - 1]?.remaining ?? 100,
      utilizationPercent: (lastMinute.length / 100) * 100,
      isNearLimit: lastMinute.length > 80,
    };
  }
}

export const rateLimitMonitor = new RateLimitMonitor();
```