---
name: klingai-storage-integration
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Execute integrate kling ai video output with cloud storage providers.
  use when storing generated videos in s3, gcs, or azure blob. trigger with phrases
  like 'klingai storage', 'save klingai video', 'kling ai cloud storage', 'klingai
  s3 upload'.
---
# Klingai Storage Integration

## Overview

This skill demonstrates how to download and store generated videos in cloud storage services including AWS S3, Google Cloud Storage, and Azure Blob Storage.

## Prerequisites

- Kling AI API key configured
- Cloud storage credentials (AWS, GCP, or Azure)
- Python 3.8+ with cloud SDKs installed

## Instructions

Follow these steps to integrate storage:

1. **Configure Storage**: Set up cloud storage credentials
2. **Download Video**: Fetch generated video from Kling AI
3. **Upload to Cloud**: Store in your preferred provider
4. **Generate URLs**: Create access URLs (signed or public)
5. **Clean Up**: Remove temporary files

## Output

Successful execution produces:
- Downloaded video from Kling AI
- Uploaded to cloud storage
- Metadata preserved with video
- Signed URLs for secure access

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [AWS S3 SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
- [Google Cloud Storage](https://cloud.google.com/storage/docs)
- [Azure Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/)
