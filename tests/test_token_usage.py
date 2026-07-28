import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "tools/token_usage.py"


def usage(input_tokens, cached, output, total):
    return {"input_tokens": input_tokens, "cached_input_tokens": cached, "cache_write_input_tokens": 0, "output_tokens": output, "reasoning_output_tokens": output // 2, "total_tokens": total}


def turn(turn_id, timestamp, counter, model="example-model", effort="high", message="TEST_MESSAGE_CONTENT"):
    return [
        {"timestamp": timestamp, "type": "turn_context", "payload": {"turn_id": turn_id, "model": model, "effort": effort}},
        {"timestamp": timestamp, "type": "event_msg", "payload": {"type": "task_started", "turn_id": turn_id}},
        {"timestamp": timestamp, "type": "event_msg", "payload": {"type": "user_message", "message": message}},
        {"timestamp": timestamp, "type": "event_msg", "payload": {"type": "token_count", "info": {"total_token_usage": counter, "last_token_usage": counter}}},
        {"timestamp": timestamp, "type": "event_msg", "payload": {"type": "task_complete", "turn_id": turn_id}},
    ]


class TokenUsageTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.home = self.base / "codex"
        self.home.mkdir()
        self.db = sqlite3.connect(self.home / "state_5.sqlite")
        self.db.execute("CREATE TABLE threads (rollout_path TEXT, source TEXT, model TEXT, reasoning_effort TEXT)")
        self.vault = self.base / "vault"
        reports = self.vault / "reports/usage"
        reports.mkdir(parents=True)
        (reports / "config.json").write_text(json.dumps({"timezone": "UTC", "pricing_cache": "reports/usage/pricing.json", "output_directory": "reports/usage/generated", "actual_cost": {"subscription_marginal_usage_usd": 0, "subscription_marginal_usage_basis": "example convention", "fixed_subscription_fee_usd": None, "actual_cash_paid_outside_subscription_usd": "unknown"}}))
        (reports / "pricing.json").write_text(json.dumps({"valid_until": "2030-01-01T00:00:00Z", "models": {"example-model": {"source_url": "https://platform.openai.com/docs/pricing", "effective_date": "2026-01-01", "input_per_million": "2", "cached_input_per_million": "0.2", "output_per_million": "8", "cache_write_multiplier": "1.25"}}}))

    def tearDown(self):
        self.db.close(); self.temp.cleanup()

    def add(self, rows, source="{}"):
        path = self.base / f"rollout-{self.db.execute('SELECT count(*) FROM threads').fetchone()[0]}.jsonl"
        path.write_text("".join(json.dumps(row) + "\n" for row in rows))
        self.db.execute("INSERT INTO threads VALUES (?, ?, ?, ?)", (str(path), source, "example-model", "high")); self.db.commit()

    def summary(self, scope="this-week"):
        result = subprocess.run([sys.executable, str(CLI), "summary", "--vault-root", str(self.vault), "--codex-home", str(self.home), "--scope", scope, "--as-of", "2026-07-24T12:00:00Z"], text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_default_includes_cost_in_every_required_section_and_honest_cash(self):
        self.add(turn("current", "2026-07-22T12:00:00Z", usage(100, 50, 20, 120)))
        output = self.summary()
        self.assertTrue(output.startswith("_Every dollar figure except the bold actual-cash line is an estimate at official API rates, not actual spend._"))
        self.assertIn("This Week: 120 Verified Tokens", output)
        self.assertIn("**Actual Cash Paid Outside Subscription: Unknown**", output)
        self.assertEqual(output.count("**Actual Cash Paid Outside Subscription:"), 1)
        self.assertNotIn("API-equivalent", output)
        self.assertIn("Weekly Trend", output); self.assertIn("Model / Effort", output); self.assertIn("Estimated Cost", output)
        self.assertIn("| Conversation | 120 | $0.00 | 100.0% |", output)

    def test_compare_uses_recent_complete_weeks_and_does_not_leak_content(self):
        self.add(turn("old", "2026-07-06T12:00:00Z", usage(100, 0, 10, 110)))
        self.add(turn("new", "2026-07-13T12:00:00Z", usage(200, 0, 20, 220)), source='{"subagent": {"kind": "test"}}')
        self.add(turn("current", "2026-07-23T12:00:00Z", usage(300, 0, 30, 330)))
        output = self.summary("compare-recent-weeks")
        self.assertIn("Latest Complete Week: 220 Verified Tokens, +100.0% versus the prior week.", output)
        self.assertIn("2026-07-05 to 2026-07-11", output); self.assertIn("2026-07-12 to 2026-07-18", output)
        self.assertNotIn("2026-07-19 to 2026-07-25", output)
        self.assertNotIn("TEST_MESSAGE_CONTENT", output); self.assertNotIn(str(self.base), output)

    def test_stale_or_unknown_models_are_unpriced(self):
        pricing = self.vault / "reports/usage/pricing.json"
        pricing.write_text(json.dumps({"valid_until": "2020-01-01T00:00:00Z", "models": {}}))
        self.add(turn("current", "2026-07-22T12:00:00Z", usage(100, 0, 20, 120), model="unknown-model"))
        output = self.summary()
        self.assertIn("| 2026-07-19 to 2026-07-25 | In Progress | 120 | 120 unpriced |", output)
        self.assertIn("pricing is missing or stale", output)

    def test_partial_pricing_keeps_priced_and_unpriced_quantities_together(self):
        self.add(turn("priced", "2026-07-22T12:00:00Z", usage(100, 0, 20, 120)))
        self.add(turn("unpriced", "2026-07-22T13:00:00Z", usage(100, 0, 20, 120), model="unknown-model"))
        output = self.summary()
        self.assertIn("$0.00; 120 unpriced", output)
        self.assertNotIn("priced +", output)

    def test_last_four_weeks_keeps_model_and_activity_cost_breakdowns(self):
        self.add(turn("recent", "2026-07-22T12:00:00Z", usage(100, 0, 20, 120)))
        output = self.summary("last-four-weeks")
        self.assertIn("| example-model | High | 120 | $0.00 | 0 |", output)
        self.assertIn("| Conversation | 120 | $0.00 | 100.0% |", output)


if __name__ == "__main__": unittest.main()
