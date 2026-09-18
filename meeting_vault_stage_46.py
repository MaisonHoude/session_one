# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: MeetingVault
def migrate_v1():
    """Migration v1: add 'decisions' and 'actions' lists to every meeting."""
    if 'meetings' not in globals():
        return
    for m in meetings:
        if 'decisions' not in m:
            m['decisions'] = []
        if 'actions' not in m:
            m['actions'] = []
    return True
