# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: MeetingVault
def tag_meeting(meeting_id, tags):
    for m in vault:
        if m['id'] == meeting_id:
            for t in tags:
                if t not in m.get('tags', []):
                    m.setdefault('tags', []).append(t)
            return meeting_id
    raise ValueError(f"Meeting {meeting_id} не найден")

def untag_meeting(meeting_id, tag):
    for m in vault:
        if m['id'] == meeting_id and tag in m.get('tags', []):
            m['tags'].remove(tag)
            return meeting_id
    raise ValueError(f"Meeting {meeting_id} не найден или тег '{tag}' отсутствует")

def list_tags(meeting_id):
    for m in vault:
        if m['id'] == meeting_id:
            return m.get('tags', [])
    raise ValueError(f"Meeting {meeting_id} не найден")
