# Chief of Staff Check-In

- Date and time: YYYY-MM-DD HH:MM TIMEZONE
- Scope:
- Projects:
- Freshness: refreshed | Last known — <time and missing source>

## Needs you now

- _For `NEEDS_USER_TEXT_APPROVAL`, name the target and include the complete
  proposed text or exact diff unchanged._
- _For a worker-owned interview, use `🚨 CHIEF INTERVIEW WAITING`, link the
  task, and direct the user to complete it there without repeating its question._
- _For other unresolved needs, link the task and include action, why, blocked
  work, safe options, and deadline._

## Big Changes

- _Use a recognizable subject and plain state._

## Workers

- _Include only a completed, blocked, or steerable task that matters now._
- _Treat `WAITING_ON_DEPENDENCY` and `DEPENDENCY_READY` as coordination, not a
  user alert unless the user must act. Accept readiness only after the exact
  validated output is integrated into the authoritative branch._
- _Treat a successful send as `DEPENDENCY_READY_SENT` until the dependent
  records `DEPENDENCY_ACK` for the same handoff ID or exposes stronger
  exact-artifact use. Repair one idle unacknowledged wait on the next bounded
  pass; never resend to active, acknowledged, or completed tasks._
- _Resume a satisfied `WAITING_ON_EXTERNAL` condition once in the same task by
  its stable resume key. Do not mislabel CI or review waiting as a dependency
  wait._

## Closure maintenance

- _Omit when no durable record changed. For at most three scanned tasks, record
  the closure lane, evidence used, missing evidence, and archive decision._

## Details for follow-up

- _Keep richer evidence and source links here._

## Source coverage

- _List refreshed approved sources and meaningful limitations._

## Vault changes

- Files:
- Commit:
