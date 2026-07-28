# Chief of Staff vault guide

Use this only after the initial interview. The pinned Chief task is the front
door; these files are its durable memory.

| Need | Use |
| --- | --- |
| Fresh status from approved sources | `$check-in` |
| Recorded portfolio snapshot, without live refresh | `$plan-overview` |
| Run a clearly authorized outcome | `$chief-of-staff` |
| Review an inactive scheduled refresh | `automations/heartbeat.md` |

## Vault map

- `PROFILE.md` — responsibilities, priorities, attention policy, and preferences.
- `projects/` — three to seven short active workstream notes.
- `plans/` — only work that needs sequencing beyond a project note.
- `sources/` — approved source scopes and their purpose.
- `threads/` — the Chief-owned index of visible worker tasks.
- `reports/workers/` — concise completed-worker handoffs.
- `check-ins/` — meaningful refresh snapshots, never copied source transcripts.
- `context-compaction-log.md` — metadata-only observability record.

## Private backup

After setup, create an empty **private** repository in the Git host you use,
verify its visibility, and add it as the `origin` remote. Routine vault changes
belong there. Never put personal project state, sources, people, task IDs, or
check-ins back into this public starter.

## Operating boundaries

The Chief uses visible saved-project tasks for implementation and substantive
changes. It records worker status from background inspection; ordinary waits,
completion, and CI do not interrupt you. A worker asks through the Chief for a
one-off decision, and may contact the Chief directly only for a time-sensitive
`URGENT_BLOCKER`. Human review comments and thread resolution always require
your same-turn approval of the exact text and action.

Read [AGENTS.md](AGENTS.md) for the complete operating contract.
