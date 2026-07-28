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
- `URGENT_BLOCKER` is reserved for material time-sensitive harm and includes
  task, action, harm, safe options, and deadline. Never use a callback for
  completion, pull-request readiness, dependency or capacity waits, normal CI
  or review issues, optional suggestions, or ordinary status.
- For a declared unavailable dependency, record `WAITING_ON_DEPENDENCY` once.
  Send `DEPENDENCY_READY` only after the exact required output is validated and
  integrated into the authoritative branch. Do not infer or wake unrelated
  work.
- Before changing, committing, pushing, creating, or updating a `README.md`,
  public or user documentation, release notes, or a pull-request title or
  description, record `NEEDS_USER_TEXT_APPROVAL` with the target and exact
  proposed text or exact diff. Wait for approval. Exact user text may proceed
  only unchanged.
- Do not install or connect apps, change automations, send external messages,
  post comments, merge, deploy, delete, or force-push without explicit
  authorization for that action.

## Completion report

Return one task-local terminal candidate: `COMPLETED`, `ABANDONED`, or
`SUPERSEDED`. Include the linked task, result or stop reason, important
artifacts, validated commit and branch when applicable, validation and current
checks, remaining risks, exact user action or `None`, whether merge/deploy/build
remains, and any blocker or dependency.

Use `templates/worker-summary.md` for important, reusable, or decision-bearing
work. The Chief chooses a proportional closure lane and archives only after
direct evidence shows the task is terminal.
