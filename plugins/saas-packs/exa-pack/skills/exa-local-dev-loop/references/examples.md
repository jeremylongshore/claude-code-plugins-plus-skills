# Examples

### Mock Exa Responses
```typescript
vi.mock('@exa/sdk', () => ({
  ExaClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=EXA=* npm run dev
```