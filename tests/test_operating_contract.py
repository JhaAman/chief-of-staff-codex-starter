import csv
import re
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
        cls.worker_needs = read("templates/worker-needs-fixture.md")
        cls.summary = read("templates/worker-summary.md")
        cls.closure = scenarios("tests/fixtures/task_closure_scenarios.csv")
        cls.coordination = scenarios(
            "tests/fixtures/dependency_coordination_scenarios.csv"
        )
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
        for state in ("DEPENDENCY_READY_SENT", "DEPENDENCY_ACK"):
            self.assertIn(state, self.worker_needs)
        self.assertIn("stable handoff ID", compact(self.worker_needs))
        self.assertIn("background inspection", compact(self.agents))
        self.assertIn("`URGENT_BLOCKER`", self.thread)
        self.assertIn("completion, pull-request readiness", compact(self.agents))

    def test_send_success_is_not_recipient_acknowledgement(self):
        case = self.coordination["send succeeds but recipient remains waiting"]
        self.assertEqual(
            (
                case["direct_send_result"],
                case["recipient_evidence"],
                case["expected_action"],
            ),
            (
                "success",
                "WAITING_ON_DEPENDENCY without acknowledgement",
                "send one Chief fallback with the same handoff ID",
            ),
        )
        for document in (self.agents, self.chief, self.thread):
            with self.subTest(document=document[:40]):
                self.assertIn("proves only enqueue acceptance", document)
                self.assertIn("`DEPENDENCY_ACK`", document)

    def test_acknowledged_handoff_reconciles_without_another_send(self):
        case = self.coordination["successful direct handoff"]
        self.assertEqual(
            (case["recipient_evidence"], case["expected_action"], case["expected_state"]),
            (
                "DEPENDENCY_ACK for the exact handoff ID",
                "reconcile ledger without another send",
                "consumed",
            ),
        )
        self.assertIn("same handoff ID", compact(self.check_in))
        self.assertIn(
            "without sending another worker turn",
            compact(self.check_in),
        )

    def test_duplicate_delivery_is_idempotent(self):
        case = self.coordination["duplicate delivery after acknowledgement"]
        self.assertEqual(
            (case["ledger_state"], case["expected_action"], case["expected_state"]),
            (
                "consumed",
                "no-op without reapplying the artifact",
                "consumed",
            ),
        )
        for document in (self.agents, self.thread):
            with self.subTest(document=document[:40]):
                self.assertIn(
                    "same handoff ID is an idempotent no-op",
                    compact(document),
                )

    def test_stale_ledger_reconciles_without_waking_the_worker(self):
        case = self.coordination["stale ledger after downstream work"]
        self.assertEqual(
            (case["ledger_state"], case["expected_action"]),
            ("waiting", "update ledger without another send"),
        )
        self.assertIn(
            "update the ledger without sending another worker turn",
            self.check_in,
        )

    def test_completed_dependent_is_not_reawakened(self):
        case = self.coordination["already-completed dependent"]
        self.assertEqual(
            (
                case["recipient_runtime"],
                case["direct_send_result"],
                case["expected_action"],
            ),
            (
                "completed",
                "not sent",
                "reconcile terminal result without sending",
            ),
        )
        self.assertIn(
            "already completed the declared outcome, do not send or resume it",
            compact(self.check_in),
        )

    def test_dependency_ack_requires_transition_out_of_wait(self):
        case = self.coordination[
            "dependency acknowledged without state transition"
        ]
        self.assertEqual(
            (
                case["recipient_evidence"],
                case["expected_action"],
                case["expected_state"],
            ),
            (
                "DEPENDENCY_ACK but still WAITING_ON_DEPENDENCY",
                "resume once with the same handoff ID",
                "ready retry sent",
            ),
        )
        for document in (self.agents, self.thread, self.check_in):
            with self.subTest(document=document[:40]):
                self.assertIn(
                    "acknowledgement includes the transition out of "
                    "`WAITING_ON_DEPENDENCY`",
                    compact(document),
                )

    def test_ignored_external_resume_gets_one_same_key_fallback(self):
        case = self.coordination["external resume send ignored"]
        self.assertEqual(
            (case["recipient_evidence"], case["expected_action"]),
            (
                "WAITING_ON_EXTERNAL without EXTERNAL_RESUME_ACK",
                "send one same-key fallback",
            ),
        )
        for document in (self.agents, self.thread, self.check_in):
            with self.subTest(document=document[:40]):
                self.assertIn("`EXTERNAL_RESUME_SENT`", document)
                self.assertIn("`EXTERNAL_RESUME_ACK`", document)
        self.assertIn(
            "only while this task is idle or unloaded",
            compact(self.thread),
        )
        self.assertIn(
            "active or terminal task must not receive the fallback",
            compact(self.thread),
        )

    def test_ignored_user_answer_gets_one_same_id_fallback(self):
        case = self.coordination["user answer relay send ignored"]
        self.assertEqual(
            (case["recipient_evidence"], case["expected_action"]),
            (
                "NEEDS_USER without ANSWER_RELAY_ACK",
                "send one same-ID fallback without asking the user again",
            ),
        )
        for document in (self.agents, self.chief, self.check_in):
            with self.subTest(document=document[:40]):
                self.assertIn("`ANSWER_RELAY_SENT`", document)
                self.assertIn("`ANSWER_RELAY_ACK`", document)
                self.assertIn("without asking the user again", compact(document))
        self.assertIn(
            "only while this task is idle or unloaded",
            compact(self.thread),
        )
        self.assertIn(
            "active or terminal task must not receive the fallback",
            compact(self.thread),
        )

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
            "tests/fixtures/chief_execution_boundary_scenarios.csv",
            "tests/fixtures/dependency_coordination_scenarios.csv",
            "tests/fixtures/task_closure_scenarios.csv",
            "tests/fixtures/text_approval_scenarios.csv",
            "tests/test_chief_execution_boundary.py",
            "tests/test_heartbeat_router.py",
            "tests/test_operating_contract.py",
        )
        changed_surfaces = "\n".join(read(path) for path in artifacts)
        for forbidden in ("Am" "an", "Jha" "Am" "an", "/" "Users/", "magic" "product"):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, changed_surfaces)
        for private_identifier in (
            r"\b[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}\b",
            r"\b[0-9a-f]{40}\b",
            r"chief-of-staff-" r"vault",
        ):
            with self.subTest(private_identifier=private_identifier):
                self.assertIsNone(re.search(private_identifier, changed_surfaces))


if __name__ == "__main__":
    unittest.main()
