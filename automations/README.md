# Automations

The heartbeat is optional and inactive by default. When approved, schedule it
at 09:00, 13:00, and 18:00 in the configured timezone. Its thin prompt lives
in `heartbeat.md`; weekday 18:00 routes to `$end-of-day-summary` and every
other run routes to `$check-in`.
