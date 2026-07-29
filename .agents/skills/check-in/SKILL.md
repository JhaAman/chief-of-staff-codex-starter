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
  user alert unless the user must act. A valid handoff names one stable handoff
  ID and an exact source already integrated into the authoritative branch.
  Record a successful send as `DEPENDENCY_READY_SENT`; enqueue acceptance is
  not recipient processing.
- Require `DEPENDENCY_ACK` with the same handoff ID after source verification.
  The acknowledgement includes the transition out of
  `WAITING_ON_DEPENDENCY`; an acknowledgement that still exposes the wait is
  incomplete. Exact downstream-use evidence for the same artifact also counts.
- During the bounded pass, do not send to an active dependent. If an idle or
  unloaded dependent still has the same wait without acknowledgement, verify
  the source and send one same-ID fallback. Record it so later passes never
  repeat it. If the dependent already completed the declared outcome, do not
  send or resume it; reconcile the terminal result.
- If acknowledgement or exact-artifact use exists while the ledger still says
  waiting, update the ledger without sending another worker turn. If
  `DEPENDENCY_ACK` exists but `WAITING_ON_DEPENDENCY` remains, resume once with
  the same handoff ID. Duplicate delivery after acknowledgement is a no-op.
- Keep later CI, review, timer, and other non-user waits separate as
  `WAITING_ON_EXTERNAL`. When the exact condition is satisfied, send one
  same-task continuation with its stable resume key and record
  `EXTERNAL_RESUME_SENT`. Require `EXTERNAL_RESUME_ACK` after leaving the wait.
  On the next bounded pass, send at most one same-key fallback to an idle or
  unloaded task; never send to an active or terminal task.
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
- After the user answers an ordinary request, create a stable relay ID, send
  the exact answer, record `ANSWER_RELAY_SENT`, and stop repeating the user
  alert. Require `ANSWER_RELAY_ACK` after the worker leaves `NEEDS_USER`. On the
  next bounded pass, send one same-ID fallback to an idle or unloaded worker
  still in the same request without asking the user again; never send to an
  active or terminal task or repeat the fallback.
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
