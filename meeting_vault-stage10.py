# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: MeetingVault
def export_to_json(meetings, actions):
    import json
    data = {
        "meetings": meetings,
        "actions": actions
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
