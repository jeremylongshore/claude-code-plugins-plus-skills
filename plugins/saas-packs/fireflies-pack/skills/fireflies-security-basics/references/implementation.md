# Implementation Guide

### Step 1: Configure Environment Variables
```bash
# .env (NEVER commit to git)
FIREFLIES_API_KEY=sk_live_***
FIREFLIES_SECRET=***

# .gitignore
.env
.env.local
.env.*.local
```

### Step 2: Implement Secret Rotation
```bash
# 1. Generate new key in Fireflies.ai dashboard
# 2. Update environment variable
export FIREFLIES_API_KEY="new_key_here"

# 3. Verify new key works
curl -H "Authorization: Bearer ${FIREFLIES_API_KEY}" \
  https://api.fireflies.com/health

# 4. Revoke old key in dashboard
```

### Step 3: Apply Least Privilege
| Environment | Recommended Scopes |
|-------------|-------------------|
| Development | `read:*` |
| Staging | `read:*, write:limited` |
| Production | `Only required scopes` |