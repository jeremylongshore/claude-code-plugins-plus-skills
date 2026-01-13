---
name: klingai-install-auth
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Execute set up kling ai api authentication and configure api keys. use
  when starting a new kling ai integration or troubleshooting auth issues. trigger
  with phrases like 'kling ai setup', 'klingai api key', 'kling ai authentication',
  'configure kl...
---
# Klingai Install Auth

## Overview

This skill guides you through obtaining and configuring Kling AI API credentials for video generation, setting up environment variables, and verifying your authentication is working correctly.

## Prerequisites

- Kling AI account (sign up at klingai.com)
- Python 3.8+ or Node.js 18+
- HTTP client library (requests, axios, or fetch)

## Instructions

Follow these steps to set up Kling AI authentication:

1. **Create Account**: Sign up at https://klingai.com
2. **Access API Settings**: Navigate to your account settings > API
3. **Generate API Key**: Create a new API key for your application
4. **Configure Environment**: Set up your environment variables
5. **Verify Setup**: Test your authentication with a simple request

## Output

Successful execution produces:
- Working Kling AI API authentication
- Verified API connectivity
- Account status and credit information

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Kling AI Documentation](https://docs.klingai.com/)
- [Kling AI API Reference](https://docs.klingai.com/api)
- [Kling AI Dashboard](https://klingai.com/dashboard)
