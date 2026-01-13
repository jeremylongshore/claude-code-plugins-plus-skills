# App Version Upgrades

## App Version Upgrades

### Check Current Version
```bash
# macOS - Check installed version
defaults read /Applications/Granola.app/Contents/Info.plist CFBundleShortVersionString

# Or in Granola app:
# Menu > About Granola
```

### Auto-Update Settings
```
Granola > Preferences > General
- Check for updates automatically: Enabled (recommended)
- Download updates in background: Enabled
- Notify before installing: Your preference
```

### Manual Update Process
```bash
# macOS via Homebrew
brew update
brew upgrade --cask granola

# Or download directly
open https://granola.ai/download

# Verify update
defaults read /Applications/Granola.app/Contents/Info.plist CFBundleShortVersionString
```

### Update Troubleshooting
```markdown