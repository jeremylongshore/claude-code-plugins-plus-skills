# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// Windsurf SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://windsurf.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/windsurf/callback',
};

// Map IdP groups to Windsurf roles
const groupRoleMapping: Record<string, WindsurfRole> = {
  'Engineering': WindsurfRole.Developer,
  'Platform-Admins': WindsurfRole.Admin,
  'Data-Team': WindsurfRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@windsurf/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.WINDSURF_OAUTH_CLIENT_ID!,
  clientSecret: process.env.WINDSURF_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/windsurf/callback',
  scopes: ['read', 'write'],
});
```