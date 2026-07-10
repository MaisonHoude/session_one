# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: MeetingVault
def summary(meetings):
    if not meetings:
        return "MeetingVault: нет данных о встречах."
    total = len(meetings)
    with_decisions = sum(1 for m in meetings if m.get("decisions"))
    with_actions = sum(1 for m in meetings if m.get("actions"))
    unique_participants = set()
    for m in meetings:
        unique_participants.update(m.get("participants", []))
    return (f"MeetingVault — сводка ({total} встреч):\n"
            f"  • с решениями: {with_decisions}\n"
            f"  • с действиями: {with_actions}\n"
            f"  • участников всего: {len(unique_participants)}")
