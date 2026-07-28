---
name: token-usage
description: Generate a privacy-safe token and API-equivalent cost summary from local Codex state. Use when the user asks for token usage, this week, the last four weeks, all time, recent complete-week comparisons, model or effort breakdowns, cache usage, or estimated cost.
---

# Token Usage

Run a fresh summary from the starter root:

```sh
python3 tools/token_usage.py summary --scope <scope>
```

Map requests to `this-week` (default), `last-four-weeks`, `all-time`, or
`compare-recent-weeks`. Run `report` instead of `summary` only when a Markdown
and JSON artifact is requested.

Keep the compact output intact: one estimate note before the first dollar,
one bold actual-cash line, three accounting bullets, then weekly, model/effort,
and activity tables with an `Estimated Cost` column. Explain the
API-rate counterfactual once, not in every cell. Never infer a cash charge,
subscription fee, or credit spend from a plan or balance snapshot.

Before adding model prices, review the official source, preserve its URL and
effective date in `reports/usage/pricing.json`, and set a short expiry. Price
only exact model names. Keep unknown or stale entries unpriced, including in
every table and comparison.

Never expose prompts, responses, task titles, IDs, source content, rollout
paths, credentials, or local account details.
