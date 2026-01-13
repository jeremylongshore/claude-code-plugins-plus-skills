# Examples

### Mock Groq Responses
```typescript
vi.mock('@groq/sdk', () => ({
  GroqClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=GROQ=* npm run dev
```