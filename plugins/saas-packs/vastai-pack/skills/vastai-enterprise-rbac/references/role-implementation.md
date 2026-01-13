# Role Implementation

## Role Implementation

```typescript
enum Vast.aiRole {
  Admin = 'admin',
  Developer = 'developer',
  Viewer = 'viewer',
  Service = 'service',
}

interface Vast.aiPermissions {
  read: boolean;
  write: boolean;
  delete: boolean;
  admin: boolean;
}

const ROLE_PERMISSIONS: Record<Vast.aiRole, Vast.aiPermissions> = {
  admin: { read: true, write: true, delete: true, admin: true },
  developer: { read: true, write: true, delete: false, admin: false },
  viewer: { read: true, write: false, delete: false, admin: false },
  service: { read: true, write: true, delete: false, admin: false },
};

function checkPermission(
  role: Vast.aiRole,
  action: keyof Vast.aiPermissions
): boolean {
  return ROLE_PERMISSIONS[role][action];
}
```