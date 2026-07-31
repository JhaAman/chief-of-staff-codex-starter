# Worker Task Index

The Chief is the only ledger writer. Record a worker only after the user
authorizes it and the visible task exists. Workers keep routine progress,
dependencies, and completion evidence task-local.

## Current Context

Keep only active, waiting, externally blocked, or otherwise genuinely current
tasks here. Default check-ins and overviews read this section. Set `Notify` to
`Blockers only` unless a high-priority task is actively awaited, in which case
use `Notify on completion`.

| Task | Origin | Project | Outcome | State | Notify | Codex task link | Worktree or branch | Pull request | Last checked | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## History

Keep every other linked result here with enough context to be understandable.
History is consulted for named tasks, projects, and dependencies; moving a row
here never archives its Codex desktop task.

| Task | Origin | Project | Outcome | State | Notify | Codex task link | Worktree or branch | Pull request | Last checked | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
