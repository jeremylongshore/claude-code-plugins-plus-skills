# Implementation Guide

### Step 1: Environment Configuration Structure
```
config/
├── base.yaml                # Shared configuration
├── development.yaml         # Development overrides
├── staging.yaml            # Staging overrides
├── production.yaml         # Production overrides
└── settings.py             # Configuration loader
```

### Step 2: Create Base Configuration
```yaml
# config/base.yaml
app:
  name: langchain-app
  version: "1.0.0"

llm:
  max_retries: 3
  request_timeout: 30

logging:
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  date_format: "%Y-%m-%d %H:%M:%S"

cache:
  enabled: true
  ttl_seconds: 3600
```

### Step 3: Environment-Specific Overrides
```yaml
# config/development.yaml
extends: base

app:
  debug: true

llm:
  provider: openai
  model: gpt-4o-mini
  temperature: 0.7
  # Use lower tier in dev

logging:
  level: DEBUG

cache:
  type: memory
  # In-memory cache for local dev

langsmith:
  tracing: true
  project: langchain-dev
```

```yaml
# config/staging.yaml
extends: base

app:
  debug: false

llm:
  provider: openai
  model: gpt-4o-mini
  temperature: 0.5

logging:
  level: INFO

cache:
  type: redis
  url: ${REDIS_URL}  # From environment

langsmith:
  tracing: true
  project: langchain-staging
```

```yaml
# config/production.yaml
extends: base

app:
  debug: false

llm:
  provider: openai
  model: gpt-4o
  temperature: 0.3
  max_retries: 5
  request_timeout: 60

logging:
  level: WARNING

cache:
  type: redis
  url: ${REDIS_URL}

langsmith:
  tracing: true
  project: langchain-production

monitoring:
  prometheus: true
  sentry: true
```

### Step 4: Configuration Loader
```python
# config/settings.py
import os
from pathlib import Path
from typing import Any, Dict, Optional
import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

class LLMConfig(BaseModel):
    provider: str = "openai"
    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_retries: int = 3
    request_timeout: int = 30

class CacheConfig(BaseModel):
    enabled: bool = True
    type: str = "memory"
    url: Optional[str] = None
    ttl_seconds: int = 3600

class LangSmithConfig(BaseModel):
    tracing: bool = False
    project: str = "default"

class Settings(BaseSettings):
    environment: str = Field(default="development", env="ENVIRONMENT")
    llm: LLMConfig = Field(default_factory=LLMConfig)
    cache: CacheConfig = Field(default_factory=CacheConfig)
    langsmith: LangSmithConfig = Field(default_factory=LangSmithConfig)

    class Config:
        env_file = ".env"

def load_config(environment: str = None) -> Settings:
    """Load configuration for specified environment."""
    env = environment or os.environ.get("ENVIRONMENT", "development")
    config_dir = Path(__file__).parent

    # Load base config
    config = {}
    base_path = config_dir / "base.yaml"
    if base_path.exists():
        with open(base_path) as f:
            config = yaml.safe_load(f) or {}

    # Load environment-specific overrides
    env_path = config_dir / f"{env}.yaml"
    if env_path.exists():
        with open(env_path) as f:
            env_config = yaml.safe_load(f) or {}
            config = deep_merge(config, env_config)

    # Resolve environment variables
    config = resolve_env_vars(config)

    return Settings(**config)

def deep_merge(base: Dict, override: Dict) -> Dict:
    """Deep merge two dictionaries."""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def resolve_env_vars(config: Any) -> Any:
    """Resolve ${VAR} patterns in config values."""
    if isinstance(config, dict):
        return {k: resolve_env_vars(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [resolve_env_vars(v) for v in config]
    elif isinstance(config, str) and config.startswith("${") and config.endswith("}"):
        var_name = config[2:-1]
        return os.environ.get(var_name, "")
    return config

# Global settings instance
settings = load_config()
```

### Step 5: Environment-Aware LLM Factory
```python
# infrastructure/llm_factory.py
from config.settings import settings
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.language_models import BaseChatModel

def create_llm() -> BaseChatModel:
    """Create LLM based on environment configuration."""
    llm_config = settings.llm

    if llm_config.provider == "openai":
        return ChatOpenAI(
            model=llm_config.model,
            temperature=llm_config.temperature,
            max_retries=llm_config.max_retries,
            request_timeout=llm_config.request_timeout,
        )
    elif llm_config.provider == "anthropic":
        return ChatAnthropic(
            model=llm_config.model,
            temperature=llm_config.temperature,
            max_retries=llm_config.max_retries,
        )
    else:
        raise ValueError(f"Unknown provider: {llm_config.provider}")
```

### Step 6: Environment-Specific Secrets
```python
# infrastructure/secrets.py
import os
from google.cloud import secretmanager

def get_secret(secret_id: str) -> str:
    """Get secret from appropriate source based on environment."""
    env = os.environ.get("ENVIRONMENT", "development")

    if env == "development":
        # Use local .env file in development
        return os.environ.get(secret_id, "")

    else:
        # Use Secret Manager in staging/production
        client = secretmanager.SecretManagerServiceClient()
        project_id = os.environ.get("GCP_PROJECT")
        name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
        response = client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")

# Usage
openai_key = get_secret("OPENAI_API_KEY")
```

### Step 7: Docker Compose for Local Environments
```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    environment:
      - ENVIRONMENT=development
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    ports:
      - "8080:8080"
    volumes:
      - ./src:/app/src
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  # Local development tools
  langsmith-proxy:
    image: langchain/langsmith-proxy:latest
    environment:
      - LANGCHAIN_API_KEY=${LANGCHAIN_API_KEY}
```