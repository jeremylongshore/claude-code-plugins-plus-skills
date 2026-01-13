# Examples

### Mock Ideogram Responses
```typescript
vi.mock('@ideogram/sdk', () => ({
  IdeogramClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=IDEOGRAM=* npm run dev
```