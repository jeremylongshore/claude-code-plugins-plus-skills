# Examples

### Mock Perplexity Responses
```typescript
vi.mock('@perplexity/sdk', () => ({
  PerplexityClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=PERPLEXITY=* npm run dev
```