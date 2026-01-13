# Examples

### Production-Ready Security
```typescript
// security/index.ts
export async function initializeLindy(): Promise<Lindy> {
  // Validate environment
  validateEnvironment();

  // Get key from secret manager
  const apiKey = await getApiKey();

  // Initialize with security options
  const lindy = new Lindy({
    apiKey,
    timeout: 30000,
    retries: 3,
  });

  // Verify connection
  await lindy.users.me();

  console.log('Lindy initialized securely');
  return lindy;
}
```