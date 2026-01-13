# Complete Debug Bundle Script

## Complete Debug Bundle Script
```bash
#!/bin/bash
# collect-debug-bundle.sh

BUNDLE_DIR="deepgram-debug-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BUNDLE_DIR"

echo "Collecting Deepgram debug bundle..."

# 1. Environment info
./debug-env.sh > "$BUNDLE_DIR/environment.txt"

# 2. Connectivity test
./debug-connectivity.sh > "$BUNDLE_DIR/connectivity.txt"

# 3. Recent logs (sanitized)
grep -i deepgram /var/log/app/*.log 2>/dev/null | tail -100 > "$BUNDLE_DIR/app-logs.txt"

# 4. Audio file info (if provided)
if [ -n "$1" ]; then
  ./debug-audio.sh "$1" > "$BUNDLE_DIR/audio-analysis.txt"
fi

# 5. Package info
cat > "$BUNDLE_DIR/README.txt" << EOF
Deepgram Debug Bundle
Generated: $(date -u +%Y-%m-%dT%H:%M:%SZ)

Contents:
- environment.txt: System and SDK versions
- connectivity.txt: API connectivity tests
- app-logs.txt: Recent application logs
- audio-analysis.txt: Audio file details (if provided)

Issue Description:
[ADD YOUR ISSUE DESCRIPTION HERE]

Request IDs:
[ADD RELEVANT REQUEST IDS HERE]
EOF

# Create archive
tar -czf "$BUNDLE_DIR.tar.gz" "$BUNDLE_DIR"
echo "Debug bundle created: $BUNDLE_DIR.tar.gz"
```