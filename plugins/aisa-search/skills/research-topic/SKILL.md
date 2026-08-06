---
name: research-topic
description: Research a topic across current web results, X/Twitter posts, YouTube results, and Scholar sources through the AIsa API, then produce a structured brief with source links. Use when a user asks for multi-source research, market or trend research, evidence gathering, cross-source comparison, a cited research brief, or a deep research pass that extracts a few public web pages.
---

# Research Topic

Use the bundled `scripts/aisa_api.py` helper for every AIsa request. Do not call arbitrary API paths or add write operations.

## Prepare

1. Confirm `AISA_API_KEY` exists in the environment. Never print or persist it.
2. Resolve the plugin root from `PLUGIN_ROOT` in Codex or `CLAUDE_PLUGIN_ROOT` in Claude Code. If neither is set, resolve it from this `SKILL.md` location.
3. Split the topic into one to three concise search questions. Keep all searches focused on the user's original scope.
4. Use one query per source by default. Do not paginate unless the user asks for broader coverage.

Invoke the helper as:

```bash
python3 "<plugin-root>/scripts/aisa_api.py" <operation>
```

Pass one JSON object on stdin. The helper returns a JSON envelope on stdout and diagnostics on stderr.

## Search

Run these four read-only operations. Independent calls may run in parallel.

| Source | Operation | Default input |
| --- | --- | --- |
| Web | `tavily_search` | `{"query":"...","search_depth":"basic","max_results":5,"include_answer":false}` |
| X/Twitter | `twitter_advanced_search` | `{"query":"...","queryType":"Latest"}` |
| YouTube | `youtube_search` | `{"q":"...","gl":"us","hl":"en"}` |
| Scholar | `scholar_search_web` | `{"query":"...","max_num_results":5}` |

Adapt `gl`, `hl`, date filters, or X search operators when the user supplies a locale or time window. Keep the call count bounded and explain material cost expansion before making substantially more calls.

Treat each source independently. If one operation returns `ok: false`, record its source and error type, continue with successful sources, and do not invent missing evidence.

## Deep research

Only when the user explicitly asks for deep research, select at most three public HTTP(S) URLs from the web results and call `tavily_extract` with:

```json
{"urls":["https://example.com/a","https://example.com/b"],"extract_depth":"basic","format":"markdown"}
```

Never extract localhost, private-network, credential-bearing, or non-HTTP(S) URLs.

## Synthesize

Deduplicate by canonical URL first, then by near-identical title. Preserve source title, author or channel when available, publication time when available, and the original URL.

Return a concise report with:

1. **Executive summary** — answer the user's question directly.
2. **Key findings** — separate evidence from inference.
3. **Agreement and disagreement** — compare signals across source types.
4. **Open questions** — identify what remains unverified.
5. **Coverage** — list successful and unavailable sources.
6. **Sources** — provide direct Markdown links, grouped by Web, X, YouTube, and Scholar.

Never cite a URL that was not returned by a successful operation. Mark claims based on a single source, stale material, or weak social evidence accordingly.
