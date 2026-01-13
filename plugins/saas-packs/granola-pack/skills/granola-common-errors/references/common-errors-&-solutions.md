# Common Errors & Solutions

## Common Errors & Solutions

### Audio Issues

#### Error: "No Audio Captured"
**Symptoms:** Meeting recorded but transcript is empty
**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Wrong audio input | System Preferences > Sound > Input > Select correct device |
| Microphone muted | Check physical mute button on device |
| Permission denied | Grant microphone access in System Preferences |
| Virtual audio conflict | Disable conflicting audio software |

```bash
# Reset audio on macOS
sudo killall coreaudiod
```

#### Error: "Poor Transcription Quality"
**Symptoms:** Many errors in transcript
**Solutions:**
1. Use quality microphone or headset
2. Reduce background noise
3. Speak clearly and at moderate pace
4. Position microphone closer

### Calendar Sync Issues

#### Error: "Meeting Not Detected"
**Symptoms:** Granola doesn't auto-start for scheduled meeting
**Solutions:**

1. **Check calendar connection:**
   - Settings > Integrations > Calendar
   - Disconnect and reconnect

2. **Verify event visibility:**
   - Event must be on synced calendar
   - You must be an attendee
   - Event needs video link

3. **Force sync:**
   - Click sync button in Granola
   - Wait 30 seconds
   - Check if meeting appears

#### Error: "Calendar Authentication Failed"
**Symptoms:** Can't connect Google/Outlook calendar
**Solutions:**
```
1. Clear browser cache
2. Log out of Google/Microsoft account
3. Log back in
4. Try connecting Granola again
5. Use private/incognito browser window
```

### Processing Issues

#### Error: "Notes Not Appearing"
**Symptoms:** Meeting ended but no notes generated
**Solutions:**

| Timeframe | Action |
|-----------|--------|
| < 2 min | Wait - processing takes time |
| 2-5 min | Check internet connection |
| 5-10 min | Restart Granola app |
| > 10 min | Contact support |

#### Error: "Processing Failed"
**Symptoms:** Error message after meeting
**Causes:**
- Audio file corrupted
- Meeting too short (< 2 min)
- Server issues
- Storage full

**Solutions:**
1. Check Granola status page
2. Verify sufficient disk space
3. Try re-uploading if option available
4. Contact support with meeting ID

### Integration Issues

#### Error: "Zapier Connection Lost"
**Symptoms:** Automations not triggering
**Solutions:**
1. Open Zapier dashboard
2. Find Granola connection
3. Click "Reconnect"
4. Re-authorize access
5. Test Zap manually

#### Error: "Slack/Notion Sync Failed"
**Symptoms:** Notes not appearing in connected apps
**Solutions:**
1. Check integration status in Settings
2. Verify target workspace permissions
3. Re-authenticate if expired
4. Check target channel/database exists

### App Issues

#### Error: "App Won't Start"
**Solutions (macOS):**
```bash
# Force quit Granola
killall Granola

# Clear preferences (caution: resets settings)
rm -rf ~/Library/Preferences/com.granola.*
rm -rf ~/Library/Application\ Support/Granola

# Reinstall
brew reinstall granola
```

**Solutions (Windows):**
```
1. Task Manager > End Granola process
2. Settings > Apps > Granola > Repair
3. If fails, uninstall and reinstall
```

#### Error: "Update Failed"
**Solutions:**
1. Close Granola completely
2. Download latest from granola.ai/download
3. Install over existing version
4. Restart computer if needed