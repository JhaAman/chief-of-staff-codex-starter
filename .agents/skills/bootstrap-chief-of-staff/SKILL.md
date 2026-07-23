---
name: bootstrap-chief-of-staff
description: Interview a user one question at a time and propose the smallest useful Chief of Staff vault. Use only for initial onboarding or an explicitly requested profile reset.
---

# Bootstrap Chief of Staff

Ask one question at a time. Do not front-load a questionnaire.

## Learn

Gather only enough to establish:

- current responsibilities and three to seven active workstreams;
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
3. Rows for `projects/index.md` and `sources/index.md`.
4. The smallest useful connector set, with one workflow per connector.
5. Notification rules and an optional heartbeat cadence.
6. Any necessary narrow changes to `AGENTS.md` or
   `automations/heartbeat.md`.

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

Stop when the vault is ready for a first manual `$check-in`. Source
authorization, task pinning, worker creation, and heartbeat activation are
separate actions.
