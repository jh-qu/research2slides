# Source: DeepWiki — NousResearch/hermes-agent

**URL**: https://deepwiki.com/NousResearch/hermes-agent  
**Tool**: DeepWiki (code-level repo analysis)  
**Fetched**: 2026-06-15

## Project Introduction

Hermes Agent is "a self-improving AI agent framework built by Nous Research" that enables
autonomous operations through conversation loops, tool integration, and persistent memory.
The system bridges natural language intent to executable code across multiple deployment interfaces.

## Three-Tier Architecture

1. **User Interface Layer**: CLI, messaging platforms (Telegram, Discord, WhatsApp), web dashboard, editor integrations
2. **Agent Logic Layer**: Core `AIAgent` orchestration managing conversation iterations and tool dispatching
3. **Execution Layer**: Abstracted environments — local machines, Docker, SSH, Modal, Singularity containers

## Runtime Modes

| Mode | Entry Point | Context |
|------|-------------|---------|
| CLI | `cli.py` | Interactive terminal with TUI interface |
| Gateway | `gateway/run.py` | Multi-platform messaging support |
| ACP | Editor integration | Agent Client Protocol for VS Code/Zed |
| Web UI | Browser dashboard | Browser-based interaction |

## Core Components

**AIAgent Class** (`run_agent.py`) — orchestrates the conversation loop, managing iteration
budgets, function call handling, and state persistence.

**Tool System** (`model_tools.py`) — runtime tool discovery and registration; tools execute
within configurable execution environments specified in `config.yaml`.

## Memory and Self-Improvement

Closed learning loop enabling agents to create and refine their own capabilities:

- **Skills System**: Agents generate Python-based tools managed through `skill_manage`
- **Persistent Memory**: Long-term storage via `MEMORY.md` and `USER.md`
- **Honcho Integration**: AI-native memory management for cross-session recall

## Configuration Structure

All persistent data in `HERMES_HOME` (default: `~/.hermes/`):

| File | Purpose |
|------|---------|
| `config.yaml` | Model selection, terminal backend, toolset config |
| `.env` | API credentials and secrets |
| `SOUL.md` | Agent identity and persona definition |
| `auth.json` | OAuth tokens and provider authentication state |
