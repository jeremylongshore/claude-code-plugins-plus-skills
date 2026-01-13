# Implementation Guide

### Step 1: Configure Environment Variables
```bash
# .env (NEVER commit to git)
CLAY_API_KEY=sk_live_***
CLAY_SECRET=***

# .gitignore
.env
.env.local
.env.*.local
```

### Step 2: Implement Secret Rotation
```bash
# 1. Generate new key in Clay dashboard
# 2. Update environment variable
export CLAY_API_KEY="new_key_here"

# 3. Verify new key works
curl -H "Authorization: Bearer ${CLAY_API_KEY}" \
  https://api.clay.com/health

# 4. Revoke old key in dashboard
```

### Step 3: Apply Least Privilege
| Environment | Recommended Scopes |
|-------------|-------------------|
| Development | `read:*` |
| Staging | `read:*, write:limited` |
| Production | `Only required scopes` |