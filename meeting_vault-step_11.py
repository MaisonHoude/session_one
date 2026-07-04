# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: MeetingVault
import json, os

DATA_FILE = "meetings.json"

def save_meetings(meetings):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(meetings, f, ensure_ascii=False, indent=2)

def load_meetings():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def get_meetings():
    meetings = load_meetings()
    if not meetings:
        save_meetings([])
    return meetings
