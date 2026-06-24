# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: MeetingVault
def edit_meeting(meeting_id: int, updates: dict) -> MeetingRecord | None:
    if not isinstance(updates, dict):
        raise ValueError("Updates must be a dictionary")
    
    for key in ["agenda", "decisions", "actions"]:
        if key in updates and not isinstance(updates[key], list):
            raise TypeError(f"Field '{key}' must be a list or omitted")

    try:
        index = next(i for i, m in enumerate(meetings) if m.id == meeting_id)
    except StopIteration:
        return None
    
    record = meetings[index]
    
    if "agenda" in updates and isinstance(updates["agenda"], list):
        record.agenda = updates["agenda"]
    if "decisions" in updates and isinstance(updates["decisions"], list):
        record.decisions = updates["decisions"]
    if "actions" in updates and isinstance(updates["actions"], list):
        record.actions = updates["actions"]
    
    record.updated_at = datetime.now()
    return record
