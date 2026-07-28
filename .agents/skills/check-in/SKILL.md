---
name: check-in
description: Refresh approved Chief of Staff sources and worker state when the user requests a check-in or an approved heartbeat invokes it.
---

# Check-In

Perform one immediate bounded refresh of relevant approved Codex tasks and
authoritative Git branch or pull-request state before updating the vault,
calling touched state current, or recommending work.

## Scope and order

1. Before any live connector inspection, read `AGENTS.md`, `PROFILE.md`,
   `projects/index.md`, `sources/index.md`, relevant notes, and
   `threads/index.md`.
2. Refresh only source scopes listed in `sources/index.md` and relevant to
   named or active work.
3. Inspect every approved, non-archived task that could have changed or could
   still be waiting on the user, including idle, completed, and not-loaded
   runtime states. Read compact task-local status or final output, not full
   transcripts.
4. Check authoritative branch and PR state for touched work, then compare it
   with the ledger, notes, and previous meaningful check-in.
5. Inspect new local compaction metadata for the primary Chief task.

Treat the ledger, notes, plans, check-ins, and summaries as caches. If a source
cannot be refreshed, label the result `Last known`, include when it was checked,
and name the missing source. Never sleep, repeatedly poll, or hold the turn
open; one immediate bounded refresh is enough.

## Update and closure

- Update only meaningful status, ownership, risk, decision, blocker, or next
  action. Keep confirmed facts separate from inference.
- Reconcile drift: landed dependencies still shown as waiting, completed tasks
  shown as active, unresolved user needs, missing PR state, duplicate or
  superseded tasks, and producers that already handed off.
- Treat `WAITING_ON_DEPENDENCY` and `DEPENDENCY_READY` as coordination, not a
  user alert unless the user must act. Verify the exact integrated source before
  resuming a declared dependent.
- After current needs, inspect at most three recent terminal-looking unarchived
  tasks using already available evidence. Runtime state is not terminal proof.
  Apply the proportional closure lanes in `AGENTS.md`; leave missing evidence
  as `Closure pending — <exact missing evidence>` and never bulk-archive.
- Keep routine closure maintenance out of the visible report unless it changes
  an active project, exposes a meaningful result, or needs the user.

## Report

- Lead with a task-local `NEEDS_USER_TEXT_APPROVAL` by naming the exact target
  and reproducing the complete proposed text or exact diff unchanged.
- Lead with `🚨 CHIEF INTERVIEW WAITING` for a worker-owned interview; link the
  task and direct the user to answer there without reproducing its question.
- Lead with an unresolved ordinary need using `🚨 CHIEF APPROVAL NEEDED` or
  `🚨 CHIEF INPUT NEEDED`, the linked task, exact action, why, blocked work,
  safe options, and deadline.
- Keep the rest short: **Big Changes**, relevant workers, source limits, and
  the smallest next action. Use plain language and recognizable subjects.
- Do not alert for ordinary progress, optional suggestions, archived work, or
  completed work without an unresolved need.

## Heartbeat behavior

An approved heartbeat follows `automations/heartbeat.md`, stays read-oriented,
and may update routine vault records after the same bounded refresh. It does
not create workers, change automation, connect sources, or take external
actions. Target cache consistency by the next meaningful Chief turn or hourly
heartbeat; perfect instant freshness would require polling or noisy callbacks.
