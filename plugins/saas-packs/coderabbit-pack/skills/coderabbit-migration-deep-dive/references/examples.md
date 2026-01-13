# Examples

### Quick Migration Status
```typescript
const status = await validateCodeRabbitMigration();
console.log(`Migration ${status.passed ? 'PASSED' : 'FAILED'}`);
status.checks.forEach(c => console.log(`  ${c.name}: ${c.result.success}`));
```