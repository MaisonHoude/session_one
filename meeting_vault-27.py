# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: MeetingVault
def reset_demo_data():
    """Сбросить демо-данные в MeetingVault."""
    global meetings, current_id
    meetings = [
        {"id": 100, "title": "Старт проекта", "date": "2024-01-15", "attendees": ["Анна", "Борис"], "agenda": ["Обсудить цели"], "decisions": ["Принять план"], "actions": [{"task": "Подготовить отчёт", "assignee": "Анна", "deadline": "2024-02-01"}]},
        {"id": 101, "title": "Регулярный митинг", "date": "2024-02-10", "attendees": ["Виктор"], "agenda": ["Отчёт за январь"], "decisions": [], "actions": []},
    ]
    current_id = 102

def clear_state():
    """Полная очистка состояния MeetingVault."""
    global meetings, current_id
    meetings = []
    current_id = 0
