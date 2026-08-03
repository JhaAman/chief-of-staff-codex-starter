import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class OperatingContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.agents = read("AGENTS.md")
        cls.thread = read("templates/thread.md")
        cls.check_in = read(".agents/skills/check-in/SKILL.md")
        cls.plan = read(".agents/skills/plan-overview/SKILL.md")
        cls.threads = read("threads/index.md")
        cls.projects = read("projects/index.md")
        cls.quality = read("reports/quality.md")

    def test_default_context_is_bounded_but_named_history_is_recalled(self):
        for document in (self.agents, self.threads, self.check_in, self.plan):
            with self.subTest(document=document[:30]):
                self.assertIn("Current Context", document)
                self.assertIn("History", document)
        self.assertIn("here never archives its Codex desktop task", self.threads)
        self.assertIn("Supporting And Historical Context", self.projects)

    def test_worker_prompt_keeps_notification_and_handoff_contracts(self):
        for heading in ("## Outcome", "## Scope", "## Acceptance", "## Delivery", "## Callback"):
            with self.subTest(heading=heading):
                self.assertIn(heading, self.thread)
        for marker in (
            "Blockers only",
            "Notify on completion",
            "TASK_COMPLETED",
            "WAITING_ON_DEPENDENCY",
            "DEPENDENCY_READY",
            "DEPENDENCY_ACK",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.thread)

    def test_formal_plan_surfaces_are_absent(self):
        self.assertFalse((ROOT / "plans").exists())
        self.assertFalse((ROOT / "templates/plan.md").exists())
        self.assertIn("Do not create workers", self.plan)
        self.assertIn("formal plan files", self.plan)

    def test_quality_signals_do_not_invent_missing_evidence(self):
        for signal in (
            "Completed-task-to-notification delay",
            "Stale Current Context rows",
            "Unresolved requests missed by scheduled check-ins",
            "Interruptions the user considered unnecessary",
        ):
            with self.subTest(signal=signal):
                self.assertIn(signal, self.quality)
        self.assertIn("Pre-change history is `Unknown`", self.quality)
        self.assertIn("Silence is not evidence", self.quality)

    def test_readme_does_not_claim_causal_productivity_gain(self):
        self.assertNotIn("more productive", read("README.md").lower())

    def test_public_contract_has_no_private_sync_identifiers(self):
        artifacts = (
            "AGENTS.md",
            "README.md",
            "GUIDE.md",
            "automations/heartbeat.md",
            "projects/index.md",
            "threads/index.md",
            "reports/quality.md",
            "templates/thread.md",
            "templates/worker-needs-fixture.md",
            "templates/worker-summary.md",
            "tests/fixtures/chief_execution_boundary_scenarios.csv",
            "tests/test_chief_execution_boundary.py",
            "tests/test_heartbeat_router.py",
        )
        text = "\n".join(read(path) for path in artifacts)
        for forbidden in ("chief-of-staff-vault", "/Users/"):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
