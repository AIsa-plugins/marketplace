# AISA Plugins Marketplace

Public marketplace for agent plugins maintained by AISA.

## Available plugins

### AISA Research

Research a topic across Tavily web search, X/Twitter, YouTube, and Scholar,
then produce a structured brief with direct source links.

- Plugin: `aisa-research`
- Skill: `research-topic`
- Version: `0.1.0`
- Requirements: Python 3.9+ and an `AISA_API_KEY`

See [plugins/aisa-research](plugins/aisa-research) for configuration, usage,
and validation details.

## Install with Claude Code

```bash
claude plugin marketplace add AIsa-plugins/marketplace
claude plugin install aisa-research@aisa
```

Start a new Claude Code session, then try:

```text
Research the AI coding agent plugin market across web, X, YouTube, and Scholar.
Return a concise brief with source links.
```

Claude Code exposes the Skill as `/aisa-research:research-topic`.

## Install with Codex

```bash
codex plugin marketplace add AIsa-plugins/marketplace
codex plugin add aisa-research@aisa
```

Start a new Codex task after installation so bundled Skills are discovered.

## Repository layout

```text
.agents/plugins/marketplace.json     Codex marketplace
.claude-plugin/marketplace.json      Claude Code marketplace
plugins/aisa-research/               Shared plugin bundle
```

The plugin contains no API keys. Set `AISA_API_KEY` in the environment that
launches the agent. Do not commit `.env` files or credentials.
