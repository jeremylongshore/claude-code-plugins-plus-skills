# Examples

### Mock FireCrawl Responses
```typescript
vi.mock('@firecrawl/sdk', () => ({
  FireCrawlClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=FIRECRAWL=* npm run dev
```