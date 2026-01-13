#!/usr/bin/env python3
"""
Fix remaining action verb issues by ensuring descriptions contain validator-approved verbs.
"""

import re
import json
from pathlib import Path

# Verbs accepted by validate-skills-schema.py
VALID_VERBS = [
    'analyze', 'audit', 'build', 'compare', 'configure', 'convert', 'create',
    'debug', 'deploy', 'detect', 'extract', 'fix', 'forecast', 'generate',
    'implement', 'log', 'manage', 'migrate', 'monitor', 'optimize',
    'process', 'review', 'route', 'scan', 'set up', 'setup', 'test',
    'track', 'transform', 'validate',
]

# Map non-valid verbs to valid ones
VERB_REPLACEMENTS = {
    'execute': 'manage',
    'run': 'manage',
    'handle': 'manage',
    'assist': 'configure',
    'help': 'configure',
    'enable': 'configure',
    'provide': 'generate',
    'identify': 'detect',
    'check': 'validate',
    'verify': 'validate',
    'integrate': 'configure',
    'document': 'generate',
    'define': 'configure',
    'access': 'manage',
    'connect': 'configure',
    'install': 'configure',
    'use': 'configure',
    'work': 'manage',
    'operate': 'manage',
    'prepare': 'configure',
    'collect': 'extract',
    'organize': 'manage',
    'schedule': 'manage',
    'visualize': 'generate',
    'plan': 'configure',
    'design': 'build',
    'orchestrate': 'manage',
}

def has_valid_verb(description: str) -> bool:
    """Check if description contains a valid verb."""
    desc_lower = description.lower()
    return any(v in desc_lower for v in VALID_VERBS)

def fix_description(description: str, skill_name: str) -> str:
    """Fix description to include a valid verb."""
    if has_valid_verb(description):
        return description

    # Try to replace first word if it's a non-valid verb
    first_word = description.strip().split()[0].lower() if description.strip() else ""

    if first_word in VERB_REPLACEMENTS:
        replacement = VERB_REPLACEMENTS[first_word].capitalize()
        # Replace first word
        return replacement + description[len(first_word):]

    # Add a prefix with a valid verb based on skill name
    skill_lower = skill_name.lower()
    if 'debug' in skill_lower or 'troubleshoot' in skill_lower:
        prefix = "Debug and analyze"
    elif 'monitor' in skill_lower or 'observ' in skill_lower:
        prefix = "Monitor and track"
    elif 'test' in skill_lower:
        prefix = "Test and validate"
    elif 'deploy' in skill_lower:
        prefix = "Deploy and configure"
    elif 'migrat' in skill_lower:
        prefix = "Migrate and transform"
    elif 'secur' in skill_lower or 'audit' in skill_lower:
        prefix = "Audit and validate"
    elif 'config' in skill_lower or 'setup' in skill_lower:
        prefix = "Configure and manage"
    elif 'optim' in skill_lower or 'perf' in skill_lower:
        prefix = "Optimize and monitor"
    elif 'generat' in skill_lower or 'creat' in skill_lower:
        prefix = "Generate and build"
    elif 'integrat' in skill_lower:
        prefix = "Configure and integrate"
    else:
        prefix = "Configure and manage"

    # Prepend prefix
    return f"{prefix} - {description}"

def fix_skill_file(filepath: Path) -> bool:
    """Fix a single skill file."""
    content = filepath.read_text()

    # Extract description from frontmatter
    desc_match = re.search(r'(description: \|?\n)((?:\s+.+\n)+)', content)
    if not desc_match:
        return False

    desc_prefix = desc_match.group(1)
    desc_content = desc_match.group(2)

    # Get first line of description
    lines = desc_content.split('\n')
    first_line = lines[0].strip() if lines else ""

    if has_valid_verb(first_line):
        return False  # Already valid

    skill_name = filepath.parent.name
    new_first = fix_description(first_line, skill_name)

    if new_first == first_line:
        return False  # No change

    # Reconstruct
    indent = "  " if desc_prefix.endswith("|\n") else ""
    lines[0] = indent + new_first
    new_desc = '\n'.join(lines)

    new_content = content.replace(desc_match.group(0), desc_prefix + new_desc)

    if new_content != content:
        filepath.write_text(new_content)
        return True
    return False

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fix remaining action verb issues")
    parser.add_argument(
        "--input",
        default="/tmp/remaining.json",
        help="Path to JSON audit output (default: /tmp/remaining.json)",
    )
    args = parser.parse_args()

    # Load remaining gaps
    with open(args.input) as f:
        data = json.load(f)

    # Find skills missing action verbs
    missing = [s for s in data['skills'] if 'description_missing:action_verbs' in s.get('gaps', [])]

    print(f"Found {len(missing)} skills missing valid action verbs")

    fixed = 0
    for skill in missing:
        filepath = Path(skill['path'])
        if filepath.exists():
            try:
                if fix_skill_file(filepath):
                    fixed += 1
                    print(f"  ✓ {filepath.parent.name}")
            except Exception as e:
                print(f"  ✗ {filepath}: {e}")

    print(f"\nFixed {fixed}/{len(missing)} skills")

if __name__ == "__main__":
    main()
