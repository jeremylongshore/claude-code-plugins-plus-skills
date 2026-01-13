# Examples

### Mock CodeRabbit Responses
```typescript
vi.mock('@coderabbit/sdk', () => ({
  CodeRabbitClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=CODERABBIT=* npm run dev
```