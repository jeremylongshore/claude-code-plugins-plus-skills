# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// FireCrawl SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://firecrawl.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/firecrawl/callback',
};

// Map IdP groups to FireCrawl roles
const groupRoleMapping: Record<string, FireCrawlRole> = {
  'Engineering': FireCrawlRole.Developer,
  'Platform-Admins': FireCrawlRole.Admin,
  'Data-Team': FireCrawlRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@firecrawl/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.FIRECRAWL_OAUTH_CLIENT_ID!,
  clientSecret: process.env.FIRECRAWL_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/firecrawl/callback',
  scopes: ['read', 'write'],
});
```