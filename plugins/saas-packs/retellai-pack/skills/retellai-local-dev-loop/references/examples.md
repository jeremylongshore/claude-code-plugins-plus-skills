# Examples

### Mock Retell AI Responses
```typescript
vi.mock('@retellai/sdk', () => ({
  RetellAIClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=RETELLAI=* npm run dev
```