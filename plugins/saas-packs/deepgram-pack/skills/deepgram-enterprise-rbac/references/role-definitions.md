# Role Definitions

## Role Definitions

```typescript
// config/roles.ts
export interface Role {
  name: string;
  description: string;
  deepgramScopes: string[];
  appPermissions: string[];
}

export const roles: Record<string, Role> = {
  admin: {
    name: 'Administrator',
    description: 'Full access to all Deepgram resources',
    deepgramScopes: ['manage:*', 'listen:*', 'usage:*', 'keys:*'],
    appPermissions: ['*'],
  },
  developer: {
    name: 'Developer',
    description: 'Transcription and development access',
    deepgramScopes: ['listen:*', 'usage:read'],
    appPermissions: [
      'transcription:create',
      'transcription:read',
      'projects:read',
    ],
  },
  analyst: {
    name: 'Analyst',
    description: 'Read-only access to transcriptions and usage',
    deepgramScopes: ['usage:read'],
    appPermissions: [
      'transcription:read',
      'usage:read',
      'reports:read',
    ],
  },
  service: {
    name: 'Service Account',
    description: 'Automated service access',
    deepgramScopes: ['listen:*'],
    appPermissions: [
      'transcription:create',
      'transcription:read',
    ],
  },
  auditor: {
    name: 'Auditor',
    description: 'Security and compliance access',
    deepgramScopes: ['usage:read', 'keys:read'],
    appPermissions: [
      'audit:read',
      'usage:read',
      'keys:read',
    ],
  },
};
```