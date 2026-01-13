---
name: detecting-data-anomalies
description: |
  Process identify anomalies and outliers in datasets using machine learning algorithms.
  Use when analyzing data for unusual patterns, outliers, or unexpected deviations from normal behavior.
  Trigger with phrases like "detect anomalies", "find outliers", or "identify unusual patterns".
allowed-tools: Read, Bash(cmd:*), Grep, Glob
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Detecting Data Anomalies

This skill provides automated assistance for detecting data anomalies tasks.

## Overview

This skill provides automated assistance for the described functionality.

## Prerequisites

Before using this skill, ensure you have:
- Dataset in accessible format (CSV, JSON, or database)
- Python environment with scikit-learn or similar ML libraries
- Understanding of data distribution and expected patterns
- Sufficient data volume for statistical significance
- Knowledge of domain-specific normal behavior
- Data preprocessing capabilities for cleaning and scaling

## Instructions

1. Load dataset using Read tool
2. Inspect data structure and identify relevant features
3. Clean data by handling missing values and inconsistencies
4. Normalize or scale features as appropriate for algorithm
5. Split temporal data if time-series analysis is needed
1. Apply selected algorithm using Bash tool
2. Generate anomaly scores for each data point
3. Classify points as normal or anomalous based on threshold
4. Extract characteristics of identified anomalies


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- Total data points analyzed
- Number of anomalies detected
- Contamination rate (percentage of anomalies)
- Algorithm used and configuration parameters
- Confidence scores for detected anomalies
- Record identifier and timestamp (if applicable)

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- Isolation Forest documentation and implementation examples
- One-Class SVM for novelty detection
- Local Outlier Factor (LOF) for density-based detection
- Autoencoder-based anomaly detection for deep learning approaches
- scikit-learn anomaly detection module