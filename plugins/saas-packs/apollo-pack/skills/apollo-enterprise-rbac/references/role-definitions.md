# Role Definitions

## Role Definitions

```typescript
// src/lib/rbac/roles.ts
import { Permission } from './permissions';

interface Role {
  name: string;
  description: string;
  permissions: Permission[];
  inherits?: string[];
}

export const ROLES: Record<string, Role> = {
  super_admin: {
    name: 'Super Admin',
    description: 'Full system access',
    permissions: Object.keys(PERMISSIONS) as Permission[],
  },

  admin: {
    name: 'Admin',
    description: 'Administrative access without billing',
    permissions: [
      'contacts:read', 'contacts:create', 'contacts:update', 'contacts:delete', 'contacts:export',
      'search:basic', 'search:advanced', 'search:bulk',
      'enrich:person', 'enrich:company', 'enrich:bulk',
      'sequences:read', 'sequences:create', 'sequences:edit', 'sequences:delete', 'sequences:enroll', 'sequences:send',
      'admin:users', 'admin:roles', 'admin:settings', 'admin:audit',
    ],
  },

  sales_manager: {
    name: 'Sales Manager',
    description: 'Manage sales team and sequences',
    permissions: [
      'contacts:read', 'contacts:create', 'contacts:update', 'contacts:export', 'contacts:reveal_email',
      'search:basic', 'search:advanced',
      'enrich:person', 'enrich:company',
      'sequences:read', 'sequences:create', 'sequences:edit', 'sequences:enroll', 'sequences:send',
    ],
  },

  sales_rep: {
    name: 'Sales Representative',
    description: 'Basic sales access',
    permissions: [
      'contacts:read', 'contacts:create', 'contacts:update', 'contacts:reveal_email',
      'search:basic',
      'enrich:person',
      'sequences:read', 'sequences:enroll',
    ],
  },

  marketing_manager: {
    name: 'Marketing Manager',
    description: 'Manage marketing campaigns',
    permissions: [
      'contacts:read', 'contacts:export',
      'search:basic', 'search:advanced', 'search:bulk',
      'enrich:person', 'enrich:company', 'enrich:bulk',
      'sequences:read', 'sequences:create', 'sequences:edit',
    ],
  },

  marketing_user: {
    name: 'Marketing User',
    description: 'Basic marketing access',
    permissions: [
      'contacts:read',
      'search:basic',
      'sequences:read',
    ],
  },

  read_only: {
    name: 'Read Only',
    description: 'View-only access',
    permissions: [
      'contacts:read',
      'search:basic',
      'sequences:read',
    ],
  },
};
```