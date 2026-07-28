# Chief of Staff for Codex

This is a starter project to run your own Chief of Staff in Codex. It's a single, pinned thread that is the only thread you work out of - it spawns, manages, and closes other threads on its own.

It operates through a single Git-backed vault, containing its memories, existing work streams, and skills. 

## Start here

1. Clone the starter into a private local folder. This removes the public
   remote before you add any personal information.

   ```bash
   git clone https://github.com/JhaAman/chief-of-staff-codex-starter.git my-chief-of-staff
   cd my-chief-of-staff
   git remote remove origin
   ```

   Create a private backup repository and add it later, after you confirm its
   visibility. Never push your vault to a public fork.

2. Open `my-chief-of-staff` as a Codex project. Create and pin one task named
   **Chief of Staff** (use this local checkout, not a worktree), then paste:

   ```text
   Read AGENTS.md, then use $bootstrap-chief-of-staff to set up my private Chief of Staff vault. Interview me one question at a time. Keep the proposal small, explain a connector only when it unlocks a concrete workflow, and ask before making changes or enabling an automation. After I approve the setup, run one safe first $check-in and tell me what to do next.
   ```

3. Answer the interview in plain language. The task will propose the smallest
   useful setup, make only what you approve, and finish with a first check-in.

That is all you need to start. Keep returning to the pinned Chief task.

## What it does

The Chief coordinates; it does not implement. A concrete request to build,
fix, test, review, or handle PR comments creates or continues a separately
saved-project worker task. Management questions and bounded verification stay
with the Chief. Workers report status in the background; only urgent blockers
interrupt you.

The defaults are deliberately private and conservative: sources are opt-in,
automations start inactive, and sending messages, comments, merges,
deployments, or connector changes always needs your approval.

## When you want more

- Run `$check-in` for a fresh update from approved sources.
- Run `$plan-overview` for a recorded portfolio snapshot without a live refresh.
- Review [the operating rules](AGENTS.md), [the optional heartbeat](automations/heartbeat.md), or [the vault map](GUIDE.md) only when you need them.

## License

MIT. See [LICENSE](LICENSE).
