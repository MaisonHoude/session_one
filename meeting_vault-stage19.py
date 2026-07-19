# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: MeetingVault
def archive_old_meetings(db, days_to_archive=90):
    """Archive meetings older than `days_to_archive` days."""
    cutoff = datetime.now() - timedelta(days=days_to_archive)
    archived = []
    for meeting in db.meetings:
        if (meeting.date < cutoff and meeting.status == "completed"):
            meeting.status = "archived"
            archived.append(meeting.id)
    return sorted(archived)
