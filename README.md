# Chief of Staff for Codex

This starter creates a private, git-backed vault for one pinned Codex Chief of
Staff. Talk to the Chief; it coordinates visible workers and keeps durable
context small.

## Start here

1. Clone the starter, then disconnect it from this public repository.

   ```bash
   git clone https://github.com/JhaAman/chief-of-staff-codex-starter.git my-chief-of-staff
   cd my-chief-of-staff
   git remote remove origin
   ```

   Never push a personal vault as a public fork.

2. Open `my-chief-of-staff` as a local Codex project and create one pinned
   task named **Chief of Staff** using the local checkout, not a worktree.

3. Paste this into that task:

   ```text
   Read AGENTS.md, then use $bootstrap-chief-of-staff to set up my private Chief of Staff vault. Interview me one question at a time. Keep the proposal small, ask before saving anything, connecting a source, creating a worker, or enabling an automation, then run one safe first $check-in after I approve it.
   ```

The Chief defaults to a bounded active project context and a task ledger split
into Current Context and History. Workers are quiet by default: the Chief
interrupts you for real blockers, while routine completion appears in a
check-in unless you explicitly opt in to completion notification.

## Useful commands

- `$check-in` — refresh approved sources and current worker context.
- `$plan-overview` — show active projects, blockers, and next actions.
- `$end-of-day-summary` — produce a concise weekday closeout.
- `$token-usage` — inspect privacy-safe local usage and API-rate estimates.

The optional [heartbeat](automations/heartbeat.md) is inactive until you review
and activate it. Its intended cadence is 09:00, 13:00, and 18:00 in your
timezone; weekday 18:00 is the closeout.

Read [GUIDE.md](GUIDE.md) for the vault layout and [AGENTS.md](AGENTS.md) for
the operating contract.
