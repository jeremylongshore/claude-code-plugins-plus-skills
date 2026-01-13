---
name: supabase-data-handling
description: |
  Implement supabase pii handling, data retention, and gdpr/ccpa compliance patterns. use when handling sensitive data, implementing data redaction, configuring retention policies, or ensuring compliance with privacy regulations for supabase integra...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Supabase Data Handling

This skill provides automated assistance for supabase data handling tasks.

## Overview
Handle sensitive data correctly when integrating with Supabase.

## Prerequisites
- Understanding of GDPR/CCPA requirements
- Supabase SDK with data export capabilities
- Database for audit logging
- Scheduled job infrastructure for cleanup

## Data Classification

| Category | Examples | Handling |
|----------|----------|----------|
| PII | Email, name, phone | Encrypt, minimize |
| Sensitive | API keys, tokens | Never log, rotate |
| Business | Usage metrics | Aggregate when possible |
| Public | Product names | Standard handling |

## PII Detection

```typescript
const PII_PATTERNS = [
  { type: 'email', regex: /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g },
  { type: 'phone', regex: /\b\d{3}[-.]?\d{3}[-.]?\d{4}\b/g },
  { type: 'ssn', regex: /\b\d{3}-\d{2}-\d{4}\b/g },
  { type: 'credit_card', regex: /\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b/g },
];

function detectPII(text: string): { type: string; match: string }[] {
  const findings: { type: string; match: string }[] = [];

  for (const pattern of PII_PATTERNS) {
    const matches = text.matchAll(pattern.regex);
    for (const match of matches) {

## Detailed Reference

See `{baseDir}/references/implementation.md` for complete data handling guide.