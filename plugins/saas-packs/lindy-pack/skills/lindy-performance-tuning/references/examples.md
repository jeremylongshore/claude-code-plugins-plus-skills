# Examples

### Complete Performance Client
```typescript
class PerformantLindyClient {
  private lindy: Lindy;
  private cache: NodeCache;
  private limiter: any;

  constructor() {
    this.lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });
    this.cache = new NodeCache({ stdTTL: 300 });
    this.limiter = pLimit(5);
  }

  async run(agentId: string, input: string) {
    const cacheKey = `${agentId}:${input}`;
    const cached = this.cache.get(cacheKey);
    if (cached) return cached;

    const result = await this.limiter(() =>
      this.lindy.agents.run(agentId, { input })
    );

    this.cache.set(cacheKey, result);
    return result;
  }
}
```