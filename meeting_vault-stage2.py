# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: MeetingVault
class MeetingData:
    def __init__(self):
        self.meetings = []
    
    def validate_date(self, date_str):
        try:
            from datetime import datetime
            if not date_str or len(date_str) < 10: return False
            datetime.strptime(date_str[:10], "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    def validate_participant(self, name):
        return bool(name and len(name.strip()) > 0)
    
    def add_meeting(self, title, date, agenda_items, decisions, actions):
        if not self.validate_date(date):
            print("Ошибка: Неверный формат даты (YYYY-MM-DD)")
            return False
        for item in agenda_items:
            if not isinstance(item, str) or len(item.strip()) == 0:
                print("Ошибка: Повестка не может содержать пустые строки")
                return False
        if not self.validate_participant(title):
            print("Ошибка: Заголовок встречи обязателен")
            return False
        meeting = {
            "id": len(self.meetings) + 1,
            "title": title.strip(),
            "date": date,
            "agenda": agenda_items,
            "decisions": decisions or [],
            "actions": actions or []
        }
        self.meetings.append(meeting)
        return True
