# Implementation Guide

### Step 1: System Information

#### macOS
```bash
# Create debug directory
mkdir -p ~/Desktop/granola-debug
cd ~/Desktop/granola-debug

# System info
sw_vers > system-info.txt
system_profiler SPHardwareDataType >> system-info.txt
system_profiler SPSoftwareDataType >> system-info.txt

# Audio configuration
system_profiler SPAudioDataType > audio-config.txt

# Display info
system_profiler SPDisplaysDataType > display-info.txt
```

#### Windows
```powershell
# Create debug directory
mkdir $env:USERPROFILE\Desktop\granola-debug
cd $env:USERPROFILE\Desktop\granola-debug

# System info
systeminfo > system-info.txt

# Audio devices
Get-WmiObject Win32_SoundDevice | Out-File audio-devices.txt
```

### Step 2: Granola Logs

#### macOS
```bash
# Granola application logs
cp -r ~/Library/Logs/Granola ./granola-logs 2>/dev/null

# Application support data (no sensitive data)
ls -la ~/Library/Application\ Support/Granola/ > app-support-listing.txt

# System logs related to Granola
log show --predicate 'process == "Granola"' --last 1h > system-logs.txt 2>/dev/null
```

#### Windows
```powershell
# Granola logs
Copy-Item "$env:LOCALAPPDATA\Granola\logs" -Destination ".\granola-logs" -Recurse

# Application event logs
Get-EventLog -LogName Application -Source "Granola" -Newest 100 | Out-File app-events.txt
```

### Step 3: Network Diagnostics
```bash
# Test Granola connectivity
curl -s -o /dev/null -w "%{http_code}" https://api.granola.ai/health > network-test.txt
curl -s -o /dev/null -w "%{http_code}" https://granola.ai >> network-test.txt

# DNS resolution
nslookup api.granola.ai >> network-test.txt 2>&1

# Trace route (optional, may take time)
traceroute -m 10 api.granola.ai >> network-test.txt 2>&1
```

### Step 4: Calendar Integration Status
```bash
# Create calendar status report
cat > calendar-status.txt << 'EOF'
Calendar Integration Checklist:

1. Calendar Provider: [Google/Outlook/Other]
2. Last Successful Sync: [Date/Time]
3. Connected Calendars: [List]
4. OAuth Token Status: [Valid/Expired/Unknown]
5. Permissions Granted: [Yes/No/Partial]

Recent Calendar Errors:
[Copy any errors from Granola settings]
EOF
```

### Step 5: Audio Configuration Check
```bash
# macOS audio test
cat > audio-check.txt << 'EOF'
Audio Configuration Report
==========================

Default Input Device: $(system_profiler SPAudioDataType | grep "Default Input" | head -1)

Input Devices Available:
$(system_profiler SPAudioDataType | grep -A5 "Input Source")

Audio Permissions:
- Granola has microphone access: [Yes/No]
- Other apps using microphone: [List]

Virtual Audio Software:
- Loopback: [Installed/Not Installed]
- BlackHole: [Installed/Not Installed]
- Other: [Specify]
EOF
```

### Step 6: Create Debug Bundle
```bash
# Package all diagnostics
cd ~/Desktop
zip -r granola-debug-$(date +%Y%m%d-%H%M%S).zip granola-debug/

echo "Debug bundle created: granola-debug-$(date +%Y%m%d-%H%M%S).zip"
echo "Send this file to help@granola.ai"
```