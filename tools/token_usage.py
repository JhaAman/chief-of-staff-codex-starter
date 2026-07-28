#!/usr/bin/env python3
"""Render privacy-safe local Codex token and API-equivalent cost summaries."""
from __future__ import annotations

import argparse, json, sqlite3, sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

FIELDS = ("input_tokens", "cached_input_tokens", "cache_write_input_tokens", "output_tokens", "reasoning_output_tokens", "total_tokens")
SCOPES = ("this-week", "last-four-weeks", "all-time", "compare-recent-weeks")

def zero(value: dict[str, Any] | None = None) -> dict[str, int]:
    value = value or {}
    return {field: int(value.get(field, 0) or 0) for field in FIELDS}

def add(target: dict[str, int], value: dict[str, int]) -> None:
    for field in FIELDS: target[field] += value[field]

def at(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)

def read(path: Path) -> dict[str, Any]: return json.loads(path.read_text(encoding="utf-8"))

def start_of_week(value: datetime, zone: ZoneInfo) -> date:
    local = value.astimezone(zone).date()
    return local - timedelta(days=(local.weekday() + 1) % 7)

def classify(source: str | None) -> str:
    try: return "subagent" if json.loads(source or "{}").get("subagent") else "conversation"
    except (json.JSONDecodeError, AttributeError): return "conversation"

def events(codex_home: Path) -> tuple[list[dict[str, Any]], list[str]]:
    conn = sqlite3.connect(f"file:{codex_home / 'state_5.sqlite'}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try: rows = conn.execute("SELECT rollout_path, source, model, reasoning_effort FROM threads").fetchall()
    finally: conn.close()
    found, warnings = [], []
    for row in rows:
        previous, current_turn, contexts = zero(), None, {}
        try:
            with Path(row["rollout_path"]).open(encoding="utf-8") as handle:
                for line in handle:
                    record = json.loads(line); payload = record.get("payload") or {}
                    if record.get("type") == "turn_context" and payload.get("turn_id"):
                        contexts[payload["turn_id"]] = (payload.get("model") or row["model"] or "unknown", payload.get("effort") or row["reasoning_effort"] or "unknown")
                    elif record.get("type") == "event_msg" and payload.get("type") == "task_started": current_turn = payload.get("turn_id")
                    elif record.get("type") == "event_msg" and payload.get("type") == "task_complete": current_turn = None
                    elif record.get("type") == "event_msg" and payload.get("type") == "token_count" and record.get("timestamp"):
                        info = payload.get("info") or {}
                        if not info.get("total_token_usage"): continue
                        total = zero(info["total_token_usage"]); delta = {field: total[field] - previous[field] for field in FIELDS}
                        if any(value < 0 for value in delta.values()):
                            warnings.append("cumulative counter reset; used last reported delta"); delta = zero(info.get("last_token_usage"))
                        previous = total
                        if any(delta.values()):
                            model, effort = contexts.get(current_turn, (row["model"] or "unknown", row["reasoning_effort"] or "unknown"))
                            found.append({"time": at(record["timestamp"]), "model": model, "effort": effort, "activity": classify(row["source"]), "tokens": delta})
        except (OSError, json.JSONDecodeError) as error: warnings.append(f"unreadable local rollout ({type(error).__name__})")
    return found, sorted(set(warnings))

def price(event: dict[str, Any], pricing: dict[str, Any], fresh: bool) -> tuple[Decimal | None, str | None]:
    if not fresh: return None, "stale pricing"
    model = pricing.get("models", {}).get(event["model"])
    needed = ("source_url", "effective_date", "input_per_million", "cached_input_per_million", "output_per_million")
    if not model: return None, f"unpriced model: {event['model']}"
    if not all(model.get(key) is not None for key in needed) or not str(model["source_url"]).startswith("https://"): return None, f"invalid pricing provenance: {event['model']}"
    t = event["tokens"]; long = model.get("long_context") or {}; long_input = int(long.get("input_threshold", 0)) and t["input_tokens"] > int(long["input_threshold"])
    im = Decimal(str(long.get("input_multiplier", 1))) if long_input else Decimal(1); om = Decimal(str(long.get("output_multiplier", 1))) if long_input else Decimal(1)
    uncached = max(0, t["input_tokens"] - t["cached_input_tokens"] - t["cache_write_input_tokens"])
    cost = (Decimal(uncached) * Decimal(str(model["input_per_million"])) * im + Decimal(t["cached_input_tokens"]) * Decimal(str(model["cached_input_per_million"])) * im + Decimal(t["cache_write_input_tokens"]) * Decimal(str(model["input_per_million"])) * Decimal(str(model.get("cache_write_multiplier", 1))) * im + Decimal(t["output_tokens"]) * Decimal(str(model["output_per_million"])) * om) / Decimal(1_000_000)
    return cost, None

def aggregate(values: list[dict[str, Any]], pricing: dict[str, Any], fresh: bool) -> dict[str, Any]:
    total, dollars, unpriced, reasons = zero(), Decimal(), 0, set()
    for value in values:
        add(total, value["tokens"]); cost, reason = price(value, pricing, fresh)
        if cost is None: unpriced += value["tokens"]["total_tokens"]; reasons.add(reason)
        else: dollars += cost
    status = "no usage" if not values else "estimated" if not unpriced else "unavailable" if not dollars else "partial"
    return {"tokens": total, "api_equivalent": {"status": status, "priced_usd": f"{dollars:.6f}", "unpriced_tokens": unpriced, "reasons": sorted(reason for reason in reasons if reason)}}

def with_breakdowns(values: list[dict[str, Any]], pricing: dict[str, Any], fresh: bool) -> dict[str, Any]:
    result = aggregate(values, pricing, fresh)
    for key, fields in (("model_effort", ("model", "effort")), ("activity", ("activity",))):
        groups: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
        for value in values: groups[tuple(value[field] for field in fields)].append(value)
        result[key] = [{"label": label, **aggregate(group, pricing, fresh)} for label, group in sorted(groups.items())]
    return result

def build(codex_home: Path, config: dict[str, Any], pricing: dict[str, Any], now: datetime) -> dict[str, Any]:
    found, warnings = events(codex_home); expiry = pricing.get("valid_until"); fresh = bool(expiry and now <= at(expiry))
    if not fresh: warnings.append("pricing is missing or stale; all API-equivalent costs are unpriced")
    zone = ZoneInfo(config.get("timezone", "UTC")); weeks: dict[date, list[dict[str, Any]]] = defaultdict(list)
    for value in found: weeks[start_of_week(value["time"], zone)].append(value)
    current = start_of_week(now, zone)
    weekly = [{"start": key.isoformat(), "end": (key + timedelta(days=6)).isoformat(), "complete": key < current, **with_breakdowns(value, pricing, fresh)} for key, value in sorted(weeks.items())]
    return {"generated_at": now.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"), "timezone": str(zone), "pricing": {"fetched_at": pricing.get("fetched_at"), "valid_until": expiry, "fresh": fresh, "models": {name: {key: value.get(key) for key in ("source_url", "effective_date")} for name, value in pricing.get("models", {}).items()}}, "actual_cost": config["actual_cost"], "warnings": sorted(set(warnings)), "all": with_breakdowns(found, pricing, fresh), "weekly": weekly}

def fmt_tokens(value: int) -> str: return f"{value / 1_000_000:.2f}M" if value >= 1_000_000 else f"{value / 1_000:.1f}K" if value >= 1_000 else str(value)
def fmt_cost(value: dict[str, Any]) -> str:
    if value["status"] == "no usage": return "—"
    if value["status"] == "estimated": return f"${Decimal(value['priced_usd']):,.2f}"
    if value["status"] == "partial": return f"${Decimal(value['priced_usd']):,.2f} priced + {fmt_tokens(value['unpriced_tokens'])} unpriced"
    return f"unavailable ({fmt_tokens(value['unpriced_tokens'])} unpriced)"

def empty(start: date, complete: bool) -> dict[str, Any]: return {"start": start.isoformat(), "end": (start + timedelta(days=6)).isoformat(), "complete": complete, **with_breakdowns([], {"models": {}}, False)}

def merge_periods(periods: list[dict[str, Any]]) -> dict[str, Any]:
    def merge(items: list[dict[str, Any]]) -> dict[str, Any]:
        total, priced, unpriced = zero(), Decimal(), 0
        for item in items:
            add(total, item["tokens"]); priced += Decimal(item["api_equivalent"]["priced_usd"]); unpriced += item["api_equivalent"]["unpriced_tokens"]
        status = "partial" if unpriced and priced else "unavailable" if unpriced else "estimated" if total["total_tokens"] else "no usage"
        return {"tokens": total, "api_equivalent": {"status": status, "priced_usd": f"{priced:.6f}", "unpriced_tokens": unpriced}}
    result = merge(periods)
    for key in ("model_effort", "activity"):
        grouped: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
        for period in periods:
            for item in period[key]: grouped[tuple(item["label"])].append(item)
        result[key] = [{"label": label, **merge(items)} for label, items in sorted(grouped.items())]
    return result

def select(report: dict[str, Any], scope: str) -> tuple[str, dict[str, Any], list[dict[str, Any]], dict[str, Any] | None]:
    weekly = report["weekly"]; current = start_of_week(at(report["generated_at"]), ZoneInfo(report["timezone"]))
    if scope == "all-time": return "All recorded usage", report["all"], weekly[-6:], None
    if scope == "compare-recent-weeks":
        complete = [week for week in weekly if week["complete"]]; return "Latest complete week", (complete[-1] if complete else empty(current, False)), complete[-2:], (complete[-2] if len(complete) > 1 else None)
    trend = [next((week for week in weekly if week["start"] == (current - timedelta(days=7 * offset)).isoformat()), empty(current - timedelta(days=7 * offset), offset > 0)) for offset in range(3, -1, -1)]
    if scope == "last-four-weeks":
        return "Last four calendar weeks", merge_periods(trend), trend, None
    return "This week", trend[-1], trend, None

def render(report: dict[str, Any], scope: str) -> str:
    label, chosen, trend, prior = select(report, scope); total = chosen["tokens"]["total_tokens"]
    change = "" if prior is None else " with no usage in the prior week" if not prior["tokens"]["total_tokens"] else f", {(total - prior['tokens']['total_tokens']) / prior['tokens']['total_tokens']:+.1%} versus the prior week"
    actual = report["actual_cost"]; cash = actual.get("actual_cash_paid_outside_subscription_usd", "unknown"); money = lambda value: f"${Decimal(str(value)):,.2f}" if value is not None else "unknown"; cash = money(cash) if isinstance(cash, (int, float)) else str(cash)
    lines = [f"{label}: {fmt_tokens(total)} verified tokens{change}.", "", f"**Actual cash paid outside subscription: {cash}**", "", f"- API-equivalent counterfactual: {fmt_cost(chosen['api_equivalent'])}; not money paid.", f"- Subscription-covered marginal usage: {money(actual.get('subscription_marginal_usage_usd'))} ({actual.get('subscription_marginal_usage_basis', 'not configured')}).", f"- Fixed subscription fee: {money(actual.get('fixed_subscription_fee_usd'))}.", "- Cached input is included in input; reasoning output is included in output.", "", "Weekly trend", "", "| Week | State | Tokens | API-equivalent |", "| --- | --- | ---: | ---: |"]
    for week in trend: lines.append(f"| {week['start']} to {week['end']} | {'complete' if week['complete'] else 'in progress'} | {week['tokens']['total_tokens']:,} | {fmt_cost(week['api_equivalent'])} |")
    lines += ["", "Model / effort", "", "| Model | Effort | Tokens | API-equivalent |", "| --- | --- | ---: | ---: |"]
    for item in chosen["model_effort"]: lines.append(f"| {item['label'][0]} | {item['label'][1]} | {item['tokens']['total_tokens']:,} | {fmt_cost(item['api_equivalent'])} |")
    if not chosen["model_effort"]: lines.append("| No usage recorded | — | 0 | — |")
    lines += ["", "Activity", "", "| Activity | Tokens | Share | API-equivalent |", "| --- | ---: | ---: | ---: |"]
    for item in chosen["activity"]: lines.append(f"| {item['label'][0]} | {item['tokens']['total_tokens']:,} | {item['tokens']['total_tokens'] / total:.1%} | {fmt_cost(item['api_equivalent'])} |")
    if not chosen["activity"]: lines.append("| No usage recorded | 0 | — | — |")
    if report["warnings"]: lines += ["", "Data quality: " + "; ".join(report["warnings"]) + "."]
    return "\n".join(lines) + "\n"

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("command", choices=("summary", "report")); parser.add_argument("--vault-root", default="."); parser.add_argument("--codex-home", default=str(Path.home() / ".codex")); parser.add_argument("--scope", choices=SCOPES, default="this-week"); parser.add_argument("--as-of"); parser.add_argument("--output-stem", default=f"usage-{date.today().isoformat()}")
    args = parser.parse_args(argv)
    try:
        root = Path(args.vault_root).resolve(); config = read(root / "reports/usage/config.json"); report = build(Path(args.codex_home).expanduser(), config, read(root / config["pricing_cache"]), at(args.as_of) if args.as_of else datetime.now(timezone.utc)); markdown = render(report, args.scope)
        if args.command == "summary": print(markdown, end=""); return 0
        output = root / config["output_directory"]; output.mkdir(parents=True, exist_ok=True); (output / f"{args.output_stem}.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8"); (output / f"{args.output_stem}.md").write_text(markdown, encoding="utf-8"); print(output / f"{args.output_stem}.json"); print(output / f"{args.output_stem}.md"); return 0
    except (OSError, ValueError, KeyError, sqlite3.Error, json.JSONDecodeError) as error: print(f"token_usage: {error}", file=sys.stderr); return 1

if __name__ == "__main__": raise SystemExit(main())
