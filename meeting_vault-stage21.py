# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: MeetingVault
class Reminder:
    def __init__(self, action_id, due_date_str):
        self.action_id = action_id
        self.due_date_str = due_date_str
        self.is_reminded = False
        
    @property
    def is_overdue(self):
        from datetime import date
        try:
            today = date.today()
            return date.fromisoformat(self.due_date_str) < today and not self.is_reminded
        except ValueError:
            return False
    
    def notify(self, action):
        if self.is_overdue and not self.is_reminded:
            print(f"⚠️ Напоминание: действие '{action.title}' просрочено (срок: {self.due_date_str})")
            self.is_reminded = True
    
    def reset(self):
        from datetime import date
        if date.fromisoformat(self.due_date_str) >= date.today():
            self.is_reminded = False

class MeetingVault:
    def __init__(self):
        self.meetings = []
        self.reminders = {}
    
    def add_meeting(self, title, participants, agenda, decisions, actions):
        meeting_id = len(self.meetings) + 1
        meeting = {
            'id': meeting_id,
            'title': title,
            'participants': participants,
            'agenda': agenda,
            'decisions': decisions,
            'actions': [Action(title=a['title'], due_date=a.get('due_date', ''), responsible=a['responsible']) for a in actions]
        }
        self.meetings.append(meeting)
        return meeting
    
    def get_meeting(self, index):
        return self.meetings[index - 1] if 0 < index <= len(self.meetings) else None
    
    def remove_meeting(self, index):
        del self.meetings[index - 1]
    
    def check_reminders(self):
        for action in self.meetings:
            for a in action['actions']:
                if not a.due_date:
                    continue
                reminder = Reminder(a.id, a.due_date)
                self.reminders[a.id] = reminder
                reminder.notify(a)

# Пример использования
vault = MeetingVault()
meeting = vault.add_meeting("Проект 'MeetingVault'", ["Орнит", "Джон"], 
    ["Обсудить API", "План релиза"], 
    ["API v2.0 утвержден", "Релиз 15 апреля"],
    [{"title": "Документировать API", "due_date": "2026-04-15", "responsible": "Орнит"},
     {"title": "Подготовить демо", "due_date": "2026-03-01", "responsible": "Джон"}])
vault.check_reminders()
