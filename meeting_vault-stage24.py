# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: MeetingVault
def print_meeting_record(meeting):
    """Compact one-meeting summary with all details."""
    lines = []
    lines.append(f"Meeting: {meeting['title']}")
    lines.append(f"Date: {meeting.get('date', 'N/A')}")
    lines.append(f"Attendees ({len(meeting['attendees'])}): {', '.join(meeting['attendees'])}")

    if meeting.get('agenda'):
        lines.append("Agenda:")
        for item in meeting['agenda']:
            lines.append(f"  - {item}")

    if meeting.get('decisions'):
        lines.append("Decisions:")
        for d in meeting['decisions']:
            lines.append(f"  ✓ {d}")

    if meeting.get('action_items'):
        lines.append("Action Items:")
        for ai in meeting['action_items']:
            assignee = ai.get('assignee', 'unassigned')
            action = ai.get('task', '')
            deadline = ai.get('deadline', 'N/A')
            lines.append(f"  • {action} → by {assignee} (by {deadline})")

    print('\n'.join(lines))
