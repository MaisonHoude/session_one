# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: MeetingVault
import unittest


class TestMeetingVault(unittest.TestCase):

    def test_create_meeting(self):
        mv = MeetingVault()
        meeting = mv.create_meeting("Team Sync", ["Alice", "Bob"], ["Q1 goals", "Budget"], "Decided: Q1 goals first")
        self.assertEqual(meeting["title"], "Team Sync")
        self.assertEqual(meeting["participants"], ["Alice", "Bob"])
        self.assertEqual(meeting["agenda"], ["Q1 goals", "Budget"])
        self.assertIn("Decided: Q1 goals first", meeting["decisions"])

    def test_add_action_item(self):
        mv = MeetingVault()
        meeting = mv.create_meeting("Sync", ["Alice"], ["Agenda"], "")
        action = mv.add_action_item(meeting, "Bob", "Send report", "2026-06-01")
        self.assertEqual(action["assignee"], "Bob")
        self.assertEqual(action["task"], "Send report")
        self.assertEqual(action["deadline"], "2026-06-01")

    def test_get_meeting(self):
        mv = MeetingVault()
        mv.create_meeting("Sync", ["Alice"], ["Agenda"], "")
        self.assertEqual(len(mv.get_meeting("Sync")), 1)

    def test_archive_meeting(self):
        mv = MeetingVault()
        mv.create_meeting("Sync", ["Alice"], ["Agenda"], "")
        self.assertEqual(len(mv.get_meeting("Sync")), 1)
        mv.archive_meeting("Sync")
        self.assertEqual(len(mv.get_meeting("Sync")), 0)
        self.assertEqual(len(mv.get_archived()), 1)

    def test_stats(self):
        mv = MeetingVault()
        mv.create_meeting("M1", ["A"], ["A1"], "")
        mv.create_meeting("M2", ["B"], ["A2"], "")
        mv.archive_meeting("M1")
        stats = mv.get_stats()
        self.assertEqual(stats["total_meetings"], 2)
        self.assertEqual(stats["archived_meetings"], 1)
        self.assertEqual(stats["active_meetings"], 1)


if __name__ == "__main__":
    unittest.main()
