# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: MeetingVault
import json, os

def load_meetings_from_file(filepath: str) -> list[dict]:
    """Загружает встречи из JSON-файла с обработкой ошибок."""
    if not os.path.exists(filepath):
        print(f"Файл не найден: {filepath}")
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict) and "meetings" in data:
            meetings = data["meetings"]
        elif isinstance(data, list):
            meetings = data
        else:
            raise ValueError("Неверный формат JSON-файла")
        print(f"Загружено {len(meetings)} встреч из '{filepath}'")
        return meetings
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
