# Permission Definitions

## Permission Definitions

```typescript
// src/lib/rbac/permissions.ts
export const PERMISSIONS = {
  // Contact permissions
  'contacts:read': 'View contact information',
  'contacts:create': 'Add new contacts',
  'contacts:update': 'Edit contact information',
  'contacts:delete': 'Delete contacts',
  'contacts:export': 'Export contact data',
  'contacts:reveal_email': 'Reveal email addresses (uses credits)',

  // Search permissions
  'search:basic': 'Basic people search',
  'search:advanced': 'Advanced search filters',
  'search:bulk': 'Bulk search operations',

  // Enrichment permissions
  'enrich:person': 'Enrich individual contacts',
  'enrich:company': 'Enrich company data',
  'enrich:bulk': 'Bulk enrichment operations',

  // Sequence permissions
  'sequences:read': 'View sequences',
  'sequences:create': 'Create new sequences',
  'sequences:edit': 'Edit sequences',
  'sequences:delete': 'Delete sequences',
  'sequences:enroll': 'Add contacts to sequences',
  'sequences:send': 'Send emails through sequences',

  // Admin permissions
  'admin:users': 'Manage users',
  'admin:roles': 'Manage roles',
  'admin:settings': 'Configure settings',
  'admin:billing': 'View/manage billing',
  'admin:audit': 'View audit logs',
  'admin:api_keys': 'Manage API keys',
} as const;

export type Permission = keyof typeof PERMISSIONS;
```