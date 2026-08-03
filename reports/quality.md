# Chief Quality Signals

Last updated: YYYY-MM-DD

Review this at the daily 18:00 pass and update it only when a value or its
evidence changes. Pre-change history is `Unknown`; do not reconstruct it from
weak proxies.

## Snapshot

| Signal | Current value | Evidence coverage |
| --- | --- | --- |
| Completed-task-to-notification delay | Unknown | No paired exact timestamps recorded yet |
| Stale Current Context rows | Unknown | Requires exact `Last checked` timestamps |
| Unresolved requests missed by scheduled check-ins | Unknown | Requires a known request and later scheduled check-in |
| Interruptions the user considered unnecessary | Unknown | Count only explicit user feedback |

## Definitions

- **Completed-task-to-notification delay:** elapsed time from a task's exact
  completion timestamp to the first exact Chief notification timestamp. Label
  samples with `Blockers only` or `Notify on completion`.
- **Stale Current Context rows:** rows whose exact `Last checked` timestamp is
  more than 24 hours old. Never scan History for this signal.
- **Unresolved requests missed by scheduled check-ins:** scheduled check-ins
  that ran after a known `Waiting for user —` request but omitted that task.
- **Interruptions the user considered unnecessary:** immediate alerts the user
  explicitly said were unnecessary. Silence is not evidence.

## Evidence log

Record only exact timestamps, task links, notification mode, and a compact
evidence reference.

| Event time | Signal | Task | Related time | Mode or evidence |
| --- | --- | --- | --- | --- |
