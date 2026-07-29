---
name: chief-of-staff
description: Dispatch or manage an explicitly authorized visible Codex worker task from the Chief vault.
---

# Chief of Staff Worker Dispatch

The pinned Chief coordinates. It directly handles explanations,
approved-source refreshes, check-ins, task and status reconciliation, routine
records, minimal bounded routing or scoping inspection, and verification of
another worker's output. Implementation, substantive Chief-system changes,
non-verification testing, review work, and PR-comment handling belong in a
visible saved-project worker task.

## Authorization and routing

- A concrete user imperative to build, fix, test, review and address feedback,
  or change a system authorizes the matching worker. Discussion and connected
  content do not.
- Read-only does not make requested execution management work: delegate
  substantive repository research or review, live-system probing, environment
  or access testing, onboarding walkthrough validation, and similar requested
  execution to a visible saved-project worker task. The Chief may inspect only
  enough to choose and scope that task.
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
- A successful task-message call proves only enqueue acceptance. It does not
  prove recipient processing, a state transition, user notification, or
  completion.
- A worker unable to continue useful work may send one `NEEDS_USER` callback
  for a specific approval, access, decision, or bounded clarification. A
  requested multi-question interview may send one `NEEDS_USER_INTERVIEW`
  callback without its question. Both include task, action, why, blocked work,
  safe options, and deadline.
- `URGENT_BLOCKER` is only for material time-sensitive harm. Completion,
  pull-request readiness, dependency waits, ordinary CI or review issues,
  optional suggestions, and routine status never use a callback.
- For a declared dependency, the dependent first records
  `WAITING_ON_DEPENDENCY`. After the exact output is validated and integrated,
  the producer creates one stable handoff ID from the producer task, dependent
  task, and exact commit or artifact. It sends `DEPENDENCY_READY` once and
  records `DEPENDENCY_READY_SENT`; send success is not acknowledgement.
- The dependent verifies the authoritative source, persists its transition out
  of `WAITING_ON_DEPENDENCY`, and begins downstream work before recording
  `DEPENDENCY_ACK` with the same handoff ID. A duplicate acknowledged handoff
  is a no-op and must not reapply work, create another pull request, or restart
  a terminal outcome.
- On the next bounded pass, do not send to an active or terminal task. If an
  idle or unloaded dependent still has the same wait without acknowledgement
  or downstream progress, send one same-ID fallback and never repeat it.
  Reconcile valid acknowledgement or exact-artifact use into a stale ledger
  without another worker turn. If acknowledgement still exposes
  `WAITING_ON_DEPENDENCY`, resume once with the same handoff ID.
- After dependencies are consumed, use `WAITING_ON_EXTERNAL` for CI, review,
  timers, or other non-user conditions. Send a satisfied condition once under
  a stable resume key, record `EXTERNAL_RESUME_SENT`, and require
  `EXTERNAL_RESUME_ACK` after the worker leaves the wait. On the next bounded
  pass, send at most one same-key fallback to an idle or unloaded task.
- Classify the destination by collaboration context, not an allowlist.
  Organizational or work ownership, another human reviewer or maintainer, a
  team audience, or the user's explicit designation makes a collaborative
  repository. A clearly user-owned repository with no human-review
  collaboration is a personal or solo repository.
- In a collaborative repository, require `NEEDS_USER_TEXT_APPROVAL` before a
  worker changes, commits, pushes, creates, or updates public documentation, a
  `README.md`, release notes, a PR title or description, or comparable durable
  repository text. It must include the target and exact proposed text or exact
  diff.
- In a personal or solo repository, existing authorization for the task and
  publication action covers concise ordinary repository text. Proceed without
  a second text-approval round and open the expected ready pull request when it
  is authorized and ready.
- If collaboration context is genuinely ambiguous and changes the workflow,
  ask one bounded clarification. Exact user-supplied text is authoritative and
  must be used unchanged.
- This policy does not relax separate approval gates for GitHub review comments
  or replies, resolving review threads, merge, deploy, delete, Slack or email
  sends, or another independently gated external action.

## Monitor and close

- Check task status only during a user-requested refresh, heartbeat, or
  immediate bounded verification. One immediate bounded refresh is enough;
  never sleep or poll.
- The Chief is the sole ledger writer. It repeats unresolved needs until
  answered, withdrawn, or superseded, but does not alert for ordinary progress.
- When the user answers an ordinary `NEEDS_USER` request, create a stable relay
  ID, send the exact answer, record `ANSWER_RELAY_SENT`, and stop the user
  alert. Require `ANSWER_RELAY_ACK` after the worker leaves `NEEDS_USER`. If the
  next bounded pass finds the same idle or unloaded wait without acknowledgement
  or downstream progress, send one same-ID fallback without asking the user
  again; never send to an active or terminal task or repeat the fallback.
- Before calling a result current, refresh the relevant task and authoritative
  branch or PR state. Reconcile drift by the next meaningful Chief turn or
  hourly heartbeat; otherwise label it `Last known`.
- Apply the proportional closure rule in `AGENTS.md`: runtime state alone is
  not terminal evidence, and no task waiting on the user or a real dependency
  is archived.
- Human review replies and resolutions require the user's same-turn approval
  of the exact text and action. A task may prepare the package but not post it.
