# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// Retell AI SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://retellai.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/retellai/callback',
};

// Map IdP groups to Retell AI roles
const groupRoleMapping: Record<string, Retell AIRole> = {
  'Engineering': Retell AIRole.Developer,
  'Platform-Admins': Retell AIRole.Admin,
  'Data-Team': Retell AIRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@retellai/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.RETELLAI_OAUTH_CLIENT_ID!,
  clientSecret: process.env.RETELLAI_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/retellai/callback',
  scopes: ['read', 'write'],
});
```