# Playground Links And Url Encoding

## Playground Links and URL Encoding

When providing links to edit Mermaid diagrams in online playgrounds (like https://mermaid.live), you MUST properly URL-encode the diagram content, especially HTML entities like `<br/>` tags.

### Common Issue: Broken `<br/>` Tags

Mermaid diagrams use `<br/>` for line breaks in node text. These MUST be encoded properly in URLs.

**❌ BROKEN** (angle brackets not encoded):
```
https://mermaid.live/edit#pako:flowchart TD
    Start{Can decide<br/>in 3 seconds?}
```

**✅ CORRECT** (all characters properly encoded):
```
https://mermaid.live/edit#pako:flowchart%20TD%0A%20%20%20%20Start%7BCan%20decide%3Cbr%2F%3Ein%203%20seconds%3F%7D
```

### URL Encoding Rules

**IMPORTANT:** Despite earlier claims that "Mermaid 11.12.1+ fixed <br/> encoding", URL encoding is STILL REQUIRED for playground links to work correctly.

Use Python's `urllib.parse.quote()` with `safe=''` to encode ALL special characters:

```python
import urllib.parse

diagram = """flowchart TD
    Start{Can decide<br/>in 3 seconds?}"""

encoded = urllib.parse.quote(diagram, safe='')
url = f"https://mermaid.live/edit#pako:{encoded}"
```

#### Key encodings:
- `<` → `%3C`
- `>` → `%3E`
- `/` → `%2F`
- Space → `%20`
- Newline → `%0A`
- `{` → `%7B`
- `}` → `%7D`

### When Providing Playground Links

Always include properly encoded playground links in your diagram output:

```markdown