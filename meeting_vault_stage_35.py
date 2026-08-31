# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: MeetingVault
def next_action_suggestion(meeting, actions):
    """Returns a short recommendation based on the meeting state and its assigned actions."""
    if not actions:
        return "Нет назначенных действий — предложите обсудить приоритеты."
    urgent = [a for a in actions if a.get("deadline") and a["deadline"] <= today()]
    if urgent:
        return f"Срочно выполните {len(urgent)} действие(я), срок {urgent[0]['deadline']}."
    if any(a.get("status") == "pending" for a in actions):
        return "Завершите оставшиеся 'pending' действия до следующего собрания."
    return "Все действия выполнены — отметьте встречу как закрытую."
