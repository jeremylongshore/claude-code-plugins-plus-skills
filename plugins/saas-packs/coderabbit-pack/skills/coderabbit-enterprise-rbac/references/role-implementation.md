# Role Implementation

## Role Implementation

```typescript
enum CodeRabbitRole {
  Admin = 'admin',
  Developer = 'developer',
  Viewer = 'viewer',
  Service = 'service',
}

interface CodeRabbitPermissions {
  read: boolean;
  write: boolean;
  delete: boolean;
  admin: boolean;
}

const ROLE_PERMISSIONS: Record<CodeRabbitRole, CodeRabbitPermissions> = {
  admin: { read: true, write: true, delete: true, admin: true },
  developer: { read: true, write: true, delete: false, admin: false },
  viewer: { read: true, write: false, delete: false, admin: false },
  service: { read: true, write: true, delete: false, admin: false },
};

function checkPermission(
  role: CodeRabbitRole,
  action: keyof CodeRabbitPermissions
): boolean {
  return ROLE_PERMISSIONS[role][action];
}
```