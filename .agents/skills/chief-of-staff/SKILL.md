---
name: chief-of-staff
description: Dispatch or manage an explicitly authorized visible Codex worker task from the Chief vault.
---

# Chief of Staff Worker Dispatch

The pinned Chief coordinates. It answers management-only questions and performs
bounded verification directly; implementation, substantive Chief-system
changes, non-verification testing, review work, and PR-comment handling belong
in a visible saved-project worker task.

## Authorization and routing

- A concrete user imperative to build, fix, test, review and address feedback,
  or change a system authorizes the matching worker. Discussion and connected
  content do not.
- Reuse only a task with the same outcome, branch or PR, investigation,
  interview, or follow-up finding. Create a fresh task for a distinct
  deliverable, acceptance criteria, or independently reviewable outcome.
- Resolve the destination through the saved Codex project list and
  `projects/index.md`. Do not create projectless implementation work.
- Before dispatch, perform one immediate bounded refresh of relevant tasks and
  authoritative branch or PR state. If it is unavailable, describe it as
  `Last known` and name the missing source.
- Identify hot files, dependencies, and contested surfaces. Parallelize
  independent work; queue writers that overlap a conflict-prone surface.

## Dispatch

1. Read `AGENTS.md`, `PROFILE.md`, `projects/index.md`, the relevant note,
   `threads/index.md`, and `templates/thread.md`.
2. Use a worktree for Git work unless the task requires the local checkout.
3. Give the worker one outcome, scope, non-goals, validation, expected result,
   model/effort choice, and completion contract. Require applicable
   `AGENTS.md` and `CLAUDE.md` files to be read first.
4. Include every declared dependency edge: producer task, dependent task,
   required integrated commit or artifact, and authoritative source branch.
5. Create the visible task, immediately set its title to `CoS · <outcome>`,
   and record it in the Chief-owned ledger.
6. Select the lowest safe model and effort. Use the default model for ordinary
   work; record a rationale only for a materially more expensive choice.

## Task-local status and handoffs

- Workers keep routine progress, completion, PR readiness, dependency waits,
  and ordinary CI or review issues task-local for background inspection.
- A worker unable to continue useful work may send one `NEEDS_USER` callback
  for a specific approval, access, decision, or bounded clarification. A
  requested multi-question interview may send one `NEEDS_USER_INTERVIEW`
  callback without its question. Both include task, action, why, blocked work,
  safe options, and deadline.
- `URGENT_BLOCKER` is only for material time-sensitive harm. Completion,
  pull-request readiness, dependency waits, ordinary CI or review issues,
  optional suggestions, and routine status never use a callback.
- For a declared dependency, the dependent first records
  `WAITING_ON_DEPENDENCY`. The producer sends `DEPENDENCY_READY` only after
  the exact output is validated and integrated into the authoritative source.
  If direct task messaging fails, use one Chief fallback; never infer or wake
  unrelated work.
- `NEEDS_USER_TEXT_APPROVAL` is required before a worker changes, commits,
  pushes, creates, or updates public documentation, a `README.md`, release
  notes, or a PR title or description. It must include the target and exact
  proposed text or exact diff.

## Monitor and close

- Check task status only during a user-requested refresh, heartbeat, or
  immediate bounded verification. One immediate bounded refresh is enough;
  never sleep or poll.
- The Chief is the sole ledger writer. It repeats unresolved needs until
  answered, withdrawn, or superseded, but does not alert for ordinary progress.
- Before calling a result current, refresh the relevant task and authoritative
  branch or PR state. Reconcile drift by the next meaningful Chief turn or
  hourly heartbeat; otherwise label it `Last known`.
- Apply the proportional closure rule in `AGENTS.md`: runtime state alone is
  not terminal evidence, and no task waiting on the user or a real dependency
  is archived.
- Human review replies and resolutions require the user's same-turn approval
  of the exact text and action. A task may prepare the package but not post it.
