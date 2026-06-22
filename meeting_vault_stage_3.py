# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: MeetingVault
class MeetingVault:
    def __init__(self):
        self._meetings = []

    def add_meeting(self, topic, attendees, decisions, actions=None):
        meeting_id = len(self._meetings) + 1
        record = {
            "id": meeting_id,
            "topic": topic,
            "attendees": attendees if isinstance(attendees, list) else [attendees],
            "decisions": decisions if isinstance(decisions, list) else [decisions] if decisions else [],
            "actions": actions or []
        }
        self._meetings.append(record)

    def get_meeting(self, meeting_id):
        for m in self._meetings:
            if m["id"] == meeting_id:
                return m
        return None
