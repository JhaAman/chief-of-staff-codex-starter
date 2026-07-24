# Worker Task Index

Do not add sample history. Record a worker only after the user explicitly
authorizes it and the task is created. Use `Chief-created` for a task created
by the Chief and `manual` for the fallback the user creates themselves.

For an unresolved user approval, input, access, or decision, set State to
`Waiting for user — <exact approval or input>`, not vague `Blocked`. Clear it
only after the Chief relays the user's answer to the worker.

| Task | Origin | Project | Outcome | State | Codex task | Worktree or branch | Pull request | Last checked | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
