# Codex Worker Tasks

`index.md` is the only durable task registry. Its **Current Context** is the
bounded default read; **History** preserves all other linked work for named
lookups. Moving a row to History does not archive the desktop task.

Use `Blockers only` by default. Use `Notify on completion` only when the Chief
records that work as high priority and the user is actively waiting for it.
For unresolved input, write `Waiting for user — <exact approval or input>`,
not a vague `Blocked`.
