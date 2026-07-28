# Chief of Staff for Codex

A small private coordination vault for one pinned Codex Chief task. The Chief
manages priorities and worker tasks; visible workers implement changes.

## Start here

1. Clone this starter into a private location and remove its public remote
   before adding personal information.

   ```bash
   git clone <starter-url> my-chief-of-staff
   cd my-chief-of-staff
   git remote remove origin
   ```

2. Open the folder as a Codex project. Create and pin one local task named
   **Chief of Staff**.

3. Paste:

   ```text
   Read AGENTS.md, then use $bootstrap-chief-of-staff to set up my private Chief of Staff vault. Interview me one question at a time. Keep the proposal small, ask before saving, connecting a source, creating a worker, or enabling an automation. After approval, run one safe first $check-in.
   ```

4. Answer the interview, approve the setup you want, then run `$check-in`.

## How it works

- The Chief handles coordination and bounded verification; workers implement.
- Check-ins use one bounded refresh of approved sources and task or Git state.
  If a source is unavailable, the result is labeled **Last known**.
- Routine worker progress stays in the worker task. Real user decisions and
  multi-question interviews surface with a linked task; urgent harm uses
  `URGENT_BLOCKER`.
- The heartbeat is optional and inactive by default. Review
  [its draft](automations/heartbeat.md) before activation.

See [the operating contract](AGENTS.md) and [the vault guide](GUIDE.md) for
details.
