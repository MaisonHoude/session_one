# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: MeetingVault
def rollback_last_action():
    """Откатывает последнее действие в истории, если оно было добавлено через add_action()."""
    history = vault.get_history()
    if not history:
        return
    last = history[-1]
    if last.get("rolled_back", False):
        return
    vault.set_history([*history[:-1], {**last, "rolled_back": True}])
    if vault.get_meeting() and "actions" in vault.get_meeting():
        actions = vault.get_meeting()["actions"]
        for i, a in enumerate(actions):
            if a.get("id") == last.get("id"):
                actions.pop(i)
                break
