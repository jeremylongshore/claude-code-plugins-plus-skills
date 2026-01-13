---
name: creating-kubernetes-deployments
description: |
  Deploy use when generating Kubernetes deployment manifests and services. Trigger with phrases like "create kubernetes deployment", "generate k8s manifest", "deploy app to kubernetes", or "create service and ingress". Produces production-ready YAML...
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Creating Kubernetes Deployments

This skill provides automated assistance for creating kubernetes deployments tasks.

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure:
- Kubernetes cluster is accessible and kubectl is configured
- Container image is built and pushed to registry
- Understanding of application resource requirements
- Namespace exists or will be created
- Ingress controller is installed (if using ingress)
- TLS certificates are available (if using HTTPS)

## Instructions

1. **Gather Requirements**: Application name, image, replicas, ports, environment
2. **Create Deployment**: Generate YAML with container spec and resource limits
3. **Add Health Checks**: Configure liveness and readiness probes
4. **Define Service**: Create ClusterIP, NodePort, or LoadBalancer service
5. **Configure Ingress**: Set up routing rules and TLS termination
6. **Add ConfigMaps/Secrets**: Externalize configuration and sensitive data
7. **Enable Auto-scaling**: Create HorizontalPodAutoscaler if needed
8. **Apply Manifests**: Use kubectl apply to deploy resources

## Output

**Deployment Manifest:**
```yaml
# {baseDir}/k8s/deployment.yaml

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- Kubernetes documentation: https://kubernetes.io/docs/
- kubectl reference: https://kubernetes.io/docs/reference/kubectl/
- Deployment best practices: https://kubernetes.io/docs/concepts/workloads/
- Example manifests in {baseDir}/k8s-examples/