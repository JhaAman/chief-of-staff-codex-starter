# Worker Task Index

Do not add sample history. Record a worker only after the user explicitly
authorizes it and the task is created. Use `Chief-created` for a task created
by the Chief and `manual` for the fallback the user creates themselves.

For an unresolved user approval, input, access, or decision, set State to
`Waiting for user — <exact approval or input>`, not vague `Blocked`. Clear it
only after the Chief relays the user's answer to the worker. Check-ins and
heartbeats scan every approved, non-archived row with this state regardless of
the runtime task status; ignore archived or cancelled work.

Workers record task-local status and final reports; the Chief alone writes this
ledger. In user-facing reports, reference a known task from this index as
`[Task title](codex://threads/<thread-id>)`; if its ID is absent, say its link
is pending. Do not present only a raw task ID.

| Task | Origin | Project | Outcome | State | Codex task link | Worktree or branch | Pull request | Last checked | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
