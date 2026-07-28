# Chief of Staff vault guide

Use this only after the initial interview. The pinned Chief task is the front
door; these files are its durable memory.

| Need | Use |
| --- | --- |
| Fresh status from approved sources | `$check-in` |
| Current portfolio snapshot | `$plan-overview` |
| Run a clearly authorized outcome | `$chief-of-staff` |
| Concise weekday closeout | `$end-of-day-summary` |
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

The Chief answers management-only questions and bounded verification. Visible
saved-project workers implement changes. It uses one bounded refresh of
relevant task and branch or pull-request state before calling status current,
or labels it **Last known** when refresh is unavailable. Routine worker status
is discovered in the background. A worker blocked on a user approval, access
request, decision, or bounded clarification may send one `NEEDS_USER`; a
requested multi-question interview may send one `NEEDS_USER_INTERVIEW`.
`URGENT_BLOCKER` is only for material time-sensitive harm. Human review
comments and thread resolution always require same-turn approval of the exact
text and action.

Read [AGENTS.md](AGENTS.md) for the complete operating contract.
