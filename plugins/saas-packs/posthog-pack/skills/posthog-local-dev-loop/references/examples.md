# Examples

### Mock PostHog Responses
```typescript
vi.mock('@posthog/sdk', () => ({
  PostHogClient: vi.fn().mockImplementation(() => ({
    // Mock methods here
  })),
}));
```

### Debug Mode
```bash
# Enable verbose logging
DEBUG=POSTHOG=* npm run dev
```