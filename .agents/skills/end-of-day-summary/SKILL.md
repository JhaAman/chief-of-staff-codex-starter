---
name: end-of-day-summary
description: Produce a concise weekday closeout from one bounded refresh of approved Chief of Staff sources and worker state.
---

# End-of-Day Summary

Perform one immediate bounded refresh of relevant approved Codex tasks and
authoritative Git branch or pull-request state before producing a closeout.
Treat the ledger, project notes, plans, and summaries as caches. If refresh is
unavailable, label the result `Last known`, state when it was checked, and name
the missing source.

After current blockers and user needs, inspect at most three recent
terminal-looking unarchived tasks using already available evidence. Apply the
proportional closure rule in `AGENTS.md`; runtime state alone never proves a
task terminal. Do not reopen long transcripts, rewrite history, bulk-archive,
or create routine user noise.

If nothing meaningful happened and nothing needs the user, produce no visible
summary. Otherwise use only populated sections, in this order:

1. `Needs you`
2. `Ready for colleagues`
3. `Completed`
4. `Next`

Use plain language and titled source links. Put every unresolved approval,
input, decision, access request, or interview wait under `Needs you`. Do not
send the summary externally without explicit approval. One immediate bounded
refresh is enough; never sleep or poll.
