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
