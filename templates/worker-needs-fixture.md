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

4. For a collaborative repository's `NEEDS_USER_TEXT_APPROVAL`, record the
   exact target and complete proposed text or exact diff. The Chief must show
   that text unchanged and wait for approval before the worker changes,
   commits, pushes, creates, or updates the outward-facing narrative. A solo
   repository with existing task and publication authority does not create
   this status solely for concise ordinary repository text.

5. For `WAITING_ON_DEPENDENCY`, record the declared producer, dependent,
   required integrated output, authoritative branch, and stable handoff ID. It
   remains background coordination unless the user must act. A successful
   `DEPENDENCY_READY` send becomes `DEPENDENCY_READY_SENT`, not consumption.
   Record `DEPENDENCY_ACK` only after the dependent verifies the authoritative
   source and leaves the dependency wait.
6. If an idle or unloaded dependent still exposes the same unacknowledged wait
   on the next bounded pass, send one fallback with the same handoff ID and
   never repeat it. Do not send to active, acknowledged, or terminal tasks.
7. If acknowledgement or exact-artifact use exists while the ledger still
   says waiting, reconcile the ledger without waking the worker. Use
   `WAITING_ON_EXTERNAL` with a stable resume key for later CI, review, timer,
   or other non-user conditions.
