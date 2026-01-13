# Examples

### Mock Windsurf Responses
```typescript
vi.mock('@windsurf/sdk', () => ({
  WindsurfClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=WINDSURF=* npm run dev
```