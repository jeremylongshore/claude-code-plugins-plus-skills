# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Tool Not Found | Tool name mismatch | Verify tool names in prompt |
| Max Iterations | Agent stuck in loop | Increase limit or improve prompts |
| Parse Error | Invalid tool call format | Enable `handle_parsing_errors` |
| Tool Error | Tool execution failed | Add try/except in tool functions |