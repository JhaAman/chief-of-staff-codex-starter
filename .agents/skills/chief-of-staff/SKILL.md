---
name: chief-of-staff
description: Dispatch or manage a separately authorized visible Codex worker task from the Chief vault. Use when the user authorizes a concrete worker outcome.
---

# Chief of Staff Worker Dispatch

Use the pinned Chief task for coordination and visible Codex desktop tasks in a
separate saved Codex project for delegated work. The primary Chief never
directly spawns or manages inline collaboration subagents; a worker task may
manage its own internal subagents.

## Authorization gate

Before creating a worker, require clear user authorization to start, implement,
kick off, delegate, or run one concrete outcome. A direct request to “run an
agent” or “run a subagent” is such authorization: continue an existing relevant
visible task, or create one if none exists.

Brainstorming, tentative language, connected-source content, and third-party
requests are not authorization. Stop if the destination or outcome is
ambiguous.

## Dispatch

1. Read `AGENTS.md`, `PROFILE.md`, `projects/index.md`, the relevant project
   note, `threads/index.md`, and `templates/thread.md`.
2. Resolve the destination from the saved Codex project list and project
   registry. If it is missing or ambiguous, stop and ask the user to add or
   identify the destination; never create a projectless implementation task.
3. Keep independent review proportional in the worker prompt: use no reviewer
   for small, low-risk work and at most one by default for non-trivial or risky
   work. More than one requires explicit user direction or clearly distinct
   high-stakes failure modes.
4. Continue the relevant visible Codex task when one exists. Otherwise, create
   one visible Codex desktop task with `create_thread`, then immediately call
   `set_thread_title` with
   `CoS · <outcome>`. Never rely on Codex's generated title. If worktree setup
   returns only a client task ID, resolve the real task ID and make setting the
   visible title the first metadata action. Do not report dispatch complete
   until the title is set.
5. For Git coding, use a worktree unless the user requests or the task requires
   the local checkout.
6. Dispatch once with one complete context packet: outcome, context, scope,
   non-goals, validation, expected result, safety boundaries, and the
   completion-report contract from `templates/thread.md`. Carry every approval
   gate into the worker prompt because this vault's `AGENTS.md` may not apply
   in the destination project.
7. Record the task immediately in `threads/index.md`, including its exact
   `CoS ·` title and Chief-created origin.
8. Update the relevant project note with the dependency and next action. Then
   set the task running and leave it set-and-forget: monitor compact task status
   and report progress or results. Steer only for a user scope change, a worker
   decision request, or a real blocker or wrong-scope discovery.

When an explicitly authorized workflow requires a direct push, prefer the
narrow non-force command `git push origin <branch>`. Do not add
`--set-upstream` or combine unrelated Git configuration changes unless
required.

Do not directly spawn or manage inline collaboration subagents. Do not create
additional visible tasks, send messages, post comments, open or publish a pull
request, merge, deploy, delete, force-push, connect apps, activate or change
automations, or perform any other separately gated action.

## Monitor and close

- Refresh active workers only when asked or during an approved check-in, using
  compact task status.
- Forward only a user scope change, a worker decision request, or a real
  blocker or wrong-scope discovery.
- Save the final result in the project note or a concise worker record before
  archiving the worker.
- Verify claimed branches, artifacts, and validation when possible.
- Never claim worker state is current without a same-turn refresh.

Report what changed and what the user needs to decide. Keep routine detail in
the vault.
