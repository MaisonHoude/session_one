# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: MeetingVault
def check_integrity(m):
    errors = []
    if not m.agenda or not isinstance(m.agenda, list):
        errors.append("agenda is missing or invalid")
    if not m.decisions or not isinstance(m.decisions, list):
        errors.append("decisions is missing or invalid")
    if not m.actions or not isinstance(m.actions, list):
        errors.append("actions is missing or invalid")
    for i, act in enumerate(m.actions):
        if act is None or not isinstance(act, dict):
            errors.append(f"action {i} is invalid: {act}")
            continue
        for key in ("description", "assignee", "due"):
            if key not in act:
                errors.append(f"action {i} missing key '{key}'")
    return errors

def repair_simple(m):
    if not m.agenda:
        m.agenda = []
    if not m.decisions:
        m.decisions = []
    if not m.actions:
        m.actions = []
    repaired = False
    for i, act in enumerate(m.actions):
        if act is None:
            m.actions[i] = {"description": "", "assignee": "", "due": None}
            repaired = True
        elif not isinstance(act, dict):
            m.actions[i] = {"description": "", "assignee": "", "due": None}
            repaired = True
        else:
            for key in ("description", "assignee", "due"):
                if key not in act:
                    act[key] = ""
                    repaired = True
    return repaired
