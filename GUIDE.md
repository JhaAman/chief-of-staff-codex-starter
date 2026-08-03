# Chief of Staff vault guide

The pinned Chief task is the front door; these files are its durable memory.

| Need | Use |
| --- | --- |
| Fresh status from approved sources | `$check-in` |
| Current portfolio snapshot | `$plan-overview` |
| Run an authorized outcome | `$chief-of-staff` |
| Concise weekday closeout | `$end-of-day-summary` |
| Review a scheduled refresh | `automations/heartbeat.md` |

## Vault map

- `PROFILE.md` — responsibilities, priorities, attention policy, and preferences.
- `projects/` — small active context plus supporting and historical notes.
- `threads/` — one Chief-owned ledger: Current Context and History.
- `sources/` — approved source scopes and their purpose.
- `reports/` — proportional worker handoffs, usage, and quality signals.
- `check-ins/` — meaningful refresh snapshots, never copied source transcripts.
- `context-compaction-log.md` — metadata-only observability record.

## Private backup

After onboarding, create an empty private repository, verify its visibility,
and add it as the vault's `origin`. Never put personal project state, sources,
people, task IDs, check-ins, or local paths back into this public starter.

## Operating boundaries

The Chief coordinates; saved-project workers implement. It uses one bounded
refresh before calling state current and labels unavailable data `Last known`.
Use `Blockers only` notification by default and opt in to `Notify on completion`
only for work the user is actively awaiting. Read [AGENTS.md](AGENTS.md) for
the complete contract.
