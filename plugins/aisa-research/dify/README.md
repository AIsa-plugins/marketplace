# AISA Research

AISA Research adds five read-only research tools to Dify: web search, web
extraction, X/Twitter search, YouTube search, and scholarly literature search.
The tools return structured JSON with source links for use by Agents and
Workflows.

## Requirements

- A Dify installation that supports Python 3.12 plugins
- An AISA API key from <https://console.aisa.one>

## Setup

Install the plugin and enter your AISA API key when Dify requests provider
credentials. The key is sent only as a bearer credential to
`https://api.aisa.one` and is never included in tool output.

## Tools

- **Web Search** searches the public web for current sources.
- **Web Extract** extracts content from one to three public HTTP(S) URLs.
- **X/Twitter Search** searches public posts using an advanced query.
- **YouTube Search** finds relevant videos and channels.
- **Scholar Search** finds scholarly literature and supporting evidence.

Web Extract rejects local, private-network, credential-bearing, and non-HTTP(S)
URLs. A response is limited to 5 MiB.

## Development

Copy `.env.example` to `.env`, add the remote debugging credentials from your
Dify workspace, install dependencies, and start the plugin:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m main
```

Package it from the repository root with:

```bash
dify plugin package ./plugins/aisa-research/dify
```
