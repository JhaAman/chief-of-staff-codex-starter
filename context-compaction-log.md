# Chief Context Compaction Log

Last updated: YYYY-MM-DD

This is a durable, metadata-only record of compactions affecting the primary
Chief task and later impacts credibly caused by bounded context. Do not copy raw
transcripts, replacement summaries, prompts, or secrets here.

## Classification and attribution

- **Observed:** explicit `compacted` or `context_compacted` platform metadata.
- **Strongly inferred:** both a new context-window lineage and
  compaction-produced replacement history, without an explicit marker.
- Do not infer compaction from token drops, summaries, omissions,
  contradictions, repeated work, or ordinary mistakes alone.
- Deduplicate events by platform window ID when available. State unknown
  measurements and retained or lost detail plainly.
- Record an impact only when concrete evidence links it to a logged event and
  supports the counterfactual that unbounded context likely would have
  prevented it.

## Observability fallback

No live compaction hook or subscriber is assumed. On the Chief's next turn,
manual check-in, or heartbeat, inspect newly available local metadata since the
last logged event. Quietly record raw events; do not alert the user for a raw
compaction event.

## Compaction events

| Log ID | Timestamp (UTC) | Status | Evidence | Window ID | Known measurements | Retained or lost detail | Follow-up |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Credibly attributable impacts

For each later impact, record:

- Impact ID and related log ID
- Discovery time and affected work
- Concrete symptom, evidence, and confidence
- Why unbounded context likely would have prevented it
- Remediation and resolution state
