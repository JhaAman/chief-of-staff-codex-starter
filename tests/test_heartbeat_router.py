import unittest
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APPROVED_PROMPT = (
    "At 6 PM on weekdays, run `$end-of-day-summary`. Otherwise run `$check-in`. "
    "Follow the selected skill and AGENTS.md. Perform one bounded pass and make "
    "no unauthorized external changes."
)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def fenced_prompt(document: str) -> str:
    marker = "```text\n"
    start = document.index(marker) + len(marker)
    return document[start : document.index("\n```", start)]


def selected_skills(local_time: datetime) -> list[str]:
    if local_time.weekday() < 5 and local_time.hour == 18:
        return ["$end-of-day-summary"]
    return ["$check-in"]


class HeartbeatRouterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.heartbeat = read("automations/heartbeat.md")
        cls.prompt = fenced_prompt(cls.heartbeat)
        cls.agents = read("AGENTS.md")
        cls.check_in = read(".agents/skills/check-in/SKILL.md")
        cls.eod = read(".agents/skills/end-of-day-summary/SKILL.md")

    def test_prompt_is_the_approved_thin_router(self):
        self.assertEqual(self.prompt, APPROVED_PROMPT)

    def test_weekday_18_routes_only_to_closeout(self):
        self.assertEqual(
            selected_skills(datetime(2026, 7, 27, 18)),
            ["$end-of-day-summary"],
        )

    def test_other_hours_route_only_to_check_in(self):
        for local_time in (
            datetime(2026, 7, 27, 8),
            datetime(2026, 7, 27, 19),
            datetime(2026, 8, 1, 18),
        ):
            with self.subTest(local_time=local_time):
                self.assertEqual(selected_skills(local_time), ["$check-in"])

    def test_selected_skills_own_detailed_contracts(self):
        self.assertLess(
            self.check_in.index("PROFILE.md"),
            self.check_in.index("Refresh only source scopes"),
        )
        self.assertLess(
            self.check_in.index("sources/index.md"),
            self.check_in.index("Refresh only source scopes"),
        )
        self.assertIn("only source scopes listed in `sources/index.md`", self.check_in)
        self.assertIn("PROFILE.md", self.eod)
        self.assertIn("only source scopes listed in `sources/index.md`", self.eod)
        self.assertIn("heartbeat that selects `$check-in`", self.agents)
        for detailed_rule in (
            "NEEDS_USER",
            "DEPENDENCY_READY",
            "context-compaction-log.md",
            "stale skill",
        ):
            with self.subTest(detailed_rule=detailed_rule):
                self.assertNotIn(detailed_rule, self.prompt)


if __name__ == "__main__":
    unittest.main()
