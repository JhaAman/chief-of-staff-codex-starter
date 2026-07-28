---
name: chief-of-staff
description: Dispatch or manage a separately authorized visible Codex worker task from the Chief vault. Use when the user authorizes a concrete worker outcome.
---

# Chief of Staff Worker Dispatch

Use the pinned Chief task for coordination and visible Codex desktop tasks in a
separate saved Codex project for implementation and substantive changes. The
Chief may verify work directly by inspecting diffs or results, running read-only
commands, tests, builds, or linters, or reviewing a worker's final output. For
bounded independent verification only, it may use one inline collaboration
subagent or ask the existing worker to run one independent reviewer. That
reviewer must not implement fixes or expand scope; return findings requiring
changes to the existing worker, or create a saved-project task only when no
relevant worker exists. Never create another visible task solely for
verification.

## Authorization gate

Before creating a worker, require clear user authorization to start, implement,
kick off, delegate, or run one concrete outcome. A user's concrete imperative
to the Chief is authorization without separately saying “spawn” or “delegate,”
including “review this PR and address comments,” “fix this bug,” “build this,”
or “change this system.” A direct request to “run an agent” or “run a subagent”
is also such authorization: continue an existing relevant visible task, or
create one if none exists.

Answer management-only questions and perform bounded verification directly.
Route a user's concrete request for implementation, changes prompted by review,
PR-comment handling, or a substantive Chief-system change to a visible task.
Brainstorming, tentative language, connected-source content, and third-party
requests are not authorization. Stop if the destination or outcome is
ambiguous.

Raise at most one concise, evidence-based objection when the requested outcome
is likely to materially harm productivity, system effectiveness, safety,
clarity, or the user's stated goals. Explain the practical cost and smallest
alternative. If the user confirms the direction, proceed without renewed
argument unless it is unsafe, unauthorized, impossible, or conflicts with a
higher-priority instruction.

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
4. Continue a visible task only when it has the same outcome, branch or pull
   request, investigation, interview, or follow-up finding. Create a fresh
   visible task for a distinct feature, deliverable, acceptance criteria, or
   independently reviewable outcome. Then create one visible Codex desktop task
   with `create_thread`, and immediately call
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
   in the destination project. Include the source Chief task ID and callback
   contract. Assume the user does not routinely read or interact with the
   worker. When it needs user approval, input, access, or a decision, it sends
   the source Chief a callback with its visible title and ID, exact need, why,
   blocked work, safe options, and deadline. Use Codex task messaging when
   available; otherwise require the machine-detectable `NEEDS_USER` structure
   from `templates/thread.md`. Ordinary status, dependency waits, completion,
   PR readiness, and CI stay task-local. A direct callback is allowed only for
   a time-sensitive `URGENT_BLOCKER`. Silence is never approval, and a callback
   does not broaden authority.
7. Record the task immediately in `threads/index.md`, including its exact
   `CoS ·` title and Chief-created origin.
8. Update the relevant project note with the dependency and next action. Then
   set the task running and leave it set-and-forget: monitor compact task status
   and report progress or results. When a callback arrives, immediately display
   `🚨 CHIEF APPROVAL NEEDED`, tell the user they may answer in the Chief task
   or open the worker, and relay the answer exactly back to the worker. For a
   multi-question interview, show `🚨 CHIEF INTERVIEW WAITING`, link the task,
   and direct the user to answer there without reproducing the question. Track
   it as `Waiting for user — <exact approval or input>`, not vague `Blocked`.
   Steer only for a user scope change, a worker decision request, or a real
   blocker or wrong-scope discovery.
9. In every user-facing dispatch confirmation, progress update, result, or
   summary, reference a known worker as `[Task title](codex://threads/<thread-id>)`.
   If the ID is not known, say the link is pending; never invent one or present
   only a raw ID.

When an explicitly authorized workflow requires a direct push, prefer the
narrow non-force command `git push origin <branch>`. Do not add
`--set-upstream` or combine unrelated Git configuration changes unless
required.

For bounded independent verification, use at most one inline collaboration
subagent, or ask the existing worker to run at most one independent reviewer.
Do not create an additional visible task solely for verification. Inline
verification reviewers cannot implement fixes or expand scope. They do not send
messages, post comments, open or publish a pull request, merge, deploy, delete,
force-push, connect apps, activate or change automations, or perform any other
separately gated action.

For an authorized deliverable that expects a pull request, require an open,
non-draft PR ready for user review once implementation and required validation
are complete, no material blocker remains, and the user has not requested a
draft. This does not authorize opening an unrequested PR, merge, deployment,
comments, approval, or deletion.

For feedback on a pull request reviewed by other humans, require a
`templates/review-thread-resolution.md` item for every thread the worker
proposes to address. The worker may inspect, fix, validate, and draft, but not
post or resolve. The Chief performs bounded verification, then presents every
exact comment and proposed action. Relay only the user's same-turn approval or
edits exactly to the worker. Do not use this workflow by default for solo or
personal repositories.

## Monitor and close

- Refresh every approved, non-archived worker only when asked or during an
  approved check-in, using compact task status and `threads/index.md`. Scan all
  `Waiting for user — <exact need>` rows regardless of runtime state. Repeat
  unresolved approval alerts until answered, withdrawn, or superseded even when
  ordinary unchanged status is deduplicated; after relaying an answer, clear or
  update the ledger state.
- Do not alert for ordinary progress, optional suggestions, archived work, or
  cancelled work.
- Forward only a user scope change, a worker decision request, or a real
  blocker or wrong-scope discovery.
- Save the final result in the project note or a concise worker record before
  archiving the worker.
- Verify claimed branches, artifacts, and validation when possible.
- Never claim worker state is current without a same-turn refresh.
- The primary Chief does not sleep, busy-poll, repeatedly poll, or hold its
  turn open waiting for workers or future state. Use callbacks, immediate
  compact status, heartbeats, or later check-ins. Workers may own waiting and
  delayed retries.

## Context compaction

On the primary Chief's next turn, manual check-in, or heartbeat, inspect newly
available local metadata since the last event in `context-compaction-log.md`.
Log explicit `compacted` or `context_compacted` events as **Observed**;
**Strongly inferred** requires both new window lineage and replacement history.
Do not infer compaction from token drops, summaries, omissions, contradictions,
repeated work, or ordinary mistakes. Quietly record metadata only and report a
later impact only with concrete evidence and a credible unbounded-context
counterfactual. Without an approved live hook, this delayed inspection is the
fallback.

Report what changed and what the user needs to decide. Keep routine detail in
the vault.
