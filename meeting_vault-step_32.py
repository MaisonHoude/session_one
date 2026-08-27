# === Stage 32: Добавь журнал действий пользователя ===
# Project: MeetingVault
from datetime import datetime

class UserActionLog:
    def __init__(self):
        self._entries = []

    def record(self, user, action_type, details, meeting_id=None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user,
            "action_type": action_type,
            "details": details,
            "meeting_id": meeting_id,
        }
        self._entries.append(entry)
        return entry

    def get_log(self, user=None, meeting_id=None):
        log = self._entries[:]
        if user:
            log = [e for e in log if e["user"] == user]
        if meeting_id:
            log = [e for e in log if e["meeting_id"] == meeting_id]
        return log

    def clear(self):
        self._entries.clear()
