# Examples

### Quick PII Scan
```typescript
const findings = detectPII(JSON.stringify(userData));
if (findings.length > 0) {
  console.warn(`PII detected: ${findings.map(f => f.type).join(', ')}`);
}
```

### Redact Before Logging
```typescript
const safeData = redactPII(apiResponse);
logger.info('FireCrawl response:', safeData);
```

### GDPR Data Export
```typescript
const userExport = await exportUserData('user-123');
await sendToUser(userExport);
```