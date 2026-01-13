# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// Groq SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://groq.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/groq/callback',
};

// Map IdP groups to Groq roles
const groupRoleMapping: Record<string, GroqRole> = {
  'Engineering': GroqRole.Developer,
  'Platform-Admins': GroqRole.Admin,
  'Data-Team': GroqRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@groq/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.GROQ_OAUTH_CLIENT_ID!,
  clientSecret: process.env.GROQ_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/groq/callback',
  scopes: ['read', 'write'],
});
```