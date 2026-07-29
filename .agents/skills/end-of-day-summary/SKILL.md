---
name: end-of-day-summary
description: Produce a concise weekday closeout from one bounded refresh of approved Chief of Staff sources and worker state.
---

# End-of-Day Summary

Before any live connector inspection, read `AGENTS.md`, `PROFILE.md`,
`projects/index.md`, `sources/index.md`, relevant notes, and `threads/index.md`.
Inspect only source scopes listed in `sources/index.md` and relevant to active
work. Then perform one immediate bounded refresh of relevant approved Codex
tasks and authoritative Git branch or pull-request state before producing a closeout.
Treat the ledger, project notes, plans, and summaries as caches. If refresh is
unavailable, label the result `Last known`, state when it was checked, and name
the missing source.

After current blockers and user needs, inspect at most three recent
terminal-looking unarchived tasks using already available evidence. Apply the
proportional closure rule in `AGENTS.md`; runtime state alone never proves a
task terminal. Do not reopen long transcripts, rewrite history, bulk-archive,
or create routine user noise.

Apply the dependency state machine in `AGENTS.md`: send success is only
`DEPENDENCY_READY_SENT`; require `DEPENDENCY_ACK` or stronger exact-artifact
use; repair one idle unacknowledged wait with the same handoff ID; never resend
to active, acknowledged, or completed tasks; reconcile stale ledger state
without waking workers; and resume a satisfied `WAITING_ON_EXTERNAL` condition
once by its stable resume key.

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
