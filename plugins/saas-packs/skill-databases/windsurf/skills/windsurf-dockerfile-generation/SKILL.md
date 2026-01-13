---
name: windsurf-dockerfile-generation
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Create optimized Dockerfiles with AI-driven best practices. Activate
  when users mention "create dockerfile", "container image", "docker optimization",
  "containerize application", or "docker best practices". Handles Docker configuration
  generation....
---
# Windsurf Dockerfile Generation

## Overview

This skill enables AI-assisted Docker configuration within Windsurf. Cascade analyzes your application to generate optimized Dockerfiles with multi-stage builds, minimal base images, proper layer caching, and security best practices. It supports Node.js, Python, Go, Java, and other common runtimes with framework-specific optimizations.

## Prerequisites

- Windsurf IDE with Cascade enabled
- Docker installed locally
- Application with defined dependencies
- Understanding of containerization concepts
- Target deployment environment defined

## Instructions

1. **Analyze Application**
2. **Select Base Image**
3. **Generate Dockerfile**
4. **Configure Security**
5. **Test and Validate**


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- Optimized production Dockerfile
- Development Dockerfile with dev tools
- docker-compose.yml for orchestration
- .dockerignore for build optimization

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Windsurf Docker Guide](https://docs.windsurf.ai/features/docker)
- [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Container Security Guide](https://docs.windsurf.ai/guides/container-security)
