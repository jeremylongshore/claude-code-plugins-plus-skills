# Validation & Reconciliation

## Validation & Reconciliation

```typescript
// src/migration/validation.ts
interface ValidationResult {
  totalSource: number;
  totalTarget: number;
  matched: number;
  mismatched: number;
  missing: number;
  extra: number;
  fieldDiscrepancies: FieldDiscrepancy[];
}

interface FieldDiscrepancy {
  recordId: string;
  field: string;
  sourceValue: any;
  targetValue: any;
}

async function validateMigration(): Promise<ValidationResult> {
  // Get all source records
  const sourceRecords = await fetchAllSourceRecords();
  const sourceMap = new Map(sourceRecords.map(r => [r.email, r]));

  // Get all migrated records from Apollo
  const apolloRecords = await fetchAllApolloContacts();
  const apolloMap = new Map(apolloRecords.map(r => [r.email, r]));

  const result: ValidationResult = {
    totalSource: sourceRecords.length,
    totalTarget: apolloRecords.length,
    matched: 0,
    mismatched: 0,
    missing: 0,
    extra: 0,
    fieldDiscrepancies: [],
  };

  // Check source records exist in Apollo
  for (const [email, sourceRecord] of sourceMap) {
    const apolloRecord = apolloMap.get(email);

    if (!apolloRecord) {
      result.missing++;
      continue;
    }

    // Compare fields
    const discrepancies = compareRecords(sourceRecord, apolloRecord);
    if (discrepancies.length === 0) {
      result.matched++;
    } else {
      result.mismatched++;
      result.fieldDiscrepancies.push(...discrepancies);
    }
  }

  // Check for extra records in Apollo
  for (const [email] of apolloMap) {
    if (!sourceMap.has(email)) {
      result.extra++;
    }
  }

  return result;
}

function compareRecords(source: any, target: any): FieldDiscrepancy[] {
  const discrepancies: FieldDiscrepancy[] = [];
  const fieldsToCompare = ['first_name', 'last_name', 'title', 'phone'];

  for (const field of fieldsToCompare) {
    const sourceValue = normalizeValue(source[field]);
    const targetValue = normalizeValue(target[field]);

    if (sourceValue !== targetValue) {
      discrepancies.push({
        recordId: source.id,
        field,
        sourceValue,
        targetValue,
      });
    }
  }

  return discrepancies;
}
```