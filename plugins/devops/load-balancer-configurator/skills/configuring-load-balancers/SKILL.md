---
name: configuring-load-balancers
description: |
  Configure use when configuring load balancers including ALB, NLB, Nginx, and HAProxy. Trigger with phrases like "configure load balancer", "create ALB", "setup nginx load balancing", or "haproxy configuration". Generates production-ready configura...
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Configuring Load Balancers

This skill provides automated assistance for configuring load balancers tasks.

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure:
- Backend servers are identified with IPs or DNS names
- Load balancer type is determined (ALB, NLB, Nginx, HAProxy)
- SSL certificates are available if using HTTPS
- Health check endpoints are defined
- Understanding of traffic distribution requirements (round-robin, least-connections)
- Cloud provider CLI installed (if using cloud load balancers)

## Instructions

1. **Select Load Balancer Type**: Choose based on requirements (L4 vs L7, cloud vs on-prem)
2. **Define Backend Pool**: List backend servers with ports and weights
3. **Configure Health Checks**: Set check interval, timeout, and healthy threshold
4. **Set Up SSL/TLS**: Configure certificates and cipher suites
5. **Define Routing Rules**: Create path-based or host-based routing
6. **Enable Session Persistence**: Configure sticky sessions if needed
7. **Add Monitoring**: Set up logging and metrics collection
8. **Test Configuration**: Validate syntax and test traffic distribution

## Output

**Nginx Configuration:**
```nginx
# {baseDir}/nginx/load-balancer.conf

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- Nginx documentation: https://nginx.org/en/docs/
- HAProxy configuration guide: https://www.haproxy.org/
- AWS ALB documentation: https://docs.aws.amazon.com/elasticloadbalancing/
- GCP Load Balancing: https://cloud.google.com/load-balancing/docs
- Example configurations in {baseDir}/lb-examples/