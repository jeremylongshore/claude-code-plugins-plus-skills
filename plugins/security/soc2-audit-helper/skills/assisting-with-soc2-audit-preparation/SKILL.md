---
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
license: MIT
description: Execute automate soc 2 audit preparation including evidence gathering,
  control assessment, and compliance gap identification. use when you need to prepare
  for soc 2 audits, assess trust service criteria compliance, document security controls,
  or g...
name: assisting-with-soc2-audit-preparation
---
# Assisting With Soc2 Audit Preparation

This skill provides automated assistance for assisting with soc2 audit preparation tasks.

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure:
- Documentation directory accessible in {baseDir}/docs/
- Infrastructure-as-code and configuration files available
- Access to cloud provider logs (AWS CloudTrail, Azure Activity Log, GCP Audit Logs)
- Security policies and procedures documented
- Employee training records available
- Incident response documentation accessible
- Write permissions for audit reports in {baseDir}/soc2-audit/

## Instructions

1. Confirm scope (services, systems, period) and applicable SOC 2 criteria.
2. Gather existing controls, policies, and evidence sources.
3. Identify gaps and draft an evidence collection plan.
4. Produce an audit-ready checklist and remediation backlog.


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

The skill produces:

**Primary Output**: SOC 2 readiness report saved to {baseDir}/soc2-audit/readiness-report-YYYYMMDD.md

**Report Structure**:
```
# SOC 2 Readiness Assessment

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- AICPA Trust Service Criteria: https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/trustdataintegritytaskforce.html
- SOC 2 Compliance Checklist: https://secureframe.com/hub/soc-2/checklist
- CIS Controls: https://www.cisecurity.org/controls/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- Drata: SOC 2 compliance automation