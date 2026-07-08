# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: MeetingVault
def search_meetings(self, query: str):
        """Search meetings by multiple fields case-insensitive."""
        results = []
        for meeting in self._meetings:
            if any(query.lower() in field.lower() for field in meeting.values()):
                results.append(meeting)
        return results
