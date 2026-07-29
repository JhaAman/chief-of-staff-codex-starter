# Codex Worker Record

- Authorized by:
- Authorization date: YYYY-MM-DD
- Authorization basis: direct concrete user request | explicit delegation
- Task:
- Visible title: CoS · <outcome>
- Source Chief task ID:
- Origin: Chief-created | manual
- Project and saved Codex project:
- Repository and base branch:
- Declared dependency handoff: None | <producer -> dependent -> required integrated commit or artifact -> authoritative branch>
- User-requested interview: None | <multi-question interview type>

## Outcome


## Scope

- _Define the authorized work._

## Non-goals

- _State exclusions explicitly._

## Validation

- _List acceptance criteria and commands._

## Expected result

- Branch or artifact:
- Pull-request expectation: none | prepared locally | explicitly authorized
- Expected PR state: non-draft ready for review | draft while incomplete | none
- Collaboration context: collaborative | solo | unclear
- Review or merge gate:

## Safety and coordination

- Read and follow applicable destination `AGENTS.md` files and repo-root
  `CLAUDE.md`, when present, before acting.
- Keep work to this outcome and validation contract. Report a distinct feature,
  deliverable, acceptance criteria, or parallelizable work instead of absorbing
  it.
- Do not edit `threads/index.md`; the Chief owns the ledger. Keep routine
  progress, dependency waits, completion, PR readiness, CI, and review status
  task-local for background inspection.
- For one approval, access request, decision, or bounded clarification that
  blocks useful work, record `NEEDS_USER` with task, action, why, blocked work,
  safe options, and deadline. Send at most one matching callback when the task
  system supports it.
- For a requested multi-question interview, use `NEEDS_USER_INTERVIEW`, ask one
  concise question at a time in this task, prefer native question UI when
  available, and never reproduce the question in a callback. Stay idle without
  polling between answers.
- A successful task-message call proves only enqueue acceptance. It does not
  prove the recipient processed the message, changed state, notified the user,
  or completed work.
- When the Chief relays an ordinary answer, apply its stable relay ID at most
  once. Record `ANSWER_RELAY_ACK` only after the exact answer moves this task
  out of `NEEDS_USER`. A duplicate acknowledged relay is a no-op; the Chief may
  send one same-ID fallback if the first enqueue produced no acknowledgement
  or downstream progress, but only while this task is idle or unloaded. An
  active or terminal task must not receive the fallback.
- `URGENT_BLOCKER` is reserved for material time-sensitive harm and includes
  task, action, harm, safe options, and deadline. Never use a callback for
  completion, pull-request readiness, dependency or capacity waits, normal CI
  or review issues, optional suggestions, or ordinary status.
- For a declared unavailable dependency, record `WAITING_ON_DEPENDENCY` once.
  After the exact output is validated and integrated into the authoritative
  branch, create one stable handoff ID from the producer task, dependent task,
  and exact commit or artifact. Inspect the dependent once; if it already
  completed the declared outcome, do not send or resume it.
- Send `DEPENDENCY_READY` once with the handoff ID, exact integrated source,
  validation evidence, and resume contract. Record `DEPENDENCY_READY_SENT`;
  send success does not prove consumption.
- On receipt, check the handoff ID first. Re-delivery of the same handoff ID is
  an idempotent no-op after acknowledgement or exact-artifact use; do not
  reapply work, create another pull request, or restart a terminal outcome.
- Verify the authoritative source, persist the state transition, and begin
  downstream work before recording `DEPENDENCY_ACK` with the same handoff ID.
  Valid acknowledgement includes the transition out of
  `WAITING_ON_DEPENDENCY`; acknowledgement that still exposes that wait is
  incomplete.
- If a direct send is not consumed, the next bounded Chief pass may send one
  fallback with the same handoff ID to this task only while it is idle or
  unloaded and still waiting. An active, acknowledged, or terminal task must
  not receive another send.
- After dependencies are consumed, use `WAITING_ON_EXTERNAL` for CI, review,
  timers, or other non-user conditions. Include one stable resume key, exact
  condition, and authoritative evidence source. Apply each resume key at most
  once and record `EXTERNAL_RESUME_ACK` only after leaving the wait. The Chief
  records `EXTERNAL_RESUME_SENT` and may send one same-key fallback if the
  first enqueue produced no acknowledgement or downstream progress, but only
  while this task is idle or unloaded. An active or terminal task must not
  receive the fallback.
- Classify the destination by collaboration context, not an allowlist.
  Organizational or work ownership, another human reviewer or maintainer, a
  team audience, or the user's explicit designation makes a collaborative
  repository. A clearly user-owned repository with no human-review
  collaboration is a personal or solo repository.
- In a collaborative repository, before changing, committing, pushing,
  creating, or updating a `README.md`, public or user documentation, release
  notes, changelogs, a pull-request title or description, or comparable
  durable repository text, record `NEEDS_USER_TEXT_APPROVAL` with the target
  and exact proposed text or exact diff. Wait for approval.
- In a personal or solo repository, existing authorization for the task and
  publication action covers concise ordinary repository text. Proceed without
  a second text-approval round and open the expected ready pull request when it
  is authorized and ready.
- If collaboration context is genuinely ambiguous and changes the workflow,
  ask one bounded clarification. Exact user-supplied text is authoritative and
  must be used unchanged.
- Do not install or connect apps, change automations, send external messages,
  post GitHub review comments or replies, resolve review threads, merge,
  deploy, delete, or force-push without explicit authorization for that action.

## Completion report

Return one task-local terminal candidate: `COMPLETED`, `ABANDONED`, or
`SUPERSEDED`. Include the linked task, result or stop reason, important
artifacts, validated commit and branch when applicable, validation and current
checks, remaining risks, exact user action or `None`, whether merge/deploy/build
remains, and any blocker or dependency.

Use `templates/worker-summary.md` for important, reusable, or decision-bearing
work. The Chief chooses a proportional closure lane and archives only after
direct evidence shows the task is terminal.
