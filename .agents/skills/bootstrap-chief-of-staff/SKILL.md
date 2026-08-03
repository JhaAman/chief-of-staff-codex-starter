---
name: bootstrap-chief-of-staff
description: Interview a user one question at a time and propose the smallest useful Chief of Staff vault. Use only for initial onboarding or an explicitly requested profile reset.
---

# Bootstrap Chief of Staff

Ask one concise question at a time. Do not front-load a questionnaire. Start
by explaining that the user will approve a small proposal before anything is
saved, connected, or scheduled.

## Learn

Gather only enough to establish:

- current responsibilities and a small Active Context plus supporting work;
- important people or groups;
- failures, delays, or surprises the user is afraid of missing;
- narrow repositories, channels, mailboxes, documents, calendars, trackers, or
  local files that answer a concrete question;
- what merits an interruption, a quiet update, or no action;
- what coding work may be delegated and which words explicitly authorize it;
- which external actions always require confirmation;
- timezone, working hours, and preferred check-in cadence.

Ask for identifiers, links, and local paths only when they unlock an approved
workflow. Distinguish confirmed facts from tentative answers.

## Propose before editing

After the interview, propose:

1. Changes to `PROFILE.md`.
2. Three to seven notes based on `templates/project.md`.
3. Active Context and Supporting And Historical Context rows for
   `projects/index.md`, plus `sources/index.md`.
4. The smallest useful connector set, with one workflow per connector.
5. `Blockers only` notification by default, optional `Notify on completion`
   for actively awaited work, and an optional 09:00/13:00/18:00 heartbeat.

Explain a connector only when it unlocks a named workflow. Keep the first
proposal usable without connectors. Treat a private backup remote as a setup
step, not as permission to create or push to one.

Do not edit files, install or connect apps, create workers, or create or
activate an automation until the user approves the proposal.

## Apply only the approved proposal

After approval:

- update only approved files and project notes;
- preserve placeholders for unknowns;
- store summaries and links, not transcripts or copied source content;
- keep inference explicit and use absolute dates;
- show the diff before committing;
- commit only when the user requested durable Git history.

Then run one manual `$check-in` using only the newly approved scopes (or the
vault's internal records when no source is approved). Use it to verify the
first-report path; do not create a worker, connect an app, or activate a
heartbeat. End with the result and the smallest next action.

Source authorization, task pinning, worker creation, and heartbeat activation
are separate actions.
