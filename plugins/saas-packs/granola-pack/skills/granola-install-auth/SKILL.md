---
name: granola-install-auth
description: |
  Install and configure granola ai meeting notes app with calendar integration. use when setting up granola for the first time, connecting calendar accounts, or configuring audio capture permissions. trigger with phrases like "install granola", "set...
allowed-tools: Read, Write, Edit, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Granola Install Auth

This skill provides automated assistance for granola install auth tasks.

## Prerequisites
- macOS 12+ or Windows 10+ (or iPhone for mobile)
- Google Calendar or Microsoft Outlook account
- Microphone permissions enabled
- Stable internet connection

## Instructions

1. Open Granola application
2. Click "Sign up" or "Log in"
3. Authenticate with Google or Microsoft account
4. Grant calendar access permissions
1. In Granola settings, go to "Integrations"
2. Connect Google Calendar or Outlook
3. Select which calendars to sync
4. Enable automatic meeting detection
1. Schedule a test meeting
2. Start the meeting
3. Confirm Granola shows "Recording" indicator


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Granola app installed and configured
- Calendar connected with meeting sync enabled
- Audio permissions granted
- Test meeting successfully captured

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Granola Download](https://granola.ai/download)
- [Granola Getting Started](https://granola.ai/help)
- [Granola Updates](https://granola.ai/updates)