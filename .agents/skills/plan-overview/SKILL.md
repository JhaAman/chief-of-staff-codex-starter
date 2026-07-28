---
name: plan-overview
description: Summarize refreshed Chief of Staff project and worker state when the user asks what is in flight, blocked, or next.
---

# Plan Overview

Produce a concise portfolio snapshot after one immediate bounded refresh of the
relevant approved Codex tasks and authoritative Git branch or pull-request
state. Use `$check-in` when broader live-source refresh is needed.

Read `PROFILE.md`, `projects/index.md`, active project notes, plans,
`threads/index.md`, and relevant decisions as cached context, then cross-check
touched work against live task and branch or PR state. Runtime completed, idle,
or not-loaded is not terminal evidence. If refresh is unavailable, label the
result `Last known`, say when it was checked, and name the missing source.

Reconcile a landed dependency, completion, unresolved user action, PR-ready or
merged state, duplicate or superseded task, or producer handoff before calling
the result current. Target cache consistency by the next meaningful Chief turn
or hourly heartbeat. Do not sleep, poll, create workers, or send messages.

Use this table:

| Project | Status | Owner | Next action | Blocker or wait |
| --- | --- | --- | --- | --- |

Mention a closure gap only when it obscures an active project's result, owner,
blocker, or next action. Link known tasks with `codex://threads/<thread-id>`;
otherwise say the link is pending.
