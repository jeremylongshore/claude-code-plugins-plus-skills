# Examples

### Quick Variant Check
```bash
# Count team size and DAU to select variant
echo "Team: $(git log --format='%ae' | sort -u | wc -l) developers"
echo "DAU: Check analytics dashboard"
```