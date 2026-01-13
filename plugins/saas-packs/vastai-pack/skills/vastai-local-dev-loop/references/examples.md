# Examples

### Mock Vast.ai Responses
```typescript
vi.mock('@vastai/sdk', () => ({
  Vast.aiClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=VASTAI=* npm run dev
```