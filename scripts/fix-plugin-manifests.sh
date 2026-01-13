#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." &>/dev/null && pwd)"

if ! command -v jq >/dev/null 2>&1; then
  echo "ERROR: jq is required (brew install jq)" >&2
  exit 1
fi

echo "Fixing plugin manifests by removing invalid fields..."

plugins_dir="${1:-$REPO_ROOT/plugins}"
if [[ ! -d "$plugins_dir" ]]; then
  echo "ERROR: plugins dir not found: $plugins_dir" >&2
  exit 1
fi

# Find all plugin.json files with invalid fields
mapfile -t plugins < <(
  find "$plugins_dir" -name "plugin.json" -type f \
    -exec rg -l '"(category|enhances|requires)"\s*:' {} \;
)

count=0
for plugin in "${plugins[@]}"; do
  echo "Fixing: $plugin"
  tmp="${plugin}.tmp"
  jq 'del(.category, .enhances, .requires)' "$plugin" >"$tmp"
  mv "$tmp" "$plugin"
  count=$((count + 1))
done

echo "✅ Fixed $count plugin manifests"
