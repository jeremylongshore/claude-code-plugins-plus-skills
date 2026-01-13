---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Manage integrate MCP servers with Windsurf for extended capabilities.
  Activate when users mention "mcp integration", "model context protocol", "external
  tools", "mcp server", or "cascade tools". Handles MCP server configuration and integration.
  Us...
name: windsurf-mcp-integration
---
# Windsurf Mcp Integration

This skill provides automated assistance for windsurf mcp integration tasks.

## Overview

This skill enables integration of MCP (Model Context Protocol) servers with Windsurf, extending Cascade's capabilities with external tools and services. MCP allows Cascade to interact with databases, filesystems, APIs, and custom tools through a standardized protocol. Configure servers, manage permissions, and enable seamless tool access within your AI-assisted development workflow.

## Prerequisites

- Windsurf IDE with MCP support enabled
- Node.js 18+ or Python 3.10+ for MCP servers
- MCP server packages installed (npm or pip)
- Network access for remote MCP servers
- Understanding of MCP protocol basics
- Admin permissions for server configuration

## Instructions

1. **Enable MCP Servers**
2. **Configure Tools**
3. **Set Up Authentication**
4. **Test Integration**
5. **Deploy to Team**


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output

- Configured MCP servers accessible via Cascade
- Tool registry with all available operations
- Permission matrix for access control
- Audit logs for tool invocations

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [MCP Protocol Specification](https://modelcontextprotocol.io/docs)
- [Windsurf MCP Guide](https://docs.windsurf.ai/features/mcp)
- [MCP Server Development](https://modelcontextprotocol.io/docs/servers)