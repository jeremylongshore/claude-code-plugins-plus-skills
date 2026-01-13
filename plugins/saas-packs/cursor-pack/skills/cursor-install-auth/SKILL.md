---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Install cursor ide and configure authentication. triggers on "install
  cursor", "setup cursor", "cursor authentication", "cursor login", "cursor license".
  use when working with cursor install auth functionality. trigger with phrases like
  "cursor in...
name: cursor-install-auth
---
# Cursor Install Auth

This skill provides automated assistance for cursor install auth tasks.

## Overview

This skill guides you through installing Cursor IDE and configuring authentication. It covers installation on macOS, Linux, and Windows, plus sign-in options, license activation, and API key configuration for custom model access.

## Prerequisites

- Supported operating system (macOS, Linux, or Windows)
- Internet connection for download and authentication
- Admin rights for installation (if required)
- Optional: API keys for custom model access

## Instructions

1. Download Cursor from cursor.com or package manager
2. Install using platform-specific method
3. Launch Cursor and click "Sign In"
4. Choose authentication method (GitHub, Google, Email)
5. Complete OAuth flow in browser
6. Return to Cursor - automatically authenticated

## Output

- Installed Cursor IDE
- Authenticated user account
- Activated license (Free, Pro, or Business)
- Ready-to-use AI features

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Cursor Download](https://cursor.com/download)
- [System Requirements](https://cursor.com/docs/requirements)
- [Cursor Pricing](https://cursor.com/pricing)
- [Account Settings](https://cursor.com/settings)