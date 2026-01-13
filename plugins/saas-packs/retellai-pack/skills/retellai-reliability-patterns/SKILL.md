---
allowed-tools: Read, Write, Edit
license: MIT
description: Implement retell ai reliability patterns including circuit breakers,
  idempotency, and graceful degradation. use when building fault-tolerant retell ai
  integrations, implementing retry strategies, or adding resilience to production
  retell ai servic...
name: retellai-reliability-patterns
---
# Retellai Reliability Patterns

This skill provides automated assistance for retellai reliability patterns tasks.

## Prerequisites
- Understanding of circuit breaker pattern
- opossum or similar library installed
- Queue infrastructure for DLQ
- Caching layer for fallbacks

## Instructions

### Step 1: Implement Circuit Breaker
Wrap Retell AI calls with circuit breaker.

### Step 2: Add Idempotency Keys
Generate deterministic keys for operations.

### Step 3: Configure Bulkheads
Separate queues for different priorities.

### Step 4: Set Up Dead Letter Queue
Handle permanent failures gracefully.

## Output
- Circuit breaker protecting Retell AI calls
- Idempotency preventing duplicates
- Bulkhead isolation implemented
- DLQ for failed operations

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Circuit Breaker Pattern](https://martinfowler.com/bliki/CircuitBreaker.html)
- [Opossum Documentation](https://nodeshift.dev/opossum/)
- [Retell AI Reliability Guide](https://docs.retellai.com/reliability)