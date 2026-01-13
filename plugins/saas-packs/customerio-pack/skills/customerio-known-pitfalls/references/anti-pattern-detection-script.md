# Anti-Pattern Detection Script

## Anti-Pattern Detection Script

```typescript
// scripts/audit-integration.ts
interface AuditResult {
  issues: string[];
  warnings: string[];
  score: number;
}

async function auditIntegration(): Promise<AuditResult> {
  const result: AuditResult = { issues: [], warnings: [], score: 100 };

  // Check for hardcoded credentials
  const files = await glob('**/*.{ts,js}');
  for (const file of files) {
    const content = await readFile(file, 'utf-8');
    if (content.includes('site_') && content.includes('api_')) {
      result.issues.push(`Possible hardcoded credentials in ${file}`);
      result.score -= 20;
    }
  }

  // Check for millisecond timestamps
  if (await hasPattern(/Date\.now\(\)(?!\s*\/\s*1000)/)) {
    result.warnings.push('Possible millisecond timestamps detected');
    result.score -= 5;
  }

  // Check for track before identify pattern
  if (await hasPattern(/track\([^)]+\)[\s\S]{0,500}identify\(/)) {
    result.issues.push('Track before identify pattern detected');
    result.score -= 15;
  }

  return result;
}
```