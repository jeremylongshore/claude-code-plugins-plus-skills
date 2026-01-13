# Examples

### Mock Clay Responses
```typescript
vi.mock('@clay/sdk', () => ({
  ClayClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=CLAY=* npm run dev
```