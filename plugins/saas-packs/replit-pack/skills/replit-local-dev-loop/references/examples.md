# Examples

### Mock Replit Responses
```typescript
vi.mock('@replit/sdk', () => ({
  ReplitClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=REPLIT=* npm run dev
```