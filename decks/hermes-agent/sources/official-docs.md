# Source: Official Documentation — hermes-agent.nousresearch.com

**URL**: https://hermes-agent.nousresearch.com/docs  
**Fetched**: 2026-06-15

## Overview

Hermes Agent is an autonomous AI system developed by Nous Research that operates
independently across multiple platforms and environments, continuously improving
through built-in learning mechanisms.

## Key Capabilities

### Learning & Improvement
- "A closed learning loop" with agent-curated memory, autonomous skill development,
  and self-improvement during operation
- Cross-session recall using full-text search and language model summarization
- User modeling based on interaction patterns

### Deployment Flexibility
- Operates on local machines, Docker containers, SSH servers, or serverless
  platforms (Daytona, Modal)
- Accessible via 20+ messaging platforms including Telegram, Discord, Slack,
  WhatsApp, and Teams
- "Runs anywhere, not just your laptop"

### Technical Features
- 60+ integrated tools including web search, image generation, text-to-speech,
  and browser automation
- Model-agnostic architecture supporting Nous Portal, OpenRouter, OpenAI,
  and custom endpoints
- MCP (Model Context Protocol) server integration
- Scheduled automation with cron-based task execution
- Parallel processing through isolated sub-agents

## Installation

```bash
# One-command install
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Also available as desktop installer for Windows/macOS.

## Documentation Resources

- Machine-readable indexes: `/llms.txt` (~17 KB) and `/llms-full.txt` (~1.8 MB)
- Comprehensive guides covering configuration, security, voice modes, and memory systems
