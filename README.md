# Chief of Staff for Codex

This starter lets you run a personal Chief of Staff inside one pinned Codex task. This is the only task you need to talk to: give it work, ask questions, or request an update, and it manages the rest.

The Chief uses a private, git-backed **Vault** as its memory. It keeps track of your priorities, active work, workers, preferences, and skills.

## Start here

1. Clone the starter and disconnect it from this repo (for privacy).

   ```bash
   git clone https://github.com/JhaAman/chief-of-staff-codex-starter.git my-chief-of-staff
   cd my-chief-of-staff
   git remote remove origin
   ```

   Never push your personal vault as a public fork.

2. Open `my-chief-of-staff` as a local Codex project.

3. Create and pin one task named **Chief of Staff** using the local checkout, not a worktree.

4. Paste this into the task:

   ```text
   Read AGENTS.md, then use $bootstrap-chief-of-staff to set up my private Chief of Staff vault. Interview me one question at a time. Keep the proposal small, explain a connector only when it unlocks a useful workflow, and ask before saving anything, connecting a source, creating a worker, or enabling an automation. After I approve the setup, apply it, run one safe first $check-in, and tell me the smallest next step.
   ```

5. Answer the interview and approve/edit the proposed setup.

6. Message pinned Chief task to assign work.

That is enough to get started. To improve quality, add Connectors such as GitHub, Slack, Google Drive, Calendar etc. These focus the Chief on your priorities. I would also setup the [heartbeat](automations/heartbeat.md) to run check-ins automatically every hour - you can ask your Chief to set that up. 

## How it works

- The Chief manages work; separate visible worker tasks implement it.
- A concrete request—fixing a bug, reviewing code, running tests, or researching something—is dispatched in the background.
- Routine worker activity stays out of your Chief conversation. The Chief comes back when it needs a decision, an interview is waiting, or something important is blocked.
- You should rarely need to open worker tasks yourself, except for longer interviews.
- Your preferences become durable instructions in the private vault, so the system can adapt as you use it.
- Sending messages, posting comments, merging, deploying, connecting sources, and other important external actions still require your approval.

## Useful commands

- `$check-in` — refresh what needs your attention.
- `$plan-overview` — see your current projects and what is next.
- `$end-of-day-summary` — produce a concise workday closeout.
- `$token-usage` — inspect the Chief’s token usage and estimated API-rate cost.

The optional [heartbeat](automations/heartbeat.md) can run check-ins automatically, but it starts disabled.

For the file layout and daily workflow, read [the vault guide](GUIDE.md). For the complete operating rules, read [AGENTS.md](AGENTS.md).
