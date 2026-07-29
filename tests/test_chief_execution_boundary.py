import csv
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def compact(text: str) -> str:
    return " ".join(text.split())


def scenarios() -> dict[str, str]:
    path = ROOT / "tests" / "fixtures" / "chief_execution_boundary_scenarios.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["scenario"]: row["route"] for row in csv.DictReader(handle)}


class ChiefExecutionBoundaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.agents = read("AGENTS.md")
        cls.skill = read(".agents/skills/chief-of-staff/SKILL.md")
        cls.scenarios = scenarios()

    def test_management_and_bounded_verification_stay_direct(self):
        for scenario in (
            "explain an existing concept",
            "refresh approved sources for current status",
            "run a check-in",
            "inspect minimally to choose and scope a task",
            "reconcile task and status state",
            "maintain routine coordination records",
        ):
            with self.subTest(scenario=scenario):
                self.assertEqual(self.scenarios[scenario], "direct management")
        self.assertEqual(
            self.scenarios["verify another worker's output"], "direct verification"
        )
        for contract in map(compact, (self.agents, self.skill)):
            self.assertIn("minimal bounded routing or scoping inspection", contract)
            self.assertIn("approved-source refresh", contract)
            self.assertRegex(contract, r"task and status (?:state|reconciliation)")
            self.assertRegex(contract, r"routine (?:coordination )?records")
            self.assertIn("bounded verification of another", contract)

    def test_substantive_read_only_execution_uses_a_visible_task(self):
        for scenario in (
            "perform substantive repository research",
            "review a repository as the requested outcome",
            "probe a live system",
            "test an environment or access",
            "validate an onboarding walkthrough",
        ):
            with self.subTest(scenario=scenario):
                self.assertEqual(self.scenarios[scenario], "visible task")
        for contract in map(compact, (self.agents, self.skill)):
            self.assertIn(
                "Read-only does not make requested execution management work",
                contract,
            )
            self.assertIn("substantive repository research or review", contract)
            self.assertIn("live-system probing", contract)
            self.assertIn("environment or access testing", contract)
            self.assertIn("onboarding walkthrough validation", contract)
            self.assertIn("inspect only enough to choose and scope", contract)


if __name__ == "__main__":
    unittest.main()
