# Chief of Staff for Codex

This is a starter project to run your own Chief of Staff in Codex. It's a single, pinned thread that is the only thread you work out of - it spawns, manages, and closes other threads on its own.

It operates through a single Git-backed **vault**, containing its memories, existing work streams, and skills. 

## Start here

1. Clone the starter, remove the public remote for your privacy.

   ```bash
   git clone https://github.com/JhaAman/chief-of-staff-codex-starter.git my-chief-of-staff
   cd my-chief-of-staff
   git remote remove origin
   ```

   Never push your vault to a public fork.

2. Open `my-chief-of-staff` in Codex as a new project. (I use 5.6 Sol High).
3. Create and pin one task named
   **Chief of Staff** (use this local checkout, not a worktree), then paste:

   ```text
   Read AGENTS.md, then use $bootstrap-chief-of-staff to set up my private Chief of Staff vault. Interview me one question at a time. Keep the proposal small, explain a connector only when it unlocks a concrete workflow, and ask before making changes or enabling an automation. After I approve the setup, run one safe first $check-in and tell me what to do next.
   ```

4. Answer the interview in plain language. 
5. It will propose an initial setup. Approve or make changes.
6. Add **connectors** (Slack, GitHub, Google Drive etc.) to the Chief.
7. Type `$check-in` to start the Vault.
8. Assign tasks to the Chief, all in one thread. 

That is all you need to start. Keep returning to the pinned Chief task.

## What it does

The Chief coordinates; it does *not* implement. Any concrete request (to fix, test, review etc.) will create or continue a **worker task**. This all happens async. All you have to do is tell the Chief what you want. If a task has an urgent blocker, the Chief will come back to you. You should almost never have to dive into the task yourself.

The Chief works better when you add **connectors**. I'm talking Slack, GitHub, Google Drive, Calendar. This way it knows what's important to you. 

## When you want more

- Run `$check-in` for a fresh update from approved sources.
- Run `$plan-overview` to see what the Chief thinks you're working on.
- Review [the operating rules](AGENTS.md), [the optional heartbeat](automations/heartbeat.md), or [the vault map](GUIDE.md) only when you need them. I never do. 

## How to improve

This is *my* Chief of Staff, designed by [me](https://github.com/JhaAman). You can edit it however you like - just tell the Chief of Staff how you'd like to make changes, and it will edit the **Vault** (this repo) accordingly, remembering your preferences for all future tasks.
