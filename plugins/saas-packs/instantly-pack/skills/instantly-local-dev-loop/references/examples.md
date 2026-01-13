# Examples

### Mock Instantly Responses
```typescript
vi.mock('@instantly/sdk', () => ({
  InstantlyClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=INSTANTLY=* npm run dev
```