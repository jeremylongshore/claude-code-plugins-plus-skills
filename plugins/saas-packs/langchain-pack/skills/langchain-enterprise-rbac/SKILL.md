---
name: langchain-enterprise-rbac
license: MIT
allowed-tools: Read, Write, Edit
description: Implement enterprise role-based access control for langchain applications.
  use when implementing user permissions, multi-tenant access, or enterprise security
  controls for llm applications. trigger with phrases like "langchain rbac", "langchain
  pe...
---
# LangChain Enterprise RBAC

## Overview
Implement role-based access control (RBAC) for LangChain applications with multi-tenant support and fine-grained permissions.

## Prerequisites
- LangChain application with user authentication
- Identity provider (Auth0, Okta, Azure AD)
- Understanding of RBAC concepts

## Instructions

### Step 1: Define Permission Model
```python
from enum import Enum
from typing import Set, Optional
from pydantic import BaseModel
from datetime import datetime

class Permission(str, Enum):
    # Chain permissions
    CHAIN_READ = "chain:read"
    CHAIN_EXECUTE = "chain:execute"
    CHAIN_CREATE = "chain:create"
    CHAIN_DELETE = "chain:delete"

    # Model permissions
    MODEL_GPT4 = "model:gpt-4"
    MODEL_GPT4_MINI = "model:gpt-4o-mini"
    MODEL_CLAUDE = "model:claude"

    # Feature permissions
    FEATURE_STREAMING = "feature:streaming"
    FEATURE_TOOLS = "feature:tools"
    FEATURE_RAG = "feature:rag"

    # Admin permissions
    ADMIN_USERS = "admin:users"
    ADMIN_BILLING = "admin:billing"
    ADMIN_AUDIT = "admin:audit"

class Role(BaseModel):
    name: str
    permissions: Set[Permission]
    description: str = ""

# Predefined roles
ROLES = {
    "viewer": Role(
        name="viewer",
        permissions={Permission.CHAIN_READ},
        description="Read-only access to chains"
    ),
    "user": Role(
        name="user",
        permissions={
            Permission.CHAIN_READ,
            Permission.CHAIN_EXECUTE,
            Permission.MODEL_GPT4_MINI,
        },
        description="Standard user with execution rights"
    ),
    "power_user": Role(
        name="power_user",
        permissions={
            Permission.CHAIN_READ,
            Permission.CHAIN_EXECUTE,
            Permission.CHAIN_CREATE,
            Permission.MODEL_GPT4_MINI,
            Permission.MODEL_GPT4,
            Permission.FEATURE_STREAMING,
            Permission.FEATURE_TOOLS,
        },
        description="Power user with advanced features"
    ),
    "admin": Role(
        name="admin",
        permissions=set(Permission),  # All permissions
        description="Full administrative access"
    ),
}
```

### Step 2: User and Tenant Management
```python
from typing import Dict, List
import uuid

class Tenant(BaseModel):
    id: str
    name: str
    allowed_models: List[str] = []
    monthly_token_limit: int = 1_000_000
    features: Set[str] = set()
    created_at: datetime = None

class User(BaseModel):
    id: str
    email: str
    tenant_id: str
    roles: List[str]
    created_at: datetime = None

    def get_permissions(self) -> Set[Permission]:
        """Get all permissions for user based on roles."""
        permissions = set()
        for role_name in self.roles:
            if role_name in ROLES:
                permissions.update(ROLES[role_name].permissions)
        return permissions

    def has_permission(self, permission: Permission) -> bool:
        """Check if user has specific permission."""
        return permission in self.get_permissions()

class UserStore:
    """User and tenant management."""

    def __init__(self):
        self.tenants: Dict[str, Tenant] = {}
        self.users: Dict[str, User] = {}

    def create_tenant(self, name: str, **kwargs) -> Tenant:
        tenant = Tenant(
            id=str(uuid.uuid4()),
            name=name,
            created_at=datetime.now(),
            **kwargs
        )
        self.tenants[tenant.id] = tenant
        return tenant

    def create_user(
        self,
        email: str,
        tenant_id: str,
        roles: List[str] = None
    ) -> User:
        if tenant_id not in self.tenants:
            raise ValueError(f"Tenant {tenant_id} not found")

        user = User(
            id=str(uuid.uuid4()),
            email=email,
            tenant_id=tenant_id,
            roles=roles or ["user"],
            created_at=datetime.now()
        )
        self.users[user.id] = user
        return user

    def get_user_tenant(self, user_id: str) -> Optional[Tenant]:
        user = self.users.get(user_id)
        if user:
            return self.tenants.get(user.tenant_id)
        return None
```

### Step 3: Permission Enforcement
```python
from functools import wraps
from fastapi import HTTPException, Depends, Request
from typing import Callable

class PermissionChecker:
    """Check and enforce permissions."""

    def __init__(self, user_store: UserStore):
        self.user_store = user_store

    def require_permission(self, permission: Permission):
        """Decorator to require specific permission."""
        def decorator(func: Callable):
            @wraps(func)
            async def wrapper(request: Request, *args, **kwargs):
                user_id = request.state.user_id  # Set by auth middleware
                user = self.user_store.users.get(user_id)

                if not user:
                    raise HTTPException(status_code=401, detail="User not found")

                if not user.has_permission(permission):
                    raise HTTPException(
                        status_code=403,
                        detail=f"Permission denied: {permission.value}"
                    )

                return await func(request, *args, **kwargs)
            return wrapper
        return decorator

    def require_any_permission(self, permissions: List[Permission]):
        """Require at least one of the specified permissions."""
        def decorator(func: Callable):
            @wraps(func)
            async def wrapper(request: Request, *args, **kwargs):
                user_id = request.state.user_id
                user = self.user_store.users.get(user_id)

                if not user:
                    raise HTTPException(status_code=401)

                if not any(user.has_permission(p) for p in permissions):
                    raise HTTPException(status_code=403)

                return await func(request, *args, **kwargs)
            return wrapper
        return decorator

# Usage
user_store = UserStore()
checker = PermissionChecker(user_store)

@app.post("/chains/{chain_id}/execute")
@checker.require_permission(Permission.CHAIN_EXECUTE)
async def execute_chain(request: Request, chain_id: str):
    # User has CHAIN_EXECUTE permission
    pass
```

### Step 4: Model Access Control
```python
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

class ModelAccessController:
    """Control access to LLM models based on permissions."""

    MODEL_PERMISSIONS = {
        "gpt-4o": Permission.MODEL_GPT4,
        "gpt-4o-mini": Permission.MODEL_GPT4_MINI,
        "claude-3-5-sonnet-20241022": Permission.MODEL_CLAUDE,
    }

    def __init__(self, user_store: UserStore):
        self.user_store = user_store

    def get_allowed_models(self, user_id: str) -> List[str]:
        """Get list of models user can access."""
        user = self.user_store.users.get(user_id)
        if not user:
            return []

        permissions = user.get_permissions()
        tenant = self.user_store.get_user_tenant(user_id)

        allowed = []
        for model, permission in self.MODEL_PERMISSIONS.items():
            if permission in permissions:
                # Also check tenant restrictions
                if tenant and tenant.allowed_models:
                    if model in tenant.allowed_models:
                        allowed.append(model)
                else:
                    allowed.append(model)

        return allowed

    def create_llm(self, user_id: str, model: str = None):
        """Create LLM instance with access control."""
        allowed = self.get_allowed_models(user_id)

        if not allowed:
            raise PermissionError("No model access")

        # Use requested model or default to first allowed
        model = model or allowed[0]

        if model not in allowed:
            raise PermissionError(f"Access denied to model: {model}")

        if model.startswith("gpt"):
            return ChatOpenAI(model=model)
        elif model.startswith("claude"):
            return ChatAnthropic(model=model)
        else:
            raise ValueError(f"Unknown model: {model}")
```

### Step 5: Tenant Isolation
```python
from langchain_core.callbacks import BaseCallbackHandler
from contextvars import ContextVar

# Context variable for current tenant
current_tenant: ContextVar[str] = ContextVar("current_tenant")

class TenantIsolationMiddleware:
    """Middleware to enforce tenant isolation."""

    def __init__(self, user_store: UserStore):
        self.user_store = user_store

    async def __call__(self, request: Request, call_next):
        user_id = request.state.user_id
        user = self.user_store.users.get(user_id)

        if user:
            # Set tenant context
            token = current_tenant.set(user.tenant_id)
            try:
                response = await call_next(request)
            finally:
                current_tenant.reset(token)
            return response

        return await call_next(request)

class TenantAwareCallback(BaseCallbackHandler):
    """Tag all LLM calls with tenant ID."""

    def on_llm_start(self, serialized, prompts, **kwargs):
        tenant_id = current_tenant.get(None)
        if tenant_id:
            # Add tenant to metadata for billing/logging
            kwargs.setdefault("metadata", {})["tenant_id"] = tenant_id

# Tenant-scoped data access
class TenantScopedVectorStore:
    """Vector store with tenant isolation."""

    def __init__(self, base_store):
        self.base_store = base_store

    def similarity_search(self, query: str, **kwargs):
        tenant_id = current_tenant.get()
        if not tenant_id:
            raise ValueError("Tenant context required")

        # Add tenant filter
        kwargs["filter"] = kwargs.get("filter", {})
        kwargs["filter"]["tenant_id"] = tenant_id

        return self.base_store.similarity_search(query, **kwargs)
```

### Step 6: Usage Quotas
```python
from datetime import datetime, timedelta
from collections import defaultdict

class UsageQuotaManager:
    """Manage usage quotas per user and tenant."""

    def __init__(self, user_store: UserStore):
        self.user_store = user_store
        self.usage = defaultdict(lambda: {"tokens": 0, "requests": 0})
        self.reset_time = {}

    def check_quota(self, user_id: str, tokens: int = 0) -> bool:
        """Check if user has available quota."""
        user = self.user_store.users.get(user_id)
        tenant = self.user_store.get_user_tenant(user_id)

        if not tenant:
            return False

        # Reset monthly quota if needed
        self._maybe_reset(tenant.id)

        current = self.usage[tenant.id]["tokens"]
        return (current + tokens) <= tenant.monthly_token_limit

    def record_usage(self, user_id: str, tokens: int) -> None:
        """Record token usage."""
        tenant = self.user_store.get_user_tenant(user_id)
        if tenant:
            self.usage[tenant.id]["tokens"] += tokens
            self.usage[tenant.id]["requests"] += 1

    def _maybe_reset(self, tenant_id: str) -> None:
        """Reset quota at start of month."""
        now = datetime.now()
        last_reset = self.reset_time.get(tenant_id)

        if not last_reset or last_reset.month != now.month:
            self.usage[tenant_id] = {"tokens": 0, "requests": 0}
            self.reset_time[tenant_id] = now

    def get_usage_report(self, tenant_id: str) -> dict:
        """Get usage report for tenant."""
        tenant = self.user_store.tenants.get(tenant_id)
        usage = self.usage[tenant_id]

        return {
            "tenant_id": tenant_id,
            "tokens_used": usage["tokens"],
            "tokens_limit": tenant.monthly_token_limit if tenant else 0,
            "requests": usage["requests"],
            "percentage_used": (usage["tokens"] / tenant.monthly_token_limit * 100) if tenant else 0
        }
```

## Output
- Permission model with roles
- User and tenant management
- Model access control
- Tenant isolation
- Usage quotas

## Resources
- [RBAC Best Practices](https://auth0.com/docs/manage-users/access-control/rbac)
- [Multi-Tenant Architecture](https://docs.microsoft.com/en-us/azure/architecture/guide/multitenant/)
- [OAuth 2.0 Scopes](https://oauth.net/2/scope/)

## Next Steps
Use `langchain-data-handling` for data privacy controls.
