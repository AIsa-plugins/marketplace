# AIsa Plugins Marketplace

Public marketplace for agent plugins maintained by AIsa.

## Available plugins

### AIsa Search

Search a topic across Tavily web search, X/Twitter, YouTube, and Scholar,
then produce a structured brief with direct source links.

- Plugin: `aisa-search`
- Skill: `research-topic`
- Version: `0.1.1`
- Requirements: Python 3.9+ and an `AISA_API_KEY`

See [plugins/aisa-search](plugins/aisa-search) for configuration, usage,
and validation details.

## Install with Claude Code

```bash
claude plugin marketplace add AIsa-plugins/marketplace
claude plugin install aisa-search@aisa
```

Start a new Claude Code session, then try:

```text
Research the AI coding agent plugin market across web, X, YouTube, and Scholar.
Return a concise brief with source links.
```

Claude Code exposes the Skill as `/aisa-search:research-topic`.

## Install with Codex

```bash
codex plugin marketplace add AIsa-plugins/marketplace
codex plugin add aisa-search@aisa
```

Start a new Codex task after installation so bundled Skills are discovered.

## Develop for Dify

The Dify implementation is a host-specific Tool Plugin kept separate from the
shared Codex and Claude Code bundle. It provides web search, web extraction,
X/Twitter search, YouTube search, and Scholar search tools.

Package it with the Dify Plugin CLI:

```bash
dify plugin package ./plugins/aisa-search/dify
```

See [plugins/aisa-search/dify](plugins/aisa-search/dify) for setup and local
debugging.

## Repository layout

```text
.agents/plugins/marketplace.json     Codex marketplace
.claude-plugin/marketplace.json      Claude Code marketplace
plugins/aisa-search/                 Shared plugin bundle
plugins/aisa-search/dify/            Dify-specific Tool Plugin
```

The plugin contains no API keys. Set `AISA_API_KEY` in the environment that
launches the agent. Do not commit `.env` files or credentials.
