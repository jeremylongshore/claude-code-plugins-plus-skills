# Role Implementation

## Role Implementation

```typescript
enum IdeogramRole {
  Admin = 'admin',
  Developer = 'developer',
  Viewer = 'viewer',
  Service = 'service',
}

interface IdeogramPermissions {
  read: boolean;
  write: boolean;
  delete: boolean;
  admin: boolean;
}

const ROLE_PERMISSIONS: Record<IdeogramRole, IdeogramPermissions> = {
  admin: { read: true, write: true, delete: true, admin: true },
  developer: { read: true, write: true, delete: false, admin: false },
  viewer: { read: true, write: false, delete: false, admin: false },
  service: { read: true, write: true, delete: false, admin: false },
};

function checkPermission(
  role: IdeogramRole,
  action: keyof IdeogramPermissions
): boolean {
  return ROLE_PERMISSIONS[role][action];
}
```