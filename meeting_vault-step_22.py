# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: MeetingVault
def check_overdue_reminders():
    """Проверяет все действия в архиве встреч на наличие просроченных напоминаний."""
    overdue = []
    for meeting in meetings:
        for action in meeting.get('actions', []):
            if action.get('assigned_to') and action.get('due_date'):
                from datetime import date, timedelta
                today = date.today()
                due = date.fromisoformat(action['due_date'])
                days_left = (today - due).days
                if days_left < 0:
                    overdue.append({
                        'meeting_id': meeting['id'],
                        'action': action['title'],
                        'assigned_to': action['assigned_to'],
                        'due_date': action['due_date'],
                        'overdue_days': abs(days_left),
                    })
    return overdue
