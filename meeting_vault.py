# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: MeetingVault
import json, os
from dataclasses import asdict, field
from datetime import datetime
from typing import List, Dict, Optional

class ActionItem:
    def __init__(self, description: str, assignee: str, due_date: str):
        self.description = description
        self.assignee = assignee
        self.due_date = due_date

class Attendee:
    def __init__(self, name: str, email: Optional[str] = None):
        self.name = name
        self.email = email

class AgendaItem:
    def __init__(self, topic: str, owner: str, status: str = "pending"):
        self.topic = topic
        self.owner = owner
        self.status = status

class MeetingRecord:
    def __init__(self, meeting_id: int, title: str, date: datetime):
        self.meeting_id = meeting_id
        self.title = title
        self.date = date
        self.attendees: List[Attendee] = []
        self.agenda: List[AgendaItem] = []
        self.decisions: List[str] = []
        self.actions: List[ActionItem] = []

    def to_dict(self) -> Dict:
        return {
            "meeting_id": self.meeting_id,
            "title": self.title,
            "date": self.date.isoformat(),
            "attendees": [asdict(a) for a in self.attendees],
            "agenda": [asdict(a) for a in self.agenda],
            "decisions": self.decisions.copy(),
            "actions": [asdict(a) for a in self.actions]
        }

class MeetingVault:
    def __init__(self, db_path: str = "meetings.db"):
        self.records: List[MeetingRecord] = []
        self.next_id = 1
        if os.path.exists(db_path):
            try:
                with open(db_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data.get('meetings', []):
                        rec = MeetingRecord(item['meeting_id'], item['title'], datetime.fromisoformat(item['date']))
                        rec.attendees = [Attendee(**a) for a in item['attendees']]
                        rec.agenda = [AgendaItem(**a) for a in item['agenda']]
                        rec.decisions = item.get('decisions', [])
                        rec.actions = [ActionItem(**a) for a in item['actions']]
                    self.records.extend(recs := data.get('meetings', []))
            except Exception:
                pass

    def add_meeting(self, title: str, date: datetime) -> MeetingRecord:
        record = MeetingRecord(self.next_id, title, date)
        self.records.append(record)
        self.next_id += 1
        return record

    def save(self):
        with open("meetings.db", 'w', encoding='utf-8') as f:
            json.dump({"meetings": [r.to_dict() for r in self.records]}, f, ensure_ascii=False, indent=2)

# --- Demo Data & Entry Point ---
