---
name: check-in
description: Refresh approved Chief of Staff sources and current worker context.
---

# Check-In

Read `AGENTS.md`, `PROFILE.md`, `projects/index.md`, `sources/index.md`, the
relevant notes, and `threads/index.md`. Refresh only approved, relevant sources
and do one immediate bounded refresh of relevant task and branch or PR state.
Treat records as caches; if a source is unavailable, label it `Last known` and
name the missing source. Never sleep or poll.

Read Current Context by default. Consult History only for named work, projects,
or declared dependencies. Reconcile meaningful drift, including landed
dependencies, unresolved user needs, task completion, and PR state.

- Surface `NEEDS_USER` and `NEEDS_USER_INTERVIEW` first with the linked task
  and exact required action. Do not echo interview questions.
- Treat `WAITING_ON_DEPENDENCY` and `DEPENDENCY_READY` as background
  coordination unless the user must act. Require the exact integrated source
  and matching `DEPENDENCY_ACK` before calling a handoff consumed.
- Validate `TASK_COMPLETED` against the task's `Notify on completion` mode;
  otherwise surface routine completion in this check-in.
- Keep the visible result short: Needs you, **Big Changes**, relevant workers,
  source limits, and the smallest next action. Do not report ordinary progress
  or optional suggestions as alerts.

At the 13:00 heartbeat, review at most one Chief feature unused for 72 hours
and not already reminded during that unused stretch. Do not report that no
reminder is due.
