# Examples

### Mock Fireflies.ai Responses
```typescript
vi.mock('@fireflies/sdk', () => ({
  Fireflies.aiClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=FIREFLIES=* npm run dev
```