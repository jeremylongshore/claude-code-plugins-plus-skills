# Pre-Upgrade Assessment

## Pre-Upgrade Assessment

### Check Current API Usage
```bash
# Find all Apollo API calls in codebase
grep -r "api.apollo.io" --include="*.ts" --include="*.js" -l

# List unique endpoints used
grep -roh "api.apollo.io/v[0-9]*/[a-z_/]*" --include="*.ts" --include="*.js" | sort -u

# Check for deprecated patterns
grep -rn "deprecated\|legacy" --include="*.ts" src/lib/apollo/
```

### Audit Script
```typescript
// scripts/apollo-audit.ts
import { readFileSync, readdirSync } from 'fs';
import { join } from 'path';

interface AuditResult {
  file: string;
  line: number;
  pattern: string;
  severity: 'warning' | 'error';
  message: string;
}

const DEPRECATED_PATTERNS = [
  {
    pattern: /\/v1\/contacts\//,
    message: 'Use /v1/people/ instead of /v1/contacts/',
    severity: 'error' as const,
  },
  {
    pattern: /organization_name/,
    message: 'Use q_organization_domains instead of organization_name',
    severity: 'warning' as const,
  },
  {
    pattern: /\.then\s*\(/,
    message: 'Consider using async/await for cleaner code',
    severity: 'warning' as const,
  },
];

function auditFile(filePath: string): AuditResult[] {
  const content = readFileSync(filePath, 'utf-8');
  const lines = content.split('\n');
  const results: AuditResult[] = [];

  lines.forEach((line, index) => {
    for (const { pattern, message, severity } of DEPRECATED_PATTERNS) {
      if (pattern.test(line)) {
        results.push({
          file: filePath,
          line: index + 1,
          pattern: pattern.source,
          severity,
          message,
        });
      }
    }
  });

  return results;
}

function auditDirectory(dir: string): AuditResult[] {
  const results: AuditResult[] = [];

  function walkDir(currentDir: string) {
    const files = readdirSync(currentDir, { withFileTypes: true });
    for (const file of files) {
      const path = join(currentDir, file.name);
      if (file.isDirectory() && !file.name.includes('node_modules')) {
        walkDir(path);
      } else if (file.name.endsWith('.ts') || file.name.endsWith('.js')) {
        results.push(...auditFile(path));
      }
    }
  }

  walkDir(dir);
  return results;
}

// Run audit
const results = auditDirectory('./src');
console.log('Apollo API Audit Results:\n');

for (const result of results) {
  const icon = result.severity === 'error' ? '[ERR]' : '[WRN]';
  console.log(`${icon} ${result.file}:${result.line}`);
  console.log(`     ${result.message}\n`);
}

console.log(`Total: ${results.length} issues found`);
```