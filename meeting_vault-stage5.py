# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: MeetingVault
def delete_meeting(meeting_id: int) -> bool:
    if not meeting_id or isinstance(meeting_id, str):
        raise ValueError("meeting_id должен быть целым числом")
    
    try:
        index = meetings.index(meeting_id)
        del meetings[index]
        
        for i in range(len(actions)):
            action = actions[i]
            if action.get('meeting_id') == meeting_id:
                del actions[i]
                break
        
        return True
    except (IndexError, TypeError):
        return False

def get_meeting_by_id(meeting_id: int) -> dict | None:
    try:
        index = meetings.index(meeting_id)
        if 0 <= index < len(meetings):
            meeting_data = {
                'id': meetings[index],
                'title': titles[index] if index < len(titles) else '',
                'agenda': agendas[index] if index < len(agendas) else [],
                'decisions': decisions[index] if index < len(decisions) else [],
                'actions': [a for a in actions if a.get('meeting_id') == meetings[index]]
            }
            return meeting_data
    except (IndexError, TypeError):
        pass
    
    return None
