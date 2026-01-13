# Role Implementation

## Role Implementation

```typescript
enum FireCrawlRole {
  Admin = 'admin',
  Developer = 'developer',
  Viewer = 'viewer',
  Service = 'service',
}

interface FireCrawlPermissions {
  read: boolean;
  write: boolean;
  delete: boolean;
  admin: boolean;
}

const ROLE_PERMISSIONS: Record<FireCrawlRole, FireCrawlPermissions> = {
  admin: { read: true, write: true, delete: true, admin: true },
  developer: { read: true, write: true, delete: false, admin: false },
  viewer: { read: true, write: false, delete: false, admin: false },
  service: { read: true, write: true, delete: false, admin: false },
};

function checkPermission(
  role: FireCrawlRole,
  action: keyof FireCrawlPermissions
): boolean {
  return ROLE_PERMISSIONS[role][action];
}
```