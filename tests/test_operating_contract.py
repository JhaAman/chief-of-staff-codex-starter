import csv
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def compact(text: str) -> str:
    return " ".join(text.split())


def scenarios(path: str) -> dict[str, dict[str, str]]:
    with (ROOT / path).open(encoding="utf-8", newline="") as handle:
        return {row["scenario"]: row for row in csv.DictReader(handle)}


class OperatingContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.agents = read("AGENTS.md")
        cls.chief = read(".agents/skills/chief-of-staff/SKILL.md")
        cls.check_in = read(".agents/skills/check-in/SKILL.md")
        cls.eod = read(".agents/skills/end-of-day-summary/SKILL.md")
        cls.plan = read(".agents/skills/plan-overview/SKILL.md")
        cls.heartbeat = read("automations/heartbeat.md")
        cls.thread = read("templates/thread.md")
        cls.summary = read("templates/worker-summary.md")
        cls.closure = scenarios("tests/fixtures/task_closure_scenarios.csv")
        cls.text_approval = scenarios("tests/fixtures/text_approval_scenarios.csv")

    def test_closure_lanes_preserve_evidence_and_open_work(self):
        self.assertEqual(self.closure["tiny completed task"]["report_required"], "no")
        self.assertEqual(self.closure["important completed task"]["report_required"], "yes")
        self.assertEqual(self.closure["runtime completed with unresolved user input"]["terminal"], "no")
        self.assertEqual(self.closure["runtime completed with unresolved dependency"]["user_visible"], "no")
        self.assertIn("Routine tasks", self.agents)
        self.assertIn("Important, reusable, or decision-bearing", compact(self.agents))
        self.assertIn("Abandoned or superseded", compact(self.agents))
        self.assertIn("Closure pending", self.agents)

    def test_state_is_refreshed_before_it_is_called_current(self):
        for document in (self.agents, self.chief, self.check_in, self.eod, self.plan):
            with self.subTest(document=document[:40]):
                self.assertIn("one immediate bounded refresh", compact(document))
                self.assertIn("Last known", compact(document))
        self.assertIn("Never sleep", self.agents)
        self.assertIn("hourly heartbeat", self.agents)

    def test_text_approval_gates_human_facing_narrative_only(self):
        for scenario in ("README edit", "pull request description edit"):
            with self.subTest(scenario=scenario):
                self.assertEqual(self.text_approval[scenario]["approval_required"], "yes")
        self.assertEqual(
            self.text_approval["exact user-supplied text"]["allowed_without_new_approval"],
            "yes if unchanged",
        )
        for document in (self.agents, self.chief, self.thread):
            with self.subTest(document=document[:40]):
                self.assertIn("NEEDS_USER_TEXT_APPROVAL", document)
                self.assertIn("exact proposed text or exact diff", compact(document))

    def test_task_local_status_and_handoffs_avoid_routine_noise(self):
        for document in (self.agents, self.chief, self.check_in, self.thread):
            with self.subTest(document=document[:40]):
                self.assertIn("WAITING_ON_DEPENDENCY", document)
                self.assertIn("DEPENDENCY_READY", document)
        self.assertIn("background inspection", compact(self.agents))
        self.assertIn("`URGENT_BLOCKER`", self.thread)
        self.assertIn("completion, pull-request readiness", compact(self.agents))

    def test_plan_overview_refreshes_task_and_git_state_not_connected_sources(self):
        compact_agents = compact(self.agents)
        compact_plan = compact(self.plan)
        self.assertIn("does not refresh connected sources", compact_agents)
        self.assertIn("broader approved-source refresh", compact_agents)
        self.assertIn("authoritative Git branch or pull-request state", compact_plan)
        self.assertIn("Use `$check-in` when broader live-source refresh is needed", self.plan)

    def test_end_of_day_keeps_proportional_closeout_rules(self):
        self.assertIn("at most three", self.eod)

    def test_public_contract_does_not_contain_private_identity_or_paths(self):
        artifacts = (
            "AGENTS.md",
            ".agents/skills/check-in/SKILL.md",
            ".agents/skills/chief-of-staff/SKILL.md",
            ".agents/skills/end-of-day-summary/SKILL.md",
            ".agents/skills/end-of-day-summary/agents/openai.yaml",
            ".agents/skills/plan-overview/SKILL.md",
            "automations/heartbeat.md",
            "templates/abandonment.md",
            "templates/check-in.md",
            "templates/thread.md",
            "templates/worker-needs-fixture.md",
            "templates/worker-summary.md",
            "tests/fixtures/task_closure_scenarios.csv",
            "tests/fixtures/text_approval_scenarios.csv",
            "tests/test_heartbeat_router.py",
            "tests/test_operating_contract.py",
        )
        changed_surfaces = "\n".join(read(path) for path in artifacts)
        for forbidden in ("Am" "an", "Jha" "Am" "an", "/" "Users/", "magic" "product"):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, changed_surfaces)


if __name__ == "__main__":
    unittest.main()
