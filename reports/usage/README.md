# Token usage reports

Run a fresh report from the starter root:

```sh
python3 tools/token_usage.py summary --scope this-week
python3 tools/token_usage.py report --output-stem week-ending-YYYY-MM-DD
```

Scopes are `this-week`, `last-four-weeks`, `all-time`, and
`compare-recent-weeks`. The tool reads local Codex counters and emits only
aggregates: no prompt, response, task title, identifier, or rollout path.

## Accounting boundary

- Cached input is already part of input; reasoning output is already part of
  output. Do not add either twice.
- API-equivalent cost is a counterfactual at published API rates, not a
  subscription charge or money paid.
- `config.json` records the selected marginal-usage convention, fixed fee, and
  authoritative cash evidence. Leave unknown values unknown.
- `pricing.json` starts empty deliberately. Add only exact-model rates from
  official pricing documentation, with source URL, effective date, retrieval
  time, and expiry. An expired cache makes every estimate unpriced.
