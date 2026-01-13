# Migration Planning

## Migration Planning

### Pre-Migration Assessment

```typescript
// scripts/migration-assessment.ts
interface MigrationAssessment {
  source: {
    system: string;
    recordCount: number;
    dataQuality: DataQualityReport;
    fieldMapping: FieldMappingAnalysis;
  };
  target: {
    apolloPlan: string;
    creditBudget: number;
    apiLimits: APILimits;
  };
  risk: {
    level: 'low' | 'medium' | 'high';
    factors: string[];
    mitigations: string[];
  };
  timeline: {
    estimatedDuration: string;
    phases: Phase[];
  };
}

async function assessMigration(sourceConfig: any): Promise<MigrationAssessment> {
  // Analyze source data
  const sourceAnalysis = await analyzeSourceData(sourceConfig);

  // Check Apollo capacity
  const apolloCapacity = await checkApolloCapacity();

  // Calculate risks
  const risks = calculateRisks(sourceAnalysis, apolloCapacity);

  // Estimate timeline
  const timeline = estimateTimeline(sourceAnalysis, apolloCapacity);

  return {
    source: sourceAnalysis,
    target: apolloCapacity,
    risk: risks,
    timeline,
  };
}

async function analyzeSourceData(config: any): Promise<SourceAnalysis> {
  const records = await fetchSourceRecords(config);

  return {
    system: config.system,
    recordCount: records.length,
    dataQuality: {
      emailValid: records.filter(r => isValidEmail(r.email)).length / records.length,
      emailPresent: records.filter(r => r.email).length / records.length,
      phonePresent: records.filter(r => r.phone).length / records.length,
      companyPresent: records.filter(r => r.company).length / records.length,
      duplicates: findDuplicates(records).length,
    },
    fieldMapping: analyzeFields(records),
  };
}
```

### Field Mapping

```typescript
// src/migration/field-mapper.ts
interface FieldMapping {
  sourceField: string;
  targetField: string;
  transform?: (value: any) => any;
  required: boolean;
  validation?: (value: any) => boolean;
}

const SALESFORCE_TO_APOLLO: FieldMapping[] = [
  {
    sourceField: 'Email',
    targetField: 'email',
    required: true,
    validation: isValidEmail,
  },
  {
    sourceField: 'FirstName',
    targetField: 'first_name',
    required: false,
  },
  {
    sourceField: 'LastName',
    targetField: 'last_name',
    required: false,
  },
  {
    sourceField: 'Title',
    targetField: 'title',
    required: false,
    transform: normalizeTitle,
  },
  {
    sourceField: 'Phone',
    targetField: 'phone',
    required: false,
    transform: normalizePhone,
  },
  {
    sourceField: 'Account.Name',
    targetField: 'organization_name',
    required: false,
  },
  {
    sourceField: 'Account.Website',
    targetField: 'organization_domain',
    transform: extractDomain,
    required: false,
  },
  {
    sourceField: 'LinkedIn_URL__c',
    targetField: 'linkedin_url',
    required: false,
    validation: isValidLinkedInUrl,
  },
];

const HUBSPOT_TO_APOLLO: FieldMapping[] = [
  { sourceField: 'properties.email', targetField: 'email', required: true },
  { sourceField: 'properties.firstname', targetField: 'first_name', required: false },
  { sourceField: 'properties.lastname', targetField: 'last_name', required: false },
  { sourceField: 'properties.jobtitle', targetField: 'title', required: false },
  { sourceField: 'properties.phone', targetField: 'phone', required: false },
  { sourceField: 'properties.company', targetField: 'organization_name', required: false },
  { sourceField: 'properties.website', targetField: 'organization_domain', transform: extractDomain, required: false },
];

function transformRecord(record: any, mappings: FieldMapping[]): any {
  const transformed: any = {};
  const errors: string[] = [];

  for (const mapping of mappings) {
    const value = getNestedValue(record, mapping.sourceField);

    if (mapping.required && !value) {
      errors.push(`Missing required field: ${mapping.sourceField}`);
      continue;
    }

    if (value) {
      let transformedValue = mapping.transform ? mapping.transform(value) : value;

      if (mapping.validation && !mapping.validation(transformedValue)) {
        errors.push(`Invalid value for ${mapping.sourceField}: ${value}`);
        continue;
      }

      transformed[mapping.targetField] = transformedValue;
    }
  }

  return { data: transformed, errors };
}
```