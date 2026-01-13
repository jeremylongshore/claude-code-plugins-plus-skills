#!/usr/bin/env python3
"""
Migrate SKILL.md files to the 2025 schema.

Adds any missing required enterprise fields:
- allowed-tools (auto-detected from skill content)
- version (defaults to 1.0.0)
- author (defaults to Intent Solutions author string)
- license (defaults to MIT)

Also optionally enhances descriptions with clear trigger phrases.
"""

import os
import re
import sys
from pathlib import Path

# Keep defaults aligned with scripts/validate-skills-schema.py
DEFAULT_AUTHOR = "Jeremy Longshore <jeremy@intentsolutions.io>"
DEFAULT_LICENSE = "MIT"

# Tool categorization rules
TOOL_PATTERNS = {
    'read-only': 'Read, Grep, Glob',
    'code-editing': 'Read, Write, Edit, Grep, Glob, Bash(cmd:*)',
    'web-research': 'Read, WebFetch, WebSearch, Grep',
    'database': 'Read, Write, Grep, Bash(cmd:*)',
    'testing': 'Read, Grep, Glob, Bash(cmd:*)',
    'analysis': 'Read, Grep, Glob, Bash(cmd:*)',
    'deployment': 'Read, Write, Grep, Bash(cmd:*)',
    'documentation': 'Read, Write, Grep, Glob',
}

RE_FRONTMATTER = re.compile(r'^---\n(.*?)\n---\n(.*)$', re.DOTALL)

def detect_tool_category(skill_content, skill_name):
    """Auto-detect appropriate tool set based on skill description"""
    content_lower = skill_content.lower()

    # Detection patterns (order matters - most specific first)
    if 'web' in content_lower and ('research' in content_lower or 'fetch' in content_lower or 'search' in content_lower):
        return 'web-research'
    elif any(word in content_lower for word in ['edit', 'modify', 'refactor', 'generate', 'create', 'build']):
        return 'code-editing'
    elif 'test' in content_lower or 'spec' in content_lower:
        return 'testing'
    elif 'database' in content_lower or 'sql' in content_lower or 'query' in content_lower:
        return 'database'
    elif any(word in content_lower for word in ['deploy', 'release', 'pipeline', 'ci', 'cd']):
        return 'deployment'
    elif 'document' in content_lower or 'readme' in content_lower:
        return 'documentation'
    elif any(word in content_lower for word in ['analyze', 'detect', 'scan', 'monitor', 'audit', 'check']):
        return 'analysis'
    else:
        return 'read-only'  # Default to most restrictive

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown"""
    match = RE_FRONTMATTER.match(content)
    if not match:
        return None, None, None

    frontmatter_str = match.group(1)
    body = match.group(2)

    # Parse frontmatter manually (simple YAML parser)
    frontmatter = {}
    current_key = None
    current_value = []

    for line in frontmatter_str.split('\n'):
        if ':' in line and not line.startswith(' '):
            # Save previous key if exists
            if current_key:
                value = '\n'.join(current_value).strip()
                if value.startswith('|'):
                    value = value[1:].strip()
                frontmatter[current_key] = value

            # Parse new key
            key, val = line.split(':', 1)
            current_key = key.strip()
            current_value = [val.strip()] if val.strip() else []
        elif current_key and line.startswith(' '):
            # Continuation of multi-line value
            current_value.append(line.strip())
        elif line.strip():
            # Single line value
            if current_value:
                current_value[0] += ' ' + line.strip()

    # Save last key
    if current_key:
        value = '\n'.join(current_value).strip()
        if value.startswith('|'):
            value = value[1:].strip()
        frontmatter[current_key] = value

    return frontmatter, frontmatter_str, body

def reconstruct_frontmatter(frontmatter):
    """Reconstruct YAML frontmatter from dict"""
    lines = []

    # Order: name, description, allowed-tools, version, author, license
    if 'name' in frontmatter:
        lines.append(f"name: {frontmatter['name']}")

    if 'description' in frontmatter:
        desc = frontmatter['description']
        if '\n' in desc or len(desc) > 80:
            lines.append('description: |')
            for line in desc.split('\n'):
                lines.append(f"  {line}")
        else:
            lines.append(f"description: {desc}")

    if 'allowed-tools' in frontmatter:
        tools = str(frontmatter['allowed-tools']).strip()
        # Avoid unscoped Bash (warned by validator).
        tools = re.sub(r'(^|,\\s*)Bash(\\s*,|$)', r'\\1Bash(cmd:*)\\2', tools)
        lines.append(f"allowed-tools: {tools}")

    if 'version' in frontmatter:
        lines.append(f"version: {frontmatter['version']}")

    if 'author' in frontmatter:
        lines.append(f"author: {frontmatter['author']}")

    if 'license' in frontmatter:
        lines.append(f"license: {frontmatter['license']}")

    return '\n'.join(lines)

def enhance_description_with_triggers(description, skill_name):
    """Enhance description with clear trigger phrases if missing"""
    if not description:
        return description

    # Check if description already has trigger phrases
    trigger_indicators = [
        'use when', 'trigger', 'activate', 'invoke',
        'when you need to', 'when the user', 'when user'
    ]

    has_triggers = any(phrase in description.lower() for phrase in trigger_indicators)

    if has_triggers:
        return description  # Already has good trigger documentation

    # Extract skill purpose from name
    skill_words = skill_name.replace('-', ' ')

    # Add trigger phrase hint
    if '\n' in description:
        # Multi-line description - add trigger hint at end
        return description.strip() + f"\n\nUse this skill when you need to {skill_words} or when requesting \"{skill_words.replace('ing', '')}\"."
    else:
        # Single line - append inline
        return description.strip() + f" Activates when you request \"{skill_words}\" functionality."

def migrate_skill_file(file_path, dry_run=False):
    """Migrate a single SKILL.md file to 2025 schema"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return False

    frontmatter, original_fm, body = extract_frontmatter(content)

    if not frontmatter:
        print(f"⚠️  No frontmatter found: {file_path}")
        return False

    # Check if already migrated
    has_allowed_tools = 'allowed-tools' in frontmatter
    has_version = 'version' in frontmatter
    has_author = 'author' in frontmatter
    has_license = 'license' in frontmatter

    if has_allowed_tools and has_version and has_author and has_license:
        print(f"✅ Already migrated: {file_path}")
        return False

    changes = []

    # Add allowed-tools if missing
    if not has_allowed_tools:
        category = detect_tool_category(content, frontmatter.get('name', ''))
        frontmatter['allowed-tools'] = TOOL_PATTERNS[category]
        changes.append(f"allowed-tools ({category})")

    # Add version if missing
    if not has_version:
        frontmatter['version'] = '1.0.0'
        changes.append("version")

    # Add enterprise defaults
    if not has_author:
        frontmatter['author'] = DEFAULT_AUTHOR
        changes.append("author")

    if not has_license:
        frontmatter['license'] = DEFAULT_LICENSE
        changes.append("license")

    # Enhance description with trigger phrases
    if 'description' in frontmatter:
        original_desc = frontmatter['description']
        enhanced_desc = enhance_description_with_triggers(original_desc, frontmatter.get('name', ''))
        if enhanced_desc != original_desc:
            frontmatter['description'] = enhanced_desc
            changes.append("enhanced description")

    if not changes:
        print(f"ℹ️  No changes needed: {file_path}")
        return False

    # Reconstruct file
    new_frontmatter = reconstruct_frontmatter(frontmatter)
    new_content = f"---\n{new_frontmatter}\n---\n{body}"

    change_str = ', '.join(changes)
    print(f"🔧 Updating {file_path.name}: {change_str}")

    if not dry_run:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        except Exception as e:
            print(f"❌ Error writing {file_path}: {e}")
            return False

    return True

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Migrate SKILL.md files to 2025 schema')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without writing')
    parser.add_argument('--limit', type=int, help='Limit number of files to process')
    parser.add_argument(
        'path',
        nargs='?',
        default=None,
        help='Path to scan (defaults to repo root plugins/).',
    )
    parser.add_argument(
        '--include-standalone-skills',
        action='store_true',
        help='Also scan repo root skills/ directory.',
    )

    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    scan_roots = []

    if args.path:
        scan_roots.append(Path(args.path))
    else:
        scan_roots.append(repo_root / "plugins")
        if args.include_standalone_skills:
            scan_roots.append(repo_root / "skills")

    skill_files = []
    for root in scan_roots:
        if not root.exists():
            continue
        if root.name == "skills":
            skill_files.extend(root.rglob('*/SKILL.md'))
        else:
            skill_files.extend(root.rglob('skills/*/SKILL.md'))

    if args.limit:
        skill_files = skill_files[:args.limit]

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Found {len(skill_files)} SKILL.md files\n")

    migrated = 0
    skipped = 0
    errors = 0

    for skill_file in skill_files:
        result = migrate_skill_file(skill_file, dry_run=args.dry_run)
        if result:
            migrated += 1
        elif result is False:
            skipped += 1
        else:
            errors += 1

    print(f"\n{'=' * 60}")
    print(f"📊 Summary:")
    print(f"   ✅ Migrated: {migrated}")
    print(f"   ⏭️  Skipped (already done): {skipped}")
    print(f"   ❌ Errors: {errors}")
    print(f"{'=' * 60}")

    if args.dry_run:
        print("\n⚠️  This was a dry run. Use without --dry-run to apply changes.")
        return 0

    if migrated > 0:
        print(f"\n✅ Successfully migrated {migrated} skills to 2025 schema")
        print("\nNext steps:")
        print("  1. Review changes: git diff")
        print("  2. Validate: python3 scripts/validate-skills-schema.py")
        print("  3. Test: Select a few skills and verify activation")
        print("  4. Commit: git commit -am 'feat: migrate skills to 2025 schema'")

    return 0 if errors == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
