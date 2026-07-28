# Worker Need Fixture

Use this generic example to verify manual check-in and heartbeat behavior.

1. Record an approved, non-archived interview worker as idle with
   `NEEDS_USER_INTERVIEW`, State `Waiting for user — answer the next interview
   question`, and a known task ID.
2. The next check-in or heartbeat must display `🚨 CHIEF INTERVIEW WAITING` and
   link the worker as `[Interview task](codex://threads/<thread-id>)`, asking
   the user to open it and complete the interview there despite its idle state.
3. After `INTERVIEW_COMPLETE`, withdrawal, or supersession, clear or update the
   waiting state. The next check-in or heartbeat must not display that alert.

4. For `NEEDS_USER_TEXT_APPROVAL`, record the exact target and complete proposed
   text or exact diff. The Chief must show that text unchanged and wait for
   approval before the worker changes, commits, pushes, creates, or updates the
   outward-facing narrative.

5. For `WAITING_ON_DEPENDENCY`, record the declared producer, dependent,
   required integrated output, and authoritative branch. It remains background
   coordination unless the user must act. Resume only after verified
   `DEPENDENCY_READY` evidence names the integrated output.
