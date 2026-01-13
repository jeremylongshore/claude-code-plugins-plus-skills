# Role Implementation

## Role Implementation

```typescript
enum Fireflies.aiRole {
  Admin = 'admin',
  Developer = 'developer',
  Viewer = 'viewer',
  Service = 'service',
}

interface Fireflies.aiPermissions {
  read: boolean;
  write: boolean;
  delete: boolean;
  admin: boolean;
}

const ROLE_PERMISSIONS: Record<Fireflies.aiRole, Fireflies.aiPermissions> = {
  admin: { read: true, write: true, delete: true, admin: true },
  developer: { read: true, write: true, delete: false, admin: false },
  viewer: { read: true, write: false, delete: false, admin: false },
  service: { read: true, write: true, delete: false, admin: false },
};

function checkPermission(
  role: Fireflies.aiRole,
  action: keyof Fireflies.aiPermissions
): boolean {
  return ROLE_PERMISSIONS[role][action];
}
```