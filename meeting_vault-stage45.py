# === Stage 45: Добавь восстановление из резервной копии ===
# Project: MeetingVault
import json, os, sys

def load_from_backup(backup_path):
    if not os.path.exists(backup_path):
        print(f"Резервная копия не найдена: {backup_path}")
        return None
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Резервная копия успешно загружена ({len(data)} записей)")
        return data
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка загрузки резервной копии: {e}")
        return None
