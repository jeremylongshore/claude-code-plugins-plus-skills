# Examples

### Singleton Pattern
```typescript
// Ensure single client instance
let instance: JuiceboxService | null = null;

export function getJuiceboxService(): JuiceboxService {
  if (!instance) {
    instance = new JuiceboxService(process.env.JUICEBOX_API_KEY!);
  }
  return instance;
}
```