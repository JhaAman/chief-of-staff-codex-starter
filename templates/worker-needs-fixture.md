# Worker Need Fixture

Use this generic example to verify manual check-in and heartbeat behavior.

1. Record an approved, non-archived interview worker as idle with State
   `Waiting for user — answer the next interview question` and a known task ID.
2. The next check-in or heartbeat must display `🚨 CHIEF APPROVAL NEEDED` and
   link the worker as `[Interview task](codex://threads/<thread-id>)`, despite
   its idle runtime state.
3. After the user answers in the Chief task and the answer is relayed to the
   worker, clear or update the waiting state. The next check-in or heartbeat
   must not display that alert.
